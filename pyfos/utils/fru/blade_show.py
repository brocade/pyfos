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

:mod:`blade_show` - PyFOS util to show the blade information.
***********************************************************************
The :mod:`blade_show` provides option to display the blade information.

This module can be used to display the blade information.

* inputs:

| Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch.
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

|  Util scripts options:

   |   --slot-number=slot-number        slot-number

* outputs:
    * Blade information. When slot-number is not provided,
      all the blades will be displayed.

.. function:: blade_show.show_blade_info(session, slot)

    * Display the blade details.

        Example usage of the method::

            # Example 1: Display all the blades
            ret = blade_show.show_blade_info(session, None)
            print (ret)

            # Example 2: Display a specific blade 1
            ret = blade_show.show_blade_info(session, 1)
            print (ret)

        Details::

            blade_obj = blade()
            if slot-number is None: # All blade slots
                result = blade_obj.get(session, None)
            else:
                result = blade_obj.get(session, slot)

        * inputs:
            :param session: session returned by login.
            :param slot: Specific slot-number or None for all the blades.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Retrieve the blade information.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_fru import blade
from pyfos.utils import brcd_util


def show_blade_info(session, slot):
    blade_obj = blade()
    if slot is None:
        result = blade_obj.get(session, None)
    else:
        result = blade_obj.get(session, slot)
    return result


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['slot_number']
    inputs = brcd_util.parse(argv, blade, filters)

    blade_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    # pyfos_util.response_print(inputs['utilobject'].displaycustomcli())
    result = show_blade_info(inputs['session'],
                             blade_obj.peek_slot_number())
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
