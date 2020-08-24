#!/usr/bin/env python3


# Copyright © 2019 Broadcom. All rights reserved.
# The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries.
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


# lldp_neighbor_show.py(pyGen v1.0.0)


"""

:mod:`lldp_neighbor_show` - PyFOS util to show for lldp_neighbor
*******************************************************************************
The :mod:`lldp_neighbor_show` PyFOS util to show for lldp_neighbor


The list of LLDP neighbor devices connected to the switch.

lldp_neighbor_show : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --dead-interval=DEAD-INTERVAL The dead interval of the the LLDP\
      neighbor.
    * --remaining-life=REMAINING-LIFE The remaining life of the LLDP neighbor.
    * --system-name=SYSTEM-NAME The system name of the LLDP neighbor.
    * --slot-port=SLOT-PORT The local interface name.
    * --remote-interface-name=REMOTE-INTERFACE-NAME The remote interface name\
      of the LLDP neighbor device connected to local switch ethernet\
      interface.
    * --chassis-id=CHASSIS-ID The chassis ID of the LLDP neighbor.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: lldp_neighbor_show.show_lldp_neighbor(session, dead_interval,\
remaining_life, system_name, slot_port, remote_interface_name, chassis_id)

    *Show lldp_neighbor*

        Example Usage of the Method::

            ret = lldp_neighbor_show.show_lldp_neighbor(session,\
            dead_interval, remaining_life, system_name, slot_port,\
            remote_interface_name, chassis_id)
            print (ret)

        Details::

            lldp_neighborObj = lldp_neighbor()
            lldp_neighborObj.set_dead_interval(dead_interval)
            lldp_neighborObj.set_remaining_life(remaining_life)
            lldp_neighborObj.set_system_name(system_name)
            lldp_neighborObj.set_slot_port(slot_port)
            lldp_neighborObj.set_remote_interface_name(remote_interface_name)
            lldp_neighborObj.set_chassis_id(chassis_id)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param dead_interval: The dead interval of the the LLDP neighbor.
            :param remaining_life: The remaining life of the LLDP neighbor.
            :param system_name: The system name of the LLDP neighbor.
            :param slot_port: The local interface name.
            :param remote_interface_name: The remote interface name of the\
              LLDP neighbor device connected to local switch ethernet\
              interface.
            :param chassis_id: The chassis ID of the LLDP neighbor.

        * Output:

            :rtype: None or more instance of class lldp_neighbor on Success \
            or a dictionary with error.

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_lldp import lldp_neighbor
from pyfos.utils import brcd_util
# End module imports


def _show_lldp_neighbor(session, lldp_neighborObj):
    objlist = lldp_neighbor.get(session)
    lldp_neighborlist = list()
    if isinstance(objlist, lldp_neighbor):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if lldp_neighborObj.peek_dead_interval() is not None and\
               lldp_neighborObj.peek_dead_interval() !=\
               objlist[i].peek_dead_interval():
                continue
            if lldp_neighborObj.peek_remaining_life() is not None and\
               lldp_neighborObj.peek_remaining_life() !=\
               objlist[i].peek_remaining_life():
                continue
            if lldp_neighborObj.peek_system_name() is not None and\
               lldp_neighborObj.peek_system_name() !=\
               objlist[i].peek_system_name():
                continue
            if lldp_neighborObj.peek_slot_port() is not None and\
               lldp_neighborObj.peek_slot_port() !=\
               objlist[i].peek_slot_port():
                continue
            if lldp_neighborObj.peek_remote_interface_name() is not None and\
               lldp_neighborObj.peek_remote_interface_name() !=\
               objlist[i].peek_remote_interface_name():
                continue
            if lldp_neighborObj.peek_chassis_id() is not None and\
               lldp_neighborObj.peek_chassis_id() !=\
               objlist[i].peek_chassis_id():
                continue
            lldp_neighborlist.append(objlist[i])
    else:
        print(objlist)
    return lldp_neighborlist


def show_lldp_neighbor(session, dead_interval=None, remaining_life=None,
                       system_name=None, slot_port=None,
                       remote_interface_name=None, chassis_id=None):
    lldp_neighborObj = lldp_neighbor()
    lldp_neighborObj.set_dead_interval(dead_interval)
    lldp_neighborObj.set_remaining_life(remaining_life)
    lldp_neighborObj.set_system_name(system_name)
    lldp_neighborObj.set_slot_port(slot_port)
    lldp_neighborObj.set_remote_interface_name(remote_interface_name)
    lldp_neighborObj.set_chassis_id(chassis_id)
    return _show_lldp_neighbor(session, lldp_neighborObj)


def validate(lldp_neighborObj):
    if lldp_neighborObj.peek_dead_interval() is None or\
       lldp_neighborObj.peek_remaining_life() is None or\
       lldp_neighborObj.peek_system_name() is None or\
       lldp_neighborObj.peek_slot_port() is None or\
       lldp_neighborObj.peek_remote_interface_name() is None or\
       lldp_neighborObj.peek_chassis_id() is None:
        return 0
    return 0


def main(argv):
    filters = ["dead_interval", "remaining_life", "system_name", "slot_port",
               "remote_interface_name", "chassis_id"]
    inputs = brcd_util.parse(argv, lldp_neighbor, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _show_lldp_neighbor(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
