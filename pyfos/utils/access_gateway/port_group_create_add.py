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

:mod:`port_group_create_add` - PyFOS util to create a new port-group or\
 add n-ports to an existing port-group.
***********************************************************************\
***************************************
The :mod:`port_group_create_add` provides option to create a port-group\
 or add n-ports to an existing port-group

This module can be used to create a portgroup when the switch is in
Access Gateway mode. Portgroups can be created only when the portgroup
policy is active. This module can also be used to add n-ports to an
existing port-group.

* inputs:

| Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch.
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

| Util scripts options:

  |    --n-port=N-PORT     N-port members of the port group
  |    --name=NAME         Port group name (of a new port-group)
  |    --id=ID             Port group ID


* outputs:
    * Status of the portgroup create operation

.. function:: port_group_create_add.create_add_port_group(session, pgid,
                  pgname, nports)

    * Create a portgroup

        Example usage of the method::

            ret = port_group_create_add.create_add_port_group(session, 1,
                      "pg1", "0/40 0/41")
            print (ret)

        Details::

            portgroup_obj = port_group()
            portgroup_obj.set_port_group_id(pgid)
            if pgname is not None:
                portgroup_obj.set_port_group_name(pgname)

            portgroup_obj.set_port_group_n_ports_n_port(nports)

            ret = portgroup_obj.post(session)

        * inputs:
            :param session: session returned by login.
            :param pgid: Port group ID.
            :param pgname: Port group name.
            :param nports: N-port members of the port group.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Create a new port group:
            port_group_create_add_nport.py -i 10.17.31.172 --id=1
                --name="pg1"--n-port=0/40
        2. Add n-ports to an existing port group 1:
            port_group_create_add_nport.py -i 10.17.31.172 --id=1
                --n-port="0/42;0/43"
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_access_gateway import port_group

# The two scripts:port_group_create and port_group_add are merged to one.
# As port_group_add uses POST operation, it will end up creating
# a port-group if it doesn't exist. To avoid confusion, both
# the port-group create and add scripts are merged to one.


def _create_add_port_group(session, restobject):
    return restobject.post(session)


def create_add_port_group(session, pgid, pgname, nports):
    portgroup_obj = port_group()
    portgroup_obj.set_port_group_id(pgid)
    if pgname is not None:
        portgroup_obj.set_port_group_name(pgname)

    portgroup_obj.set_port_group_n_ports_n_port(nports)

    result = _create_add_port_group(session, portgroup_obj)
    return result


def validate(portgroup_obj):
    if (portgroup_obj.peek_port_group_id() is None or
            not portgroup_obj.peek_port_group_n_ports_n_port()):
        return 1
    return 0


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['port_group_id', 'port_group_name',
               'port_group_n_ports_n_port']
    inputs = brcd_util.parse(argv, port_group, filters, validate)

    session = brcd_util.getsession(inputs)

    # pyfos_util.response_print(inputs['utilobject'].displaycustomcli())
    result = _create_add_port_group(inputs['session'], inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
