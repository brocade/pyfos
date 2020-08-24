#!/usr/bin/env python3

# Copyright © 2018-2019 Broadcom. All rights reserved. The term "Broadcom"
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

"""

:mod:`zone_allow_pair_to_peer` - PyFOS util for specific Zoning use case.
***********************************************************************************
The :mod:`zone_allow_pair_to_peer` provides for a specific Zoning use case.

This module is a stand-alone script and API that can be used to create a
Peer Zone between a pair of hosts/targets without having to go through a
Zone DB management of creating Zones, adding to CFG, enabling CFG, etc.
The script creates a new Peer Zone a using target name along with a
prefix, adds port WWNs to the newly created zone, adds to the current CFG or
creates a new CFG to add the newly created Zone, and enable the CFG. If a Peer
Zoning with the target name already exists, the new target is simply added.

* Inputs:
    * -L=<login>: Login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: IP address.
    * --hostport=<WWN>: PWWN of the host.
    * --targetname=<hostname>: String name of the target or target port.
    * --targetport=<WWN>: PWWN of the target.
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
       a  VFID of 128 is assumed.

* Outputs:
    * Indicates if Zone DB has been changed or not due to the execution.
    * Python dictionary content with detailed string descriptions.

"""

import inspect
import sys
from pyfos import pyfos_auth
import pyfos.pyfos_brocade_zone as pyfos_zone
from pyfos import pyfos_util
from pyfos.utils import brcd_util


g_session = None
ZONE_PREFIX = "az__pz__"
CFG_NAME = "az__cfg"

# no updates to the db
RET_ZONE_EXIST_IN_CFG = -2
RET_ERR = -1
# updates to the db
RET_ZONE_CREATED_ADDED_TO_NEW_CFG = 1
RET_ZONE_UPDATED_ADDED_TO_NEW_CFG = 2
RET_ZONE_EXIST_ADDED_TO_NEW_CFG = 3
RET_ZONE_CREATED_ADDED_TO_CFG = 4
RET_ZONE_UPDATED_ADDED_TO_CFG = 5
RET_ZONE_EXIST_ADDED_TO_CFG = 6
RET_ZONE_UPDATED_IN_CFG = 7
RET_ZONE_CREATED_IN_CFG = 8


def usage():
    print("  Script specific options:")
    print("")
    print("    --hostport=HOSTPORT          WWN of host port")
    print("    --targetname=TARGETNAME      name of target")
    print("    --targetport=TARGETPORT      WWN of target port")
    print("")


def find_matching_zone(prezone_defined, zonename, hostport, targetport):
    found_matching_zone = False
    found_matching_zone_with_target = False
    found_matching_zone_with_host = False
    for zone in prezone_defined.peek_zone():
        if zonename == zone["zone-name"]:
            found_matching_zone = True

            for mem in zone["member-entry"]["principal-entry-name"]:
                if mem == targetport:
                    found_matching_zone_with_target = True
                    for mem2 in zone["member-entry"]["entry-name"]:
                        if mem2 == hostport:
                            found_matching_zone_with_host = True
                            break
                    break

            break

    return (found_matching_zone, found_matching_zone_with_target,
            found_matching_zone_with_host)


def find_matching_cfg(prezone_defined, cfgname, zonename):
    found_matching_cfg = False
    found_matching_cfg_with_zone = False
    for cfg in prezone_defined.peek_cfg():
        if cfgname == cfg["cfg-name"]:
            found_matching_cfg = True

            for mem in cfg["member-zone"]["zone-name"]:
                if mem == zonename:
                    found_matching_cfg_with_zone = True
                    break

    return found_matching_cfg, found_matching_cfg_with_zone


