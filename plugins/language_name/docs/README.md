# Language Name Function

This plugin provides a new scripting function `$language_name()` that allows the user to retrieve the full name for a three-character language code for use within scripts.

## Usage

The function is used as `$language_name(code)`, where `code` is the three-character language code.
It will typically be used to expand the `%language%` and `%_releaselanguage%` tags.

The language used for the return values will be based on the user's interface language set in the Picard options.  Languages currently supported are English, French, German, Spanish, Dutch, Russian and Chinese.  Note that some translations may be incorrect or incomplete, and any help correcting / completing the current translations or translation to other languages would be appreciated.  English is the language used for all user interface languages not currently supported.

For example, assuming the user interface is set to english, `$language_name(%language%)` will return `English` if the language code is `eng`, or `Gwich´in` if the language code is `gwi`, or `Klingon` if the code is `tlh`. (Yes, Klingon is actually officially recognized in the ISO 639-3 list of languages.)

If an unknown code is entered, the function will return `unknown`.  If there is no code entered, `missing` will be returned.

## Technical Notes

This function uses a subset of the ISO 639-3 language codes as found on the [Wikipedia](https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes) website.
