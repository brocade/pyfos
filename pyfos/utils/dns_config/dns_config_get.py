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

:mod:`dns_config_get` - PyFOS util for getting the DNS config parameters
*******************************************************************************
The :mod:`dns_config_get` util for getting the switch DNS configuration.

This module is a standalone script that can be used to display IP address
of DNS servers and the domain name

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.


* outputs:
    * Python dictionary content with RESTCONF response data.

.. function:: show_dns_config(session)

        Example usage of the method::

            ret = dns_config_get.show_dns_config(session)
            print (ret)

        Details::

            filters = ['dns_servers_dns_server', 'domain_name']
            result = fibrechannel_switch.get(session, None, filters)
            return result

        * inputs:
            :param session: session returned by login.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Retrieve the DNS Servers configured in switch
        2. Retrieve domain name of the switch.


"""

import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
import sys
import pyfos.utils.brcd_util as brcd_util
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
    if (session['version'] < version.fosversion("8.2.1")):
        print("GET operation on dns-servers/dns-server\
 and domain-name are supported from FOS v8.2.1")
        pyfos_auth.logout(session)
        return
    result = show_dns_config(inputs['session'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
