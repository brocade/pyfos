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

:mod:`port_group_show` - PyFOS util to show the port-group information.
***************************************************************************
The :mod:`port_group_show` provides option to display the port-group
information.

This module can be used to display the AG port-groups. Port-groups are
supported only when the port group policy is enabled.

* inputs:

| Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch.
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

|  Util scripts options:

   |   --id=ID             Port-group ID

* outputs:
    * Port group information. When port-group ID is not provided,
      all the existing port-groups will be displayed.

.. function:: port_group_show.show_port_group(session, pgid)

    * Display the port-groups configured on the AG.

        Example usage of the method::

            # Example 1: Display all the port-groups
            ret = port_group_show.show_port_group(session, None)
            print (ret)

            # Example 2: Display a specific port-group 1
            ret = port_group_show.show_port_group(session, 1)
            print (ret)

        Details::

            portgroup_obj = port_group()
            if pgid is None: # All port-groups
                result = portgroup_obj.get(session, None)
            else:
                result = portgroup_obj.get(session, pgid)

        * inputs:
            :param session: session returned by login.
            :param pgid: Specific port-group ID or None for all port-groups.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Retrieve the AG port-group information.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_access_gateway import port_group


def show_port_group(session, pgid):
    portgroup_obj = port_group()
    if pgid is None:
        result = portgroup_obj.get(session, None)
    else:
        result = portgroup_obj.get(session, pgid)
    return result


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['port_group_id']
    inputs = brcd_util.parse(argv, port_group, filters)

    portgroup_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    # pyfos_util.response_print(inputs['utilobject'].displaycustomcli())
    result = show_port_group(inputs['session'],
                             portgroup_obj.peek_port_group_id())
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
