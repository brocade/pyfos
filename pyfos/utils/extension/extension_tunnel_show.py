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

:mod:`extension_tunnel_show` - PyFOS util for displaying a tunnel object.
***********************************************************************************
The :mod:`extension_tunnel_show` util provides tunnel display functionality.

This module is a stand-alone script that can be used to show the extension
tunnel.

extension_tunnel_show.py: Usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * -n,--name=NAME: Sets the name.
    * -a,--admin-enabled=VALUE: Enables or disables the admin status.
    *    --ipsec-enabled=VALUE: Sets the IPsec policy.
    *    --ficon=VALUE: Sets the FICON enabled state.
    *    --ip-extension=VALUE: Sets IP extension.

* Output:
    * Python dictionary content with RESTCONF response data.

.. function:: extension_tunnel_show.show_extension_tunnel(session,\
name, ipsec, ipextn, ficon, admin)

    *Show an Extension Tunnel*

        Example Usage of the Method::

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

        * Input:
            :param session: The session returned by the login.
            :param name: Sets the VE_Port name expressed as slot/port.
            :param admin: Sets the admin enabled state.
            :param ipsec: Sets the IPsec policy enabled state.
            :param ipextn: Sets the IP extension enabled state.
            :param ficon: Sets the FICON enabled state.

        * Output:
            :rtype: A list of tunnel instances that match the input.

        *Use Cases*

         Show the tunnel details.

"""


import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_extension_tunnel import extension_tunnel
from pyfos.utils import brcd_util


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


# pylint: disable=W0613
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
