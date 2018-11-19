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

:mod:`port_group_fport_add` - PyFOS util for adding f-ports to a portgroup
*******************************************************************************
The :mod:`port_group_fport_add` provides option to add f-ports to a portgroup

This module can be used to add f-ports to a portgroup when
load-balancing mode is enabled in the port-group. Note that there
must be atleast an n-port in the port-group to be able to add f-ports
to the port-group.

* inputs:

| Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch.
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

| Util scripts options:

  |    --id=ID             Port group ID
  |    --f-port=F-PORT     F-port members of the port group
                           (only when load-balancing mode is enabled)


* outputs:
    * Status of the portgroup f-port add operation

.. function:: port_group_fport_add.add_fports(session, pgid, fports)

    * Add f-port members to a portgroup

        Example usage of the method::

            ret = port_group_fport_add.add_fports(session, 4, "0/1 0/2")
            print (ret)

        Details::

            portgroup_obj = port_group()
            portgroup_obj.set_port_group_id(pgid)
            if fports is not None:
                portgroup_obj.set_port_group_f_ports_f_port(fports)

            result = portgroup_obj.post(session)

        * inputs:
            :param session: session returned by login.
            :param pgid: Port group ID.
            :param fports: F-port members of the port group.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Add f-port members to the port-group
           port_group_fport_add.py -i 10.17.31.173 --id=3 --f-port="0/5;0/6"

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_access_gateway import port_group


def _add_fports(session, restobject):
    return restobject.post(session)


def add_fports(session, pgid, fports):
    portgroup_obj = port_group()
    portgroup_obj.set_port_group_id(pgid)
    if fports is not None:
        portgroup_obj.set_port_group_f_ports_f_port(fports)
    result = _add_fports(session, portgroup_obj)
    return result


def validate(portgroup_obj):
    if (portgroup_obj.peek_port_group_id() is None or
            not portgroup_obj.peek_port_group_f_ports_f_port()):
        return 1
    return 0


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['port_group_id', 'port_group_f_ports_f_port']
    inputs = brcd_util.parse(argv, port_group, filters, validate)

    portgroup_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    # pyfos_util.response_print(inputs['utilobject'].displaycustomcli())
    result = _add_fports(inputs['session'], portgroup_obj)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
