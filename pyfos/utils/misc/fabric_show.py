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

:mod:`fabricshow` - PyFOS util for specific fabric op use case.
***********************************************************************************
The :mod:`fabricshow` provides for specific fabric op use case.

This module is a stand-alone script that can be used to display
switches in a fabric.

* Inputs:
    * -L=<login>: Login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        a VFID of 128 is assumed.

* Outputs:
    * List of switches and their attributes.

"""

import sys
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_fabric import fabric_switch
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def main(argv):

    filters = []
    inputs = brcd_util.parse(argv, fabric_switch, filters)
    session = brcd_util.getsession(inputs)

    fabric = fabric_switch.get(inputs['session'])
    if isinstance(fabric, list):
        for switch in fabric:
            pyfos_util.response_print(switch)
    else:
        pyfos_util.response_print(fabric)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
