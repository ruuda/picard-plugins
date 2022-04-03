# Key Wheel Converter \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/key_wheel_converter/key_wheel_converter.zip)\]

## Overview

This plugin provides the ability to convert key information between 'camelot', 'open key', 'standard' and 'traktor' formats.
It adds four new scripting functions:

* **$key2camelot(key)** returns the key string `key` in camelot key format.
* **$key2openkey(key)** returns the key string `key` in open key format.
* **$key2standard(key\[,symbols\])** returns the key string `key` in standard key format.  If the optional argument `symbols` is set, then the '♭' and '#' symbols will be used, rather than spelling out '-Flat' and '-Sharp'.
* **$key2traktor(key)** returns the key string `key` in traktor key format.

The `key` argument can be entered in any of the supported formats, such as '2B' (camelot), '6d' (open key), 'A♭ Minor' (standard with symbols), 'A-Flat Minor' (standard with text) or 'C#' (traktor).  If the `key` argument is not recognized as one of the standard keys in the supported formats, then an empty string will be returned.
