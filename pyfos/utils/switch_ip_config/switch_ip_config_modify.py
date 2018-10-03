#!/usr/bin/env python3.5

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

:mod:`switch_ip_config_modify` - PyFOS util to modify IP config.
********************************************************************************
The :mod:`switch_ip_config_modify` Util is used to modify the
IP config(IP address, static gateways and subnet mask) set for the switch.

This module is a stand-alone script that can be used to
modify the IP config for the switch.

switch_ip_config_modify.py: Usage

* Infrastructure options:
    * -i,--ipaddr=IPADDR: IP address of FOS switch.
    * -L,--login=LOGIN: Login name.
    * -P,--password=PASSWORD: Password.
    * -f,--vfid=VFID: VFID to which the request is directed[Optional].
    * -s,--secured=MODE: HTTPS mode "self" or "CA"[Optional].
    * -v,--verbose: Verbose mode[Optional].

* Util scripts options:
    * --addresses=SWITCH_IPS: List of maximum 2 IPv4/IPv6 addresses assigned
        to switch. One IPv4 and one IPv6 address is allowed.
    * -g,--gateways=GATEWAY_IPS: List of static IPv4/IPv6
        ip-address of maximum 2 gateways.
    * -m,--mask=VALUE: Subnet mask assigned to switch
* Outputs:
    * Python dictionary content with RESTCONF response data.

.. function:: switch_ip_config_modify.modify_switch_ip_config_params(session,\
ip_addresses, gateways, subnet_mask)

    *Modify IP addresses , static IP address of gateways and subnet-mask \
of the switch*

        Example usage of the method::

             ret = switch_ip_config_modify.modify_switch_ip_config_params(\
session, ip_addresses, gateways , subnet_mask)
             print (ret)

        Details::

             swobject = fibrechannel_switch()
             if ip_addresses is not None:
                 swobject.set_ip_address_ip_address(ip_addresses)
             if gateways is not None:
                 swobject.set_ip_static_gateway_list_ip_static_gateway(gateways)
             if subnet_mask is not None:
                 swobject.set_subnet_mask(subnet_mask)
             result = _modify_switch_ip_config_params(session, swobject)
             return result

        * Inputs:
            :param session: Session returned by login.
            :param ip_addresses: List of IPv4/IPv6 addresses for the switch.
            :param gateways: List of IPv4/IPv6 address of switch IP network \
gateways.
            :param subnet_mask: Subnet mask assigned to the switch

        * Outputs:
            :rtype: Dictionary of return status matching rest response.

        *Use cases*

         Modify the IP addresses of switch, IP address of gateways and \
subnet mask of a switch.

"""

import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
import sys
import pyfos.utils.brcd_util as brcd_util
from pyfos.pyfos_brocade_fibrechannel_switch import fibrechannel_switch
import pyfos.pyfos_version as version


def _modify_switch_ip_config_params(session, swobject):
        if swobject.peek_name() is None:
            current_swobj = fibrechannel_switch.get(session)
            swobject.set_name(current_swobj.peek_name())
        result = swobject.patch(session)
        return result


def modify_switch_ip_config_params(session, ip_addresses=None, gateways=None,
                                   subnet_mask=None):
        swobject = fibrechannel_switch()
        if ip_addresses is not None:
            swobject.set_ip_address_ip_address(ip_addresses)
        if gateways is not None:
            swobject.set_ip_static_gateway_list_ip_static_gateway(gateways)
        if subnet_mask is not None:
            swobject.set_subnet_mask(subnet_mask)
        result = _modify_switch_ip_config_params(
            session, swobject)
        return result


def validate(swobject):
        if swobject.peek_ip_static_gateway_list_ip_static_gateway() \
           == "[]" and \
           swobject.peek_subnet_mask() is None and \
           swobject.peek_ip_address_ip_address() == "[]":
            return 1
        return 0


def main(argv):
        filters = ["ip_address_ip_address",
                   "ip_static_gateway_list_ip_static_gateway", "subnet_mask"]
        inputs = brcd_util.parse(argv, fibrechannel_switch, filters,
                                 validate)
        session = brcd_util.getsession(inputs)
        swobject = inputs['utilobject']
        if (session['version'] < version.fosversion("8.2.1")):
            skipattributes = ""
            if swobject.peek_subnet_mask() is not None:
                skipattributes += "subnet-mask"
            if swobject.peek_ip_static_gateway_list_ip_static_gateway() != \
               "[]":
                if len(skipattributes) > 0:
                    skipattributes += ","
                skipattributes += "ip-static-gateway-list/ip-static-gateway"
            if len(skipattributes) > 0:
                print("Skipping following attributes:(", skipattributes,
                      ") for patch as the switch fos version[",
                      session['version'].to_string(),
                      "]is below the supported attribute version of 8.2.1")
            if swobject.peek_ip_address_ip_address() == "[]":
                pyfos_auth.logout(session)
                return
        result = _modify_switch_ip_config_params(session, swobject)
        pyfos_util.response_print(result)
        pyfos_auth.logout(session)


if __name__ == "__main__":
        main(sys.argv[1:])
