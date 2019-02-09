PLUGIN_NAME = 'Language Name Function'
PLUGIN_AUTHOR = 'Bob Swift (rdswift)'
PLUGIN_DESCRIPTION = '''
This plugin provides a new script function to replace the
three-character language code with the full name of the language.
'''

##########################################################################
#
#   The ISO 639-3 language codes were provided by www.iso639-3.sil.org
#
#   Contributors to this plugin:
#       Bob Swift (rdswift) - original author
#
##########################################################################

PLUGIN_VERSION = "0.2"
PLUGIN_API_VERSIONS = ["2.0"]
PLUGIN_LICENSE = "GPL-2.0-or-later"
PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-2.0.html"

PLUGIN_USER_GUIDE_URL = "https://github.com/rdswift/picard-plugins/blob/2.0_RDS_Plugins/plugins/language_name/docs/README.md"

import string
from picard import config
from picard.script import register_script_function

UI_LANGUAGE = config.setting['ui_language'][:2] if ('ui_language' in config.setting) else 'en'
if UI_LANGUAGE == 'en':
    from picard.plugins.language_name.languages_en import LANGUAGE_LIST
elif UI_LANGUAGE == 'de':
    from picard.plugins.language_name.languages_de import LANGUAGE_LIST
elif UI_LANGUAGE == 'fr':
    from picard.plugins.language_name.languages_fr import LANGUAGE_LIST
elif UI_LANGUAGE == 'es':
    from picard.plugins.language_name.languages_es import LANGUAGE_LIST
elif UI_LANGUAGE == 'nl':
    from picard.plugins.language_name.languages_nl import LANGUAGE_LIST
elif UI_LANGUAGE == 'ru':
    from picard.plugins.language_name.languages_ru import LANGUAGE_LIST
elif UI_LANGUAGE == 'zh':
    from picard.plugins.language_name.languages_zh import LANGUAGE_LIST
else:
    from picard.plugins.language_name.languages_en import LANGUAGE_LIST

def language_name(parser, text):
    if text:
        return LANGUAGE_LIST[text.lower()] if ((text.lower() in LANGUAGE_LIST) and LANGUAGE_LIST[text.lower()]) else 'unknown'
    return 'missing'

register_script_function(language_name)
