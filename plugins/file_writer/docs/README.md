# File Writer \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/file_writer/file_writer.zip)\]

## Overview

This plugin adds scripting functions to allow writing text to an output file, and sanitizing text to ensure that it is suitable for use in a file path.

Usage: **$writeline(file,text\[,reset\])**

This will write `text` (followed by a newline) to `file`.  The text will be appended to the file unless `reset` is set, in which case the file will be overwritten.  If the destination `file` path is not specified as an absolute path to the destination file (beginning with a Windows drive letter and colon or path separator), then the path will be considered relative to the ***Destination directory*** specified in Picard's **File Naming Options** settings.  If the target path does not exist, it will be created automatically.

***NOTE:*** The text will be written to the file with a character encoding of UTF-8.

Usage: **$sanitize_text(text)**

This will return a sanitized version of `text` suitable for use in a file path, including applying the ***Replace non-ASCII characters***, ***Windows compatibility*** and ***Replace directory separators with*** settings specified in Picard's **File Naming Compatibility** settings.

***NOTE:*** It is strongly recommended to use the `$sanitize_text()` function on all tags used in defining the file path used in the `$writeline()` function to avoid inconsistencies that might occur due to a tag including a directory separator (/) or incompatible characters.

## Examples

### Example 1

The following will write a text file containing a list of all the tracks on an album.  The file name will be in the form "AlbumArtist - Album" and will be written in the main output directory.

```
$set(_reset,$if($and($lt(%discnumber%,2),$lt(%tracknumber%,2)),1,))
$set(_filename,$sanitize_text(%albumartist% - %album%))
$writeline(%_filename%,$if($gt(%totaldiscs%,1)$num(%discnumber%,2)-)$num(%tracknumber%,2) %title%,%_reset%)
```

### Example 2

Similar to Example 1, the following will write a text file containing a list of all the tracks on an album.  The file name will be in the form "AlbumArtist - Album" and will be written in a separate Windows directory called `C:\Albums`.

```
$set(_reset,$if($and($lt(%discnumber%,2),$lt(%tracknumber%,2)),1,))
$set(_filename,$sanitize_text(%albumartist% - %album%))
$writeline(C:\\Albums\\%_filename%,$if($gt(%totaldiscs%,1),$num(%discnumber%,2)-)$num(%tracknumber%,2) %title%,%_reset%)
```

### Example 3

The following will keep a log of all albums processed.  The file will be written to the `/var/log/PicardProcessing` file on a Linux system.  Note that this should be added to the file renaming script so that the log entry is only written when the release is saved.

```
$if($and($lt(%discnumber%,2),$lt(%tracknumber%,2)),
  $writeline(/var/log/PicardProcessing,$datetime(): %musicbrainz_albumid% : %albumartist% - %album%)
)
```
