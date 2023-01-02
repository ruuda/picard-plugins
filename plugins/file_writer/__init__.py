# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Bob Swift (rdswift)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.

PLUGIN_NAME = 'File Writer'
PLUGIN_AUTHOR = 'Bob Swift (rdswift)'
PLUGIN_DESCRIPTION = '''
This plugin adds a scripting function <strong>$writeline()</strong> to allow writing text to an output file.
It also adds a function <strong>$sanitize_text()</strong> to ensure that the text provided (generally from a
metadata tag value) is suitable to include in a file path. Sanitizing text will replace all path separators
and perform any cleanup specified in the File Naming Compatability settings.
<br /><br />
Please see the <a href="https://github.com/rdswift/picard-plugins/blob/2.0_RDS_Plugins/plugins/file_writer/README.md">user guide</a> on GitHub for more information.
'''

PLUGIN_VERSION = "0.2"
PLUGIN_API_VERSIONS = ["2.0"]
PLUGIN_LICENSE = "GPL-2.0 or later"
PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-2.0.html"

import os
import re

from picard import log
from picard.config import get_config
from picard.const.sys import (
    IS_MACOS,
    IS_WIN,
)
from picard.script import register_script_function
from picard.util import (
    is_absolute_path,
    normpath,
    replace_win32_incompat,
    sanitize_filename,
)
from picard.util.filenaming import make_save_path
from picard.util.textencoding import replace_non_ascii


_re_replace_underscores = re.compile(r'[\s_]+')


def func_writeline(parser, file_to_write, text_to_write, reset_file=None):
    if file_to_write.strip():
        config = get_config()
        settings = config.setting
        write_mode = 'w' if reset_file else 'a'
        if settings["replace_spaces_with_underscores"]:
            file_to_write = _re_replace_underscores.sub('_', file_to_write.strip())
        if not is_absolute_path(file_to_write):
            if settings['move_files'] and settings['move_files_to']:
                file_to_write = os.path.join(settings['move_files_to'], file_to_write)
        file_to_write = make_save_path(normpath(file_to_write), IS_WIN, IS_MACOS)
        try:
            os.makedirs(os.path.dirname(file_to_write), exist_ok=True)
            with open(file_to_write, write_mode, encoding='utf8') as f:
                f.write(text_to_write + '\n')
        except OSError as ex:
            log.error(f"Error writing to file: {file_to_write} (Exception: {ex})")
    else:
        log.error("Missing file path to write.")
    return ""


def func_sanitize_text(parser, text):
    # make sure string can safely be used in a path name
    config = get_config()
    settings = config.setting
    win_compat = IS_WIN or settings["windows_compatibility"]
    # Set default for Picard versions earlier than v2.9
    replace_dir_separator = settings["replace_dir_separator"] if settings["replace_dir_separator"] is not None else "_"

    sanitized = text

    # replace non-ASCII characters
    if settings["ascii_filenames"]:
        sanitized = replace_non_ascii(sanitized, win_compat=win_compat)

    # replace incompatible characters
    if win_compat:
        # Check for Picard versions earlier than v2.9 that don't support the `replacements` parameter
        if settings["win_compat_replacements"] is not None:
            sanitized = replace_win32_incompat(sanitized, replacements=settings["win_compat_replacements"])
        else:
            sanitized = replace_win32_incompat(sanitized)

    if settings["replace_spaces_with_underscores"]:
        sanitized = _re_replace_underscores.sub('_', sanitized.strip())

    # remove null characters
    sanitized = sanitized.replace("\x00", "")

    return sanitize_filename(sanitized, repl=replace_dir_separator, win_compat=win_compat)


# Register the new functions
register_script_function(func_writeline, name='writeline',
    documentation="""`$writeline(file,text[,reset])`

This will write `text` (followed by a newline) to `file`. The text will be appended
to the file unless `reset` is set, in which case the file will be overwritten.""")

register_script_function(func_sanitize_text, name='sanitize_text',
    documentation="""`$sanitize_text(text)`

Returns a sanitized version of `text` suitable for use in a file path, including applying the
"ASCII Filenames", "Windows Compatibility" and "Replacement Directory Separator" settings.""")
