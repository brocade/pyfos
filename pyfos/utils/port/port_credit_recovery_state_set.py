#!/usr/bin/env python3

# Copyright © 2018 Broadcom. All rights reserved. The term "Broadcom"
# refers to Broadcom Inc. and/or its subsidiaries.
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

:mod:`port_credit_recovery_state_set` - \
        PyFOS util for specific port op use case.
**********************************************************************************************
The :mod:`port_credit_recovery_state_set` \
       provides for a specific port op use case.

This module is a stand-alone script that can be used to set/reset a port as a
credit_recoveryport.

* Infrastructure options:
    * -L=<login>: Login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: IP address.
    * -u=<user name>: string name to be assigned to switch.
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.

* Util script options:
    -n,--name=NAME                                       Port in slot/port.
    --credit_recovery_enabled=CREDIT_RECOVERY_ENABLED \
                                        Set "credit-recovery-enabled" <0|1>


* Outputs:
    * Python dictionary content with RESTCONF response data.

"""

import sys
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_interface import fibrechannel
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def usage():
    print("usage:")
    print('portcfgcredit_recoveryport.py -i <ipaddr> \
            --name <name> --enable/--disable')


def validate(fcObject):
    if fcObject.peek_name() is None or \
       fcObject.peek_credit_recovery_enabled() is None:
        return 1
    return 0


def main(argv):
    filters = ["name", "credit_recovery_enabled"]
    inputs = brcd_util.parse(argv, fibrechannel, filters, validate)

    fcObject = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    result = fcObject.patch(session)
    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
