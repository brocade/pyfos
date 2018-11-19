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

:mod:`port_group_remove` - PyFOS util to remove the port-group.
***********************************************************************************
The :mod:`port_group_remove` provides option to remove the port-group.

This module can be used to delete the port-groups. Port-group 0 is the default
port-group and it cannot be removed.

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

* outputs:
    status of the port-group delete operation.

.. function:: port_group_remove.remove_port_group(session, pgid)

    * Remove a port-group.

        Example usage of the method:

            ret = port_group_remove.remove_port_group(session, 1)
            print (ret)

        Details::

            portgroup_obj = port_group()
            portgroup_obj.set_port_group_id(pgid)
            result = portgroup_obj.delete(session)

        * inputs:
            :param session: session returned by login.
            :param pgid: port-group ID.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Delete a port-group
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_access_gateway import port_group


def remove_port_group(session, pgid):
    portgroup_obj = port_group()
    portgroup_obj.set_port_group_id(pgid)
    result = portgroup_obj.delete(session)
    return result


def validate(portgroup_obj):
    if portgroup_obj.peek_port_group_id() is None:
        print("Missing input(s)")
        return 1
    return 0


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['port_group_id']
    inputs = brcd_util.parse(argv, port_group, filters, validate)

    portgroup_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    # pyfos_util.response_print(inputs['utilobject'].displaycustomcli())
    result = remove_port_group(inputs['session'],
                               portgroup_obj.peek_port_group_id())
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
