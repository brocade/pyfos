#!/usr/bin/env python3

# Copyright © 2018 Broadcom.  All rights reserved. The term "Broadcom"
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

:mod:`switch_name_set` - PyFOS util for specific switch op use case.
***********************************************************************************
The :mod:`switch_name_set` provides for a specific switch op use case.

This module is a stand-alone script that can be used to set a switch name.

* Inputs:
    * -L=<login>: Login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: IP address.
    * --username=<user name>: string name to be assigned to a switch.
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
       a  VFID of 128 is assumed.

* Outputs:
    * Python dictionary content with RESTCONF response data.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_fibrechannel_switch import fibrechannel_switch


def usage():
    print("  Script specific options:")
    print("")
    print("    --username=NAME              user friendly name")
    print("")


def validate(fcObject):
    if fcObject.peek_user_friendly_name() is None or \
       fcObject.peek_name() is None:
        return 1
    return 0


def main(argv):
    filters = ["user_friendly_name", "name"]
    inputs = brcd_util.parse(argv, fibrechannel_switch, filters, validate)

    switchObject = inputs['utilobject']

    session = brcd_util.getsession(inputs)
    result = switchObject.patch(session)
    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
