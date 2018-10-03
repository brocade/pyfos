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

:mod:`extension_tunnel_statistics_show` - PyFOS util to display tunnel stats.
***********************************************************************************
The :mod:`extension_tunnel_statistics_show` Util to display tunnel stats.

This module is a stand-alone script that can be used to show extension
tunnel statistics.

extension_tunnel_statistics_show.py: Usage

* Infrastructure options:
    * -i,--ipaddr=IPADDR: IP address of FOS switch.
    * -L,--login=LOGIN: Login name.
    * -P,--password=PASSWORD: Password.
    * -f,--vfid=VFID: VFID to which the request is directed.
    * -s,--secured=MODE: HTTPS mode "self" or "CA"[Optional].
    * -v,--verbose: Verbose mode[Optional].

* Util scripts options:
    * -n,--name=NAME: Set name or slot/port of the tunnel.
    * --operational-status: Set operational-status of the ciruit.

* Outputs:
    * Python dictionary content with RESTCONF response data.

.. function:: extension_tunnel_statistics_show.\
show_extension_tunnel_statistics(session,name, cid, local, remote)

    *show extension tunnel*

        Example usage of the method::

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

        * Inputs:
            :param session: Session returned by login.
            :param name: VE port name expressed as slot/port.
            :param opstatus: Tunnel operational-status.

        * Outputs:
            :rtype: List of tunnels

        *Use cases*

         Show a tunnel details.

"""


import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_extension_tunnel import extension_tunnel_statistics
import sys
import pyfos.utils.brcd_util as brcd_util


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
