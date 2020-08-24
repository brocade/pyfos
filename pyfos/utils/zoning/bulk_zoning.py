#!/usr/bin/env python3

# Copyright © 2018-2019 Broadcom. All Rights Reserved. The term “Broadcom”
# refers to Broadcom Inc. and/or its subsidiaries.
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

# pylint: disable=W1401
"""

:mod:`bulk_zoning` - PyFOS util for bulk Zoning update use case.
***********************************************************************************
The :mod:`bulk_zoning` supports bulk Zoning update use case.

This module is a stand-alone script used to apply bulk Zoning updates
from \*.txt or \*.xlsx files based on file extension.

When using a \*.txt file, the script simply walks through the list of
commands and executes them in sequence within a single session.
A reference example txt file is under the same directory as
bulk_zoning.py (that is, pyfos/utils/zoning/bulk_zoning.txt).

When using a \*.xlsx file, the script is used to create
Zones or Peer Zones, along with Aliases. By default, Zones are created
using initiator and target Aliases as members. If Peer Zones are
preferred, the --usepeer option is used with "WWN" or an empty string.
If "WWN" is specified, Peer Zones are created with WWNs as
members. Otherwise, initiator or target Aliases are used as Zone members.
A reference example .xlsx file is under the same directory as
bulk_zoning.py (that is, pyfos/utils/zoning/bulk_zoning.xlsx).

Zone names can be auto-generated or explicitly specified.

For a given row, if the Zone name is empty or set to "auto":

    * If in defaut mode:
        The script will create an "Init/Target" Zone.
        The Zone name used is <prefix>_<initiatoralias>_<targetalias>, or
        <initiatoralias>_<targetalias> if prefix is empty.
    * If in Peer Zone mode:
        The script will create (or add to) a Peer Zone with
        one target and all the associated initiators. The name used
        is <prefix>_<targetalias>, or <targetalias> if prefix
        is empty.

If Zone name is set for a given row:

    * If in default mode:
        The script will create (or add to) a Zone with all
        the initiators and targets associated with the Zone name
    * If in Peer Zone mode:
        The script will create (or add to) a Peer Zone with
        one target and all the associated initiators. If two targets
        are configured, the script will error out.

If auto-generated Zone name and explicit Zone name are the same, the script
will consider that to be the same Zone and process as such.

* Inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address.
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.
    * --filename=<file name>: The file containing Zoning policies.
    * --xlscheck=<sheet name>: The name of the sheet to execute
        dry-run on. Any changes are identified but not applied
        to FOS. If no <sheet name> is given, the first sheet
        is processed.
    * --xlsapply=<sheet name>: The name of the sheet to apply
        Zone changes. If no <sheet name> is given, the first
        sheet is processed.
    * --usepeer="WWN" or empty: If specified, Peer Zones are
        created with the target as sole principal member with all
        associated initiators being non-principal members. Members
        can be Aliases or WWNs based on the option given.

* Outputs:
    * Status output in user readable text.

"""


import sys
import re
import xlrd
from pyfos import pyfos_auth
import pyfos.pyfos_brocade_zone as pyfos_zone
from pyfos.utils import brcd_util
import pyfos.utils.zoning.zoning_alias_create_add as aliascreate
import pyfos.utils.zoning.zoning_zone_create_add as zonecreate
import pyfos.utils.zoning.zoning_cfg_create_add as cfgcreate
import pyfos.utils.zoning.zoning_cfg_enable as cfgenable

WARN = '\x1b[1;30;41m'
CHANGED = '\x1b[1;31;42m'
END = '\x1b[0m'


def usage():
    print("  Script specific options:")
    print("")
    print("    --filename=FILENAME          name of file containing zone info")
    print("    --xlscheck=SHEET             sheet name to be checked")
    print("    --xlsapply=SHEET             sheet name to be applied")
    print("    --usepeer=MODE              \"WWN\" or empty")
    print("")


def parse_alicreate(command_line):
    command_line[1] = command_line[1].replace("\"", "")
    command_line[2] = command_line[2].replace("\"", "")
    members = command_line[2].split(";")
    print("Create Alias -", command_line[1], "with", members)
    aliases = [
                {
                    "alias-name": command_line[1],
                    "member-entry": {"alias-entry-name": members}
                }
            ]
    return aliases


