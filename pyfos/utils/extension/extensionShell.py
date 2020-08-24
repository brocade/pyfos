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

:mod:`extensionShell` - PyFOS util for emulating an extension shell.
********************************************************************************
The :mod:`extensionShell` util provides CLI kinds of shell functionality.

This module is a stand-alone script that can be used for basic operation
using an extension CLI. It does not cover all the supported CLI commands.

* Supported Objects:
    * ipif
    * iproute
    * fciptunnel
    * fcipcircuit

* Operations:
    * portcfg
    * portshow

Example::

    portshow ipif
    portshow iproute
    portshow fciptunnel
    portshow fcipcircuit

"""

import getpass
import getopt
import sys
import json
import atexit
import re
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_extension_tunnel import extension_tunnel
from pyfos.pyfos_brocade_extension_tunnel import extension_circuit_statistics
from pyfos.pyfos_brocade_extension_tunnel import extension_circuit
from pyfos.pyfos_brocade_interface import extension_ip_interface
from pyfos.pyfos_brocade_extension_ip_route import extension_ip_route
from pyfos.pyfos_rest_util import rest_object


isHttps = None
session = None


show_usage_str = """Usage:
  portshow [<SlotNumber>/]<PortNumber>
    OR
  portshow [<SlotNumber>/]<PortNumber> -link -force
    OR
  portshow -i <port_index | portindex_range> [-f]

        -i:             Confirms port swap has been disabled and to give port
        index as operand
        -x:             Confirms port swap has been disabled and to give port
        index in HEX format as operand
        -f:             ignores non-existing indexes
        portindex_range:Specifies the range of port index
        <portindex1-portindex2>
        (example: 12-14)
    OR
  portshow <option> [<SlotNumber>/]<PortNumber> [<Args>]

Options:
 ipif         To show current IP Addresses
 iproute      To show current IP Route entries
 fciptunnel   To show current FCIP Tunnel info
 fcipcircuit  To show current FCIP Circuit info
 ipsec-policy To show current IPSEC Policy info (7840 / SX6)

 Note: Some of the above commands require additional parameters, such as:
       <slot/>vePort or <slot/>gePort or 'all'
"""

show_ipif_str = """Usage:
  portShow ipif [<slot>/][<port>] [<options>]

Port Format:
   ge#                 - FX8-24 / 7840 / SX6
   xge#                - FX8-24
   ge#.dp#             - 7840 / SX6
   dp#                 - 7840 / SX6

Optional Arguments:
  -l,--link-local      - Display link local addresses [7840 / SX6 only].
  -v,--validate <ver>  - Validate IP configs for specified version.
     --filter <args>   - Limit the output to specific filter criteria.
                         Use portShow ipif --filter -help for details.
"""

cfg_ipif_str = """Usage:  portCfg ipif [<slot>/]<port> <option> [<args>]

Port Format:
   ge#             - FX8-24
   xge#            - FX8-24
   ge#.dp#         - 7840 / SX6
   lan.dp#         - 7840 / SX6

Options:
   create          - Create a new IP interface.
   modify          - Modify an existing IP interface. (7840 / SX6 only).
   delete          - Delete an existing IP interface.

Args:
   <ipaddr>/<pfx> [mtu <mtu>] [vlan <vlanid>]
      or
   <ipaddr> netmask <mask> [mtu <mtu>] [vlan <vlanid>]

   ipaddr          - IP Address to use for operation.
   pfx/netmask     - Prefix length / Netmask (create only).
   mtu             - MTU size (create only).
   vlan            - Specify the VLAN-ID (create 7840 / SX6 only).
   -x,--crossport  - Specify 10G crossport (FX8-24 xge ports only).

Examples:
  portcfg ipif ge2.dp0 create 10.1.42.10/24 vlan 100
  portcfg ipif 8/xge0 create 10.1.42.10/24
  portcfg ipif ge3 create 10.1.42.10 netmask 255.255.255.0
  portcfg ipif lan.dp0 create 10.1.42.10/24 vlan 100
"""

show_iproute_str = """
Usage:
  portShow iproute [<slot>/][<port>] [<options>]

  portCfgShow iproute [<slot>/]<port>

Port Format:
   ge#                 - FX8-24 / 7840 / SX6
   xge#                - FX8-24
   ge#.dp#             - 7840 / SX6
   dp#                 - 7840 / SX6

Optional Arguments:
  -l,--link-local      - Display link local addresses [7840 / SX6 only].
     --filter <args>   - Limit the output to specific filter criteria.
                         Use portShow iproute --filter -help for details.
"""

cfg_iproute_str = """Usage:  portCfg iproute [<slot>/]<port> <option> [<args>]

Port Format:
   ge#             - FX8-24
   xge#            - FX8-24
   ge#.dp#         - 7840 / SX6
   lan.dp#         - 7840 / SX6

Options:
   create          - Create a new IP route.
   modify          - Modify an existing IP route. (7840 / SX6 only).
   delete          - Delete an existing IP route.

