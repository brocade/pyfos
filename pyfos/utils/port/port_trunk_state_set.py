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

:mod:`port_trunk_state_set` - PyFOS util for setting a port as a trunk port.
*******************************************************************************
The :mod:`port_trunk_state_set` util for setting a port as a trunk port.

This module is a stand-alone script that can be used to set or reset a port\
 as a trunk port.

* Infrastructure Options:
    * -L=<login>: The login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: The password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: The IP address.
    * -u=<user name>: The string name to be assigned to a switch.
    * -f=<VFID>: The VFID or -1 if VF is disabled. If unspecified,
        a VFID of 128 is assumed.

* Util Script Options:
    --name=NAME                     The port in slot/port format.
    --trunk_enabled=TRUNK_ENABLED      Sets the trunk port enabled flag <0|1>.


* Output:
    * Python dictionary content with RESTCONF response data.

"""

import sys
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_interface import fibrechannel
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def validate(fcObject):
    if fcObject.peek_name() is None or \
       fcObject.peek_trunk_port_enabled() is None:
        return 1
    return 0


def main(argv):
    filters = ["name", "trunk_port_enabled"]
    inputs = brcd_util.parse(argv, fibrechannel, filters, validate)

    fcObject = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    result = fcObject.patch(session)
    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
