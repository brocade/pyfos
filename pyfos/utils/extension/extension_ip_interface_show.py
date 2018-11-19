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

:mod:`extension_ip_interface_show` - PyFOS util for displaying an IP interface.
********************************************************************************
The :mod:`extension_ip_interface_show` util displays an IP interface.

This module is a stand-alone script that can be used to display extension
IP interfaces based on input values.

extension_ip_interface_show.py: Usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * -n,--name=NAME: Sets the name.
    * -m,--mtu-size=VALUE: Sets the MTU size.
    * -p,--ip-prefix-length=VALUE: Sets the IP prefix length.
    * -d,--dp-id=VALUE: Sets the DP ID.
    *    --ip-address=VALUE: Sets the IP address.
    *    --vlan-id=VALUE: Sets the VLAN ID.

* Output:
    * Python dictionary content with RESTCONF response data.

.. function:: extension_ip_interface_show.show_extension_ip(session,\
name, dp, ip, prefix, vlan=None, mtu=None)

    *Delete Extension IP Interface*

        Example Usage of the Method::

            ret = extension_ip_interface_show.show_extension_ip(session,
            name, dp, ip, prefix, vlan=None, mtu=None)
            print (ret)

        Details::

            IP = {
                            "name": name,
                            "dp-id": dp,
                            "ip-address": ip
                            "ip-prefix-length": prefix
                      }
            result = extension_ip_interface_show._show_extension_ip(session,
            IP)

        * Input:
            :param session: The session returned by login.
            :param name: Sets the GE_Port name expressed as slot/port.
            :param dp-id: Sets the DP instance.
            :param ip: Sets the extension IP address.
            :param prefix: Sets the prefix length for the IP Address.

        * Output:
            :rtype: Returns a list of IP interface instances.

        *Use Cases*

         Show an extension IP interface.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_extension_ip_interface import extension_ip_interface
from pyfos.utils import brcd_util


isHttps = "0"


def _show_extension_ip(session, ipobject):
    objlist = extension_ip_interface.get(session)
    myiplist = []
    if isinstance(objlist, extension_ip_interface):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if not isinstance(objlist[i], extension_ip_interface):
                continue
            if ipobject.peek_name() is not None and ipobject.peek_name() != objlist[i].peek_name():
                continue
            if ipobject.peek_ip_address() is not None and ipobject.peek_ip_address() != objlist[i].peek_ip_address():
                continue
            if ipobject.peek_dp_id() is not None and ipobject.peek_dp_id() != objlist[i].peek_dp_id():
                continue
            if ipobject.peek_ip_prefix_length() is not None and ipobject.peek_ip_prefix_length() != objlist[i].peek_ip_prefix_length():
                continue
            if ipobject.peek_vlan_id() is not None and ipobject.peek_vlan_id() != objlist[i].peek_vlan_id():
                continue
            if ipobject.peek_mtu_size() is not None and ipobject.peek_mtu_size() != objlist[i].peek_mtu_size():
                continue
            myiplist.append(objlist[i])
    else:
        print(objlist)
    return myiplist


def show_extension_ip(session, name, dp, ip, prefix, vlan=None, mtu=None):
    value_dict = {'name': name, 'dp-id': dp, 'ip-prefix-length': prefix}
    if vlan is not None:
        value_dict.update({'vlan-id': vlan})
    if mtu is not None:
        value_dict.update({'mtu-size': mtu})
    value_dict.update({'ip-address': ip})
    ipobject = extension_ip_interface(value_dict)
    result = _show_extension_ip(session, ipobject)
    return result


def main(argv):
    # myinput = "-i 10.17.3.70 -n 4/17 -d 0 --ip-address 124.10.10.1 -p 24"
    # myinput = "-i 10.17.3.70 -n 7/17"
    # myinput = "-i 10.17.3.70 --vlan-id 100"
    # myinput = "-i 10.17.3.70 --mtu-size 1567"
    # argv = myinput.split()
    filters = ["name", "mtu_size", "ip_prefix_length",
               "ip_address", "dp_id", "vlan_id"]
    inputs = brcd_util.parse(argv, extension_ip_interface, filters)
    ipobject = inputs['utilobject']
    session = brcd_util.getsession(inputs)
    result = _show_extension_ip(session, ipobject)
    if len(result) == 0:
        print("No IP Interface found.")
    else:
        pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
