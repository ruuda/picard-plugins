# Language Name Function

This plugin provides a new scripting function `$language_name()` that allows the user to retrieve the full name for a three-character language code for use within scripts.

## Usage

The function is used as `$language_name(code)`, where `code` is the three-character language code.
It will typically be used to expand the `%language%` and `%_releaselanguage%` tags.

For example, `$language_name(%language%)` will return `English` if the language code is `eng`, or `GwichÊ¼in` if the language code is `gwi`, or `Klingon` if the code is `tlh`. (Yes, Klingon is actually officially recognized in the ISO 639-3 list of languages.)

If an unknown code (or no code) is entered, the function will return an empty string.

## Technical Notes

This function uses the ISO 639-3 (Part 2B) language codes, provided by the www.iso639-3.sil.org website.
