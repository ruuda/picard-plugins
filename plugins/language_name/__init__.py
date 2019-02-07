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

PLUGIN_VERSION = "0.1"
PLUGIN_API_VERSIONS = ["2.0"]
PLUGIN_LICENSE = "GPL-2.0-or-later"
PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-2.0.html"

PLUGIN_USER_GUIDE_URL = "https://github.com/rdswift/picard-plugins/blob/2.0_RDS_Plugins/plugins/language_name/docs/README.md"

import string
from picard.plugins.language_name.language_list import LANGUAGE_LIST
from picard.script import register_script_function

def language_name(parser, text):
    if text:
        return LANGUAGE_LIST[text.lower()] if LANGUAGE_LIST[text.lower()] else ''
    return ''

register_script_function(language_name)
