#!/usr/bin/env python3

# Copyright © 2020 Broadcom. All Rights Reserved. The term “Broadcom” refers to
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

:mod:`fabric_traffic_controller_show` - \
PyFOS util to show Fabric Traffic Controller entries.
**********************************************************************************************
The :mod:`fabric_traffic_controller_show` \
supports 'fabricNotification --show' CLI use case.

This module is a stand-alone script and API that can be used to display
all Fabric Traffic Controller (i.e., Fabric Notifcation) device entries.
If an N_Port ID is specified, only that specific entry will be displayed.

* inputs:
    * -L=<login>: Login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: IP address.
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        a VFID of 128 is assumed.
    * --n-port-id=<N_PORTID>: N_Port ID.

* Outputs:
    * List of devices.

"""

import sys
from pyfos import pyfos_auth
import pyfos.pyfos_brocade_fabric_traffic_controller as pyfos_ftc
from pyfos import pyfos_util
from pyfos.utils import brcd_util

isHttps = "0"


def main(argv):
    # Parse input arguments
    filters = ['n_port_id']
    inputs = brcd_util.parse(argv,
                             pyfos_ftc.fabric_traffic_controller_device,
                             filters)

    # Get Fabric Traffic Controller (FTC) object
    ftc_object = inputs['utilobject']

    # Get session
    session = brcd_util.getsession(inputs)

    # Print Fabric Traffic Controller properties
    result = ftc_object.get(session, ftc_object.peek_n_port_id())

    pyfos_util.response_print(result)

    # Logout
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
