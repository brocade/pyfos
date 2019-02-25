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

:mod:`dns_config_show` - PyFOS util for showing the DNS configuration \
 parameters.
**********************************************************************************
The :mod:`dns_config_show` util displaying the switch DNS configuration.

This module is a stand-alone script that can be used to display the \
 IP addresses of DNS servers and the domain name.

* Input:
    * -L=<login>: The login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: The password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: The IP address.
    * -f=<VFID>: The VFID or -1 if VF is disabled. If unspecified,
        a VFID of 128 is assumed.


* Output:
    * Python dictionary content with RESTCONF response data.

.. function:: show_dns_config(session)

        Example Usage of the Method::

            ret = dns_config_show.show_dns_config(session)
            print (ret)

        Details::

            filters = ['dns_servers_dns_server', 'domain_name']
            result = fibrechannel_switch.get(session, None, filters)
            return result

        * Input:
            :param session: The session returned by the login.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Retrieve the DNS servers configured in a switch.
        2. Retrieve the domain name of the switch.


"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_fibrechannel_switch import fibrechannel_switch
import pyfos.pyfos_version as version


def show_dns_config(session):
    filters = ['dns_servers_dns_server', 'domain_name']
    result = fibrechannel_switch.get(session, None, filters)
    return result


def main(argv):

    filters = []
    inputs = brcd_util.parse(argv, fibrechannel_switch, filters)

    session = brcd_util.getsession(inputs)
    if session['version'] < version.fosversion("8.2.1"):
        print("GET operation on dns-servers/dns-server\
 and domain-name are supported from FOS v8.2.1")
        pyfos_auth.logout(session)
        return
    result = show_dns_config(inputs['session'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
