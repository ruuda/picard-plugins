PLUGIN_NAME = 'Language Name'
PLUGIN_AUTHOR = 'Bob Swift (rdswift)'
PLUGIN_DESCRIPTION = '''
This plugin provides a new script function $language_name() to replace the
three-character language code with the full name of the language.
<br /><br />
By default, the language used for the return values will be based on the
user's interface language set in the Picard options.  This can be overridden
in the 'Scripting'->'Language Name' section of Picard's options settings.
<br /><br />
Languages currently supported are English, French, German, Spanish, Dutch,
Russian and Chinese.  Note that some translations may be incorrect or incomplete.
Any help correcting / completing the current translations or translation to other
languages would be appreciated.  English is the language used for all user
interface languages not currently supported.
'''

###############################################################################
#
#  ISO 639-3 codes: https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes
#
#  Contributors to this plugin:
#       rdswift (Bob Swift)     - original author
#       hiccup                  - Dutch translations
#
###############################################################################

PLUGIN_VERSION = "0.3"
PLUGIN_API_VERSIONS = ["2.0"]
PLUGIN_LICENSE = "GPL-2.0-or-later"
PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-2.0.html"

PLUGIN_USER_GUIDE_URL = "https://github.com/rdswift/picard-plugins/blob/2.0_RDS_Plugins/plugins/language_name/docs/README.md"

import string
from picard import config, log
from picard.script import register_script_function
from picard.const import UI_LANGUAGES
from picard.ui.options import register_options_page, OptionsPage
from picard.plugins.language_name.ui_options_language_name import Ui_LanguageNameOptionsPage

SUPPORTED_LANGUAGES = ['en', 'fr', 'de', 'es', 'nl', 'ru', 'zh']

def language_name(parser, text):
    if text:
        return LanguageList.get_language(text.lower())
    return 'missing'

###############################################################################
#
#  Use a new class to hold language names to allow configuration settings to
#  be loaded before selecting the language file to load.  The selected output
#  language is checked with each language name lookup, and the language file
#  is only loaded / reloaded if the selected output language has changed.
#  This allows changing the selection without having to restart Picard.
#
###############################################################################

class LanguageList():

    RETURN_LANGUAGE = ''
    LANGUAGE_LIST = {}

    def __init__(self):
        pass

    @classmethod
    def get_language(cls, text):
        user_lang = config.setting['ui_language'][:2]
        user_lang = user_lang if (user_lang in SUPPORTED_LANGUAGES) else 'en'
        old_lang = cls.RETURN_LANGUAGE
        if ((config.setting['language_name_override']) and (config.setting['language_name_language'] in SUPPORTED_LANGUAGES)):
            new_lang = config.setting['language_name_language']
        else:
            new_lang = user_lang

        if new_lang != old_lang:
            log.debug("{0}: Selected language changed from '{1}' to '{2}'".format(PLUGIN_NAME, old_lang, new_lang,))

            if new_lang == 'en':
                from picard.plugins.language_name.languages_en import LANGUAGE_LIST
            elif new_lang == 'de':
                from picard.plugins.language_name.languages_de import LANGUAGE_LIST
            elif new_lang == 'fr':
                from picard.plugins.language_name.languages_fr import LANGUAGE_LIST
            elif new_lang == 'es':
                from picard.plugins.language_name.languages_es import LANGUAGE_LIST
            elif new_lang == 'nl':
                from picard.plugins.language_name.languages_nl import LANGUAGE_LIST
            elif new_lang == 'ru':
                from picard.plugins.language_name.languages_ru import LANGUAGE_LIST
            elif new_lang == 'zh':
                from picard.plugins.language_name.languages_zh import LANGUAGE_LIST
            else:
                new_lang = 'en'
                from picard.plugins.language_name.languages_en import LANGUAGE_LIST
            cls.RETURN_LANGUAGE = new_lang
            cls.LANGUAGE_LIST = dict(LANGUAGE_LIST)
            log.debug("{0}: Loaded language list for '{1}'".format(PLUGIN_NAME, new_lang,))
        if text:
            return cls.LANGUAGE_LIST[text.lower()] if ((text.lower() in cls.LANGUAGE_LIST) and cls.LANGUAGE_LIST[text.lower()]) else 'unknown'
        return 'missing'


class LanguageNameOptionsPage(OptionsPage):

    NAME = "language_name"
    TITLE = "Language Name"
    PARENT = "scripting"

    options = [
        config.BoolOption("setting", "language_name_override", False),
        config.TextOption("setting", "language_name_language", 'en'),
    ]

    def __init__(self, parent=None):
        super(LanguageNameOptionsPage, self).__init__(parent)
        self.ui = Ui_LanguageNameOptionsPage()
        self.ui.setupUi(self)

        temp = {}
        language_list = [(l[0], l[1], _(l[2])) for l in UI_LANGUAGES]
        for lang_code, native, translation in language_list:
            if native and native != translation:
                name = '%s (%s)' % (translation, native)
            else:
                name = translation
            lang_code = lang_code[:2]
            if (lang_code in SUPPORTED_LANGUAGES) and not (lang_code in temp):
                temp[lang_code] = name
        for lang_code in sorted(temp):
            self.ui.language_name_language.addItem(temp[lang_code], lang_code)

    def load(self):
        # Settings
        self.ui.language_name_override.setChecked(config.setting["language_name_override"])
        current_language = config.setting["language_name_language"] if (config.setting["language_name_language"] in SUPPORTED_LANGUAGES) else 'en'
        self.ui.language_name_language.setCurrentIndex(self.ui.language_name_language.findData(current_language))

    def save(self):
        config.setting['language_name_override'] = self.ui.language_name_override.isChecked()
        config.setting['language_name_language'] = self.ui.language_name_language.itemData(self.ui.language_name_language.currentIndex())


register_script_function(language_name)
register_options_page(LanguageNameOptionsPage)
