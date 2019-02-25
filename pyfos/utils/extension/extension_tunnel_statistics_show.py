#!/usr/bin/env python3

# Copyright © 2018 Broadcom. All Rights Reserved. The term “Broadcom” refers to
# Broadcom Inc. and/or its subsidiaries.
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

:mod:`extension_tunnel_statistics_show` - PyFOS util to display tunnel \
statistics.
***********************************************************************************
The :mod:`extension_tunnel_statistics_show` util displays tunnel statistics.

This module is a stand-alone script that can be used to show extension
tunnel statistics.

extension_tunnel_statistics_show.py: Usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * -n,--name=NAME: Sets the name or slot/port of the tunnel.
    * --operational-status: Sets the operational status of the circuit.

* Output:
    * Python dictionary content with RESTCONF response data.

.. function:: extension_tunnel_statistics_show.\
show_extension_tunnel_statistics(session,name, cid, local, remote)

    *Show an Extension Tunnel*

        Example Usage of the Method::

                ret = extension_tunnel_statistics_show.
                show_extension_tunnel_statistics(session,
                name, opstatus)
                print (ret)

        Details::

            tunnel = {
                            "name": name,
                            "operational-status": opstatus,
                      }
            result = extension_tunnel_statistics_show.
            _show_extension_tunnel_statistics(session,
            tunnel)

        * Input:
            :param session: The session returned by the login.
            :param name: Sets the VE_Port name expressed as slot/port.
            :param opstatus: Sets the tunnel operational status.

        * Output:
            :rtype: A list of tunnels.

        *Use Cases*

         Show tunnel details.

"""


import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_extension_tunnel import extension_tunnel_statistics
from pyfos.utils import brcd_util


isHttps = "0"


def _show_extension_tunnel_statistics(session, tnlobject):
    objlist = extension_tunnel_statistics.get(session)
    tnllist = []
    if isinstance(objlist, extension_tunnel_statistics):
        objlist = [objlist]

    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if tnlobject.peek_name() is not None and\
               tnlobject.peek_name() != objlist[i].peek_name():
                continue
            if tnlobject.peek_operational_status() is not None and\
               tnlobject.peek_peek_operational_status() !=\
               objlist[i].peek_peek_operational_status():
                continue
            tnllist.append(objlist[i])
    else:
        print(objlist)
    return tnllist


def show_extension_tunnel_statistics(session, name, opstatus=None):
    value_dict = {'name': name, 'operational-status': opstatus}
    tnlobject = extension_tunnel_statistics(value_dict)
    result = _show_extension_tunnel_statistics(session, tnlobject)
    return result


def main(argv):
    # myinput = "-i 10.17.3.70  -n 4/19 -c 0"
    # myinput = "--verbose"
    # argv = myinput.split()
    filters = ["name", "tunnel_id", "operational_status"]
    inputs = brcd_util.parse(argv, extension_tunnel_statistics, filters)
    tnlobject = inputs['utilobject']
    session = brcd_util.getsession(inputs)
    result = _show_extension_tunnel_statistics(session, tnlobject)
    if len(result) == 0:
        print("No tunnel found.")
    else:
        pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
