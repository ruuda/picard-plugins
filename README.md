# Bob Swift's MusicBrainz Picard Plugins

This branch of the picard-plugins repository hosts plugins for [MusicBrainz Picard](https://picard.musicbrainz.org/) that have been developed by Bob Swift (rdswift).  Not all of these plugins have been submitted to the [musicbrainz/picard-plugins](https://github.com/musicbrainz/picard-plugins) repository.  Some have been developed for personal use, and some specialty plugins have been developed on request or in response to discussion in the [MetaBrainz Community Forum](https://community.metabrainz.org/).

Note that all plugins in this branch of the repository are released under the GNU General Public License version 2 ("GPL") or a license compatible with it. See https://www.gnu.org/licenses/license-list.html for a list of compatible licenses.

# Available Plugins

## AlbumArtist Extension \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/albumartistextension/albumartistextension.py)\]

This plugin provides standardized, credited and sorted artist information for the album artist.  This is useful when your tagging or renaming scripts require both the standardized artist name and the credited artist name, or more detailed information about the album artists.

The information is provided in the following variables:

* **_\_aaeStdAlbumArtists_** = The standardized version of the album artists.
* **_\_aaeCredAlbumArtists_** = The credited version of the album artists.
* **_\_aaeSortAlbumArtists_** = The sorted version of the album artists.
* **_\_aaeStdPrimaryAlbumArtist_** = The standardized version of the first (primary) album artist.
* **_\_aaeCredPrimaryAlbumArtist_** = The credited version of the first (primary) album artist.
* **_\_aaeSortPrimaryAlbumArtist_** = The sorted version of the first (primary) album artist.
* **_\_aaeAlbumArtistCount_** = The number of artists comprising the album artist.

PLEASE NOTE: Tagger scripts are required to make use of these hidden variables.


## Data Dumper \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/data_dumper/data_dumper.py)\]

This plugin saves the output for the track and release metadata to a text file.  By default, the file is called 'data_dump.txt' and it is saved in the file naming destination directory.

This can be used to help develop release and track plugins by providing a log of the information passed to the plugin.


## RDS Naming Variables \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/data_dumper/data_dumper.py)\]

This plugin provides specialized album and track variables for use in naming scripts. Note that standardized artist information is used for the Album Artist variables, and credited artist information is used for the Track Artist variables. The information is provided in the following:

* **_\_PAA_** = Primary Album Artist
* **_\_PAAS_** = Primary Album Artist Sort
* **_\_FAA_** = Full Album Artist
* **_\_FAAS_** = Full Album Artist Sort
* **_\_FAAPS_** = Full Album Artist Primary Sort
* **_\_AAC_** = Album Artist(s) Count
* **_\_PTA_** = Primary Track Artist
* **_\_ATA_** = Additional Track Artist(s)
* **_\_FTA_** = Full Track Artist(s)
* **_\_TAC_** = Track Artist(s) Count
* **_\_ANT_** = Album Name Trimmed
* **_\_TNT_** = Track Name Trimmed

PLEASE NOTE: Tagger scripts are required to make use of these hidden variables.


## Release Language Title \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/release_language_title/release_language_title.py)\]

This plugin provides full language title for the release as a variable (_releaselanguagetitle) for use in naming scripts.

PLEASE NOTE: Tagger scripts are required to make use of this hidden variable.

