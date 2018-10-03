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

:mod:`switch_ip_config_get` - PyFOS util for getting the IP config parameters
*******************************************************************************
The :mod:`switch_ip_config_get` util for getting the switch IP configuration.

This module is a standalone script that can be used to display the IP addresses
of switch, IP address of switch gateways and the subnet mask of switch

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

.. function:: show_switch_ip_config(session)

        Example usage of the method::

            ret = switch_ip_config_get.show_switch_ip_config(session)
            print (ret)

        Details::

            filters = ['ip_address_ip_address',\
'ip_static_gateway_list_ip_static_gateway', 'subnet_mask']
            result = fibrechannel_switch.get(session, None, filters)
            return result

        * inputs:
            :param session: session returned by login.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Retrieve the gateways configured in switch
        2. Retrieve subnet mask of the switch.


"""

import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
import sys
import pyfos.utils.brcd_util as brcd_util
from pyfos.pyfos_brocade_fibrechannel_switch import fibrechannel_switch
import pyfos.pyfos_version as version


def show_switch_ip_config(session):
    filters = ['ip_address_ip_address',
               'ip_static_gateway_list_ip_static_gateway', 'subnet_mask']
    result = fibrechannel_switch.get(session, None, filters)
    return result


def main(argv):

    filters = []
    inputs = brcd_util.parse(argv, fibrechannel_switch, filters)

    session = brcd_util.getsession(inputs)
    if (session['version'] < version.fosversion("8.2.1")):
        print("GET operation on ip-static-gateway-list/ip-static-gateway\
 and subnet_mask are supported from FOS v8.2.1")
    result = show_switch_ip_config(inputs['session'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
