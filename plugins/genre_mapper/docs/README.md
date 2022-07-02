# Genre Mapper \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/genre_mapper/genre_mapper.zip)\]

## Overview

This plugin provides the ability to standardize genres in the "genre" tag by matching the genres as found to a standard genre as defined in the genre replacement mapping configuration option. Once installed a settings page will be added to Picard's options, which is where the plugin is configured.

This plugin is set to run at low priority so that any other plugins that might affect the list of genres are processed first.

---

## Settings

The settings panel allows the user to provide a list of the original/replacement pairs used to modify the genres provided in the "genre" tag. Each pair must be entered on a separate line in the form:

```
[genre match test string]=[replacement genre]
```

Supported wildcards in the test string part of the mapping include '*' and '?' to match any number of characters and a single character respectively.  Blank lines and lines beginning with an equals sign (=) will be ignored. If the replacement part of the pair is blank, any matching genres will be removed. Case-insensitive tests are used when matching. Replacements will be made in the order they are found in the list.

There is also a setting which allows the user to choose whether or not to apply the first matching pair only, or continue processing the remaining pairs with the updated genre.  By default, all of the pairs are processed.

---

## Examples

### Example 1

Suppose that you want to combine all the different types of rock genres (e.g. Country Rock, Hard Rock, Progressive Rock, Punk Rock, Rock 'n' Roll) into a single "Rock" entry.  This could be done using the following matching pairs configuration:

```
=============================
= Combine all "Rock" genres =
=============================
*rock*=Rock
```


### Example 2

Similar to Example 1, except that you want to keep "Punk Rock" separate from "Rock".  This could be done by enabling the "Apply only the first matching replacement" option and using the following matching pairs configuration:

```
====================
= Keep "Punk Rock" =
====================
punk rock=Punk Rock

=============================
= Combine all "Rock" genres =
=============================
*rock*=Rock
```

This would cause a genre of "Punk Rock" to match the first test, keep the genre as "Punk Rock" and stop processing that genre entry.  If the "Apply only the first matching replacement" option was not enabled, processing would continue and the next match would change the genre to "Rock".


### Example 3

Similar to Example 2, except that you want to keep processing rather than stop on the first match.  This could be done by disabling the "Apply only the first matching replacement" option and using the following matching pairs configuration:

```
================================================
= Keep "Punk Rock" as temporary "Temp1" tag so =
= that it doesn't match any following lines    =
================================================
punk rock=Temp1

=============================
= Combine all "Rock" genres =
=============================
*rock*=Rock

===========================================
= Additional processing pairs as required =
===========================================

==============================================
= Change the "Temp1" tag back to "Punk Rock" =
==============================================
temp1=Punk Rock
```

This would cause a genre of "Punk Rock" to match the first test, changing the genre to "Temp1" (not matched in any of the following processing pairs) and continue processing.  The final processing pair matches the "Temp1" genre set earlier and changes the genre back to "Punk Rock".
