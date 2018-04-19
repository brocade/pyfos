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

:mod:`extension_ip_route_modify` - PyFOS util to modify an IP route.
********************************************************************************
The :mod:`extension_ip_route_modify` Util is used to modify an IP route.

This module is a stand-alone script that can be used to modify an extension
IP route.

extension_ip_route_modify.py: Usage

* Infrastructure options:
    * -i,--ipaddr=IPADDR: IP address of FOS switch.
    * -L,--login=LOGIN: Login name.
    * -P,--password=PASSWORD: Password.
    * -f,--vfid=VFID: VFID to which the request is directed.
    * -s,--secured=MODE: HTTPS mode "self" or "CA"[Optional].
    * -v,--verbose: Verbose mode[Optional].

* Util scripts options:
    * -n,--name=NAME: Set name
    * -g,--ip-gateway=VALUE: Set ip-gateway
    * -p,--ip-prefix-length=VALUE: Set ip-prefix-length
    * -d,--dp-id=VALUE: Set dp-id
    *    --ip-address=VALUE: Set ip-address

* Outputs:
    * Python dictionary content with RESTCONF response data.


.. function:: extension_ip_route_modify.modify_extension_ip_route(session,\
name, dp, ip, prefix, gateway)

    *Modify an extension IP route*

        Example usage of the method::

            ret = extension_ip_route_modify.modify_extension_ip_route(
            session, name, dp, ip, prefix, gateway)
            print (ret)

        Details::

            IProute = {
                            "name": name,
                            "dp-id": dp,
                            "ip-address": ip
                            "ip-prefix-length": prefix
                            "ip-gateway": gateway
                      }
            result = extension_ip_route_modify._modify_extension_ip_route(
            session, IProute)

        * Inputs:
            :param session: Session returned by login.
            :param name: GE port name expressed as slot/port.
            :param dp-id: DP Instance.
            :param ip: Extension IP-Address.
            :param prefix: Prefix length for the IP Address.
            :param gateway: IP address gateway.

        * Outputs:
            :rtype: Dictionary of return status matching rest response.

        *Use cases*

         Modify an new extension IP route.
"""

import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_extension_ip_route import extension_ip_route
import sys
import pyfos.utils.brcd_util as brcd_util

isHttps = "0"


def _modify_extension_ip_route(session, iprouteobject):
        result = iprouteobject.patch(session)
        return result


def modify_extension_ip_route(session, name, dp, ip, prefix, gateway):
        value_dict = {'name': name, 'dp-id': dp, 'ip-address': ip,
                      'ip-prefix-length': prefix, 'ip-gateway': gateway}
        iprouteobject = extension_ip_route()
        iprouteobject.load(value_dict, 1)
        result = _modify_extension_ip_route(session, iprouteobject)
        return result


def validate(iprouteobject):
        if iprouteobject.peek_name() is None or \
           iprouteobject.peek_dp_id() is None or \
           iprouteobject.peek_ip_prefix_length() is None or \
           iprouteobject.peek_ip_address() is None or \
           iprouteobject.peek_ip_gateway() is None:
            return 1
        return 0


def main(argv):
        # myinput = str("-i 10.17.3.70  -n 4/17 -d 0 " +
        #               "--ip-address 154.10.10.0 " +
        #               "-g 134.10.10.125 -p 24 ")
        # argv = myinput.split()
        filters = ["name", "ip_prefix_length", "ip_address", "dp_id",
                   "ip_gateway"]
        inputs = brcd_util.parse(argv, extension_ip_route, filters, validate)
        iprouteobject = inputs['utilobject']
        session = brcd_util.getsession(inputs)
        result = _modify_extension_ip_route(session, iprouteobject)
        pyfos_util.response_print(result)
        pyfos_auth.logout(session)


if __name__ == "__main__":
        main(sys.argv[1:])