def parse_zonecreate(command_line):
    peerzone_index = -1
    principal_index = -1
    members_index = -1

    for index in range(0, len(command_line)):
        if command_line[index] == "--peerzone":
            peerzone_index = index
        elif command_line[index] == "-principal":
            principal_index = index
        elif command_line[index] == "-members":
            members_index = index

    if (peerzone_index != -1 and principal_index != -1 and
            members_index != -1):
        zonename = command_line[peerzone_index + 1].replace("\"", "")
        pmembers = (
                command_line[principal_index + 1].replace("\"", "").split(";"))
        members = command_line[members_index + 1].replace("\"", "").split(";")
        print(
                "Create Zone -", zonename, "with principal", pmembers,
                "and members", members)
        zones = [
                    {
                        "zone-name": zonename,
                        "zone-type": pyfos_zone.ZONE_TYPE_PEER,
                        "zone-type-string": pyfos_zone.ZONE_TYPE_STRING_PEER,
                        "member-entry":
                            {
                                "principal-entry-name": pmembers,
                                "entry-name": members
                            }
                    }
                ]
        return zones
    else:
        command_line[1] = command_line[1].replace("\"", "")
        command_line[2] = command_line[2].replace("\"", "")
        members = command_line[2].split(";")
        print("Create Zone -", command_line[1], "with", members)
        zones = [
                    {
                        "zone-name": command_line[1],
                        "member-entry": {"entry-name": members}
                    }
                ]
        return zones


def parse_cfgadd_or_create(command_line):
    command_line[1] = command_line[1].replace("\"", "")
    command_line[2] = command_line[2].replace("\"", "")
    members = command_line[2].split(";")
    print("Create CFG -", command_line[1], "with", members)
    cfgs = [
            {
                "cfg-name": command_line[1],
                "member-zone": {"zone-name": members}
            }
           ]
    return cfgs


def process_txt(session, filename):
    current_effective = pyfos_zone.effective_configuration.get(session)

    file = open(filename, "r")
    for line in file:
        if len(line) > 0:
            # pylint: disable=W1401
            command_line = re.split('\s|\,', line)
            if command_line[0] == "alicreate":
                aliases = parse_alicreate(command_line)
                result = aliascreate.aliascreate(session, aliases)
                if 'success-code' in result and result['success-code'] == 201:
                    print("\tcreate succeeded")
                else:
                    print(result)
            elif command_line[0] == "zonecreate":
                zones = parse_zonecreate(command_line)
                result = zonecreate.zonecreate(session, zones)
                if 'success-code' in result and result['success-code'] == 201:
                    print("\tcreate succeeded")
                else:
                    print(result)
            elif command_line[0] == "cfgadd":
                cfgs = parse_cfgadd_or_create(command_line)
                result = cfgcreate.cfgcreate(session, cfgs)
                if 'success-code' in result and result['success-code'] == 201:
                    print("\tadd succeeded")
                else:
                    print(result)
            elif command_line[0] == "cfgcreate":
                cfgs = parse_cfgadd_or_create(command_line)
                result = cfgcreate.cfgcreate(session, cfgs)
                if 'success-code' in result and result['success-code'] == 201:
                    print("\tcreate succeeded")
                else:
                    print(result)
            elif command_line[0] == "cfgenable":
                command_line[1] = command_line[1].replace("\"", "")
                print("cfgenable with", command_line[1])
                result = cfgenable.cfgenable(
                        session, command_line[1],
                        current_effective.peek_checksum())
                if 'success-code' in result and result['success-code'] == 204:
                    print("\tenable succeeded")
                else:
                    print(result)


DOESNT_EXIST = 0
EXIST_SAME = 1
EXIST_DIFF_SUBSET = 2
EXIST_DIFF_NON_SUBSET = 3