def zone_allow_pair_to_peer(session, prefix, hostport,
                            targetname, targetport, if_no_cfg, checkmode):
    """Create/add a pair of hosts and targets to a peer Zone.

    Example usage of the method to create a new peer zone with a pair::

        ret_code, result = zone_allow_pair_to_peer.zone_allow_pair_to_peer(
            session, "az__pz__", "11:22:33:44:55:66:77:88",
            "mytarget", "88:77:66:55:44:33:22:11", "cfg_if_there_is_non", True)
        if ret_code > 0:
            print ("zone db changed", ret_code, result)
        else:
            print ("zone db didn't change", ret_code, result)

    :param session: session returned by login.
    :param prefix: prefix for the peer Zone name.
    :param hostport: WWN of the host port.
    :param targetname: string name of the target.
    :param targetport: WWN of the target port.
    :param if_no_cfg: CFG name to be used if there are no enabled CFG.
    :param checkmode: indicate if Zone DB is to be updated or
        return status only.
    :rtype: Return code and dictionary of status description.

    *Use cases*

        1. Pass in host/target pair to create peer zone.
        2. Pass in host/target pair to create peer zone.

    """

    cfgname = if_no_cfg
    zonename = prefix + targetname

    prezone_defined = pyfos_zone.defined_configuration.get(session)
    if pyfos_util.is_failed_resp(prezone_defined):
        return (RET_ERR, {"line": inspect.currentframe().f_lineno,
                          "error": prezone_defined})

    prezone_effective = pyfos_zone.effective_configuration.get(session)
    if pyfos_util.is_failed_resp(prezone_effective):
        return (RET_ERR, {"line": inspect.currentframe().f_lineno,
                          "error": prezone_effective})

    # check to see if we have a cfg for the zone already
    found_matching_cfg, found_matching_cfg_with_zone = find_matching_cfg(
            prezone_defined, cfgname, zonename)

    # check to see if we have a peer zone for the target already
    (found_matching_zone, found_matching_zone_with_target,
     found_matching_zone_with_host) = find_matching_zone(
                    prezone_defined, zonename, hostport, targetport)

    # if didn't find the matching zone with the name, let's create one
    ZONE_EXISTED = 0
    ZONE_CREATED = 1
    ZONE_MODIFIED = 2
    zone_action = ZONE_EXISTED
    if not found_matching_zone:
        if checkmode is False:
            zones = [
                     {
                        "zone-name": zonename,
                        "zone-type": pyfos_zone.ZONE_TYPE_PEER,
                        "zone-type-string": pyfos_zone.ZONE_TYPE_STRING_PEER,
                        "member-entry": {
                                         "principal-entry-name": [targetport],
                                         "entry-name": [hostport]
                                        }
                     }
                    ]
            new_defined = pyfos_zone.defined_configuration()
            new_defined.set_zone(zones)
            result = new_defined.post(session)
            if pyfos_util.is_failed_resp(result):
                return (RET_ERR, {"line": inspect.currentframe().f_lineno,
                                  "error": result})

            zone_action = ZONE_CREATED
    else:
        # I found zone. but it has unknown WWN for the principal target
        if not found_matching_zone_with_target:
            return (RET_ERR,
                    {"line": inspect.currentframe().f_lineno,
                     "error": "found expected zone but unexpected target WWN"})
        else:
            # I found the zone & the target but the host is missing
            # let's add to it
            if not found_matching_zone_with_host:
                if checkmode is False:
                    zones = [
                        {
                          "zone-name": zonename,
                          "zone-type": pyfos_zone.ZONE_TYPE_PEER,
                          "zone-type-string": pyfos_zone.ZONE_TYPE_STRING_PEER,
                          "member-entry": {"entry-name": [hostport]}
                        }
                            ]
                    new_defined = pyfos_zone.defined_configuration()
                    new_defined.set_zone(zones)
                    result = new_defined.post(session)
                    if pyfos_util.is_failed_resp(result):
                        return (RET_ERR,
                                {"line": inspect.currentframe().f_lineno,
                                 "error": result})

                    zone_action = ZONE_MODIFIED

    # check to see if we have an enabled cfg
    # if nothing is enabled, just create a new cfg and add the
    # zone
    if prezone_effective.peek_cfg_name() is None:
        if checkmode is False:
            if (found_matching_cfg is False or
                    found_matching_cfg_with_zone is False):
                # if cfg is not found or member is not found, post to create or
                # add to it.
                cfgs = [
                            {
                                "cfg-name": cfgname,
                                "member-zone": {"zone-name": [zonename]}
                            }
                       ]
                new_defined = pyfos_zone.defined_configuration()
                new_defined.set_cfg(cfgs)
                result = new_defined.post(session)
                if pyfos_util.is_failed_resp(result):
                    return (RET_ERR, {"line": inspect.currentframe().f_lineno,
                                      "error": result})

            new_effective = pyfos_zone.effective_configuration()
            new_effective.set_cfg_name(cfgname)
            new_effective.set_checksum(prezone_effective.peek_checksum())
            result = new_effective.patch(session)
            if pyfos_util.is_failed_resp(result):
                return (RET_ERR, {"line": inspect.currentframe().f_lineno,
                                  "error": result})

        if zone_action is ZONE_CREATED:
            return (RET_ZONE_CREATED_ADDED_TO_NEW_CFG,
                    {"return_str": zonename +
                     " created and added to new cfg of " + cfgname})
        elif zone_action is ZONE_MODIFIED:
            return (RET_ZONE_UPDATED_ADDED_TO_NEW_CFG,
                    {"return_str": "host added to " +
                     zonename + " added to new cfg of " + cfgname})
        else:
            return (RET_ZONE_EXIST_ADDED_TO_NEW_CFG,
                    {"return_str": "existing " +
                     zonename + " added to new cfg of " + cfgname})
    else:
        # we have something that is already enabled
        # let's add to the existing cfg
        found_in_cfg = False
        for cfg in prezone_defined.peek_cfg():
            if prezone_effective.peek_cfg_name() == cfg["cfg-name"]:
                for mem in cfg["member-zone"]["zone-name"]:
                    if mem == zonename:
                        found_in_cfg = True
                        break

        if found_in_cfg:
            if zone_action is ZONE_EXISTED:
                return (RET_ZONE_EXIST_IN_CFG,
                        {"return_str": "already zoned in " +
                         zonename + " and effective in " +
                         prezone_effective.peek_cfg_name()})
            elif zone_action is ZONE_MODIFIED:
                # if zone is already part of cfg but modified,
                # just enable again
                if checkmode is False:
                    new_effective = pyfos_zone.effective_configuration()
                    new_effective.set_cfg_name(
                            prezone_effective.peek_cfg_name())
                    new_effective.set_checksum(
                            prezone_effective.peek_checksum())
                    result = new_effective.patch(session)
                    if pyfos_util.is_failed_resp(result):
                        return (RET_ERR, {
                            "line": inspect.currentframe().f_lineno,
                            "error": result})

                return (RET_ZONE_UPDATED_IN_CFG,
                        {"return_str": "added to " +
                         zonename + " and effective in " +
                         prezone_effective.peek_cfg_name()})
            else:
                # we have a new zone created but already in the cfg?
                # seems like an error case. but still works nevertheless
                # just return no change
                return (RET_ZONE_CREATED_IN_CFG,
                        {"return_str": "created " + zonename +
                         " and already effective in " +
                         prezone_effective.peek_cfg_name()})
        else:
            # not found in cfg. add to the existing cfg and enable
            if checkmode is False:
                cfgs = [
                       {
                            "cfg-name": prezone_effective.peek_cfg_name(),
                            "member-zone": {"zone-name": [zonename]}
                       }
                       ]
                new_defined = pyfos_zone.defined_configuration()
                new_defined.set_cfg(cfgs)
                result = new_defined.post(session)
                if pyfos_util.is_failed_resp(result):
                    return (RET_ERR, {"line": inspect.currentframe().f_lineno,
                                      "error": result})

                new_effective = pyfos_zone.effective_configuration()
                new_effective.set_cfg_name(prezone_effective.peek_cfg_name())
                new_effective.set_checksum(prezone_effective.peek_checksum())
                result = new_effective.patch(session)
                if pyfos_util.is_failed_resp(result):
                    return (RET_ERR, {"line": inspect.currentframe().f_lineno,
                                      "error": result})

            if zone_action is ZONE_CREATED:
                return (RET_ZONE_CREATED_ADDED_TO_CFG,
                        {"return_str": zonename +
                         " created and added to existing cfg of " +
                         prezone_effective.peek_cfg_name()})
            elif zone_action is ZONE_MODIFIED:
                return (RET_ZONE_UPDATED_ADDED_TO_CFG,
                        {"return_str": "added to " + zonename +
                         " and added to existing cfg of " +
                         prezone_effective.peek_cfg_name()})
            else:
                return (RET_ZONE_EXIST_ADDED_TO_CFG,
                        {"return_str": "existing " + zonename +
                         " added to existing cfg of " +
                         prezone_effective.peek_cfg_name()})


