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

:mod:`switch_configuration_modify` - PyFOS util for configuring switch use case
*******************************************************************************
The :mod:`switch_configuration_modify` provides for configuring switch use case

This module is a standalone script that can be used to display switch
attributes

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.

* Util scripts options:

    * --wwn-mode=WWN-MODE                             Configures port id wwn.
    * --area-mode=AREA-MODE                           Configures port id area.
    * --edge-hold-time=EDGE-HOLD-TIME                 Configures Edge hold time

* outputs:
    * HTTP Status in JSON format

.. function:: patch_switch_conf (session, wwn, eht, am)

        Example usage of the method::

            ret = switch_configuration_modify.patch_switch_conf (session,
                    wwn, eht, am)
            print (ret)

        Details::

            val = {
                "wwn-port-id-mode": wwn,
                "edge-hold-time": eht,
                "area-mode": am
                }
            obj = switch_configuration(val)
            result = _patch_switch_conf(session, obj)
            return result

        * inputs:
            :param session: session returned by login.
            :param am: Configures port id based on area.
            :param eht: Configures Edge hold time in seconds.
            :param wwn: Configures port id based on wwn.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Patch the configuration parameters of switch.

"""

import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_brocade_fibrechannel_configuration as py_fc
import pyfos.pyfos_util as pyfos_util
import sys
import pyfos.utils.brcd_util as brcd_util

switch = py_fc.switch_configuration


def validate(obj):
    flag = 0
    if obj.peek_wwn_port_id_mode() is not None:
        flag = flag + 1
    if obj.peek_edge_hold_time() is not None:
        flag = flag + 1
    if obj.peek_area_mode() is not None:
        flag = flag + 1

    return 0 if flag >= 1 else 1


def patch_switch_conf(session, wwn, eht, am):
    val = {
        "wwn-port-id-mode": wwn,
        "edge-hold-time": eht,
        "area-mode": am
        }
    obj = switch(val)
    result = _patch_switch_conf(session, obj)
    return result


def _patch_switch_conf(session, restobject):
    return restobject.patch(session)


def main(argv):

    filters = ['wwn_port_id_mode', 'area_mode', 'edge_hold_time']
    inputs = brcd_util.parse(argv, switch, filters, validate)
    session = brcd_util.getsession(inputs)

    result = _patch_switch_conf(inputs['session'], inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
