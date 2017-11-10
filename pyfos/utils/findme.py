#!/usr/bin/env python3

# Copyright 2017 Brocade Communications Systems, Inc.  All rights reserved.
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

:mod:`findme` - PyFOS util for misc use case.
***********************************************************************************
The :mod:`findme` provides for misc use case.

This module is a standalone script that can be used to find if the device
is connected locally and where in the Zone DB are mentioned.

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * -d=<device>: WWN of the device in question
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.

* outputs:
    * Display of physical location and Zone DB mentions

"""
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_zone as pyfos_zone
import pyfos.pyfos_switchfcport as pyfos_switchfcport
import sys
import pyfos.utils.brcd_util as brcd_util

isHttps = "0"


def print_connected_location(session, device_wwn):
    connected_ports = []
    ports = pyfos_switchfcport.fibrechannel.get(session)
    for port in ports:
        neighbor_list = port.peek_neighbor_wwn()
        if len(neighbor_list) > 0:
            for device in neighbor_list:
                if device_wwn == device:
                    connected_ports.append(port.peek_name())
    return connected_ports


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
    print("usage:")
    print('findme.py -i <ipaddr> -d <device>')


def main(argv):
    inputs = brcd_util.generic_input(argv, usage)

    session = pyfos_auth.login(inputs["login"], inputs["password"],
                               inputs["ipaddr"], isHttps)
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
        for connected_port in connected_ports:
            print(device_wwn + " is connected at " + connected_port)

    aliases = find_in_aliases(session, device_wwn)

    if aliases:
        print(" ")
        print("the device is in alias(es):")
        for alias in aliases:
            print(alias)

    zones = find_in_zones(session, device_wwn, aliases)

    if zones:
        print(" ")
        print("the device is in zone(s):")
        for zone in zones:
            print(zone)

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

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
