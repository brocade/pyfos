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

:mod:`snmp_trap_capability_show`-PyFOS util to show the snmp trap capability.
*****************************************************************************
The :mod:`snmp_trap_capability_show` provides option to display the
snmp trap capability information.

This module can be used to display the snmp trap_capability information
including the trap name, trap enabled state and severity level

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

  Util scripts options:

* outputs:
    * SNMP trap capability configuration details.

.. function:: snmp_trap_cap_info(session)

    * Display the snmp trap capability information.

        Example usage of the method:

            result = snmp_trap_cap_info(inputs['session'])
            print (result)

        Details::

           snmp_trap_cap_info = trap_capability()
           result = snmp_trap_cap_obj.get(session)

        * inputs:
            :param session: session returned by login.

        * outputs:
            :rtype: dictionary of return snmp trap capability rest response

        *use cases*

        1. Retrieve the snmp trap capability configurations details.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_snmp import trap_capability


def snmp_trap_cap_info(session):
    snmp_trap_cap_obj = trap_capability()
    result = snmp_trap_cap_obj.get(session)
    return result


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['none']
    inputs = brcd_util.parse(argv, trap_capability, filters)

    session = brcd_util.getsession(inputs)

    result = snmp_trap_cap_info(inputs['session'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
