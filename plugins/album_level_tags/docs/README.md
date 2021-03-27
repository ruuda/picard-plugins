# Album Level Tags \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/album_level_tags/album_level_tags.zip)\]

## Overview

This plugin provides the ability to access album level tags from scripts run during track processing.  The plugin
adds three new scripting functions to set, get and unset variables that are common to all tracks for an album. This
allows things like finding and storing the earliest recording date of all of the tracks on the album.  Each album's
information is stored separately, and is reset when the album is refreshed. The information is cleared when an album
is removed.

## What it Does

This plugin creates a temporary storage dictionary in Picard each time an album is retrieved from MusicBrainz.
Information can be added, updated, retrieved or removed from the dictionary, and the information stored is consistent
across all of the tracks for the album.  When the album is removed from Picard, all of the information in the temporary
dictionary is removed and the memory released.

***NOTE:*** This plugin makes no additional calls to the MusicBrainz website api for the information.

## Scripting Functions Added

The plugin adds three new scripting functions:

### $setalbumtag(name,value)

This records the `value` in an album-specific dictionary under the key `name`.

### $getalbumtag(name)

This retrieves the `value` for the key `name` from an album-specific dictionary.

### $unsetalbumtag(name)

This removes the `value` for the key `name` from an album-specific dictionary.

## Examples

### Example 1:

Find the earliest recording date of any of the tracks on the album, so that it can be used in the file naming script.

Create a tagging script containing the following:

```
$set(_testdate1,$if2($getalbumtag(earliest_date),9999))
$setalbumtag(earliest_date,$min(%_testdate1%,$if2(%_recording_firstreleasedate%,9999)))
```

The date for the album is now available in the file naming script using `$getalbumtag(earliest_date)`.

### Example 2:

Get a list of all tracks on the album so that it can be included as a tag in each of the tracks.

Create a tagging script containing the following:

```
$setalbumtag(all_tracks,$if($getalbumtag(all_tracks),; )%tracknumber%. %title%)
```

Now to make the combined list available as a tag for all tracks, you need to create another tagging script after the previous one containing the following:

```
$set(all_tracks,$getalbumtag(all_tracks))
```

The complete track list will now be stored in each of the track files under the tag name `all_tracks`.
