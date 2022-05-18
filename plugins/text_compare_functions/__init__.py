# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 Bob Swift (rdswift)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.

PLUGIN_NAME = 'Text Compare Functions'
PLUGIN_AUTHOR = 'Bob Swift (rdswift)'
PLUGIN_DESCRIPTION = '''
<p>
This plugin provides text-based comparison scripting functions similar to the integer-based comparison functions
`$lt()`, `$lte()`, `$gt()` and `$gte()`, plus two additional functions `$tmin()` and `$tmax()` to find the minimum
and maximum values using a text-based comparison.  These can be used for comparing non-integer values such as dates.
</p><p>
Please see the <a href="https://github.com/rdswift/picard-plugins/blob/2.0_RDS_Plugins/plugins/text_compare_functions/docs/README.md">user guide</a> on GitHub for more information.
</p>
'''
PLUGIN_VERSION = '0.1'
PLUGIN_API_VERSIONS = ['2.0', '2.1', '2.2', '2.3', '2.4', '2.6', '2.7']
PLUGIN_LICENSE = 'GPL-2.0-or-later'
PLUGIN_LICENSE_URL = 'https://www.gnu.org/licenses/gpl-2.0.html'

PLUGIN_USER_GUIDE_URL = 'https://github.com/rdswift/picard-plugins/blob/2.0_RDS_Plugins/plugins/text_compare_functions/docs/README.md'

from picard.script import register_script_function


def func_tlt(parser, x, y):
    """Text based less than test.

    Tests:

    >>> func_tlt(None, 'A', 'B')
    '1'
    >>> func_tlt(None, 'B', 'A')
    ''
    """
    return "1" if x < y else ""


def func_tlte(parser, x, y):
    """Text based less than or equal to test.

    Tests:

    >>> func_tlte(None, 'A', 'B')
    '1'
    >>> func_tlte(None, 'A', 'A')
    '1'
    >>> func_tlte(None, 'B', 'A')
    ''
    """
    return "" if x > y else "1"


def func_tgt(parser, x, y):
    """Text based greater than test.

    Tests:

    >>> func_tgt(None, 'A', 'B')
    ''
    >>> func_tgt(None, 'B', 'A')
    '1'
    """
    return "1" if x > y else ""


def func_tgte(parser, x, y):
    """Text based greater than or equal to test.

    Tests:

    >>> func_tgte(None, 'A', 'B')
    ''
    >>> func_tgte(None, 'A', 'A')
    '1'
    >>> func_tgte(None, 'B', 'A')
    '1'
    """
    return "" if x < y else "1"


def func_tmin(parser, *args):
    """Text based minimum extractor.

    Tests:

    >>> func_tmin(None, 'A', 'B', 'C')
    'A'
    >>> func_tmin(None, 'C', 'B', 'A')
    'A'
    >>> func_tmin(None, 'A')
    'A'
    >>> func_tmin(None)
    ''
    """
    if args:
        return min(args)
    return ""


def func_tmax(parser, *args):
    """Text based maximum extractor.

    Tests:

    >>> func_tmax(None, 'A', 'B', 'C')
    'C'
    >>> func_tmax(None, 'C', 'B', 'A')
    'C'
    >>> func_tmax(None, 'A')
    'A'
    >>> func_tmax(None)
    ''
    """
    if args:
        return max(args)
    return ""


# Register the new functions
register_script_function(func_tlt, name='tlt',
    documentation="""`$tlt(x,y)`

Returns true if `x` is less than `y` using a text comparison.""")

register_script_function(func_tlte, name='tlte',
    documentation="""`$tlte(x,y)`

Returns true if `x` is less than or equal to `y` using a text comparison.""")

register_script_function(func_tgt, name='tgt',
    documentation="""`$tgt(x,y)`

Returns true if `x` is greater than `y` using a text comparison.""")

register_script_function(func_tgte, name='tgte',
    documentation="""`$tgte(x,y)`

Returns true if `x` is greater than or equal to `y` using a text comparison.""")

register_script_function(func_tmin, name='tmin',
    documentation="""`$tmin(x,...)`

Returns the minimum value using a text comparison.
Can be used with an arbitrary number of arguments.""")

register_script_function(func_tmax, name='tmax',
    documentation="""`$tmax(x,...)`

Returns the maximum value using a text comparison.
Can be used with an arbitrary number of arguments.""")
