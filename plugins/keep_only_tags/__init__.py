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

PLUGIN_NAME = 'Keep Only Tags'
PLUGIN_AUTHOR = 'Bob Swift (rdswift)'
PLUGIN_DESCRIPTION = '''
This plugin allows the user to determine which tags are written to the
output files by Picard. Tags that you wish to keep are entered in a page
in the options settings, with each tag on a separate line. Blank lines
will be ignored. The entries are not case-sensitive.
<br /><br />
If a tag in the list ends with an asterisk (\*), then it will keep any tags
beginning with the tag.  For example, if your list contains "performer:\*"
then all tags beginning with "performer:" will be kept, such as
"performer:instrument" and "performer:vocals".
<br /><br />
All tags that are removed will still be available as variables with "\_ko\_"
prepended to the tag name. For example, if you choose not to keep the
"musicbrainz_trackid" tag, it will still be available to scripts as
"\_ko_musicbrainz_trackid".
<br /><br />
Please see the <a href="https://github.com/rdswift/picard-plugins/blob/2.0_RDS_Plugins/plugins/keep_only_tags/docs/README.md">user guide</a> on GitHub for more information.
'''
PLUGIN_VERSION = '0.1'
PLUGIN_API_VERSIONS = ['2.0', '2.1', '2.2']
PLUGIN_LICENSE = 'GPL-2.0-or-later'
PLUGIN_LICENSE_URL = 'https://www.gnu.org/licenses/gpl-2.0.html'

PLUGIN_USER_GUIDE_URL = 'https://github.com/rdswift/picard-plugins/blob/2.0_RDS_Plugins/plugins/keep_only_tags/docs/README.md'

from picard import config, log
from picard.metadata import (Metadata, register_album_metadata_processor,
                             register_track_metadata_processor)
from picard.plugin import PluginPriority
from picard.plugins.keep_only_tags.ui_options_keep_only_tags import \
    Ui_KeepOnlyTagsOptionsPage
from picard.ui.options import OptionsPage, register_options_page

TAG_LIST = """\
acoustid_id
acoustid_fingerprint
album
albumartist
albumartistsort
albumsort
arranger
artist
artistsort
artists
asin
barcode
bpm
catalognumber
comment:description
compilation
composer
composersort
conductor
copyright
director
discnumber
discsubtitle
encodedby
encodersettings
engineer
gapless
genre
grouping
key
isrc
language
license
lyricist
lyrics:description
media
djmixer
mixer
mood
movement
movementtotal
movementnumber
musicbrainz_artistid
musicbrainz_discid
musicbrainz_originalartistid
musicbrainz_originalalbumid
musicbrainz_recordingid
musicbrainz_albumartistid
musicbrainz_releasegroupid
musicbrainz_albumid
musicbrainz_trackid
musicbrainz_trmid
musicbrainz_workid
musicip_fingerprint
musicip_puid
originalalbum
originalartist
originalfilename
originaldate
originalyear
performer:*
podcast
podcasturl
producer
rating
label
releasecountry
date
releasestatus
releasetype
remixer
replaygain_album_gain
replaygain_album_peak
replaygain_album_range
replaygain_reference_loudness
replaygain_track_gain
replaygain_track_peak
replaygain_track_range
script
show
showsort
showmovement
subtitle
totaldiscs
totaltracks
tracknumber
title
titlesort
website
work
writer
"""

def get_tag_lists():
    tag_dict_1 = {}
    tag_dict_2 = {}
    tag_list = str(config.setting['keep_only_tags_list']).splitlines()
    for tag_name in [x.strip().lower() for x in tag_list]:
        if tag_name:
            star = tag_name.find('*')
            if star > 0:
                tag_dict_2[tag_name[:star]] = 1
            else:
                tag_dict_1[tag_name] = 1
    return tag_dict_1.keys(), tag_dict_2.keys()


def update_tags(album, metadata, *args):
    tag_list_1, tag_list_2 = get_tag_lists()
    if tag_list_1 or tag_list_2:
        target = Metadata()
        target.copy(metadata)
        for (key, value) in target.rawitems():
            if not (key.startswith('~') or key.lower() in tag_list_1):
                update = True
                for test_key in tag_list_2:
                    if str(key).lower().startswith(test_key):
                        update = False
                        break
                if update:
                    # metadata.add('~ko_' + key, value)
                    metadata['~ko_' + key] = metadata[key]
                    del metadata[key]
                    text = "{0}: Replacing tag '{1}' with variable '_ko_{1}'".format(PLUGIN_NAME, key)
                    log.debug(text)
    else:
        text = '{0}: Empty list of tags to keep.  Processing aborted.'.format(PLUGIN_NAME,)
        log.error(text)


class KeepOnlyTagsOptionsPage(OptionsPage):

    NAME = "keep_only_tags"
    TITLE = "Keep Only Tags"
    PARENT = "plugins"

    options = [
        config.TextOption("setting", "keep_only_tags_list", TAG_LIST),
    ]

    def __init__(self, parent=None):
        super(KeepOnlyTagsOptionsPage, self).__init__(parent)
        self.ui = Ui_KeepOnlyTagsOptionsPage()
        self.ui.setupUi(self)

    def load(self):
        self.ui.tag_list_text.setText(config.setting["keep_only_tags_list"])

    def save(self):
        self._set_settings(config.setting)

    def restore_defaults(self):
        super().restore_defaults()

    def _set_settings(self, settings):
        settings["keep_only_tags_list"] = self.ui.tag_list_text.toPlainText()


register_options_page(KeepOnlyTagsOptionsPage)
# Register the plugin to run at a LOW priority so that other plugins that
# modify the tag information can complete their processing and this plugin
# is working with the latest updated data.
VERY_LOW_PRIORITY = PluginPriority.LOW - 100
register_album_metadata_processor(update_tags, priority=VERY_LOW_PRIORITY)
register_track_metadata_processor(update_tags, priority=VERY_LOW_PRIORITY)
