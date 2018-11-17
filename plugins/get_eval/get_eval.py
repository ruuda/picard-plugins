PLUGIN_NAME = 'Get Eval Function'
PLUGIN_AUTHOR = 'Bob Swift (rdswift)'
PLUGIN_DESCRIPTION = '''
This plugin provides the ability to evaluate specified code within Picard
and return the results as a string for use within scripts.
'''

PLUGIN_VERSION = "0.1"
PLUGIN_API_VERSIONS = ["2.0"]
PLUGIN_LICENSE = "GPL-2.0 or later"
PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-2.0.html"

from picard import log
from picard.script import register_script_function


def get_eval(parser, text):
    return_value = ""
    if text:
        try:
            return_value = "{0}".format(eval(text))
        except Exception as ex:
            return_value = ""
            log.error("%s: Exception: %s",
                    PLUGIN_NAME, ex)
            log.error("%s: Invalid evaluation argument: `%s`",
                    PLUGIN_NAME, text)
    log.debug("%s: Input: `%s`  ===>  Output: `%s`",
            PLUGIN_NAME, text, return_value)
    return return_value

register_script_function(get_eval)
