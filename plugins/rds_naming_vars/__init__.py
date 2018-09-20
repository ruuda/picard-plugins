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

PLUGIN_NAME = 'RDS Naming Variables'
PLUGIN_AUTHOR = 'Bob Swift (rdswift)'
PLUGIN_DESCRIPTION = '''
This plugin provides specialized album and track variables for use in
naming scripts. Note that standardized artist information is used for
the Album Artist variables, and credited artist information is used for
the Track Artist variables. The information is provided in the following:
<br /><ul>
<li>_PAA = Primary Album Artist
<li>_PAAS = Primary Album Artist Sort
<li>_FAA = Full Album Artist
<li>_FAAS = Full Album Artist Sort
<li>_FAAPS = Full Album Artist Primary Sort
<li>_AAC = Album Artist(s) Count
<li>_PTA = Primary Track Artist
<li>_ATA = Additional Track Artist(s)
<li>_FTA = Full Track Artist(s)
<li>_TAC = Track Artist(s) Count
<li>_ANT = Album Name Trimmed
<li>_TNT = Track Name Trimmed
</ul>
PLEASE NOTE: Tagger scripts are required to make use of these hidden
variables.
'''

PLUGIN_VERSION = "0.1"
PLUGIN_API_VERSIONS = ["2.0"]
PLUGIN_LICENSE = "GPL-2.0 or later"
PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-2.0.html"

from picard import config, log
from picard.metadata import (register_album_metadata_processor,
                             register_track_metadata_processor)
from picard.plugin import PluginPriority
from picard.ui.options import register_options_page, OptionsPage
from picard.plugins.rds_naming_vars.ui_options_rds_naming_vars import Ui_RdsNamingVarsOptionsPage

def rds_make_album_vars(album, album_metadata, release_metadata):
    if config.setting["album_title_trim_size"]:
        TITLE_LENGTH = config.setting["album_title_trim_size"]
    else:
        TITLE_LENGTH = 0
    album_id = release_metadata['id']
    album_title = release_metadata['title']
    if config.setting["trim_album_titles"] and TITLE_LENGTH and len(album_title) > TITLE_LENGTH:
        album_title = album_title[:TITLE_LENGTH] + '...'
    album_metadata["~ANT"] = album_title
    # Test for valid metadata node for the release
    if 'artist-credit' in release_metadata:
        # Initialize variables to default values
        sort_primary_artist = ""
        std_artist = ""
        sort_artist = ""
        artist_count = 0
        # The 'artist-credit' key should always be there.
        # This check is to avoid a runtime error if it doesn't exist for some reason.
        for artist_credit in release_metadata['artist-credit']:
            # Initialize temporary variables for each loop.
            temp_std_name = ""
            temp_sort_name = ""
            temp_phrase = ""
            # Check if there is a 'joinphrase' specified.
            if 'joinphrase' in artist_credit:
                temp_phrase = artist_credit['joinphrase']
            else:
                metadata_error(album_id, 'artist-credit.joinphrase')
            # Check if there is a 'name' specified.
            if 'name' in artist_credit:
                temp_cred_name = artist_credit['name']
            else:
                metadata_error(album_id, 'artist-credit.name')
            # Check if there is an 'artist' specified.
            if 'artist' in artist_credit:
                # Check if there is a 'name' specified.
                if 'name' in artist_credit['artist']:
                    temp_std_name = artist_credit['artist']['name']
                else:
                    metadata_error(album_id, 'artist-credit.artist.name')
                if 'sort-name' in artist_credit['artist']:
                    temp_sort_name = artist_credit['artist']['sort-name']
                else:
                    metadata_error(album_id, 'artist-credit.artist.sort-name')
            else:
                metadata_error(album_id, 'artist-credit.artist')
            std_artist += temp_std_name + temp_phrase
            sort_artist += temp_sort_name + temp_phrase
            if artist_count < 1:
                album_metadata["~PAA"] = temp_std_name
                album_metadata["~PAAS"] = temp_sort_name
                sort_primary_artist += temp_sort_name + temp_phrase
            else:
                sort_primary_artist += temp_std_name + temp_phrase
            artist_count += 1
    else:
        metadata_error(album_id, 'artist-credit')
    if std_artist:
        album_metadata["~FAA"] = std_artist
    if sort_primary_artist:
        album_metadata["~FAAPS"] = sort_primary_artist
    if sort_artist:
        album_metadata["~FAAS"] = sort_artist
    if artist_count:
        album_metadata["~AAC"] = artist_count
    return None


