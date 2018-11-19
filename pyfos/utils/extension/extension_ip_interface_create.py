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

:mod:`extension_ip_interface_create` - PyFOS util for creating an \
IP interface.
*******************************************************************************
The :mod:`extension_ip_interface_create` util is used to create an \
IP interface.

This module is a stand-alone script that can be used to create an extension
IP address.

extension_ip_interface_create.py: Usage

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

* Outputs:
    * Python dictionary content with RESTCONF response data.

.. function:: extension_ip_interface_create.create_extension_ip(session,\
name, dp, ip, prefix, vlan=None, mtu=None)

    *Create Extension IP Address*

        Example Usage of the Method::

            ret = extension_ip_interface_create.create_extension_ip(session,
            name, dp, ip, prefix, vlan=None, mtu=None)
            print (ret)

        Details::

            IP = {
                            "name": name,
                            "dp-id": dp,
                            "ip-address": ip
                            "ip-prefix-length": prefix
                            "vlan-id": vlan
                            "mtu-size": mtu
                      }
            result = extension_ip_interface_create._create_extension_ip(
            session, IP)

        * Input:
            :param session: The session returned by login.
            :param name: Sets the GE_Port name expressed as slot/port.
            :param dp-id: Sets the DP instance.
            :param ip: Sets the extension IP address.
            :param prefix: Sets the prefix length for the IP address.
            :param vlan: Sets the VLAN ID.
            :param mtu: Sets the MTU size.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

         Create a new extension IP interface.
"""


import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_extension_ip_interface import extension_ip_interface
from pyfos.utils import brcd_util


isHttps = "0"


def _create_extension_ip(session, ipobject):
    result = ipobject.post(session)
    return result


def create_extension_ip(session, name, dp, ip, prefix, vlan=None, mtu=None):
    value_dict = {'name': name, 'dp-id': dp, 'ip-prefix-length': prefix}
    value_dict.update({'ip-address': ip})
    if vlan is not None:
        value_dict.update({'vlan-id': vlan})
    if mtu is not None:
        value_dict.update({'mtu-size': mtu})
    ipobject = extension_ip_interface(value_dict)
    result = _create_extension_ip(session, ipobject)
    return result


def validate(ipobject):
    if ipobject.peek_name() is None or \
       ipobject.peek_dp_id() is None or \
       ipobject.peek_ip_prefix_length() is None or \
       ipobject.peek_ip_address() is None:
        return 1
    return 0


def main(argv):
    # myinput = "-i 10.17.3.70  -n 4/17 -d 0 --ip-address 134.10.10.1 -p 24"
    # argv = myinput.split()
    filters = ["name", "mtu_size", "ip_prefix_length",
               "ip_address", "dp_id", "vlan_id"]
    inputs = brcd_util.parse(argv, extension_ip_interface, filters, validate)
    ipobject = inputs['utilobject']
    session = brcd_util.getsession(inputs)
    result = _create_extension_ip(session, ipobject)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
