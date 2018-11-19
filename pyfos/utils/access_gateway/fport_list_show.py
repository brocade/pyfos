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

:mod:`fport_list_show` - PyFOS util to show the F_Port information.
*******************************************************************************
The :mod:`fport_list_show` util provides the option to display \
F_Port information.

This module can be used to display F_Port information including the online \
status, the current N_Port, and more.

* Input:

| Infrastructure Options:

|   -i,--ipaddr=IPADDR:     The IP address of the FOS switch.
|   -L,--login=LOGIN:       The login name.
|   -P,--password=PASSWORD: The password.
|   -f,--vfid=VFID:         The VFID to which the request is \
                             directed [OPTIONAL].
|   -s,--secured=MODE:      The HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose:           Verbose mode [OPTIONAL].

  Util Script Options:

|      --f-port=VALUE      Sets the f-port.

* Output:
    * F_Port online status and current N_Port mapping details.

.. function:: fport_list_show.show_f_ports(session, f-port)

    * Display the F_Ports configured on the AG and their details.

        Example Usage of the Method:

            ret = fport_list_show.show_f_ports(session, f_port)
            print (ret)

        Details::

           fportlist_obj = f_port_list()
           if f_port is None:
               result = fportlist_obj.get(session, None)
           else:
               result = fportlist_obj.get(session, f_port)

        * Input:
            :param session: The session returned by login.
            :param port_group_id: The specific F_Port name or None for \
              all F_Ports.

        * Output:
            :rtype: Dictionary of return status matching the REST response.

        *Use Cases*

        1. Retrieve the AG F_Ports information.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_access_gateway import f_port_list


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
