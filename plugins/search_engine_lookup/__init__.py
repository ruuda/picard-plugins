# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Bob Swift (rdswift)
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

PLUGIN_NAME = 'Search Engine Lookup'
PLUGIN_AUTHOR = 'Bob Swift'
PLUGIN_DESCRIPTION = '''Adds a right click option on a cluster to look up album information using a search engine in a browser window.'''
PLUGIN_VERSION = '0.0.1'
PLUGIN_API_VERSIONS = ['2.2', '2.3']
PLUGIN_LICENSE = "GPL-2.0"
PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-2.0.txt"

from urllib.parse import quote_plus

from picard import log
from picard.cluster import Cluster
from picard.ui.itemviews import BaseAction, register_cluster_action
from picard.util.webbrowser2 import open


class SearchEngineLookup(BaseAction):
    NAME = 'Search engine lookup'

    def callback(self, cluster_list):
        ENGINE = r'https://www.google.com/search?q='
        for cluster in cluster_list:
            if isinstance(cluster, Cluster):
                parts = []
                url = ENGINE
                if 'albumartist' in cluster.metadata and cluster.metadata['albumartist']:
                    parts.extend(str(cluster.metadata['albumartist']).split())
                if 'album' in cluster.metadata and cluster.metadata['albumartist']:
                    parts.append('album')
                    parts.extend(str(cluster.metadata['album']).split())
                if parts:
                    url = ENGINE + quote_plus(' '.join(parts))
                    log.debug("{0}: Looking up {1}".format(PLUGIN_NAME, url,))
                    open(url)
                else:
                    log.error("{0}: No existing metadata to lookup.".format(PLUGIN_NAME,))
            else:
                log.error("{0}: Argument is not a cluster. {1}".format(PLUGIN_NAME, cluster,))


register_cluster_action(SearchEngineLookup())
