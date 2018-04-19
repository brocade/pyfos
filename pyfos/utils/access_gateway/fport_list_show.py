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

:mod:`fport_list_show` - PyFOS util to show the f-port information.
*******************************************************************************
The :mod:`fport_list_show` provides option to display the
f-port information.

This module can be used to display the f-ports information
including the online status, current n-port and more.

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

  Util scripts options:

|      --f-port=VALUE      set "f-port"

* outputs:
    * F-port online-status and current n-port mapping details.

.. function:: fport_list_show.show_f_ports(session, f-port)

    * Display the F-ports configured on the AG and their details.

        Example usage of the method:

            ret = fport_list_show.show_f_ports(session, f_port)
            print (ret)

        Details::

           fportlist_obj = f_port_list()
           if f_port is None:
               result = fportlist_obj.get(session, None)
           else:
               result = fportlist_obj.get(session, f_port)

        * inputs:
            :param session: session returned by login.
            :param port_group_id: Specific f-port name or None for all f-ports

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Retrieve the AG F-ports information.
"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_access_gateway import f_port_list
import pyfos.utils.brcd_util as brcd_util


def show_f_ports(session, f_port):
    fportlist_obj = f_port_list()
    if f_port is None:
        result = fportlist_obj.get(session, None)
    else:
        result = fportlist_obj.get(session, f_port)
    return result


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['f_port']
    inputs = brcd_util.parse(argv, f_port_list, filters)

    fport_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    # pyfos_util.response_print(inputs['utilobject'].displaycustomcli())
    result = show_f_ports(inputs['session'],
                          fport_obj.peek_f_port())
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
