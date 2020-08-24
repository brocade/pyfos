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

:mod:`port_state_set` - PyFOS util for specific port op use case.
***********************************************************************************
The :mod:`port_state_set` provides for specific port op use case.

This module is a standalone script that can be used to enable or disable
a port

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.

* Util scripts options:
    --name=NAME                               Port in slot/port.

* outputs:
    * Python dictionary content with RESTCONF response data

"""

import sys
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_interface import fibrechannel
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def validate(fcObject):
    if fcObject.peek_name() is None or \
       fcObject.peek_enabled_state() is None:
        return 1
    return 0


def usage():
    print("  Util scripts options:\n")
    print("    -n,--name=NAME                 " +
          "             Port in slot/port.")
    print("    -e,--enabled_state=ENABLED_STATE" +
          "            enable | disable <0|1>")


def main(argv):
    filters = ["name", "enabled_state"]
    inputs = brcd_util.parse(argv, fibrechannel, filters, validate)

    fcObject = inputs['utilobject']
    if fcObject.peek_enabled_state() == 1:
        fcObject.set_enabled_state(2)
    elif fcObject.peek_enabled_state() == 0:
        fcObject.set_enabled_state(6)
    else:
        print("Invalid value for enabled_state")
        brcd_util.full_usage(usage, filters)
        sys.exit()
    session = brcd_util.getsession(inputs)

    result = fcObject.patch(session)
    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
