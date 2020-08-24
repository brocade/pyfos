#!/usr/bin/env python3

# Copyright © 2012-2021 Broadcom. All rights reserved.
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

"""

:mod:`fabric_discovery` - PyFOS util for fabric discovery using \
custom login methods.
******************************************************************************\
**********************************
The :mod:`fabric_discovery` PyFOS util for fabric discovery using \
custom login methods.

Introduction
---------------------
All Pyfos util scripts are more generic/optimized and not extensible for
multiple operations with different objects. This is to provide new reference
util script on how to combine multiple objects for various operations.

This module :mod:`fabric_discovery` is a stand-alone script that can be used
to discover switches in a fabric and get the uptime from individual switches
using custom login methods. It could be enhanced to do other
fabric operations as well.


Fabric Discovery Process
--------------------------------
The stand-alone script will do the fabric discovery operation and get
the switch uptime for all the switches in the fabric. The below are
the steps followed to achieve this.

1. Do login to seed switch from the input
     a. Uses credentials specified in the script file
     b. pyfos_auth.login() method is used for login
2. Get fabric objects
     a. Invokes /brocade-fabric/fabric-switch URI from seed switch
3. Do logout
     a. Logout from seed switch
4. Do the below for all fabric objects
     a. Get IP address of individual switches
     b. Do login to each switch with input credentials
     c. Query /brocade-fibrechannel-switch/fibrechannel-switch URI
     d. Peek up-time from switch object add it to dictionary
     e. Do logout
5. Print all uptime data from fabric switches in dictionary format

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
import pyfos.pyfos_brocade_fabric as pyfos_fabric
from pyfos.pyfos_brocade_fibrechannel_switch import fibrechannel_switch

ISHTTPS = "False"
USERNAME = "admin"
PASSWORD = ""
IPADDRESS = ""
VFID = -1


# Get session from switch
def get_session(ip):
    return pyfos_auth.login(USERNAME, PASSWORD, ip, ISHTTPS)


# Get fabric details from the input seed switch
def get_fabric_from_seedswitch():

    fabric = []
    # Get session from input seed switch
    session = get_session(IPADDRESS)
    if pyfos_auth.is_failed_login(session):
        print("Login failed due to",
              session.get(pyfos_auth.CREDENTIAL_KEY)
              [pyfos_auth.LOGIN_ERROR_KEY])
        sys.exit()
    else:
        pyfos_auth.vfid_set(session, VFID)

        # Get fabric from seed switch
        fabric = pyfos_fabric.fabric_switch.get(session)

        pyfos_auth.logout(session)

    return fabric


# Get fabric ipaddress list
def get_fabric_ipaddr_list(fabric_switches):

    fabric_switch_ips = []
    # Check if its valid list
    if isinstance(fabric_switches, list):
        for entry in fabric_switches:
            ip = entry.peek_ip_address()
            if ip is not None:
                fabric_switch_ips.append(ip)
    else:
        # Peek individual ipaddress from fabric and add into list
        ip = fabric_switches.peek_ip_address()
        if ip is not None:
            fabric_switch_ips.append(ip)

    return fabric_switch_ips


# Get uptime from individual switches
def get_uptime_from_fabric(fabric_switch_ips):

    # Define a dictionary
    fabric_uptime = {}
    # Get uptime from all the fabric switches
    for ip in fabric_switch_ips:
        session = get_session(ip)
        if pyfos_auth.is_failed_login(session):
            print("Login failed due to",
                  session.get(pyfos_auth.CREDENTIAL_KEY)
                  [pyfos_auth.LOGIN_ERROR_KEY])
            continue

        switch = fibrechannel_switch.get(session)
        if pyfos_util.is_failed_resp(switch):
            pyfos_util.response_print(switch)
            continue

        # Peek uptime from fabric switch
        if isinstance(switch, list):
            for entry in switch:
                uptime = entry.peek_up_time()
        else:
            uptime = switch.peek_up_time()

        # Update dictionary
        fabric_uptime[ip] = uptime

        pyfos_auth.logout(session)

    return fabric_uptime


def main():
    # Get fabric from seed switch
    fabric = get_fabric_from_seedswitch()

    # If response is success, get ipaddress list
    if pyfos_util.is_failed_resp(fabric):
        pyfos_util.response_print(fabric)
        sys.exit()
    else:
        fabric_switch_ips = get_fabric_ipaddr_list(fabric)

    # Get uptime list from fabric switches
    uptime_list = get_uptime_from_fabric(fabric_switch_ips)

    if not uptime_list:
        print("No switch available in the fabric.")
    else:
        print("Fabric uptime: " + str(uptime_list))


if __name__ == "__main__":
    main()
