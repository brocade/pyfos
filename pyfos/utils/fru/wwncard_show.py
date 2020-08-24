#!/usr/bin/env python3

# Copyright 2019 Broadcom. All rights reserved.
# The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries.
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

# wwncard_show.py(pyGen v1.0.0)

"""

:mod:`wwncard_show` - PyFOS util to show the wwncard unit information.
***************************************************************************
The :mod:`wwncard_show` util displays the wwncard unit information.

This module can be used to display the wwncard unit information.

* Input:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     The IP address of the FOS switch.
|   -L,--login=LOGIN       The login name.
|   -P,--password=PASSWORD The password.
|   -f,--vfid=VFID         The VFID to which the request is \
                            directed [OPTIONAL].
|   -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           Verbose mode [OPTIONAL].


|  Util Script Options:

   |   --unit-number=unit-number    Sets the unit number.

* Output:
    * WWN unit information. When the unit number is not provided,
      all units will be displayed.

.. function:: wwn_unit_show.show_wwn_unit(session, unit)

    * Displays the wwn unit details.

        Example Usage of the Method::

            # Example 1: Display all the wwn_units
            ret = wwn_unit_show.show_wwn_unit(session, None)
            print (ret)

            # Example 2: Display a specific wwn-unit 1
            ret = wwn_unit_show.show_wwn_unit(session, 1)
            print (ret)

        Details::

            wwn_obj = wwn()
            if unit-number is None: # All wwn units
                result = wwn_obj.get(session, None)
            else:
                result = wwn_obj.get(session, unit)

        * Input:
            :param session: The session returned by the login.
            :param unit: The specific unit number or none for all wwn units.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Retrieve the wwn unit information.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_fru import wwn
from pyfos.utils import brcd_util


def show_wwn_unit(session, unit):
    wwn_obj = wwn()
    if unit is None:
        result = wwn_obj.get(session, None)
    else:
        result = wwn_obj.get(session, unit)
    return result


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['unit_number']
    inputs = brcd_util.parse(argv, wwn, filters)

    wwn_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    # pyfos_util.response_print(inputs['utilobject'].displaycustomcli())
    result = show_wwn_unit(inputs['session'],
                           wwn_obj.peek_unit_number())
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
