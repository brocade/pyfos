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

:mod:`snmp_mib_capability_show` - PyFOS util to show the snmp mib capability.
*****************************************************************************
The :mod:`snmp_mib_capability_show` provides option to display the
snmp mib capability information.

This module can be used to display the snmp mib_hapability information
including the mib name, mib enabled state

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

  Util scripts options:

     --mib-name=MIB-NAME                       MIB name

* outputs:
    * SNMP mib capability configuration details.

.. function:: snmp_mib_cap_info(session)

    * Display the snmp mib capability information.

        Example usage of the method:

            result = snmp_mib_cap_info(inputs['session'])
            print (result)

        Details::

           snmp_mib_cap_obj = mib_capability()
           result = snmp_mib_cap_obj.get(session)

        * inputs:
            :param session: session returned by login.

        * outputs:
            :rtype: dictionary of return snmp mib capability rest response

        *use cases*

        1. Retrieve the snmp mib capability configurations details.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_snmp import mib_capability


def snmp_mib_cap_info(session, mib_cap_obj):
    snmp_mib_cap_obj = mib_capability()
    if mib_cap_obj is None:
        result = snmp_mib_cap_obj.get(session, None)
    else:
        result = snmp_mib_cap_obj.get(session, mib_cap_obj)

    return result


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['mib_name']
    inputs = brcd_util.parse(argv, mib_capability, filters)

    mib_cap_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    result = snmp_mib_cap_info(
        inputs['session'], mib_cap_obj.peek_mib_name())
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