Args:
   <ipaddr>/<pfx> <gateway>
      or
   <ipaddr> netmask <mask> <gateway>

   ipaddr          - IP Address to use for operation.
   pfx/netmask     - Prefix length / Netmask.
   gateway         - Gateway IP address to use (create/modify only).
   -x,--crossport  - Specify 10G crossport (FX8-24 xge ports only).

Examples:
  portcfg iproute ge2.dp0 create 10.1.142.0/24 10.1.42.1
  portcfg iproute 8/xge1 create 10.1.142.100/32 10.1.42.2
  portcfg iproute ge3 create 10.1.142.0 netmask 255.255.255.0 10.1.42.1
  portcfg iproute ge3.dp1 delete 10.1.142.0/24
"""

show_tnl_str = """Usage:
  portshow fciptunnel [<slot>/][port]
"""

cfg_tnl_str = """
Usage:   portCfg fciptunnel [<slot>/]<port> <option> [<args>]

Option:    create - Create the specified tunnel/circuit
           modify - Modify the specified tunnel/circuit
           delete - Delete the specified tunnel/circuit

Optional Arguments:
  -b,--min-comm-rate <kbps>    -  Set the minimum guaranteed rate.
  -B,--max-comm-rate <kbps>    -  Set the maximum rate.
"""

show_circuit_str = """Usage:
  portshow fciptunnel [<slot>/][port]

"""


cfg_circuit_str = """Usage:   portCfg fcipcircuit [<slot>/]<port> <option> <cid> [<args>]

Option:    create - Create the specified tunnel/circuit
           modify - Modify the specified tunnel/circuit
           delete - Delete the specified tunnel/circuit

Optional Arguments:
  -a,--admin-status <enable|disable> -
                               -  Set the admin-status of the circuit.
  -S,--local-ip <ipaddr>|none  -  Set local IP address.
  -D,--remote-ip <ipaddr>|none -  Set remote IP address.
     --local-ha-ip <ipaddr>|none -
                               -  Set local HA IP address. This allows for HCL
                                  operations on local switch. [7840 / SX6 only]
     --remote-ha-ip <ipaddr>|none -
                               -  Set remote HA IP address. This allows for HCL
  -b,--min-comm-rate <kbps>    -  Set the minimum guaranteed rate.
  -B,--max-comm-rate <kbps>    -  Set the maximum rate.
