# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Bob Swift (rdswift)
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

PLUGIN_NAME = 'Genre Mapper'
PLUGIN_AUTHOR = 'Bob Swift'
PLUGIN_DESCRIPTION = '''
Standardize genres in the "genre" tag by matching the genres as found to a standard
genre as defined in the genre replacement mapping configuration option.
<br /><br />
Please see the <a href="https://github.com/rdswift/picard-plugins/blob/2.0_RDS_Plugins/plugins/genre_mapper/docs/README.md">user guide</a> on GitHub for more information.
'''
PLUGIN_VERSION = '0.1'
PLUGIN_API_VERSIONS = ['2.0', '2.1', '2.2', '2.3', '2.6', '2.7', '2.8']
PLUGIN_LICENSE = "GPL-2.0"
PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-2.0.txt"

import re

from picard import (
    config,
    log,
)
from picard.metadata import (
    MULTI_VALUED_JOINER,
    register_track_metadata_processor,
)
from picard.plugin import PluginPriority
from picard.plugins.genre_mapper.ui_options_genre_mapper import (
    Ui_GenreMapperOptionsPage,
)

from picard.ui.options import (
    OptionsPage,
    register_options_page,
)


pairs_split = re.compile(r"\r\n|\n\r|\n").split

OPT_MATCH_PAIRS = 'genre_mapper_replacement_pairs'
OPT_MATCH_FIRST = 'genre_mapper_apply_first_match_only'


class GenreMapperOptionsPage(OptionsPage):

    NAME = "genre_mapper"
    TITLE = "Genre Mapper"
    PARENT = "plugins"

    options = [
        config.TextOption("setting", OPT_MATCH_PAIRS, ''),
        config.BoolOption("setting", OPT_MATCH_FIRST, False),
    ]

    def __init__(self, parent=None):
        super(GenreMapperOptionsPage, self).__init__(parent)
        self.ui = Ui_GenreMapperOptionsPage()
        self.ui.setupUi(self)

    def load(self):
        # Enable external link
        self.ui.format_description.setOpenExternalLinks(True)

        # Replacement settings
        self.ui.genre_mapper_replacement_pairs.setPlainText(config.setting[OPT_MATCH_PAIRS])
        self.ui.genre_mapper_first_match_only.setChecked(config.setting[OPT_MATCH_FIRST])

    def save(self):
        # Replacement settings
        config.setting[OPT_MATCH_PAIRS] = self.ui.genre_mapper_replacement_pairs.toPlainText()
        config.setting[OPT_MATCH_FIRST] = self.ui.genre_mapper_first_match_only.isChecked()


def make_re(map_string):
    re_string = str(map_string).strip()
    re_string = map_string.replace('.', '\n').replace('*', '.*').replace('?', '.').replace('\n', '\\.')
    re_string = re_string.replace('^', '\\^').replace('$', '\\$')
    return '^' + re_string + '$'


def track_genre_mapper(album, metadata, *args):
    if 'genre' not in metadata or not metadata['genre']:
        log.debug("%s: No genres found for %s", PLUGIN_NAME, metadata['title'],)
        return
    replacements = []
    for pair in pairs_split(config.setting[OPT_MATCH_PAIRS]):
        if "=" not in pair:
            continue
        original, replacement = pair.split('=', 1)
        original = original.strip()
        replacement = replacement.strip()
        if not original:
            log.warning('%s: Missing genre mapping pair: "%s" = "%s"', PLUGIN_NAME, original, replacement,)
            continue
        replacements.append((make_re(original), replacement))
        log.debug('%s: Add genre mapping pair: "%s" = "%s"', PLUGIN_NAME, original, replacement,)
    if not replacements:
        log.warning("%s: No genre replacement maps defined.", PLUGIN_NAME,)
        return
    genres = {}
    metadata_genres = str(metadata['genre']).split(MULTI_VALUED_JOINER)
    for genre in metadata_genres:
        for (original, replacement) in replacements:
            if genre and re.fullmatch(original, genre, re.IGNORECASE):
                genre = replacement
                if config.setting[OPT_MATCH_FIRST]:
                    break
        if genre:
            genres[genre.title()] = True
    metadata['genre'] = [x for x in genres.keys()]


# Register the plugin to run at a LOW priority.
register_track_metadata_processor(track_genre_mapper, priority=PluginPriority.LOW)
register_options_page(GenreMapperOptionsPage)
