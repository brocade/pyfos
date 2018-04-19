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

:mod:`device_find` - PyFOS util for misc use case.
***********************************************************************************
The :mod:`device_find` provides for misc use case.

This module is a stand-alone script that can be used to determine if the device
is connected locally and where in the Zone DB it is mentioned.

* Inputs:
    * -L=<login>: Login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: IP address.
    * --device=<device>: WWN of the device in question.
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        a VFID of 128 is assumed.

* Outputs:
    * Displays physical location and Zone DB mentions.

"""
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_brocade_zone as pyfos_zone
import pyfos.pyfos_brocade_fibrechannel as pyfos_switchfcport
import pyfos.pyfos_brocade_name_server as pyfos_name_server
import pyfos.pyfos_util as pyfos_util
import sys
import pyfos.utils.brcd_util as brcd_util


def print_connected_location(session, device_wwn):
    connected_ports = []
    ports = pyfos_switchfcport.fibrechannel.get(session)
    if not pyfos_util.is_failed_resp(ports):
        # check the list of ports
        if isinstance(ports, list):
            for port in ports:
                neighbor_list = port.peek_neighbor_wwn()
                if len(neighbor_list) > 0:
                    for device in neighbor_list:
                        if device_wwn == device:
                            connected_ports.append(port.peek_name())
        # otherwise, just one port returned
        else:
            neighbor_list = ports.peek_neighbor_wwn()
            if len(neighbor_list) > 0:
                for device in neighbor_list:
                    if device_wwn == device:
                        connected_ports.append(ports.peek_name())

    return connected_ports


def find_in_name_server(session, device_wwn):
    ns_attributes = pyfos_name_server.fibrechannel_name_server.get(session, None)
    ns_entries = []
    if isinstance(ns_attributes, list):
        for ns_attribute in ns_attributes:
            if ns_attribute.peek_node_name() == device_wwn:
                ns_entries.append(ns_attribute.peek_port_id())
            elif ns_attribute.peek_port_name() == device_wwn:
                ns_entries.append(ns_attribute.peek_port_id())
    else:
        if ns_attributes.peek_node_name() == device_wwn:
            ns_entries.append(ns_attributes.peek_port_id())
        elif ns_attributes.peek_port_name() == device_wwn:
            ns_entries.append(ns_attributes.peek_port_id())

    return ns_entries


def find_in_aliases(session, device_wwn):
    current_defined = pyfos_zone.defined_configuration.get(session)

    aliases = []
    current_aliases = current_defined.peek_alias()
    for alias in current_aliases:
        for alias_entry_name in alias["member-entry"]["alias-entry-name"]:
            if alias_entry_name == device_wwn:
                aliases.append(alias["alias-name"])

    return aliases


def find_in_zones(session, device_wwn, aliases):
    current_defined = pyfos_zone.defined_configuration.get(session)

    zones = []
    current_zones = current_defined.peek_zone()
    for zone in current_zones:
        for entry_name in zone["member-entry"]["entry-name"]:
            if entry_name == device_wwn:
                zones.append(zone["zone-name"])
            for alias in aliases:
                if alias == entry_name:
                    zones.append(zone["zone-name"])
        if "principal-member-entry" in zone:
            for entry_name in zone["principal-member-entry"]["entry-name"]:
                if entry_name == device_wwn:
                    zones.append(zone["zone-name"])
                for alias in aliases:
                    if alias == entry_name:
                        zones.append(zone["zone-name"])

    return zones


def find_in_cfgs(session, device_wwn, zones):
    current_defined = pyfos_zone.defined_configuration.get(session)

    cfgs = []
    current_cfgs = current_defined.peek_cfg()
    for cfg in current_cfgs:
        for zone_name in cfg["member-zone"]["zone-name"]:
            for zone in zones:
                if zone == zone_name:
                    cfgs.append(cfg["cfg-name"])

    return cfgs


def usage():
    print("  Script specific options:")
    print("")
    print("    --device=DEVICE              wwn of device to be searched")
    print("")


def main(argv):
    valid_options = ["device"]
    inputs = brcd_util.generic_input(argv, usage, valid_options)

    session = pyfos_auth.login(inputs["login"], inputs["password"],
                               inputs["ipaddr"], inputs["secured"],
                               verbose=inputs["verbose"])
    if pyfos_auth.is_failed_login(session):
        print("login failed because",
              session.get(pyfos_auth.CREDENTIAL_KEY)
              [pyfos_auth.LOGIN_ERROR_KEY])
        usage()
        sys.exit()

    brcd_util.exit_register(session)

    vfid = None
    if 'vfid' in inputs:
        vfid = inputs['vfid']

    if vfid is not None:
        pyfos_auth.vfid_set(session, vfid)

    if "device" not in inputs:
        pyfos_auth.logout(session)
        usage()
        sys.exit()
    device_wwn = inputs["device"]

    connected_ports = print_connected_location(session, device_wwn)
    if connected_ports:
        print(" ")
        for connected_port in connected_ports:
            print(device_wwn + " is locally connected at " + connected_port)
    else:
        print(" ")
        print(device_wwn + " is NOT locally connected")

    ns_entries = find_in_name_server(session, device_wwn)
    if ns_entries:
        print(" ")
        for ns_entry in ns_entries:
            print(device_wwn + " is connected in fabric at " + ns_entry)
    else:
        print(" ")
        print("the device is NOT in NS Database")


    aliases = find_in_aliases(session, device_wwn)
    if aliases:
        print(" ")
        print("the device is in alias(es):")
        for alias in aliases:
            print(alias)
    else:
        print(" ")
        print("the device is NOT in any alias(es)")

    zones = find_in_zones(session, device_wwn, aliases)

    if zones:
        print(" ")
        print("the device is in zone(s):")
        for zone in zones:
            print(zone)
    else:
        print(" ")
        print("the device is NOT in zone(s):")

    cfgs = find_in_cfgs(session, device_wwn, zones)

    current_effective = pyfos_zone.effective_configuration.get(session)

    if cfgs:
        print(" ")
        print("the device is in cfg(s):")
        for cfg in cfgs:
            if cfg == current_effective.peek_cfg_name():
                print(cfg, "<---- enabled cfg")
            else:
                print(cfg)
    else:
        print(" ")
        print("the device is NOT in cfg(s):")

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
