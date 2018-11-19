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

:mod:`port_group_mode` - PyFOS util for enabling and disabling port-group modes
*******************************************************************************
The :mod:`port_group_mode` provides options to modify the port-group modes.

This module is a standalone script that can be used to enable or disable
the port-group modes. Supported port-group modes are load balancing mode
and multiple fabric name monitoring mode.

* inputs:

| Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch.
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

| Util scripts options:

  |    --id=ID                 Port-group ID
  |    --lb-mode=LB-MODE       Load balancing mode <0|1>
  |    --mfnm-mode=MFNM-MODE   Multiple fabric name monitoring mode <0|1>

* outputs:

    * Status of the port-group mode set operation

.. function:: port_group_mode.set_port_group_mode(session, pgid, \
pgmode, enabled)

    * Modify a port-group: Enable or disable a port-group mode

        Example usage of the method::

            ret = port_group_mode.set_port_group_mode(session, pgid, \
PORT_GROUP_MODE.LB_MODE, 1)
            print (ret)

        Details::

            class PORT_GROUP_MODE:
                LB_MODE = 0
                MFNM_MODE = 1

            portgroup_obj = port_group()
            portgroup_obj.set_port_group_id(pgid)
            if pgmode == PORT_GROUP_MODE.LB_MODE:
                portgroup_obj.set_port_group_modes_load_balancing_mode_enabled(enabled)
            else:
                portgroup_obj.set_port_group_modes_multiple_fabric_name_monitoring_mode_enabled(enabled)
            result = portgroup_obj.patch(session)

        * inputs:
            :param session: session returned by login.
            :param pgid: port-group identifier.
            :param pgmode: port-group mode: Load-balancing or
                multiple-fabric-name-monitoring mode
            :param enabled: 0 (disable) or 1 (enable)

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Enable/Disable the port-group modes
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_access_gateway import port_group


class PORT_GROUP_MODE:
    LB_MODE = 0
    MFNM_MODE = 1


def _set_port_group_mode(session, restobject):
    return restobject.patch(session)


def set_port_group_mode(session, pgid, pgmode, enabled):
    portgroup_obj = port_group()
    portgroup_obj.set_port_group_id(pgid)
    if pgmode == PORT_GROUP_MODE.LB_MODE:
        portgroup_obj.set_port_group_modes_load_balancing_mode_enabled(enabled)
    else:
        # breaking down lengthier line for flake8 (80 chars line-length)
        (portgroup_obj.
            set_port_group_modes_multiple_fabric_name_monitoring_mode_enabled(
                enabled))
    result = _set_port_group_mode(session, portgroup_obj)
    return result


def validate(portgroup_obj):
    # using variables instead of calling functions as the
    # function names are lengthy and difficult to fit the
    # the line length less than 80 chars for flake8.
    lb_mode = portgroup_obj.peek_port_group_mode_load_balancing_mode_enabled()
    mfnm_mode = portgroup_obj.\
        peek_port_group_mode_multiple_fabric_name_monitoring_mode_enabled()

    if (portgroup_obj.peek_port_group_id() is None or
       (lb_mode is None and mfnm_mode is None)):
        return 1
    return 0


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['port_group_id', 'port_group_mode_load_balancing_mode_enabled',
               'port_group_mode_multiple_fabric_name_monitoring_mode_enabled']
    inputs = brcd_util.parse(argv, port_group, filters, validate)

    session = brcd_util.getsession(inputs)

    # pyfos_util.response_print(inputs['utilobject'].displaycustomcli())
    result = _set_port_group_mode(inputs['session'], inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
