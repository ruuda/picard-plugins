# Bob Swift's MusicBrainz Picard Plugins

This branch of the picard-plugins repository hosts plugins for [MusicBrainz Picard](https://picard.musicbrainz.org/) that have been developed by Bob Swift (rdswift).  Not all of these plugins have been submitted to the [musicbrainz/picard-plugins](https://github.com/musicbrainz/picard-plugins) repository.  Some have been developed for personal use, and some specialty plugins have been developed on request or in response to discussion in the [MetaBrainz Community Forum](https://community.metabrainz.org/).

Note that all plugins in this branch of the repository are released under the GNU General Public License version 2 ("GPL") or a license compatible with it. See [https://www.gnu.org/licenses/license-list.html](https://www.gnu.org/licenses/license-list.html) for a list of compatible licenses.

-------

## Additional Artists Variables \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/additional_artists_variables/additional_artists_variables.zip)\]

This plugin provides specialized album and track variables for use in naming scripts. It is based on the
"Album Artist Extension" plugin, but expands the functionality to also include track artists. Note that it
cannot be used as a direct drop-in replacement for the "Album Artist Extension" plugin because the variables
are provided with different names.  This will require changes to existing scripts if switching to this plugin.

This plugin reads the album and track metadata provided to Picard and exposes the information in a number
of additional variables for use in Picard scripts.  The plugin has been designed such that the information
is presented consistently regardless of whether or not the `Use standardized artist names` option is selected.
This means that some of the information available through the standard Picard tags will be duplicated in the
variables provided by this plugin.

***NOTE:*** This plugin makes no additional calls to the MusicBrainz website api for the information.

-------
<!--
## Artist Variables \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/artist_variables/artist_variables.zip)\]

This plugin provides specialized album and track variables for use in naming scripts, without any additional calls to the MusicBrainz website api for additional information. The information is provided in the following variables:

### Album Variables

* **_PriAArtistID** - The ID of the primary / first album artist listed
* **_PriAArtistStd** - The primary / first album artist listed (standardized)
* **_PriAArtistCred** - The primary / first album artist listed (as credited)
* **_PriAArtistSort** - The primary / first album artist listed (sort name)
* **_AdditionalAArtistID** - The IDs of all album artists listed except for the primary / first artist, separated by a semicolon and space
* **_AdditionalAArtistStd** - All album artists listed (standardized) except for the primary / first artist, separated with strings provided from the release entry
* **_AdditionalAArtistCred** - All album artists listed (as credited) except for the primary / first artist, separated with strings provided from the release entry
* **_FullAArtistStd** - All album artists listed (standardized), separated with strings provided from the release entry
* **_FullAArtistCred** - All album artists listed (as credited), separated with strings provided from the release entry
* **_FullAArtistSort** - All album artists listed (sort names), separated with strings provided from the release entry
* **_FullAArtistPriSort** - The primary / first album artist listed (sort name) followed by all additional album artists (standardized), separated with strings provided from the release entry
* **_AArtistCount** - The number of artists listed as album artists

### Track Variables

* **_PriTArtistID** - The ID of the primary / first track artist listed
* **_PriTArtistStd** - The primary / first track artist listed (standardized)
* **_PriTArtistCred** - The primary / first track artist listed (as credited)
* **_PriTArtistSort** - The primary / first track artist listed (sort name)
* **_AdditionalTArtistID** - The IDs of all track artists listed except for the primary / first artist, separated by a semicolon and space
* **_AdditionalTArtistStd** - All track artists listed (standardized) except for the primary / first artist, separated with strings provided from the track entry
* **_AdditionalTArtistCred** - All track artists listed (as credited) except for the primary / first artist, separated with strings provided from the track entry
* **_FullTArtistStd** - All track artists listed (standardized), separated with strings provided from the track entry
* **_FullTArtistCred** - All track artists listed (as credited), separated with strings provided from the track entry
* **_FullTArtistSort** - All track artists listed (sort names), separated with strings provided from the track entry
* **_FullTArtistPriSort** - The primary / first track artist listed (sort name) followed by all additional track artists (standardized), separated with strings provided from the track entry
* **_TArtistCount** - The number of artists listed as track artists

**PLEASE NOTE**: Tagger scripts are required to make use of these hidden variables.

-------
-->

## Keep Only Tags \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/keep_only_tags/keep_only_tags.zip)\]

This plugin allows the user to determine which tags are written to the output files by Picard. Tags that you wish to keep are entered in a page
in the options settings, with each tag on a separate line. Blank lines will be ignored. The entries are not case-sensitive.

If a tag in the list ends with an asterisk (\*), then it will keep any tags beginning with the tag.  For example, if your list contains "**performer:\***"
then all tags beginning with "**performer:**" will be kept, such as "**performer:instrument**" and "**performer:vocals**".

All tags that are removed will still be available as variables with "**\_ko\_**" prepended to the tag name. For example, if you choose not to keep the
"**musicbrainz_trackid**" tag, it will still be available to scripts as "**_ko_musicbrainz_trackid**".

---

## Album Level Tags \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/album_level_tags/album_level_tags.zip)\]

This plugin provides the ability to access album level tags from scripts run during track processing.  The plugin
adds three new scripting functions to set, get and unset variables that are common to all tracks for an album. This
allows things like finding and storing the earliest recording date of all of the tracks on the album.  Each album's
information is stored separately, and is reset when the album is refreshed. The information is cleared when an album
is removed.

--------
## Data Dumper \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/data_dumper/data_dumper.zip)\]

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

## Language Name \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/language_name/language_name.zip)\]

This plugin provides a new scripting function `$language_name()` that allows the user to retrieve the full name for a three-character language code for use within scripts.

Please see the [user guide](https://github.com/rdswift/picard-plugins/blob/2.0_RDS_Plugins/plugins/language_name/docs/README.md) for more information.

-------

## Search Engine Lookup \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/search_engine_lookup/search_engine_lookup.zip)\]

This plugin adds a right click option on a cluster, providing the ability to lookup the cluster using a search engine in a browser window.

Please see the [user guide](https://github.com/rdswift/picard-plugins/blob/2.0_RDS_Plugins/plugins/search_engine_lookup/docs/README.md) for more information.

-------

## Label Variables \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/label_variables/label_variables.zip)\]

This plugin provides variables containing label information for a release for use in user or file naming scripts.

Please see the [user guide](https://github.com/rdswift/picard-plugins/blob/2.0_RDS_Plugins/plugins/label_variables/README.md) for more information.

<!--

-------

## Release Language Title \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/release_language_title/release_language_title.py)\]

This plugin provides full language title for the release as a variable (_releaselanguagetitle) for use in naming scripts.  See the [discussion](https://community.metabrainz.org/t/help-with-file-naming-with-special-rule-for-soundtracks/398631) on the MetaBrainz Community Forum.

**PLEASE NOTE**: Tagger scripts are required to make use of this hidden variable.
-->
