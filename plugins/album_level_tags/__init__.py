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

PLUGIN_NAME = 'Album Level Tags'
PLUGIN_AUTHOR = 'Bob Swift (rdswift)'
PLUGIN_DESCRIPTION = '''
This plugin provides the ability to access album level tags from scripts run during track processing.  The plugin
adds three new scripting functions to set, get and unset variables that are common to all tracks for an album. This
allows things like finding and storing the earliest recording date of all of the tracks on the album.  Each album's
information is stored separately, and is reset when the album is refreshed. The information is cleared when an album
is removed.
<br /><br />
Please see the <a href="https://github.com/rdswift/picard-plugins/blob/2.0_RDS_Plugins/plugins/album_level_tags/docs/README.md">user guide</a> on GitHub for more information.
'''
PLUGIN_VERSION = '0.1'
PLUGIN_API_VERSIONS = ['2.0', '2.1', '2.2']
PLUGIN_LICENSE = 'GPL-2.0-or-later'
PLUGIN_LICENSE_URL = 'https://www.gnu.org/licenses/gpl-2.0.html'

PLUGIN_USER_GUIDE_URL = 'https://github.com/rdswift/picard-plugins/blob/2.0_RDS_Plugins/plugins/album_level_tags/docs/README.md'

from picard import log
from picard.album import register_album_post_removal_processor
from picard.metadata import register_album_metadata_processor
from picard.plugin import PluginPriority
from picard.script import register_script_function, script_function
from picard.script.parser import normalize_tagname


ALBUM_LEVEL_TAGS = {}


def process_error(album_id, error_message):
    log.error("{0}: {1!r}: {2}".format(PLUGIN_NAME, album_id, error_message,))


def album_level_tags_init_album(album, album_metadata, release_metadata):
    album_id = str(album.id)
    ALBUM_LEVEL_TAGS[album_id] = {}
    process_error(album_id, "Initializing tag dictionary for '{0}'.".format(album_id,))


def album_post_removal_processor(album):
    album_id = str(album.id)
    if album_id in ALBUM_LEVEL_TAGS:
        del ALBUM_LEVEL_TAGS[album_id]


@script_function(documentation=N_(
    """`$unsetalbumtag(name)`

Unsets the album tag variable `name`.
"""
))
def func_unsetalbumtag(parser, name):
    id = parser.context['musicbrainz_albumid']
    if id and id in ALBUM_LEVEL_TAGS:
        name = normalize_tagname(name)
        if name in ALBUM_LEVEL_TAGS[id]:
            del ALBUM_LEVEL_TAGS[id][name]
    else:
        process_error(id, "ID not found in album level tags dictionary for $unsetalbumtag({0}).".format(name,))
    return ""


@script_function(documentation=N_(
    """`$setalbumtag(name,value)`

Sets the album tag variable `name` to `value`.
"""
))
def func_setalbumtag(parser, name, value):
    id = parser.context['musicbrainz_albumid']
    if id and id in ALBUM_LEVEL_TAGS:
        name = normalize_tagname(name)
        if name:
            if value:
                ALBUM_LEVEL_TAGS[id][normalize_tagname(name)] = value
            else:
                func_unsetalbumtag(parser, name)
    else:
        process_error(id, "ID not found in album level tags dictionary for $setalbumtag({0},{1}).".format(name, value))
    return ""


@script_function(documentation=N_(
    """`$getalbumtag(name)`

Gets the album tag variable `name`.
"""
))
def func_getalbumtag(parser, name):
    id = parser.context['musicbrainz_albumid']
    if id and id in ALBUM_LEVEL_TAGS:
        name = normalize_tagname(name)
        if name in ALBUM_LEVEL_TAGS[id]:
            return ALBUM_LEVEL_TAGS[id][name]
    else:
        process_error(id, "ID not found in album level tags dictionary for $getalbumtag({0}).".format(name,))
    return ""


# Register the functions
register_album_metadata_processor(album_level_tags_init_album, priority=PluginPriority.HIGH)
register_album_post_removal_processor(album_post_removal_processor)
register_script_function(func_setalbumtag)
register_script_function(func_getalbumtag)
register_script_function(func_unsetalbumtag)
