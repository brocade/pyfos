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

:mod:`port_group_del` - PyFOS util to delete n-ports/f-ports from a portgroup
*******************************************************************************
The :mod:`port_group_del` provides option to delete n-ports/f-ports \
from a portgroup.

This module can be used to delete n-ports from a portgroup when the switch is
in Access Gateway mode. It is possible to delete f-ports from a portgroup when
load-balancing mode is enabled in the port-group.

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
  |    --n-port=N-PORT     N-port members of the port group
  |    --f-port=F-PORT     F-port members of the port group
                           (only when load-balancing mode is enabled)


* outputs:
    * Status of the portgroup n-port of f-port delete operation

.. function:: port_group_del.del_members(session, pgid, nports, fports)

    * Delete n-port members or f-ports from a portgroup

        Example usage of the method::

            # Example 1: remove n-ports from port-group 1
            ret = port_group_del.del_members(session, 1, "0/40 0/41", None)
            print (ret)

            # Example 2: remove f-ports from port-group 4
            ret = port_group_del.del_members(session, 4, None, "0/1 0/2")
            print (ret)

        Details::

            portgroup_obj = port_group()
            portgroup_obj.set_port_group_id(pgid)
            if nports is not None:
                portgroup_obj.set_port_group_n_ports_n_port(nports)
            if fports is not None:
                portgroup_obj.set_port_group_f_ports_f_port(fports)

            result = portgroup_obj.delete(session)

        * inputs:
            :param session: session returned by login.
            :param pgid: Port group ID.
            :param nports: N-port members of the port group.
            :param fports: F-port members of the port group.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Delete n-port members from the port-group
        2. Delete f-port members from the port-group

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_access_gateway import port_group


def _del_members(session, restobject):
    return restobject.delete(session)


def del_members(session, pgid, nports, fports):
    portgroup_obj = port_group()
    portgroup_obj.set_port_group_id(pgid)
    if nports is not None:
        portgroup_obj.set_port_group_n_ports_n_port(nports)
    if fports is not None:
        portgroup_obj.set_port_group_f_ports_f_port(fports)
    result = _del_members(session, portgroup_obj)
    return result


def validate(portgroup_obj):
    if (portgroup_obj.peek_port_group_id() is None or
       (not portgroup_obj.peek_port_group_n_ports_n_port() and
           not portgroup_obj.peek_port_group_f_ports_f_port())):
        return 1
    return 0


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['port_group_id', 'port_group_n_ports_n_port',
               'port_group_f_ports_f_port']
    inputs = brcd_util.parse(argv, port_group, filters, validate)

    portgroup_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    # pyfos_util.response_print(inputs['utilobject'].displaycustomcli())
    result = _del_members(inputs['session'], portgroup_obj)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
