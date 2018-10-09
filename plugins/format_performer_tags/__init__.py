# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Bob Swift (rdswift)
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

PLUGIN_NAME = 'Format Performer Tags'
PLUGIN_AUTHOR = 'Bob Swift (rdswift)'
PLUGIN_DESCRIPTION = '''
This plugin provides options with respect to the formatting of performer
tags.  It has been developed using the 'Standardise Performers' plugin by
Sophist as the basis for retrieving and processing the performer data for
each of the tracks.  The format of the resulting tags can be customized
in the option settings page.
'''

PLUGIN_VERSION = "0.2"
PLUGIN_API_VERSIONS = ["2.0"]
PLUGIN_LICENSE = "GPL-2.0 or later"
PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-2.0.html"

import re
from picard import config, log
from picard.metadata import register_track_metadata_processor
from picard.plugin import PluginPriority
from picard.ui.options import register_options_page, OptionsPage
from picard.plugins.format_performer_tags.ui_options_format_performer_tags import Ui_FormatPerformerTagsOptionsPage

performers_split = re.compile(r", | and ").split

WORD_LIST = ['guest', 'solo', 'additional', 'minor', 'lead', 'background']

def format_performer_tags(album, metadata, *args):
    word_dict = {}
    for word in WORD_LIST:
        word_dict[word] = config.setting['format_group_' + word]
    for key, values in list(filter(lambda filter_tuple: filter_tuple[0].startswith('performer:') or filter_tuple[0].startswith('~performersort:'), metadata.rawitems())):
        mainkey, subkey = key.split(':', 1)
        if not subkey:
            continue
        instruments = performers_split(subkey)
        log.debug("%s: Formatting Performer [%s]",
                  PLUGIN_NAME,
                  subkey,
                  )
        groups = { 1: [], 2: [], 3: [], }
        words = instruments[0].split()
        for word in words[:]:
            if not word in WORD_LIST:
                break
            groups[word_dict[word]].append(word)
            words.remove(word)
        instruments[0] = " ".join(words)
        display_group = {}
        for group_number in range(1, 4):
            if groups[group_number]:
                log.debug("%s: groups[%s]: %s", PLUGIN_NAME, group_number, groups[group_number],)
                groups[group_number].sort(reverse=config.setting["format_group_{0}_sort_desc".format(group_number)])
                display_group[group_number] = config.setting["format_group_{0}_start_char".format(group_number)] + " ".join(groups[group_number]) + config.setting["format_group_{0}_end_char".format(group_number)]
                display_group[group_number] = display_group[group_number] + " " if group_number < 2 else " " + display_group[group_number]
            else:
                display_group[group_number] = ""
        log.debug("%s: display_group: %s", PLUGIN_NAME, display_group,)
        del metadata[key]
        for instrument in instruments:
            newkey = '%s:%s%s%s' % (mainkey, display_group[1], instrument, display_group[2])
            log.debug("%s: newkey: %s", PLUGIN_NAME, newkey,)
            for value in values:
                metadata.add_unique(newkey, value + display_group[3])


class FormatPerformerTagsOptionsPage(OptionsPage):

    NAME = "format_performer_tags"
    TITLE = "Format Performer Tagss"
    PARENT = "plugins"

    options = [
        config.IntOption("setting", "format_group_additional", 1),
        config.IntOption("setting", "format_group_guest", 1),
        config.IntOption("setting", "format_group_minor", 1),
        config.IntOption("setting", "format_group_solo", 1),
        config.IntOption("setting", "format_group_lead", 1),
        config.IntOption("setting", "format_group_background", 1),
        config.TextOption("setting", "format_group_1_start_char", ''),
        config.TextOption("setting", "format_group_1_end_char", ''),
        config.BoolOption("setting", "format_group_1_sort_desc", False),
        config.TextOption("setting", "format_group_2_start_char", '('),
        config.TextOption("setting", "format_group_2_end_char", ')'),
        config.BoolOption("setting", "format_group_2_sort_desc", False),
        config.TextOption("setting", "format_group_3_start_char", '('),
        config.TextOption("setting", "format_group_3_end_char", ')'),
        config.BoolOption("setting", "format_group_3_sort_desc", False),
    ]

    def __init__(self, parent=None):
        super(FormatPerformerTagsOptionsPage, self).__init__(parent)
        self.ui = Ui_FormatPerformerTagsOptionsPage()
        self.ui.setupUi(self)

    def load(self):
        self.ui.format_group_additional.setValue(config.setting["format_group_additional"])
        self.ui.format_group_guest.setValue(config.setting["format_group_guest"])
        self.ui.format_group_minor.setValue(config.setting["format_group_minor"])
        self.ui.format_group_solo.setValue(config.setting["format_group_solo"])
        self.ui.format_group_lead.setValue(config.setting["format_group_lead"])
        self.ui.format_group_background.setValue(config.setting["format_group_background"])
        self.ui.format_group_1_start_char.setText(config.setting["format_group_1_start_char"])
        self.ui.format_group_1_end_char.setText(config.setting["format_group_1_end_char"])
        self.ui.format_group_1_sort_desc.setChecked(config.setting["format_group_1_sort_desc"])
        self.ui.format_group_2_start_char.setText(config.setting["format_group_2_start_char"])
        self.ui.format_group_2_end_char.setText(config.setting["format_group_2_end_char"])
        self.ui.format_group_2_sort_desc.setChecked(config.setting["format_group_2_sort_desc"])
        self.ui.format_group_3_start_char.setText(config.setting["format_group_3_start_char"])
        self.ui.format_group_3_end_char.setText(config.setting["format_group_3_end_char"])
        self.ui.format_group_3_sort_desc.setChecked(config.setting["format_group_3_sort_desc"])

    def save(self):
        config.setting["format_group_additional"] = self.ui.format_group_additional.value()
        config.setting["format_group_guest"] = self.ui.format_group_guest.value()
        config.setting["format_group_minor"] = self.ui.format_group_minor.value()
        config.setting["format_group_solo"] = self.ui.format_group_solo.value()
        config.setting["format_group_lead"] = self.ui.format_group_lead.value()
        config.setting["format_group_background"] = self.ui.format_group_background.value()
        config.setting["format_group_1_start_char"] = self.ui.format_group_1_start_char.text()
        config.setting["format_group_1_end_char"] = self.ui.format_group_1_end_char.text()
        config.setting["format_group_1_sort_desc"] = self.ui.format_group_1_sort_desc.isChecked()
        config.setting["format_group_2_start_char"] = self.ui.format_group_2_start_char.text()
        config.setting["format_group_2_end_char"] = self.ui.format_group_2_end_char.text()
        config.setting["format_group_2_sort_desc"] = self.ui.format_group_2_sort_desc.isChecked()
        config.setting["format_group_3_start_char"] = self.ui.format_group_3_start_char.text()
        config.setting["format_group_3_end_char"] = self.ui.format_group_3_end_char.text()
        config.setting["format_group_3_sort_desc"] = self.ui.format_group_3_sort_desc.isChecked()


# Register the plugin to run at a HIGH priority.
register_track_metadata_processor(format_performer_tags, priority=PluginPriority.HIGH)
register_options_page(FormatPerformerTagsOptionsPage)
