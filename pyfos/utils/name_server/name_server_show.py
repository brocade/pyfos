#!/usr/bin/env python3

# Copyright © 2018 Broadcom. All Rights Reserved. The term “Broadcom” refers to
# Broadcom Inc. and/or its subsidiaries.
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

:mod:`name_server_show` - PyFOS util to show Name Server entries.
***********************************************************************************
The :mod:`name_server_show` supports 'nsshow' CLI use case.

This module is a stand-alone script and API that can be used to display
all NS entries. If a port ID is specified, only that specific entry will
be displayed.

* inputs:
    * -L=<login>: Login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: IP address.
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        a VFID of 128 is assumed.
    * --port-id=<PORTID>: Port ID.

* Outputs:
    * List of devices.

"""

import sys
from pyfos import pyfos_auth
import pyfos.pyfos_brocade_name_server as pyfos_name_server
from pyfos import pyfos_util
from pyfos.utils import brcd_util

isHttps = "0"


def main(argv):
    # Parse input arguments
    filters = ['port_id']
    inputs = brcd_util.parse(argv, pyfos_name_server.fibrechannel_name_server,
                             filters)

    # Get Name Server object
    name_server_object = inputs['utilobject']

    # Get session
    session = brcd_util.getsession(inputs)

    # Print Name Server properties
    result = name_server_object.get(session, name_server_object.peek_port_id())
    pyfos_util.response_print(result)

    # Logout
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