def main(argv):
    # pylint: disable=W0603
    global g_session
    valid_options = ["hostport", "targetname", "targetport"]
    inputs = brcd_util.generic_input(argv, usage, valid_options)

    g_session = pyfos_auth.login(inputs["login"], inputs["password"],
                                 inputs["ipaddr"], inputs["secured"],
                                 verbose=inputs["verbose"])
    if pyfos_auth.is_failed_login(g_session):
        print("login failed because",
              g_session.get(pyfos_auth.CREDENTIAL_KEY)
              [pyfos_auth.LOGIN_ERROR_KEY])
        brcd_util.full_usage(usage, valid_options)
        sys.exit()

    brcd_util.exit_register(g_session)

    vfid = None
    if 'vfid' in inputs:
        vfid = inputs['vfid']

    if vfid is not None:
        pyfos_auth.vfid_set(g_session, vfid)

    ret_code, details = zone_allow_pair_to_peer(
            g_session, ZONE_PREFIX, inputs["hostport"],
            inputs["targetname"], inputs["targetport"], CFG_NAME, False)

    if ret_code > 0:
        print("zone db updated", ret_code)
    else:
        print("zone db remains", ret_code)

    print(details)

    pyfos_auth.logout(g_session)


if __name__ == "__main__":
    main(sys.argv[1:])