def find_in_db(defined, entry_type, name, members, usepeer):
    if pyfos_zone.ALIAS == entry_type:
        for alias in defined.peek_alias():
            if alias["alias-name"] == name:
                current_members = alias["member-entry"]["alias-entry-name"]
                current_members.sort()
                members.sort()
                if current_members == members:
                    return EXIST_SAME
                else:
                    if set(members) < set(current_members):
                        return EXIST_DIFF_SUBSET
                    else:
                        return EXIST_DIFF_NON_SUBSET
        return DOESNT_EXIST
    elif pyfos_zone.ZONE == entry_type:
        for zone in defined.peek_zone():
            if zone["zone-name"] == name:
                if usepeer:
                    current_members = zone["member-entry"]["entry-name"]
                    current_members.sort()
                    current_pmembers = (
                            zone["member-entry"]["principal-entry-name"])
                    current_pmembers.sort()
                    pmembers = members[0:1]
                    pmembers.sort()
                    npmembers = members[1:]
                    npmembers.sort()
                    if (current_members == npmembers and
                            current_pmembers == pmembers):
                        return EXIST_SAME
                    else:
                        if (set(npmembers) < set(current_members) and
                                set(pmembers) < set(current_pmembers)):
                            return EXIST_DIFF_SUBSET
                        else:
                            return EXIST_DIFF_NON_SUBSET
                else:
                    current_members = zone["member-entry"]["entry-name"]
                    current_members.sort()
                    members.sort()
                    if current_members == members:
                        return EXIST_SAME
                    else:
                        if set(members) < set(current_members):
                            return EXIST_DIFF_SUBSET
                        else:
                            return EXIST_DIFF_NON_SUBSET
        return DOESNT_EXIST
    elif pyfos_zone.CFG == entry_type:
        for cfg in defined.peek_cfg():
            if cfg["cfg-name"] == name:
                current_members = cfg["member-zone"]["zone-name"]
                current_members.sort()
                members.sort()
                if current_members == members:
                    return EXIST_SAME
                else:
                    if set(members) < set(current_members):
                        return EXIST_DIFF_SUBSET
                    else:
                        return EXIST_DIFF_NON_SUBSET
        return DOESNT_EXIST

    return DOESNT_EXIST


def handle_alias_create(session, defined, name, members, apply_to_fos):
    print("Create Alias -", name, "with", members)
    status = find_in_db(defined, pyfos_zone.ALIAS, name, members, False)
    if status == EXIST_SAME:
        print("\talready exist")
        return 0
    elif status == EXIST_DIFF_SUBSET:
        print("\talready exist and members are already a subset", members)
        return 0
    elif status == EXIST_DIFF_NON_SUBSET:
        print("\texist but members are different. adding", members)
        if apply_to_fos:
            aliases = [
                        {
                            "alias-name": name,
                            "member-entry": {"alias-entry-name": members}
                        }
                      ]
            result = aliascreate.aliascreate(session, aliases)
            if 'success-code' in result and result['success-code'] == 201:
                print(CHANGED, "\tadd succeeded", END)
            else:
                print(result)
        else:
            print(CHANGED, "\tneed change", END)

        return 1
    else:
        aliases = [
                    {
                        "alias-name": name,
                        "member-entry": {"alias-entry-name": members}
                    }
                  ]
        if apply_to_fos:
            result = aliascreate.aliascreate(session, aliases)
            if 'success-code' in result and result['success-code'] == 201:
                print(CHANGED, "\tcreate succeeded", END)
            else:
                print(result)
        else:
            print(CHANGED, "\tneed change", END)

        return 1


def handle_zone_create(session, defined, name, members, usepeer, apply_to_fos):
    print("Create Zone -", name, "with", members)
    status = find_in_db(defined, pyfos_zone.ZONE, name, members, usepeer)
    if usepeer:
        zones = [
                    {
                        "zone-name": name,
                        "zone-type": pyfos_zone.ZONE_TYPE_PEER,
                        "zone-type-string": pyfos_zone.ZONE_TYPE_STRING_PEER,
                        "member-entry":
                            {
                                "principal-entry-name": members[0:1],
                                "entry-name": members[1:]
                            }
                    }
                ]
    else:
        zones = [
                    {
                        "zone-name": name,
                        "member-entry": {"entry-name": members}
                    }
                ]

    if status == EXIST_SAME:
        print("\talready exist")
        return 0
    elif status == EXIST_DIFF_SUBSET:
        print("\talready exist and members are already a subset", members)
        return 0
    elif status == EXIST_DIFF_NON_SUBSET:
        print("\texist but members are different. adding", members)
        if apply_to_fos:
            result = zonecreate.zonecreate(session, zones)
            if 'success-code' in result and result['success-code'] == 201:
                print(CHANGED, "\tadd succeeded", END)
            else:
                print(result)
        else:
            print(CHANGED, "\tneed change", END)

        return 1
    else:
        if apply_to_fos:
            result = zonecreate.zonecreate(session, zones)
            if 'success-code' in result and result['success-code'] == 201:
                print(CHANGED, "\tcreate succeeded", END)
            else:
                print(result)
        else:
            print(CHANGED, "\tneed change", END)

        return 1


