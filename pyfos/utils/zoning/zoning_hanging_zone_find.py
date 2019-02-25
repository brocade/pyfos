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

:mod:`zoning_hanging_zone_find` - PyFOS util for misc use case.
***********************************************************************************
The :mod:`zoning_hanging_zone_find` provides for misc use case.

This module is a stand-alone script that can be used to display zones
containing no online devices. The script also gives an option to delete
those zones & save the DB. If the effective cfg contains one of the zones
to be deleted, the script will fail. The effective cfg should be updated
to remove the zone before executing the script again.

Online/offline states of devices are taken at the time of the script
execution and they may not account for devices taken offline on purpose
or devices that are toggling due to various reasons. Therefore, the
list of zones to be removed may contain those zones that do not
contain any online devices due to above reasons.

* Inputs:
    * -L=<login>: Login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: IP address.
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        a VFID of 128 is assumed.

* Outputs:
    * Displays "Hanging Zones" and Zones to remain. Then the script
        accepts interactive "YES" input to purge those zones or any
        other inputs to skip.

"""


import sys
from pyfos import pyfos_auth
import pyfos.pyfos_brocade_zone as pyfos_zone
import pyfos.pyfos_brocade_name_server as pyfos_name_server
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def online_in_name_server_by_wwn(ns_attributes, device_wwn):
    if isinstance(ns_attributes, list):
        for ns_attribute in ns_attributes:
            if ns_attribute.peek_node_name() == device_wwn:
                return True
            elif ns_attribute.peek_port_name() == device_wwn:
                return True
    else:
        if ns_attributes.peek_node_name() == device_wwn:
            return True
        elif ns_attributes.peek_port_name() == device_wwn:
            return True

    return False


def online_in_name_server_by_alias(current_defined, ns_attributes,
                                   device_alias):
    current_aliases = current_defined.peek_alias()
    for alias in current_aliases:
        if alias["alias-name"] == device_alias:
            for alias_entry_name in alias["member-entry"]["alias-entry-name"]:
                if pyfos_util.isWWN(alias_entry_name):
                    if online_in_name_server_by_wwn(ns_attributes,
                                                    alias_entry_name):
                        return True
                elif pyfos_util.isDCommaI(alias_entry_name):
                    if online_in_name_server_by_dcommai(ns_attributes,
                                                        alias_entry_name):
                        return True

    return False


def online_in_name_server_by_dcommai(ns_attributes, device_dcommai):
    domain_s, index_s = device_dcommai.split(",")
    domain = int(domain_s, 10)
    index = int(index_s, 10)

    if isinstance(ns_attributes, list):
        for ns_attribute in ns_attributes:
            pid = ns_attribute.peek_port_id()
            dev_domain = int(pid, 16) >> 16
            if (domain == dev_domain and
                    index == ns_attribute.peek_port_index()):
                return True
    else:
        pid = ns_attributes.peek_port_id()
        dev_domain = int(pid, 16) >> 16
        if domain == dev_domain and index == ns_attributes.peek_port_index():
            return True

    return False


filtered_zone_names = [
    "t_r_a_f_f_i_c_i_s_o_prop__zn",
    "red_______base"
    ]

filtered_zone_prefixes = [
    "red_0917",
    "red_1109",
    "lsan_red_0917",
    "lsan_red_1109"
    "msfr_zn"
    ]

filtered_cfg_names = [
    "t_r_a_f_f_i_c_i_s_o_c__fg",
    "m_u_l_t_i_r_e_d_i_r__cfg"
    ]

filtered_cfg_prefixes = [
    "msfr_cfg_",
    "r_e_d_i_r_c__fg"
    ]


def cfg_to_be_filtered(cfg_name):
    for prefix in filtered_cfg_prefixes:
        if cfg_name.startswith(prefix):
            return True

    for name in filtered_cfg_names:
        if name == cfg_name:
            return True

    return False


def zone_to_be_filtered(zone_name, current_defined):
    if zone_name.startswith("BFA") and zone_name.endswith("BLUN"):
        return True

    for prefix in filtered_zone_prefixes:
        if zone_name.startswith(prefix):
            return True

    for name in filtered_zone_names:
        if name == zone_name:
            return True

    current_cfgs = current_defined.peek_cfg()
    for cfg in current_cfgs:
        if not cfg_to_be_filtered(cfg["cfg-name"]):
            continue

        for name in cfg["member-zone"]["zone-name"]:
            if name == zone_name:
                return True

    return False


def process_all_zones(session):
    current_defined = pyfos_zone.defined_configuration.get(session)
    current_effective = pyfos_zone.effective_configuration.get(session)

    ns_attributes = pyfos_name_server.fibrechannel_name_server.get(session,
                                                                   None)

    hanging_zones = []
    online_zones = []
    current_zones = current_defined.peek_zone()
    for zone in current_zones:
        online_device = 0
# checking to see if the zone needs to be skipped because it is part
# of special zones such as TI Zones, RD Zones, etc.
        if zone_to_be_filtered(zone["zone-name"], current_defined):
            online_zones.append(zone["zone-name"])
            continue

        for entry_name in zone["member-entry"]["entry-name"]:
            if pyfos_util.isWWN(entry_name):
                if online_in_name_server_by_wwn(ns_attributes, entry_name):
                    online_device = online_device + 1
            elif pyfos_util.isDCommaI(entry_name):
                if online_in_name_server_by_dcommai(ns_attributes, entry_name):
                    online_device = online_device + 1
            else:
                if online_in_name_server_by_alias(current_defined,
                                                  ns_attributes, entry_name):
                    online_device = online_device + 1
        for entry_name in zone["member-entry"]["principal-entry-name"]:
            if pyfos_util.isWWN(entry_name):
                if online_in_name_server_by_wwn(ns_attributes, entry_name):
                    online_device = online_device + 1
            elif pyfos_util.isDCommaI(entry_name):
                if online_in_name_server_by_dcommai(ns_attributes, entry_name):
                    online_device = online_device + 1
            else:
                if online_in_name_server_by_alias(current_defined,
                                                  ns_attributes, entry_name):
                    online_device = online_device + 1

        if online_device == 0:
            hanging_zones.append(zone["zone-name"])
        else:
            online_zones.append(zone["zone-name"])

    return hanging_zones, online_zones, current_effective.peek_checksum()


def usage():
    print("  Script specific options:")
    print("")
    print("")


def main(argv):
    valid_options = []
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

    hanging_zones, online_zones, checksum = process_all_zones(session)

    if hanging_zones:
        print(" ")
        print("hanging zone(s):")
        for zone in hanging_zones:
            print(zone)
    else:
        print(" ")
        print("no hanging zones")

    if online_zones:
        print(" ")
        print("zone(s) with at least one online device or special zones:")
        for zone in online_zones:
            print(zone)
    else:
        print(" ")
        print("no zones with at least one online device or special zones")

    if len(hanging_zones) != 0:
        print("")
        user_input = input("Delete all hanging zones? (YES in all caps or "
                           "anything else to skip) ")
        if user_input == "YES":
            print("Deleting hanging zones")
            new_defined = pyfos_zone.defined_configuration()
            delete_zones = []
            for zone in hanging_zones:
                delete_zones.append({"zone-name": zone})

            new_defined.set_zone(delete_zones)
            result = new_defined.delete(session)
            if pyfos_util.is_failed_resp(result):
                print("Failed to delete. \n\nAborting transaction", result)
                new_effective = pyfos_zone.effective_configuration()
                new_effective.set_cfg_action(pyfos_zone.CFG_ACTION_ABORT)
                result = new_effective.patch(session)
                if pyfos_util.is_failed_resp(result):
                    print("Failed to abort", result)
                else:
                    print("Aborted")
            else:
                print("Deleted hanging zones")
                print("CFG Save")
                new_effective = pyfos_zone.effective_configuration()
                new_effective.set_cfg_action(pyfos_zone.CFG_ACTION_SAVE)
                new_effective.set_checksum(checksum)
                result = new_effective.patch(session)
                if pyfos_util.is_failed_resp(result):
                    print("Failed to CFG Save. \n\nAborting transaction",
                          result)
                    new_effective = pyfos_zone.effective_configuration()
                    new_effective.set_cfg_action(pyfos_zone.CFG_ACTION_ABORT)
                    result = new_effective.patch(session)
                    if pyfos_util.is_failed_resp(result):
                        print("Failed to abort", result)
                    else:
                        print("Aborted")
                else:
                    print("CFG Save success")

        else:
            print("No changes to Zone DB")

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
