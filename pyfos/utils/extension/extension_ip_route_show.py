#!/usr/bin/env python3


# Copyright 2019-2020 Brocade Communications Systems LLC.
# All rights reserved.
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


# extension_ip_route_show.py(pyGen v1.0.0)


"""

:mod:`extension_ip_route_show` - PyFOS util to show for\
extension_ip_route
*******************************************************************************
The :mod:`extension_ip_route_show` PyFOS util to show for extension_ip_route


Represents static IP route on the IP interface defined on extension blade or\
system.

extension_ip_route_show : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --ip-prefix-length=IP-PREFIX-LENGTH The prefix length operator for the\
      destination IP address. Once set, prefix length can not be changed.
    * --dp-id=DP-ID Extension Data Path Processor ID associated with the IP\
      Route. Based on platform either it will have a single DP or dual DP.\
      In case of single DP only DP0 is supported, and in case of dual DP\
      both DP0 and DP1 are supported.  0 : DP0 1 : DP1
    * --ip-gateway=IP-GATEWAY Specifies the IP address of an IP router that\
      can route packets to the destination IP address. The gateway address\
      must be on the same IP subnet as one of the port IP addresses. This\
      operand is optional with IPv6 addresses. Once set, IP gateway can not\
      changed.
    * --name=NAME The name of the interface.
    * --status-flags=STATUS-FLAGS Iproute Flags:   U = Usable  G = Gateway  H\
      = Host  C = Created (Interface)  S = Static  L = LinkLayer
    * --ip-address=IP-ADDRESS Specifies the destination IPv4/IPv6 address.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: extension_ip_route_show.show_extension_ip_route(session,\
ip_prefix_length, dp_id, ip_gateway, name, status_flags, ip_address)

    *Show extension_ip_route*

        Example Usage of the Method::

            ret = extension_ip_route_show.show_extension_ip_route(session,\
            ip_prefix_length, dp_id, ip_gateway, name, status_flags,\
            ip_address)
            print (ret)

        Details::

            extension_ip_routeObj = extension_ip_route()
            extension_ip_routeObj.set_ip_prefix_length(ip_prefix_length)
            extension_ip_routeObj.set_dp_id(dp_id)
            extension_ip_routeObj.set_ip_gateway(ip_gateway)
            extension_ip_routeObj.set_name(name)
            extension_ip_routeObj.set_status_flags(status_flags)
            extension_ip_routeObj.set_ip_address(ip_address)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param ip_prefix_length: The prefix length operator for the\
              destination IP address. Once set, prefix length can not be\
              changed.
            :param dp_id: Extension Data Path Processor ID associated with the\
              IP Route. Based on platform either it will have a single DP or\
              dual DP. In case of single DP only DP0 is supported, and in\
              case of dual DP both DP0 and DP1 are supported.  0 : DP0 1 :\
              DP1
            :param ip_gateway: Specifies the IP address of an IP router that\
              can route packets to the destination IP address. The gateway\
              address must be on the same IP subnet as one of the port IP\
              addresses. This operand is optional with IPv6 addresses. Once\
              set, IP gateway can not changed.
            :param name: The name of the interface.
            :param status_flags: Iproute Flags:   U = Usable  G = Gateway  H =\
              Host  C = Created (Interface)  S = Static  L = LinkLayer
            :param ip_address: Specifies the destination IPv4/IPv6 address.

        * Output:

            :rtype: None or more instance of class extension_ip_route on\
            Success  or a dictionary with error.

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_extension_ip_route import extension_ip_route
from pyfos.utils import brcd_util
# End module imports


def _show_extension_ip_route(session, extension_ip_routeObj):
    objlist = extension_ip_route.get(session)
    extension_ip_routelist = list()
    if isinstance(objlist, extension_ip_route):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if extension_ip_routeObj.peek_ip_prefix_length() is not None and\
               extension_ip_routeObj.peek_ip_prefix_length() !=\
               objlist[i].peek_ip_prefix_length():
                continue
            if extension_ip_routeObj.peek_dp_id() is not None and\
               extension_ip_routeObj.peek_dp_id() != objlist[i].peek_dp_id():
                continue
            if extension_ip_routeObj.peek_ip_gateway() is not None and\
               extension_ip_routeObj.peek_ip_gateway() !=\
               objlist[i].peek_ip_gateway():
                continue
            if extension_ip_routeObj.peek_name() is not None and\
               extension_ip_routeObj.peek_name() != objlist[i].peek_name():
                continue
            if extension_ip_routeObj.peek_status_flags() is not None and\
               extension_ip_routeObj.peek_status_flags() !=\
               objlist[i].peek_status_flags():
                continue
            if extension_ip_routeObj.peek_ip_address() is not None and\
               extension_ip_routeObj.peek_ip_address() !=\
               objlist[i].peek_ip_address():
                continue
            extension_ip_routelist.append(objlist[i])
    else:
        print(objlist)
    return extension_ip_routelist


def show_extension_ip_route(session, ip_prefix_length=None, dp_id=None,
                            ip_gateway=None, name=None, status_flags=None,
                            ip_address=None):
    extension_ip_routeObj = extension_ip_route()
    extension_ip_routeObj.set_ip_prefix_length(ip_prefix_length)
    extension_ip_routeObj.set_dp_id(dp_id)
    extension_ip_routeObj.set_ip_gateway(ip_gateway)
    extension_ip_routeObj.set_name(name)
    extension_ip_routeObj.set_status_flags(status_flags)
    extension_ip_routeObj.set_ip_address(ip_address)
    return _show_extension_ip_route(session, extension_ip_routeObj)


def main(argv):
    filters = ["ip_prefix_length", "dp_id", "ip_gateway", "name",
               "status_flags", "ip_address"]
    inputs = brcd_util.parse(argv, extension_ip_route, filters)
    session = brcd_util.getsession(inputs)
    result = _show_extension_ip_route(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