def handle_cfg_create(session, defined, name, members, apply_to_fos):
    print("Create CFG -", name, "with", members)
    status = find_in_db(defined, pyfos_zone.CFG, name, members, False)
    if status == EXIST_SAME:
        print("\talready exist")
        return 0
    elif status == EXIST_DIFF_SUBSET:
        print("\talready exist and members are already a subset", members)
        return 0
    elif status == EXIST_DIFF_NON_SUBSET:
        print("\texist but members are different. adding", members)
        if apply_to_fos:
            cfgs = [
                    {
                        "cfg-name": name,
                        "member-zone": {"zone-name": members}
                    }
                   ]
            result = cfgcreate.cfgcreate(session, cfgs)
            if 'success-code' in result and result['success-code'] == 201:
                print(CHANGED, "\tadd succeeded", END)
            else:
                print(result)
        else:
            print(CHANGED, "\tneed change", END)

        return 1
    else:
        cfgs = [
                {
                    "cfg-name": name,
                    "member-zone": {"zone-name": members}
                }
               ]
        if apply_to_fos:
            result = cfgcreate.cfgcreate(session, cfgs)
            if 'success-code' in result and result['success-code'] == 201:
                print(CHANGED, "\tcreate succeeded", END)
            else:
                print(result)
        else:
            print(CHANGED, "\tneed change", END)

        return 1