"""


def usage(myobject=None, cmd='show'):
    if myobject:
        if isinstance(myobject, extension_ip_interface):
            if cmd == 'show':
                print(show_ipif_str)
            if cmd == 'cfg':
                print(cfg_ipif_str)
        if isinstance(myobject, extension_ip_route):
            if cmd == 'show':
                print(show_iproute_str)
            if cmd == 'cfg':
                print(cfg_iproute_str)
        if isinstance(myobject, extension_tunnel):
            if cmd == 'show':
                print(show_tnl_str)
            if cmd == 'cfg':
                print(cfg_tnl_str)
        if isinstance(myobject, extension_circuit):
            if cmd == 'show':
                print(show_circuit_str)
            if cmd == 'cfg':
                print(cfg_circuit_str)
    else:
        print(show_usage_str)


def exit_handler():
    # pylint: disable=W0603
    global session
    if session is not None:
        pyfos_auth.logout(session)


# pylint: disable=W0613
def parse_circuit(user_command, myobject, value_dict):
    # pylint: disable=W0612
    try:
        opts, args = getopt.getopt(user_command, "b:B:S:D:",
                                   ["min-comm-rate=", "max-comm-rate=",
                                    "local-ip", "remote-ip", ])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        # print(opt)
        if opt in ("-b", "--min-comm-rate"):
            # print(arg)
            value_dict.update({'minimum-communication-rate': arg})
        elif opt in ("-B", "--max-comm-rate="):
            # print(arg)
            value_dict.update({'maximum-communication-rate': arg})
        elif opt in ("-S", "--local-ip="):
            # print(arg)
            value_dict.update({'local-ip-address': arg})
        elif opt in ("-D", "--remote-ip="):
            # print(arg)
            value_dict.update({'remote-ip-address': arg})


def parse_port(arg, myobject, value_dict):
    pattern_verify = re.search('[0-9]*[/][0-9]*', arg)
    if pattern_verify:
        port = arg.split('.')
        # print(port)
        if len(port) > 0:
            name = port[0]
            if isinstance(myobject,
                          (extension_ip_interface, extension_ip_route)):
                name = re.sub('ge', '', port[0])
            value_dict.update({'name': name})

        if len(port) > 1:
            dp = re.sub('DP', '', re.sub('dp', '', port[1]))
            value_dict.update({'dp-id': dp})
        return 0
    print("Incorrect name and or dp-id value specified \"" + arg + "\"")
    return 1


def parse_ipaddress(arg, myobject, value_dict):
    # pylint: disable=W1401
    pattern_verify = re.split('\.|:', arg)
    # print(pattern_verify)
    if pattern_verify:
        if isinstance(myobject, (extension_ip_interface, extension_ip_route)):
            iplist = arg.split('/')
            # print(iplist)
            if len(iplist) > 0:
                value_dict.update({'ip-address': iplist[0]})
            if len(iplist) > 1:
                value_dict.update({'ip-prefix-length': iplist[1]})
            return 0
    if isinstance(myobject, (extension_ip_interface, extension_ip_route)):
        print("Incorrect ip-address/ip-prefix-length" +
              "value specified \"" + arg + "\"")
        return 1
    else:
        return 0


def parse_ipgateway(arg, myobject, value_dict):
    pattern_verify = re.split('[.|:]', arg)
    # print(pattern_verify)
    if len(pattern_verify):
        if isinstance(myobject, (extension_ip_interface, extension_ip_route)):
            iplist = arg.split('/')
            print(iplist)
            if len(iplist) > 0 and len(iplist) < 2:
                value_dict.update({'ip-gateway': iplist[0]})
            return 0
    if isinstance(myobject, (extension_ip_interface, extension_ip_route)):
        print("Incorrect ip-gateway value specified \"" +
              arg + "\"")
        return 1
    else:
        return 0


def parse_cid(arg, myobject, value_dict):
    # pylint: disable=W1401
    pattern_verify = re.search('\d', arg)
    # print(arg, pattern_verify)
    if pattern_verify:
        if isinstance(myobject,
                      (extension_circuit, extension_circuit_statistics)):
            # print(arg, pattern_verify)
            value_dict.update({'circuit-id': arg})
            return 0
    if isinstance(myobject, extension_circuit):
        print("Incorrect cid value specified \"" +
              arg + "\"")
        return 1
    else:
        return 0


def handler(user_command):
    argv = user_command.split()
    argc = len(argv)
    if argc < 2:
        return
    i = 0
    value_dict = dict()
    myobject = None
    cmd = None
    op = "undef"

    # print(argv)
    while i < argc and i <= 4:
        if i == 0 and argv[i] == 'portshow':
            cmd = 'show'
        elif i == 0 and argv[i] == 'portcfg':
            cmd = 'cfg'
        elif i == 0:
            print(argv[i], "Incorrect Argument passed")
            usage()
            return

        if i == 1 and argv[i] == 'ipif':
            myobject = extension_ip_interface()
        if i == 1 and argv[i] == 'iproute':
            myobject = extension_ip_route()
        if i == 1 and argv[i] == 'fciptunnel':
            myobject = extension_tunnel()
        if i == 1 and argv[i] == 'fcipcircuit':
            myobject = extension_circuit()

        if i == 2:
            if argv[i] == 'help':
                usage()
            if parse_port(argv[i], myobject, value_dict):
                return
        if cmd == 'cfg' and i == 3:
            if argv[i] == 'create' or argv[i] == 'modify' or\
               argv[i] == 'delete':
                op = argv[i]
            else:
                print("Incorrect option used")
                usage(myobject)
        if cmd == 'show' and i == 3:
            if parse_ipaddress(argv[i], myobject, value_dict):
                return
            if cmd == 'cfg' and i == 4:
                if parse_cid(argv[i], myobject, value_dict):
                    return
                elif parse_ipaddress(argv[i], myobject, value_dict):
                    return
        i += 1
    if cmd == 'cfg':
        # if argc > 4 and isinstance(myobject, extension_tunnel):
        #       parse_tunnel(user_command, myobject, value_dict)
        if argc > 4 and isinstance(myobject, extension_circuit):
            parse_circuit(argv[i:argc], myobject, value_dict)

    if myobject:
        myobject.load(value_dict, 1)
        # print(value_dict)
    else:
        return
    if cmd == 'show':
        if argc == 2:
            result = myobject.show_all(session)
            print(json.dumps(result, cls=pyfos_util.json_encoder,
                  sort_keys=True, indent=4))
        elif argc > 2:
            result = super(rest_object, myobject).get(session)
            print(json.dumps(result, cls=pyfos_util.json_encoder,
                  sort_keys=True, indent=4))
    elif cmd == 'cfg':
        if op == 'create':
            result = myobject.post(session)
            print(result)
        elif op == 'modify':
            result = myobject.patch(session)
            print(result)
        elif op == 'delete':
            result = myobject.delete(session)
            print(result)
        else:
            print("Incorrect options used")
            usage(myobject)
            return
    else:
        print("Incorrect options used")
        usage(myobject)
        return


def shell(username):
    shell_str = "REST sw128:" + username + ">"
    cmd = input(shell_str)
    while cmd != 'exit':
        if len(cmd) == 0:
            usage()
        else:
            handler(cmd)
        cmd = input(shell_str)


# pylint: disable=W0603, W0613
def main(argv):
    global session
    atexit.register(exit_handler)
    ipaddr = input("Switch IP:")
    login = input("Login:")
    password = getpass.getpass()

    session = pyfos_auth.login(login, password, ipaddr, isHttps)
    if 'login-error' in session.get('credential').keys():
        print("login failed because",
              session.get('credential')['login-error'])
        sys.exit()
    shell(login)
    pyfos_auth.logout(session)
    session = None


if __name__ == "__main__":
    main(sys.argv[1:])
