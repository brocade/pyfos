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
The :mod:`blade_extncfg_set` Set the extension blade modes.

This module is a standalone script that can be used to create an extension
tunnel.

blade_extncfg_set.py: Usage

* Infrastructure options:
    * -i,--ipaddr=IPADDR:IP address of FOS switch.
    * -L,--login=LOGIN:login name.
    * -P,--password=PASSWORD:password.
    * -f,--vfid=VFID:VFID to which the request is directed to.
    * -s,--secured=MODE:HTTPS mode "self" or "CA"[OPTIONAL].
    * -v,--verbose:verbose mode[OPTIONAL].

* Util scripts options:
    * --slot=SLOT : set "slot-number"
    * --app-mode=VALUE : set "extension-app-mode"
    * --ve-mode=VALUE : set "extension-ve-mode"
    * --ge-mode=VALUE : set "extension-ge-mode"

* Outputs:
    * Python dictionary content with RESTCONF response data

.. function:: blade_extncfg_set.extncfg_set(session, slot,\
appmode, vemode, gemode)

    *Set extension blade modes*

        Example usage of the method::

                ret = blade_extncfg_set.extncfg_set(session,
                slot, appmode, vemode, gemode)
                print (ret)

        * inputs:
            :param session: session returned by login
            :param slot: blade slot number for pizzabox its 0.
            :param appmode: blade app mode configuration
            :param vemode: blade ve mode configuration
            :param gemode: blade ge mode configuration

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. set the extension mode for the blade or switch.
"""


import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_fru import blade
import sys
import pyfos.utils.brcd_util as brcd_util

isHttps = "0"


def _extncfg_set(session, bldobject):
    result = bldobject.patch(session)
    return result


def extncfg_set(session, slot, appmode=None, vemode=None, gemode=None):
    if slot is None or (appmode is None and
       vemode is None and
       gemode is None):
        return ({'Error': "Please provide valid inputs"
                 "for atleast one modes"})

    value_dict = {
                    'slot-number': slot,
                    'extension-ve-mode': vemode,
                    'extension-ge-mode': gemode,
                    'extension-app-mode': appmode,
                 }
    bldobject = blade(value_dict)
    result = _extncfg_set(session, bldobject)
    return result


def main(argv):
    # myinput=str("-i 10.17.3.70  --name 4/19")
    # argv = myinput.split()
    filters = ['slot_number', 'extension_ve_mode', 'extension_app_mode',
               'extension_ge_mode']
    inputs = brcd_util.parse(argv, blade, filters)
    bldobject = inputs['utilobject']
    if bldobject.peek_slot_number() is None or (bldobject.peek_slot_number()
       is None and bldobject.peek_slot_number() is None and
       bldobject.peek_slot_number() is None):
            print("Missing options in the commandline:")
            print(inputs['utilusage'])
            sys.exit(1)
    session = brcd_util.getsession(inputs)
    result = _extncfg_set(session, bldobject)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
