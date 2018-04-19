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

:mod:`extension_ip_interface_delete` - PyFOS util to delete an IP interface
********************************************************************************
The :mod:`extension_ip_interface_delete` Util is used for IP Interface deletion.

This module is a stand-alone script that can be used to delete an extension
IP Interface.

extension_ip_interface_delete.py: Usage

* Infrastructure options:
    * -i,--ipaddr=IPADDR: IP address of FOS switch.
    * -L,--login=LOGIN: Login name.
    * -P,--password=PASSWORD: Password.
    * -f,--vfid=VFID: VFID to which the request is directed.
    * -s,--secured=MODE: HTTPS mode "self" or "CA"[Optional].
    * -v,--verbose: Verbose mode[Optional].

* Util scripts options:
    * -n,--name=NAME: Set name.
    * -p,--ip-prefix-length=VALUE: Set ip-prefix-length.
    * -d,--dp-id=VALUE: Set dp-id.
    *    --ip-address=VALUE: Set ip-address.

* Outputs:
    * Python dictionary content with RESTCONF response data.

.. function:: extension_ip_interface_delete.delete_extension_ip(session,\
name, dp, ip, prefix, vlan=None, mtu=None)

    *Delete extension IP Interface*

        Example usage of the method::

            ret = extension_ip_interface_delete.delete_extension_ip(session,
            name, dp, ip, prefix, vlan=None, mtu=None)
            print (ret)

        Details::

            IP = {
                            "name": name,
                            "dp-id": dp,
                            "ip-address": ip
                            "ip-prefix-length": prefix

                      }
            result = extension_ip_interface_delete._delete_extension_ip(
            session, IP)

        * Inputs:
            :param session: Session returned by login.
            :param name: GE port name expressed as slot/port.
            :param dp-id: DP Instance.
            :param ip: Extension IP-Address.
            :param prefix: Prefix length for the IP Address.

        * Outputs:
            :rtype: Dictionary of return status matching rest response.

        *Use cases*

         Delete an extension IP Interface.
"""

import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_extension_ip_interface import extension_ip_interface
import sys
import pyfos.utils.brcd_util as brcd_util


isHttps = "0"


def _delete_extension_ip(session, ipobject):
        result = ipobject.delete(session)
        return result


def delete_extension_ip(session, name, dp, ip, prefix, vlan=None, mtu=None):
        value_dict = {'name': name, 'dp-id': dp, 'ip-prefix-length': prefix}
        if vlan is not None:
                value_dict.update({'vlan-id': vlan})
        if mtu is not None:
                value_dict.update({'mtu-size': mtu})
        value_dict.update({'ip-address': ip})
        ipobject = extension_ip_interface(value_dict)
        result = _delete_extension_ip(session, ipobject)
        return result


def validate(ipobject):
        if ipobject.peek_name() is None or \
           ipobject.peek_dp_id() is None or \
           ipobject.peek_ip_address() is None:
            return 1
        return 0


def main(argv):
        # myinput = "-i 10.17.3.70 -n 4/17 -d 0 --ip-address 134.10.10.1 -p 24"
        # argv = myinput.split()
        filters = ["name", "ip_prefix_length", "ip_address", "dp_id"]
        inputs = brcd_util.parse(argv, extension_ip_interface, filters,
                                 validate)
        ipobject = inputs['utilobject']
        session = brcd_util.getsession(inputs)
        result = _delete_extension_ip(session, ipobject)
        pyfos_util.response_print(result)
        pyfos_auth.logout(session)


if __name__ == "__main__":
        main(sys.argv[1:])
