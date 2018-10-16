# Format Performer Tags \[[Download](https://github.com/rdswift/picard-plugins/raw/2.0_RDS_Plugins/plugins/format_performer_tags/format_performer_tags.zip)\]

## Description

This plugin allows the user to configure the way that instrument and vocal performer tags are written. Once
installed a settings page will be added to Picard's options, which is where the plugin is configured.

These settings will determine the format for any Performer tags prepared. The format is divided into six
parts: the performer; the instrument or vocals; and four user selectable sections for the extra
information. This is set out as:

\[Section 1\]Instrument/Vocals\[Section 2\]\[Section 3\]: Performer\[Section 4\]

You can select the section in which each of the extra information words appears.  These extra information
words are "additional", "guest", "solo" and type of vocal.

For each of the sections you can select the starting character(s), the character(s) separating entries, and
the ending character(s).  Note that leading or trailing spaces must be included in the settings and will not
be automatically added.  If no separator characters are entered, the items will be automatically separated
by a single space.

Note that sections that don't contain any entries for a givien performer tag will not be included in the
tag, including any start or end text configured for the section.

For example, some of the ways that a performer relationship for Billy Preston playing a guest solo on the
Rhodes piano could be configured to be saved include:

* Performer [guest solo rhodes piano]: Billy Preston
* Performer [solo rhodes piano]: Billy Preston (guest)
* Performer [rhodes piano]: Billy Preston (guest solo)
* Performer [rhodes piano, guest solo]: Billy Preston
* Performer [rhodes piano, solo]: Billy Preston (guest)
* Performer [rhodes piano, guest]: Billy Preston (solo)

This shows only a few examples of the many possible displays that can be configured.

## Settings

The first group of settings is the **Keyword Section Assignments**.  This is where you select the section in
which each of the keywords will be displayed.  Selection is made by clicking the radio button corresponding
to the desired section for each of the keywords.

The second group of settings is the **Section Display Settings**.  This is where you configure the text
included at the beginning and end of each section displayed, and the characters used to separate multiple
items within a section.  Note that leading or trailing spaces must be included in the settings and will not
be automatically added.  If no separator characters are entered, the items will be automatically separated
by a single space.

The initial default settings are:

```
Keyword 'additional':  Section 3
Keyword 'guest':       Section 4
Keyword 'solo':        Section 3
All 'vocals' keywords: Section 2

Section 1 starting text:   ''
Section 1 ending text:     ''
Section 1 separator text:  ''

Section 2 starting text:   ', '
Section 2 ending text:     ''
Section 2 separator text:  ''

Section 3 starting text:   ' ('
Section 3 ending text:     ''
Section 3 separator text:  ')'

Section 4 starting text:   ' ('
Section 4 ending text:     ''
Section 4 separator text:  ')'
```

These settings will produce tags such as:

* Performer [rhodes piano (solo)]: Billy Preston (guest)
* Performer [percussion]: Steve Berlin (guest), Kris MacFarlane, Séan McCann
* Performer [vocal, background]: Jeen (guest)