def process_xlsx_direct_generic(
        session, filename, sheet_name, apply_to_fos, usepeer, usepeer_wwn):

    HOST_STR = "Initiator Alias"
    HOST_WWN_STR = "Initiator Alias WWN"
    STORAGE_STR = "Target Alias"
    STORAGE_WWN_STR = "Target Alias WWN"
    CFG_STR = "Active Zone CFG"
    ZONE_PREFIX_STR = "Zone Prefix"
    ZONE_NAME_STR = "Zone Name"

    current_effective = pyfos_zone.effective_configuration.get(session)
    current_defined = pyfos_zone.defined_configuration.get(session)

    host_index = -1
    host_wwn_index = -1
    target_index = -1
    target_wwn_index = -1
    cfg_index = -1
    zone_prefix_index = -1
    zone_name_index = -1

    print("processing file", filename)

    book = xlrd.open_workbook(filename)

    sheet_index = -1
    if sheet_name:
        for index in range(0, book.nsheets):
            if book.sheet_names()[index] == sheet_name:
                sheet_index = index

        if sheet_index == -1:
            print("unknown sheet", sheet_name)
            return
        print("processing sheet", sheet_name)
    else:
        sheet_index = 0
        print("processing the first sheet")

    sh = book.sheet_by_index(sheet_index)

    for column in range(sh.ncols):
        # print(sh.row(0)[column].value)
        if HOST_STR == sh.row(0)[column].value:
            host_index = column
        elif HOST_WWN_STR == sh.row(0)[column].value:
            host_wwn_index = column
        elif STORAGE_STR == sh.row(0)[column].value:
            target_index = column
        elif STORAGE_WWN_STR == sh.row(0)[column].value:
            target_wwn_index = column
        elif CFG_STR == sh.row(0)[column].value:
            cfg_index = column
        elif ZONE_PREFIX_STR == sh.row(0)[column].value:
            zone_prefix_index = column
        elif ZONE_NAME_STR == sh.row(0)[column].value:
            zone_name_index = column

    if host_index is -1:
        print("missing required header", HOST_STR)
        return
    elif host_wwn_index is -1:
        print("missing required header", HOST_WWN_STR)
        return
    elif target_index is -1:
        print("missing required header", STORAGE_STR)
        return
    elif target_wwn_index is -1:
        print("missing required header", STORAGE_WWN_STR)
        return
    elif cfg_index is -1:
        print("missing required header", CFG_STR)
        return
    elif zone_prefix_index is -1:
        print("missing required header", ZONE_PREFIX_STR)
        return
    elif zone_name_index is -1:
        print("missing required header", ZONE_NAME_STR)
        return

    host_alias_create = {}
    target_alias_create = {}
    zone_create = {}
    cfg_add = {}
    cfg_name = None

    for row in range(1, sh.nrows):
        host_port_name = None
        target_port_name = None
        new_zone_name = None

        if (not sh.row(row)[host_index].value or
                not sh.row(row)[host_wwn_index].value or
                not sh.row(row)[target_index].value or
                not sh.row(row)[target_wwn_index].value or
                not sh.row(row)[cfg_index].value or
                not sh.row(row)[zone_name_index].value):
            print(
                    WARN,
                    "Row number", row + 1, "is not processed"
                    " due to missing fields. All fields are required"
                    " except Zone Prefix",
                    END)
            continue

        if sh.row(row)[host_index].value:
            host_port_name = sh.row(row)[host_index].value
            if host_port_name not in host_alias_create:
                host_alias_create[host_port_name] = (
                        sh.row(row)[host_wwn_index].value)
            else:
                if (host_alias_create[host_port_name] !=
                        sh.row(row)[host_wwn_index].value):
                    print(
                            WARN, "initiator alias", host_port_name,
                            "is associated with both",
                            host_alias_create[host_port_name],
                            sh.row(row)[host_wwn_index].value, END)
                    return

        if sh.row(row)[target_index].value:
            target_port_name = sh.row(row)[target_index].value
            if target_port_name not in target_alias_create:
                target_alias_create[target_port_name] = (
                        sh.row(row)[target_wwn_index].value)
            else:
                if (target_alias_create[target_port_name] !=
                        sh.row(row)[target_wwn_index].value):
                    print(
                            WARN, "target alias", target_port_name,
                            "is associated with both",
                            target_alias_create[target_port_name],
                            sh.row(row)[target_wwn_index].value, END)
                    return

        if usepeer:
            if host_port_name and target_port_name:
                if (not sh.row(row)[zone_name_index].value or
                        sh.row(row)[zone_name_index].value == "auto"):
                    if sh.row(row)[zone_prefix_index].value:
                        new_zone_name = (
                                sh.row(row)[zone_prefix_index].value +
                                "_" + target_port_name)
                    else:
                        new_zone_name = target_port_name
                else:
                    new_zone_name = sh.row(row)[zone_name_index].value

                if new_zone_name not in zone_create:
                    members = []
                    if usepeer_wwn:
                        members.append(target_alias_create[target_port_name])
                        members.append(host_alias_create[host_port_name])
                    else:
                        members.append(target_port_name)
                        members.append(host_port_name)
                    zone_create[new_zone_name] = members
                    cfg_add[new_zone_name] = sh.row(row)[cfg_index].value
                    if (cfg_name is not None and
                            cfg_name != sh.row(row)[cfg_index].value):
                        print(
                                WARN, "two different cfgs are specified",
                                cfg_name,
                                sh.row(row)[cfg_index].value, END)
                        return
                    cfg_name = sh.row(row)[cfg_index].value
                else:
                    if usepeer_wwn:
                        if (target_alias_create[target_port_name] !=
                                zone_create[new_zone_name][0]):
                            print(
                                    WARN, "two different targets specified",
                                    target_alias_create[target_port_name],
                                    zone_create[new_zone_name][0], "for",
                                    new_zone_name, END)
                            return
                        zone_create[new_zone_name].append(
                                host_alias_create[host_port_name])
                    else:
                        if target_port_name != zone_create[new_zone_name][0]:
                            print(
                                    WARN, "two different targets specified",
                                    target_port_name,
                                    zone_create[new_zone_name][0], "for",
                                    new_zone_name, END)
                            return
                        zone_create[new_zone_name].append(host_port_name)
            else:
                print(
                        WARN, "invalid initiator", host_port_name,
                        "or invalid target name",
                        target_port_name, END)
                return
        else:
            if host_port_name and target_port_name:
                if (not sh.row(row)[zone_name_index].value or
                        sh.row(row)[zone_name_index].value == "auto"):
                    if sh.row(row)[zone_prefix_index].value:
                        new_zone_name = (
                                sh.row(row)[zone_prefix_index].value +
                                "_" + host_port_name + "_" + target_port_name)
                    else:
                        new_zone_name = host_port_name + "_" + target_port_name
                else:
                    new_zone_name = sh.row(row)[zone_name_index].value

                if new_zone_name not in zone_create:
                    members = []
                    members.append(host_port_name)
                    members.append(target_port_name)
                    zone_create[new_zone_name] = members
                    cfg_add[new_zone_name] = sh.row(row)[cfg_index].value
                    if (cfg_name is not None and
                            cfg_name != sh.row(row)[cfg_index].value):
                        print(
                                WARN, "two different cfgs are specified",
                                cfg_name,
                                sh.row(row)[cfg_index].value, END)
                        return
                    cfg_name = sh.row(row)[cfg_index].value
                else:
                    if host_port_name not in zone_create[new_zone_name]:
                        zone_create[new_zone_name].append(host_port_name)
                    if target_port_name not in zone_create[new_zone_name]:
                        zone_create[new_zone_name].append(target_port_name)
                    if (cfg_name is not None and
                            cfg_name != sh.row(row)[cfg_index].value):
                        print(
                                WARN, "two different cfgs are specified",
                                cfg_name,
                                sh.row(row)[cfg_index].value, END)
                        return
                    cfg_name = sh.row(row)[cfg_index].value
            else:
                print(
                        WARN, "invalid initiator", host_port_name,
                        "or invalid target",
                        target_port_name, END)
                return

    changed = 0
    for key, value in host_alias_create.items():
        changed += handle_alias_create(
                session, current_defined, key, [value], apply_to_fos)
    for key, value in target_alias_create.items():
        changed += handle_alias_create(
                session, current_defined, key, [value], apply_to_fos)
    for key, value in zone_create.items():
        changed += handle_zone_create(
                session, current_defined, key, value, usepeer, apply_to_fos)

    cfg_members = []
    for key, value in cfg_add.items():
        cfg_members.append(key)
    changed += handle_cfg_create(
            session, current_defined, cfg_name, cfg_members, apply_to_fos)

    if changed > 0:
        print("enable cfg", cfg_name)
        if apply_to_fos:
            result = cfgenable.cfgenable(
                session, cfg_name,
                current_effective.peek_checksum())
            if 'success-code' in result and result['success-code'] == 204:
                print(CHANGED, "\tenable succeeded", END)
            else:
                print(result)
        else:
            print(CHANGED, "\tneed change", END)
    else:
        if current_effective.peek_cfg_name() == cfg_name:
            print("Zone DB not changed. No reason to enable", cfg_name)
        else:
            print(cfg_name, "is not enabled. enabling")
            if apply_to_fos:
                result = cfgenable.cfgenable(
                    session, cfg_name,
                    current_effective.peek_checksum())
                if 'success-code' in result and result['success-code'] == 204:
                    print(CHANGED, "\tenable succeeded", END)
                else:
                    print(result)
            else:
                print(CHANGED, "\tneed change", END)


def main(argv):
    valid_options = ["filename", "usepeer", "xlscheck", "xlsapply"]
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

    if "filename" not in inputs:
        print("filename missing")
        brcd_util.full_usage(usage, valid_options)
        sys.exit()

    filename = inputs["filename"]
    if filename.endswith("txt"):
        process_txt(session, filename)
    elif filename.endswith("xlsx"):
        usepeer = False
        usepeer_wwn = False
        if "usepeer" in inputs:
            usepeer = True
            usepeer_wwn = bool(inputs["usepeer"] == "WWN")

        if "xlscheck" in inputs:
            process_xlsx_direct_generic(
                    session, filename, inputs["xlscheck"],
                    False, usepeer, usepeer_wwn)
        elif "xlsapply" in inputs:
            process_xlsx_direct_generic(
                    session, filename, inputs["xlsapply"],
                    True, usepeer, usepeer_wwn)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
