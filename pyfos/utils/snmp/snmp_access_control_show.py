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

:mod:`snmp_access_control_show` - PyFOS util to show the snmp access control.
*****************************************************************************
The :mod:`snmp_access_control_show` provides option to display the
snmp access control information.

This module can be used to display the snmp access control information
including the index, host and access level

* inputs:

| Infrastructure options:

 |   -i,--ipaddr=IPADDR     IP address of FOS switch.
 |   -L,--login=LOGIN       login name.
 |   -P,--password=PASSWORD password.
 |   -f,--vfid=VFID         VFID to which the request is directed to[OPTIONAL].
 |   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
 |   -v,--verbose           verbose mode [OPTIONAL].

|  Util scripts options:

 | --index=VALUE            Index of snmp access control list

* outputs:
    * SNMP access control details.

.. function:: snmp_access_control_info(session, access_control)

    * Display the snmp access control information.

        Example usage of the method::

            result = snmp_access_control_info(inputs['session'],
                        access_control)
            print (result)

        Details::

           snmp_access_control_obj = access_control()
           result = snmp_access_control_obj.get(session)

        * inputs:
            :param session: session returned by login.

        * outputs:
            :rtype: dictionary of return snmp access control rest response

        *use cases*

        1. Retrieve the snmp access control details.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_snmp import access_control


def snmp_access_control_info(session, access_control_obj):
    snmp_access_control_obj = access_control()
    if access_control_obj is None:
        result = snmp_access_control_obj.get(session, None)
    else:
        result = snmp_access_control_obj.get(session, access_control_obj)
    return result


def main(argv):
    # Print arguments
    # print(sys.argv[1:])

    filters = ['index']
    inputs = brcd_util.parse(argv, access_control, filters)

    access_control_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    result = snmp_access_control_info(
        inputs['session'], access_control_obj.peek_index())

    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
