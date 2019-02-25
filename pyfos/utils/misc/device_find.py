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
import sys
from pyfos import pyfos_auth
import pyfos.pyfos_brocade_zone as pyfos_zone
import pyfos.pyfos_brocade_fibrechannel_switch as pyfos_switch
import pyfos.pyfos_brocade_name_server as pyfos_name_server
from pyfos.utils import brcd_util


def is_device_local(ns_entry, domain_id):
    # Local variables
    port = None

    # Get PID
    pid = ns_entry.peek_port_id()

    # Mask PID to get domain
    entry_domain = pid[2] + pid[3]

    # Compare domains
    if domain_id == int(entry_domain, 16):
        port = ns_entry.peek_port_index()

    return port


# Find device entry in Name Server
def find_in_name_server(session, device_wwn):
    # Local variables
    local_ports = []
    device_pids = []

    # Get Name Server database
    ns_entries = pyfos_name_server.fibrechannel_name_server.get(session, None)

    # Get domain ID
    switch_info = pyfos_switch.fibrechannel_switch.get(session, None)
    domain_id = switch_info.peek_domain_id()

    # Iterate through Name Server entries
    if isinstance(ns_entries, list):
        for entry in ns_entries:
            if (entry.peek_node_name() == device_wwn or
                    entry.peek_port_name() == device_wwn):
                device_pids.append(entry.peek_port_id())
                port = is_device_local(entry, domain_id)
                if port is not None:
                    local_ports.append(int(port))
    else:
        if (ns_entries.peek_node_name() == device_wwn or
                ns_entries.peek_port_name() == device_wwn):
            device_pids.append(ns_entries.peek_port_id())
            port = is_device_local(ns_entries, domain_id)
            if port is not None:
                local_ports.append(port)

    return (device_pids, local_ports)


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


def find_in_cfgs(session, zones):
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
        brcd_util.full_usage(usage, valid_options)
        sys.exit()

    brcd_util.exit_register(session)

    vfid = None
    if 'vfid' in inputs:
        vfid = inputs['vfid']

    if vfid is not None:
        pyfos_auth.vfid_set(session, vfid)

    if "device" not in inputs:
        pyfos_auth.logout(session)
        brcd_util.full_usage(usage, valid_options)
        sys.exit()
    device_wwn = inputs["device"]

    (device_pids, local_ports) = find_in_name_server(session, device_wwn)
    if local_ports:
        print(" ")
        for local_port in local_ports:
            print(device_wwn + " is locally connected at " + str(local_port))
    else:
        print(" ")
        print(device_wwn + " is NOT locally connected")

    if device_pids:
        print(" ")
        for pid in device_pids:
            print(device_wwn + " is connected in fabric at " + pid)
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

    cfgs = find_in_cfgs(session, zones)

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
