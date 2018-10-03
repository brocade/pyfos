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

:mod:`powersupply_show` - PyFOS util to show the powersupply unit information.
******************************************************************************
The :mod:`powersupply_show` provides option to display the powersupply
unit information.

This module can be used to display the powersupply unit information.

* inputs:

| Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch.
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

|  Util scripts options:

   |   --unit-number=unit-number        unit-number

* outputs:
    * Powersupply unit information. When unit-number is not provided,
      all the units will be displayed.

.. function:: ps_unit_show.show_ps_unit(session, unit)

    * Display the powersupply unit details.

        Example usage of the method::

            # Example 1: Display all the ps_units
            ret = ps_unit_show.show_ps_unit(session, None)
            print (ret)

            # Example 2: Display a specific ps-unit 1
            ret = ps_unit_show.show_ps_unit(session, 1)
            print (ret)

        Details::

            ps_obj = power_supply()
            if unit-number is None: # All powersupply units
                result = ps_obj.get(session, None)
            else:
                result = ps_obj.get(session, unit)

        * inputs:
            :param session: session returned by login.
            :param unit: Specific unit-number or None for all ps-units.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Retrieve the powersupply unit information.
"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_fru import power_supply
import pyfos.utils.brcd_util as brcd_util


def show_ps_unit(session, unit):
    ps_obj = power_supply()
    if unit is None:
        result = ps_obj.get(session, None)
    else:
        result = ps_obj.get(session, unit)
    return result


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['unit_number']
    inputs = brcd_util.parse(argv, power_supply, filters)

    ps_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    # pyfos_util.response_print(inputs['utilobject'].displaycustomcli())
    result = show_ps_unit(inputs['session'],
                          ps_obj.peek_unit_number())
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
