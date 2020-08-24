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

:mod:`dns_config_modify` - PyFOS util to modify the DNS configuration.
********************************************************************************
The :mod:`dns_config_modify` util is used to modify the
DNS configuration (DNS servers and domain name) set for the switch.

This module is a stand-alone script that can be used to
modify the DNS configuration for the switch.

dns_config_modify.py: Usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed [Optional].
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * -d,--dns-servers=DNS_IPS: Sets the of IPv4 or IPv6 addresses for a
        maximum of two DNS servers.
    * -n,--domain-name=VALUE: Sets the domain name assigned to the switch.

* Output:
    * Python dictionary content with RESTCONF response data.

.. function:: dns_config_modify.modify_dns_config_params(session,\
servers, name)

    *Modify the IP address and domain name (can be an empty string) of the \
      DNS servers*

        Example Usage of the Method::

             ret = dns_config_modify.modify_dns_config_params(session,
             servers , name)
             print (ret)

        Details::

             swobject = fibrechannel_switch()
             swobject.set_dns_servers_dns_server(servers)
             if name is not None:
                 swobject.set_domain_name(name)
             result = _modify_dns_config_params(
                 session, swobject)
             return result

        * Input:
            :param session: The session returned by the login.
            :param servers: A list of IPv4 or IPv6 addresses of the \
                             DNS servers.
            :param name: The domain name assigned to the switch.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

         Modify the DNS servers and domain name (can be an empty string)
         of a switch.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_fibrechannel_switch import fibrechannel_switch
import pyfos.pyfos_version as version


def _modify_dns_config_params(session, swobject):
    if swobject.peek_name() is None:
        current_swobj = fibrechannel_switch.get(session)
        if isinstance(current_swobj, fibrechannel_switch):
            swobject.set_name(current_swobj.peek_name())
        else:
            return current_swobj
    result = swobject.patch(session)
    return result


def modify_dns_config_params(session, servers, name=None):
    swobject = fibrechannel_switch()
    swobject.set_dns_servers_dns_server(servers)
    if name is not None:
        swobject.set_domain_name(name)
    result = _modify_dns_config_params(
        session, swobject)
    return result


def validate(swobject):
    if swobject.peek_dns_servers_dns_server() == "[]" and \
       swobject.peek_domain_name() is None:
        return 1
    return 0


def main(argv):
    filters = ["dns_servers_dns_server", "domain_name"]
    inputs = brcd_util.parse(argv, fibrechannel_switch, filters,
                             validate)
    swobject = inputs['utilobject']
    session = brcd_util.getsession(inputs)
    if session['version'] < version.fosversion("8.2.1"):
        skipattributes = ""
        if swobject.peek_domain_name() is not None:
            skipattributes += "domain-name"
        if swobject.peek_dns_servers_dns_server() != "[]":
            if len(skipattributes) > 0:
                skipattributes += ","
            skipattributes += "dns-servers/dns-server"
        if len(skipattributes) > 0:
            print("Skipping following attributes:(", skipattributes,
                  ") for patch as the switch fos version[",
                  session['version'].to_string(),
                  "]is below the supported attribute version of 8.2.1")
        pyfos_auth.logout(session)
        return
    result = _modify_dns_config_params(session, swobject)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
