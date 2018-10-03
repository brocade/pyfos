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

:mod:`fan_show` - PyFOS util to show the fan unit information.
***************************************************************************
The :mod:`fan_show` provides option to display the fan unit information.

This module can be used to display the FAN unit information.

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
    * Fan unit information. When unit-number is not provided,
      all the units will be displayed.

.. function:: fan_unit_show.show_fan_unit(session, unit)

    * Display the fan unit details.

        Example usage of the method::

            # Example 1: Display all the fan_units
            ret = fan_unit_show.show_fan_unit(session, None)
            print (ret)

            # Example 2: Display a specific fan-unit 1
            ret = fan_unit_show.show_fan_unit(session, 1)
            print (ret)

        Details::

            fan_obj = fan()
            if unit-number is None: # All fan units
                result = fan_obj.get(session, None)
            else:
                result = fan_obj.get(session, unit)

        * inputs:
            :param session: session returned by login.
            :param unit: Specific unit-number or None for all fan-units.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Retrieve the FAN unit information.
"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_fru import fan
import pyfos.utils.brcd_util as brcd_util


def show_fan_unit(session, unit):
    fan_obj = fan()
    if unit is None:
        result = fan_obj.get(session, None)
    else:
        result = fan_obj.get(session, unit)
    return result


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['unit_number']
    inputs = brcd_util.parse(argv, fan, filters)

    fan_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    # pyfos_util.response_print(inputs['utilobject'].displaycustomcli())
    result = show_fan_unit(inputs['session'],
                           fan_obj.peek_unit_number())
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
