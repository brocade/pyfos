#!/usr/bin/env python3


# Copyright © 2019-2020 Broadcom. All rights reserved.
# The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries.
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


# extension_ip_interface_modify.py(pyGen v1.0.0)


"""

:mod:`extension_ip_interface_modify` - PyFOS util to modify for\
 extension_ip_interface
******************************************************************************\
*******************************************************************************
The:mod:`extension_ip_interface_modify` PyFOS util to modify for\
 extension_ip_interface


Represents the IP interface defined on extension blade or system.

extension_ip_interface_modify: usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].
    * -a,--authtoken: AuthToken value or AuthTokenManager config\
    file[OPTIONAL].
    * -z,--nosession: Sessionless authentication based login[OPTIONAL].
    * --nocredential: No credential to be sent in the request[OPTIONAL].

* Util Script Options:
    * --dp-id=DP-ID: Extension Data Path Processor ID associated with the IP\
      interface. Based on platform either it will have a single DP or dual\
      DP. In case of single DP only DP0 is supported, and in case of dual DP\
      both DP0 and DP1 are supported  0 : DP0 1 : DP1.
    * --vlan-id=VLAN-ID: Specifies the VLAN ID. This operand is optional.
    * --ip-address=IP-ADDRESS: Specifies the source IPv4/IPv6 address of the\
      interface.
    * --mtu-size=MTU-SIZE: Specifies the maximum transmission unit size. The\
      permitted range is 1280 Bytes to 9216 Bytes or the special value 1\
      which is equivalent to 'auto' mode to  enable PMTU discovery. The\
      discovered value of MTU in 'auto' mode can be found as a circuit\
      attribute.
    * --ip-prefix-length=IP-PREFIX-LENGTH: The prefix length operator for the\
      IP address. Once set, prefix length cannot be changed.
    * --name=NAME: The name of the interface.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: extension_ip_interface_modify.modify_extension_ip_interface(\
session, dp_id, vlan_id, ip_address, mtu_size, ip_prefix_length, name)

    *Modify extension_ip_interface*

    Example Usage of the Method::

            ret =\
 extension_ip_interface_modify.modify_extension_ip_interface(session, dp_id,\
 vlan_id, ip_address, mtu_size, ip_prefix_length, name)
            print(ret)

    Details::

        extension_ip_interfaceObj = extension_ip_interface()
        extension_ip_interfaceObj.set_dp_id(dp_id)
        extension_ip_interfaceObj.set_vlan_id(vlan_id)
        extension_ip_interfaceObj.set_ip_address(ip_address)
        extension_ip_interfaceObj.set_mtu_size(mtu_size)
        extension_ip_interfaceObj.set_ip_prefix_length(ip_prefix_length)
        extension_ip_interfaceObj.set_name(name)
        ret = _modify_extension_ip_interface(session,\
 extension_ip_interfaceObj)
        print(ret)

    **Inputs**

    :param session: The session returned by the login.
    :param dp_id: Extension Data Path Processor ID associated with the IP\
      interface. Based on platform either it will have a single DP or dual\
      DP. In case of single DP only DP0 is supported, and in case of dual DP\
      both DP0 and DP1 are supported  0 : DP0 1 : DP1.
    :param vlan_id: Specifies the VLAN ID. This operand is optional.
    :param ip_address: Specifies the source IPv4/IPv6 address of the\
      interface.
    :param mtu_size: Specifies the maximum transmission unit size. The\
      permitted range is 1280 Bytes to 9216 Bytes or the special value 1\
      which is equivalent to 'auto' mode to  enable PMTU discovery. The\
      discovered value of MTU in 'auto' mode can be found as a circuit\
      attribute.
    :param ip_prefix_length: The prefix length operator for the IP address.\
      Once set, prefix length cannot be changed.
    :param name: The name of the interface.

    **Output**

    :rtype: Dictionary of response

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_interface import extension_ip_interface

from pyfos.utils import brcd_util
# End module imports


def _modify_extension_ip_interface(session, extension_ip_interfaceObj):
    return extension_ip_interfaceObj.patch(session)


def modify_extension_ip_interface(session, dp_id=None, vlan_id=None,
                                  ip_address=None, mtu_size=None,
                                  ip_prefix_length=None, name=None):
    extension_ip_interfaceObj = extension_ip_interface()
    extension_ip_interfaceObj.set_dp_id(dp_id)
    extension_ip_interfaceObj.set_vlan_id(vlan_id)
    extension_ip_interfaceObj.set_ip_address(ip_address)
    extension_ip_interfaceObj.set_mtu_size(mtu_size)
    extension_ip_interfaceObj.set_ip_prefix_length(ip_prefix_length)
    extension_ip_interfaceObj.set_name(name)
    return _modify_extension_ip_interface(session, extension_ip_interfaceObj)


def validate(extension_ip_interfaceObj):
    if extension_ip_interfaceObj.peek_dp_id() is None or\
       extension_ip_interfaceObj.peek_ip_address() is None or\
       extension_ip_interfaceObj.peek_name() is None or\
       bool(extension_ip_interfaceObj.peek_mtu_size() is None and
            extension_ip_interfaceObj.peek_vlan_id() is None):
        return 1
    return 0


def main(argv):
    filters = ["dp_id", "vlan_id", "ip_address", "mtu_size",
               "ip_prefix_length", "name"]
    inputs = brcd_util.parse(argv, extension_ip_interface, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _modify_extension_ip_interface(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
