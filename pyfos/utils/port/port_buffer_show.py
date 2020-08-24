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

:mod:`port_buffer_show` - PyFOS util for specific port use case.
***********************************************************************************
The :mod:`port_buffer_show` provides for a specific port use case.

This module is a stand-alone script that can be used to display
portbuffershow cli output. If no name is given, stats from all ports
are displayed. Otherwise, of the specified port:.

* Inputs:
    * -L=<login>: Login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, an  interactive
        prompt will request one.
    * -i=<IP address>: IP address.
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.

* Util scripts options:
    --name=NAME                               Port in slot/port.

* Outputs:
    * Display of portbuffershow for all ports or a specified port.

"""


import sys
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_interface import fibrechannel
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def usage():
    print("  Script specific options:")
    print("")
    print("    --name=NAME                  name of port. [OPTIONAL]")
    print("")


def validate(fcObject):
    return 0


def main(argv):
    filters = ["name"]
    inputs = brcd_util.parse(argv, fibrechannel, filters, validate)

    fcObject = inputs['utilobject']

    session = brcd_util.getsession(inputs)
    filters = ['current_buffer_usage', 'average_receive_frame_size',
               'average_transmit_frame_size',
               'average_receive_buffer_usage', 'recommended_buffers',
               'measured_link_distance',
               'average_transmit_buffer_usage', 'chip_instance',
               'port_type_string', 'reserved_buffers',
               'chip_buffers_available', 'default_index']
    port = fcObject.getInstances(session, filters)
    pyfos_util.response_print(port)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
