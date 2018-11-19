#!/usr/bin/env python3

# Copyright 2018 Brocade Communications Systems LLC.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may also obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""

:mod:`blade_extncfg_set` - PyFOS util for setting extension blade modes.
********************************************************************************
The :mod:`blade_extncfg_set` util sets the extension blade modes.

This module is a stand-alone script that can be used to create an extension
tunnel.

blade_extncfg_set.py: Usage

* Input:

* Infrastructure options:
    * -i,--ipaddr=IPADDR     The IP address of the FOS switch.
    * -L,--login=LOGIN       The login name.
    * -P,--password=PASSWORD The password.
    * -f,--vfid=VFID         The VFID to which the request is \
                              directed [OPTIONAL].
    * -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
    * -v,--verbose           Verbose mode [OPTIONAL].

* Util Script Options:
    * --slot=SLOT: Sets the "slot-number".
    * --app-mode=VALUE: Sets the "extension-app-mode".
    * --ve-mode=VALUE: Sets the "extension-ve-mode".
    * --ge-mode=VALUE: Sets the "extension-ge-mode".

* Output:
    * Python dictionary content with RESTCONF response data.

.. function:: blade_extncfg_set.extncfg_set(session, slot,\
appmode, vemode, gemode)

    *Set Extension Blade Modes*

        Example Usage of the Method::

                ret = blade_extncfg_set.extncfg_set(session,
                slot, appmode, vemode, gemode)
                print (ret)

        * Input:
            :param session: The session returned by login.
            :param slot: The blade slot number for pizzabox is 0.
            :param appmode: The blade app mode configuration.
            :param vemode: The blade ve mode configuration.
            :param gemode: The blade ge mode configuration.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Set the extension mode for the blade or switch.
"""


import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_fru import blade
from pyfos.utils import brcd_util


def _extncfg_set(session, bldobject):
    result = bldobject.patch(session)
    return result


def extncfg_set(session, slot, appmode=None, vemode=None, gemode=None):
    if slot is None or \
        (appmode is None and
         vemode is None and
         gemode is None):
        return ({'Error': "Please provide valid inputs" +
                          "for atleast one modes"})

    value_dict = {
        'slot-number': slot,
        'extension-ve-mode': vemode,
        'extension-ge-mode': gemode,
        'extension-app-mode': appmode
        }
    bldobject = blade(value_dict)
    result = _extncfg_set(session, bldobject)
    return result


def validate(bldobject):
    if bldobject.peek_slot_number() is None or \
       bldobject.peek_slot_number() \
       is None and bldobject.peek_slot_number() is None and \
       bldobject.peek_slot_number() is None:
        print("Missing options in the commandline:")
        return 1
    return 0


def main(argv):
    # myinput=str("-i 10.17.3.70  --name 4/19")
    # argv = myinput.split()
    filters = ['slot_number', 'extension_ve_mode', 'extension_app_mode',
               'extension_ge_mode']
    inputs = brcd_util.parse(argv, blade, filters, validate)
    bldobject = inputs['utilobject']
    session = brcd_util.getsession(inputs)
    result = _extncfg_set(session, bldobject)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