def rds_make_track_vars(album, album_metadata, track_metadata, release_metadata):
    if config.setting["track_title_trim_size"]:
        TITLE_LENGTH = config.setting["track_title_trim_size"]
    else:
        TITLE_LENGTH = 0
    album_id = release_metadata['id']
    track_title = track_metadata['title']
    if config.setting["trim_track_titles"] and TITLE_LENGTH and len(track_title) > TITLE_LENGTH:
        track_title = track_title[:TITLE_LENGTH] + '...'
    album_metadata["~TNT"] = track_title
    # Test for valid metadata node for the release
    if 'artist-credit' in track_metadata:
        # Initialize variables to default values
        additional_artist = ""
        full_artist = ""
        artist_count = 0
        # The 'artist-credit' key should always be there.
        # This check is to avoid a runtime error if it doesn't exist for some reason.
        for artist_credit in track_metadata['artist-credit']:
            # Initialize temporary variables for each loop.
            temp_name = ""
            temp_phrase = ""
            # Check if there is a 'joinphrase' specified.
            if 'joinphrase' in artist_credit:
                temp_phrase = artist_credit['joinphrase']
            else:
                metadata_error(album_id, 'artist-credit.joinphrase', metadata_group='track')
            # Check if there is a 'name' specified.
            if 'name' in artist_credit:
                temp_name = artist_credit['name']
            else:
                metadata_error(album_id, 'artist-credit.name', metadata_group='track')
            full_artist += temp_name + temp_phrase
            if artist_count < 1:
                album_metadata["~PTA"] = temp_name
            else:
                additional_artist += temp_name + temp_phrase
            artist_count += 1
    else:
        metadata_error(album_id, 'artist-credit', metadata_group='track')
    if additional_artist:
        album_metadata["~ATA"] = additional_artist
    if full_artist:
        album_metadata["~FTA"] = full_artist
    if artist_count:
        album_metadata["~TAC"] = artist_count
    return None


def metadata_error(album_id, metadata_element, metadata_group='release'):
    log.error("%s: %r: Missing '%s' in %s metadata.",
            PLUGIN_NAME, album_id, metadata_element, metadata_group)


class RdsNamingVarsOptionsPage(OptionsPage):

    NAME = "rds_naming_vars"
    TITLE = "Naming Variables"
    PARENT = "plugins"

    options = [
        config.BoolOption("setting", "trim_album_titles", False),
        config.IntOption("setting", "album_title_trim_size", 50),
        config.BoolOption("setting", "trim_track_titles", False),
        config.IntOption("setting", "track_title_trim_size", 50),
    ]

    def __init__(self, parent=None):
        super(RdsNamingVarsOptionsPage, self).__init__(parent)
        self.ui = Ui_RdsNamingVarsOptionsPage()
        self.ui.setupUi(self)

    def load(self):
        self.ui.trim_album_titles.setChecked(config.setting["trim_album_titles"])
        self.ui.album_title_trim_size.setValue(config.setting["album_title_trim_size"])
        self.ui.trim_track_titles.setChecked(config.setting["trim_track_titles"])
        self.ui.track_title_trim_size.setValue(config.setting["track_title_trim_size"])

    def save(self):
        config.setting["trim_album_titles"] = self.ui.trim_album_titles.isChecked()
        config.setting["album_title_trim_size"] = self.ui.album_title_trim_size.value()
        config.setting["trim_track_titles"] = self.ui.trim_track_titles.isChecked()
        config.setting["track_title_trim_size"] = self.ui.track_title_trim_size.value()


# Register the plugin to run at a LOW priority so that other plugins that
# modify the artist information can complete their processing and this plugin
# is working with the latest updated data.
register_album_metadata_processor(rds_make_album_vars, priority=PluginPriority.LOW)
register_track_metadata_processor(rds_make_track_vars, priority=PluginPriority.LOW)
register_options_page(RdsNamingVarsOptionsPage)
