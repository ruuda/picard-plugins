# Bob Swift's MusicBrainz Picard Plugins

This branch of the picard-plugins repository hosts plugins for [MusicBrainz Picard](https://picard.musicbrainz.org/) that have been developed by Bob Swift (rdswift).  Not all of these plugins have been submitted to the [musicbrainz/picard-plugins](https://github.com/musicbrainz/picard-plugins) repository.  Some have been developed for personal use, and some specialty plugins have been developed on request or in response to discussion in the [MetaBrainz Community Forum](https://community.metabrainz.org/).

Note that all plugins in this branch of the repository are released under the GNU General Public License version 2 ("GPL") or a license compatible with it. See https://www.gnu.org/licenses/license-list.html for a list of compatible licenses.

-------

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

**PLEASE NOTE**: Tagger scripts are required to make use of these hidden variables.

-------

## Data Dumper \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/data_dumper/data_dumper.py)\]

This plugin saves the output for the track and release metadata to a text file.  By default, the file is called 'data_dump.txt' and it is saved in the file naming destination directory.

This can be used to help develop release and track plugins by providing a log of the information passed to the plugin.

-------

## Format Performer Tags \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/format_performer_tags/format_performer_tags.zip)\]

This plugin allows the user to configure the way that instrument and vocal performer tags are written. Once
installed a settings page will be added to Picard's options, which is where the plugin is configured.

Please see the [user guide](https://github.com/rdswift/picard-plugins/blob/2.0_RDS_Plugins/plugins/format_performer_tags/docs/README.md) for more information.

-------

## Get Eval Function \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/get_eval/get_eval.zip)\]
This plugin provides a new scripting function `$get_eval()` that allows the user to evaluate specified python code within Picard and return the results as a string for use within scripts.

This allows access to all metadata fields and the ability to use native python processing commands directly from a script without having to create and load additional plugins. 

Please see the [user guide](https://github.com/rdswift/picard-plugins/blob/2.0_RDS_Plugins/plugins/get_eval/README.md) for more information.

-------

## Performer Tag Replace \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/performer_tag_replace/performer_tag_replace.zip)\]

This plugin provides the ability to replace text in performer tags. Once installed a settings page will be
added to Picard's options, which is where the plugin is configured.

Please see the [user guide](https://github.com/rdswift/picard-plugins/blob/2.0_RDS_Plugins/plugins/performer_tag_replace/docs/README.md) for more information.

-------

## RDS Naming Variables \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/rds_naming_vars/rds_naming_vars.zip)\]

This plugin provides specialized album and track variables for use in naming scripts. Note that standardized artist information is used for the Album Artist variables, and credited artist information is used for the Track Artist variables. The information is provided in the following, with examples based on the artist being a collection of three artists ("Sarah Blackwood, Jenni Pleau & Emily Bones"):

* **_\_PAA_** = Primary Album Artist (e.g. "Sarah Blackwood")
* **_\_PAAS_** = Primary Album Artist Sort (e.g. "Blackwood, Sarah")
* **_\_FAA_** = Full Album Artist (e.g. "Sarah Blackwood, Jenni Pleau & Emily Bones")
* **_\_FAAS_** = Full Album Artist Sort (e.g. "Blackwood, Sarah, Pleau, Jenni & Bones, Emily")
* **_\_FAAPS_** = Full Album Artist Primary Sort (e.g. "Blackwood, Sarah, Jenni Pleau & Emily Bones")
* **_\_AAC_** = Album Artist(s) Count (e.g. 3)
* **_\_PTA_** = Primary Track Artist (e.g. "Sarah Blackwood")
* **_\_ATA_** = Additional Track Artist(s) (e.g. "Jenni Pleau & Emily Bones")
* **_\_FTA_** = Full Track Artist(s) (e.g. "Sarah Blackwood, Jenni Pleau & Emily Bones")
* **_\_TAC_** = Track Artist(s) Count (e.g. 3)
* **_\_ANT_** = Album Name Trimmed
* **_\_TNT_** = Track Name Trimmed

**PLEASE NOTE**: Tagger scripts are required to make use of these hidden variables.

-------

## Release Language Title \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/release_language_title/release_language_title.py)\]

This plugin provides full language title for the release as a variable (_releaselanguagetitle) for use in naming scripts.  See the [discussion](https://community.metabrainz.org/t/help-with-file-naming-with-special-rule-for-soundtracks/398631) on the MetaBrainz Community Forum.

**PLEASE NOTE**: Tagger scripts are required to make use of this hidden variable.

