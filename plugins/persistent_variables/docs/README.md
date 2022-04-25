# Persistent Variables \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/persistent_variables/persistent_variables.zip)\]

## Overview

This plugin provides the ability to store and retrieve script variables that persist across tracks and albums.
This allows things like finding and storing the earliest recording date of all of the tracks on an album.

There are two types of persistent variables maintained - album variables and session variables. Album variables
persist across all tracks on an album.  Each album's information is stored separately, and is reset when the
album is refreshed. The information is cleared when an album is removed.  Session variables persist across all
albums and tracks, and are cleared when Picard is shut down or restarted.

## Scripting Functions Added

This plugin adds eight new scripting functions to allow management of persistent script variables:

### $set_a(name,value)

Sets the album persistent variable `name` to `value`.

### $unset_a(name)

Unsets the album persistent variable `name`.

### $get_a(name)

Gets the album persistent variable `name`.

### $clear_a()

Clears all album persistent variables.

### $set_s(name,value)

Sets the session persistent variable `name` to `value`.

### $unset_s(name)

Unsets the session persistent variable `name`.

### $get_s(name)

Gets the session persistent variable `name`.

### $clear_s()

Clears all session persistent variables.

## Persistent Variables Viewer

You can view the persistent variables currently set by right-clicking on a file, track or album and selecting "View
persistent variables" from the Plugins section of the context menu.  This will display the variables associated with
the selected album as well as all session variables.

## Examples

### Example 1:

Find the earliest recording date of any of the tracks on the album, so that it can be used in the file naming script.

Create a tagging script containing the following:

```
$set(_testdate1,$if2($get_a(earliest_date),9999))
$set_a(earliest_date,$min(%_testdate1%,$if2(%_recording_firstreleasedate%,9999)))
```

The date for the album is now available in the file naming script using `$get_a(earliest_date)`.

### Example 2:

Get a list of all tracks on the album so that it can be included as a tag in each of the tracks.

Create a tagging script containing the following:

```
$set_a(all_tracks,$if($get_a(all_tracks),; )%tracknumber%. %title%)
```

Now to make the combined list available as a tag for all tracks, you need to create another tagging script after the previous one containing the following:

```
$set(all_tracks,$get_a(all_tracks))
```

The complete track list will now be stored in each of the track files under the tag name `all_tracks`.
