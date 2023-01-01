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
<br /><br />
Please see the <a href="https://github.com/rdswift/picard-plugins/blob/2.0_RDS_Plugins/plugins/file_writer/README.md">user guide</a> on GitHub for more information.
'''

PLUGIN_VERSION = "0.1"
PLUGIN_API_VERSIONS = ["2.0"]
PLUGIN_LICENSE = "GPL-2.0 or later"
PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-2.0.html"

import os

from picard import (
    config,
    log,
)
from picard.const.sys import (
    IS_MACOS,
    IS_WIN,
)
from picard.script import register_script_function
from picard.util import (
    is_absolute_path,
    normpath,
)
from picard.util.filenaming import make_save_path


def func_writeline(parser, file_to_write, text_to_write, reset_file=None):
    if file_to_write.strip():
        write_mode = 'w' if reset_file else 'a'
        if not is_absolute_path(file_to_write):
            if config.setting['move_files'] and config.setting['move_files_to']:
                file_to_write = os.path.join(config.setting['move_files_to'], file_to_write)
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


# Register the new functions
register_script_function(func_writeline, name='writeline',
    documentation="""`$writeline(file,text[,reset])`

This will write `text` (followed by a newline) to `file`. The text will be appended
to the file unless `reset` is set, in which case the file will be overwritten.""")
