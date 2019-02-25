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

:mod:`snmp_system_show` - PyFOS util to show the snmp system information.
*************************************************************************
The :mod:`snmp_system_show` provides option to display the
snmp system information.

This module can be used to display the snmp system information
including the system description,  location, contact, inform-enabled,
encryption-enabled, audit interval, snmp default configuration, snmp security
level, snmpv1 enabled.

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

  Util scripts options:

|     None.

* outputs:
    * SNMP system configuration details.

.. function:: snmp_system_info(session)

    * Display the snmp system information.

        Example usage of the method:

            result = snmp_system_info(inputs['session'])
            print (result)

        Details::

            snmp_system_obj = snmp_system()
            result = snmp_system_obj.get(session)

        * inputs:
            :param session: session returned by login.

        * outputs:
            :rtype: dictionary of return snmp system rest response

        *use cases*

        1. Retrieve the snmp system details.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_snmp import system


def snmp_system_info(session):
    snmp_system_obj = system()
    result = snmp_system_obj.get(session)
    return result


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['none']
    inputs = brcd_util.parse(argv, system, filters)

    session = brcd_util.getsession(inputs)

    result = snmp_system_info(inputs['session'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
