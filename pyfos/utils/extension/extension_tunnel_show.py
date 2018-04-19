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

:mod:`extension_tunnel_show` - PyFOS util for Displaying tunnel object.
***********************************************************************************
The :mod:`extension_tunnel_show` util provides tunnel Display functionality.

This module is a stand-alone script that can be used to show the extension
tunnel.

extension_tunnel_show.py: Usage

* Infrastructure options:
    * -i,--ipaddr=IPADDR: IP address of FOS switch.
    * -L,--login=LOGIN: Login name.
    * -P,--password=PASSWORD: Password.
    * -f,--vfid=VFID: VFID to which the request is directed.
    * -s,--secured=MODE: HTTPS mode "self" or "CA"[Optional].
    * -v,--verbose: Verbose mode[Optional].

* Util scripts options:
    * -n,--name=NAME: Set name.
    * -a,--admin-enabled=VALUE: Set admin-enabled.
    *    --ipsec-enabled=VALUE: Set ipsec-policy.
    *    --ficon=VALUE: Set ficon.
    *    --ip-extension=VALUE: Set ip-extension.

* Outputs:
    * Python dictionary content with RESTCONF response data.

.. function:: extension_tunnel_show.show_extension_tunnel(session,\
name, ipsec, ipextn, ficon, admin)

    *show extension tunnel*

        Example usage of the method::

                ret = extension_tunnel_show.show_extension_tunnel(session,
                name)
                print (ret)

        Details::

            tunnel = {
                            "name": name,
                            "admin-enabled": admin,
                            "ipsec-enabled": ipsec,
                            "ip-extension" : ipextn,
                            "ficon" : ficon,
                      }
            result = extension_tunnel_show._show_extension_tunnel(session,
            tunnel)

        * Inputs:
            :param session: Session returned by login.
            :param name: VE port name expressed as slot/port.
            :param admin: Admin enabled state.
            :param ipsec: Ipsec policy enabled state.
            :param ipextn: IP Extension enabled state.
            :param ficon: Ficon enabled state.

        * Outputs:
            :rtype: List of tunnel instances matching the inputs.

        *Use cases*

         Show tunnel details.

"""


import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_extension_tunnel import extension_tunnel
import sys
import pyfos.utils.brcd_util as brcd_util


isHttps = "0"


def _show_extension_tunnel(session, tnlobject):
    objlist = extension_tunnel.get(session)
    tnllist = []
    if isinstance(objlist, extension_tunnel):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if tnlobject.peek_name() is not None and\
               tnlobject.peek_name() != objlist[i].peek_name():
                continue
            if tnlobject.peek_admin_enabled() is not None and\
               tnlobject.peek_admin_enabled() !=\
               objlist[i].peek_admin_enabled():
                continue
            if tnlobject.peek_tunnel_status() is not None and\
               tnlobject.peek_tunnel_status() !=\
               objlist[i].peek_tunnel_status():
                continue
            if tnlobject.peek_ipsec_enabled() is not None and\
               tnlobject.peek_ipsec_enabled() !=\
               objlist[i].peek_ipsec_enabled():
                continue
            if tnlobject.peek_ip_extension() is not None and\
               tnlobject.peek_ip_extension() !=\
               objlist[i].peek_ip_extension():
                continue
            if tnlobject.peek_ficon() is not None and\
               tnlobject.peek_ficon() != objlist[i].peek_ficon():
                continue
            tnllist.append(objlist[i])
    else:
        print(objlist)
    return tnllist


def show_extension_tunnel(session, name=None, ipsec=None, ipextn=None,
                          ficon=None, admin=None):
    tnlobject = extension_tunnel()
    tnlobject.set_name(name)
    tnlobject.set_ip_extension(ipsec)
    tnlobject.set_admin_enabled(admin)
    tnlobject.set_ipsec_enabled(ipsec)
    result = _show_extension_tunnel(session, tnlobject)
    return result


def main(argv):
    # myinput = "-i 10.17.3.70 -a 1 -n 4/19 --tunnel-status 12"
    # argv = myinput.split()
    filters = ["name", "admin_enabled", "ipsec_enabled",
               "ip_extension", "ficon"]
    inputs = brcd_util.parse(argv, extension_tunnel, filters)
    tnlobject = inputs['utilobject']
    session = brcd_util.getsession(inputs)
    result = _show_extension_tunnel(session, tnlobject)
    if len(result) == 0:
        print("No tunnels found.")
    else:
        pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
