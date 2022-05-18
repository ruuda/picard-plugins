# Text Compare Functions \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/text_compare_functions/text_compare_functions.zip)\]

## Overview

This plugin provides text-based comparison scripting functions similar to the integer-based comparison functions
`$lt()`, `$lte()`, `$gt()` and `$gte()`, plus two additional functions to find the minimum and maximum values using
a text-based comparison.  These can be used for comparing non-integer values such as dates.

## Scripting Functions Added

This plugin adds six new scripting functions to allow text-based operations:

### $tlt(x,y)

Returns true if `x` is less than `y` using a text comparison.

### $tlte(x,y)

Returns true if `x` is less than or equal to `y` using a text comparison.

#### $tgt(x,y)

Returns true if `x` is greater than `y` using a text comparison.

### $tgte(x,y)

Returns true if `x` is greater than or equal to `y` using a text comparison.

### $tmin(x,...)

Returns the minimum value using a text comparison.
Can be used with an arbitrary number of arguments.

### $tmax(x,...)

Returns the maximum value using a text comparison.
Can be used with an arbitrary number of arguments.

## Examples

### Example 1:

Determine if the release is a re-issue based on the release date, so that it can be
used in the file naming script.

```
$set(_type,$if($and(%date%,%originaldate%),$if($tgt(%date%,%originaldate%),Original Release,Re-Release),Unknown))
```

### Example 2:

Find the earliest of recording date or release date.

```
$set(_type,$if($or(%date%,%originaldate%),$tmin($if2(%date%,9999-12-31),$if2(%date%,9999-12-31)),0000-00-00))
```
