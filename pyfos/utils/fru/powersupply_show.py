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

:mod:`powersupply_show` - PyFOS util to show the power supply unit information.
**********************************************************************************
The :mod:`powersupply_show` util shows the power supply unit information.

This module can be used to display the power supply unit information.

* Input:

| Infrastructure Options:

|   -i,--ipaddr=IPADDR     The IP address of the FOS switch.
|   -L,--login=LOGIN       The login name.
|   -P,--password=PASSWORD The password.
|   -f,--vfid=VFID         The VFID to which the request is \
                            directed [OPTIONAL].
|   -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           Verbose mode [OPTIONAL].

|  Util Script Options:

   |   --unit-number=unit-number     Sets the unit number.

* Output:
    * Power supply unit information. When the unit number is not provided,
      all power supply units will be displayed.

.. function:: ps_unit_show.show_ps_unit(session, unit)

    * Displays the power supply unit details.

        Example Usage of the Method::

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

        * Input:
            :param session: The session returned by the login.
            :param unit: The specific unit number or none for all \
                          power supply units.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Retrieve the power supply unit information.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_fru import power_supply
from pyfos.utils import brcd_util


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
