#!/usr/bin/env python3

# Copyright © 2018 Broadcom. All rights reserved. The term "Broadcom"
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

:mod:`zone_allow_pair` - PyFOS util for specific Zoning use case.
***********************************************************************************
The :mod:`zone_allow_pair` provides for a specific Zoning use case.

This module is a stand-alone script and API that can be used to create a Zone
between a pair of hosts/targets without having to go through the Zone DB
management of creating Zones, adding to CFG, enabling CFG, etc. The script
creates a new zone using a host and target name along with a
prefix, adds port WWNs to the newly created Zone, adds to the current CFG or
creates a new CFG to add to the newly created Zone, and enables the CFG.

* Inputs:
    * -L=<login>: Login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: IP address.
    * --hostname=<hostname>: String name of the host or host port.
    * --hostport=<WWN>: PWWN of the host.
    * --targetname=<targetname>: String name of the target or target port.
    * --targetport=<WWN>: PWWN of the target.
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
       a VFID of 128 is assumed.

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
ZONE_PREFIX = "az_tupl_"
CFG_NAME = "az__cfg"

# no updates to the db
RET_ZONE_EXIST_IN_CFG = -2
RET_ERR = -1
# updates to the db
RET_ZONE_CREATED_ADDED_TO_NEW_CFG = 1
RET_ZONE_EXIST_ADDED_TO_NEW_CFG = 3
RET_ZONE_CREATED_ADDED_TO_CFG = 4
RET_ZONE_EXIST_ADDED_TO_CFG = 6
RET_ZONE_CREATED_IN_CFG = 8


def usage():
    print("  Script specific options:")
    print("")
    print("    --hostname=HOSTNAME          name of host")
    print("    --hostport=HOSTPORT          WWN of host port")
    print("    --targetname=TARGETNAME      name of target")
    print("    --targetport=TARGETPORT      WWN of target port")
    print("")


def zonename_get(prefix, hostname, targetname):
    return prefix + hostname + "_" + targetname


# pylint: disable=R1710
def zone_allow_pair(session, prefix, hostname, hostport,
                    targetname, targetport, if_no_cfg, checkmode):
    """Create/add a pair of hosts and targets to a tuple Zone.

    Example usage of the method to create a new tuple zone with a pair::

        ret_code, result = zone_allow_pair.zone_allow_pair(
            session, "az__pz__", "myhost", "11:22:33:44:55:66:77:88",
            "mytarget", "88:77:66:55:44:33:22:11", "cfg_if_there_is_non", True)
        if ret_code > 0:
            print ("zone db changed", result)
        else:
            print ("zone db didn't change", result)

    :param session: session returned by login.
    :param prefix: prefix for the peer Zone name.
    :param hostname: string name of the host.
    :param hostport: WWN of the host port.
    :param targetname: string name of the target.
    :param targetport: WWN of the target port.
    :param if_no_cfg: CFG name to be used if there is no enabled CFG.
    :param checkmode: indicates if Zone DB is to be updated or
        return status only.
    :rtype: Return code and dictionary of status description.

    *Use cases*

        1. Pass in host/target pair to create tuple zone.
        2. Pass in host/target pair to create tuple zone.

    """
    # pylint: disable=R1710
    cfgname = if_no_cfg
    zonename = zonename_get(prefix, hostname, targetname)
    cfgmem = [zonename]
    zonemem = [hostport, targetport]

    prezonedb = pyfos_zone.effective_configuration.get(session)
    if pyfos_util.is_failed_resp(prezonedb):
        return (RET_ERR, {"return_str": None,
                          "line": inspect.currentframe().f_lineno,
                          "error": prezonedb})

    # check to see if we have an enabled cfg
    if prezonedb.peek_cfg_name() is None:
        if checkmode is False:
            zones = [
                     {
                         "zone-name": zonename,
                         "member-entry": {"entry-name": zonemem}
                     }
                    ]
            new_defined = pyfos_zone.defined_configuration()
            new_defined.set_zone(zones)
            result = new_defined.post(session)
            if pyfos_util.is_failed_resp(result):
                return (RET_ERR, {"return_str": None,
                                  "line": inspect.currentframe().f_lineno,
                                  "error": result})

            cfgs = [
                    {
                        "cfg-name": cfgname,
                        "member-zone": {"zone-name": cfgmem}
                    }
                   ]
            new_defined = pyfos_zone.defined_configuration()
            new_defined.set_cfg(cfgs)
            result = new_defined.post(session)
            if pyfos_util.is_failed_resp(result):
                return (RET_ERR, {"return_str": None,
                                  "line": inspect.currentframe().f_lineno,
                                  "error": result})

            new_effective = pyfos_zone.effective_configuration()
            new_effective.set_cfg_name(cfgname)
            checksum = prezonedb.peek_checksum()
            new_effective.set_checksum(checksum)
            result = new_effective.patch(session)
            if pyfos_util.is_failed_resp(result):
                return (RET_ERR, {"return_str": None,
                                  "line": inspect.currentframe().f_lineno,
                                  "error": result})

            return (RET_ZONE_CREATED_ADDED_TO_NEW_CFG,
                    {"return_str": zonename +
                     " created and added to new cfg of " + cfgname,
                     "line": None,
                     "error": None})
    else:
        # we have something that is already enabled
        found_in_effective_zone = False
        found_in_zone = None
        found_in_cfg = None
        for zone in prezonedb.peek_enabled_zone():
            found_host = False
            found_target = False
            for mem in zone["member-entry"]["entry-name"]:
                if mem == hostport:
                    found_host = True
                elif mem == targetport:
                    found_target = True
            if found_host and found_target:
                found_in_effective_zone = True
                found_in_zone = zone
                found_in_cfg = prezonedb.peek_cfg_name()
                break

        if found_in_effective_zone is True:
            return (RET_ZONE_EXIST_IN_CFG,
                    {"return_str": "already zoned in " +
                     found_in_zone["zone-name"] +
                     " and effective in " + found_in_cfg,
                     "line": None,
                     "error": None})
        else:
            if checkmode is False:
                zones = [
                         {
                             "zone-name": zonename,
                             "member-entry": {"entry-name": zonemem}
                         }
                        ]
                new_defined = pyfos_zone.defined_configuration()
                new_defined.set_zone(zones)
                result = new_defined.post(session)
                if pyfos_util.is_failed_resp(result):
                    return (RET_ERR, {"line": inspect.currentframe().f_lineno,
                                      "error": result})

                cfgs = [
                        {
                            "cfg-name": prezonedb.peek_cfg_name(),
                            "member-zone": {"zone-name": [zonename]}
                        }
                       ]
                new_defined = pyfos_zone.defined_configuration()
                new_defined.set_cfg(cfgs)
                result = new_defined.post(session)
                if pyfos_util.is_failed_resp(result):
                    return (RET_ERR, {"return_str": None,
                                      "line": inspect.currentframe().f_lineno,
                                      "error": result})

                new_effective = pyfos_zone.effective_configuration()
                new_effective.set_cfg_name(prezonedb.peek_cfg_name())
                checksum = prezonedb.peek_checksum()
                new_effective.set_checksum(checksum)
                result = new_effective.patch(session)
                if pyfos_util.is_failed_resp(result):
                    return (RET_ERR, {"return_str": None,
                                      "line": inspect.currentframe().f_lineno,
                                      "error": result})

                return (RET_ZONE_CREATED_ADDED_TO_CFG,
                        {"return_str": zonename +
                         " created and added to existing cfg of " +
                         prezonedb.peek_cfg_name(),
                         "line": None,
                         "error": None})


def main(argv):
    # pylint: disable=W0603
    global g_session

    valid_options = ["hostname", "hostport", "targetname", "targetport"]
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

    if "hostname" not in inputs:
        print("--hostname is mandatory")
        brcd_util.full_usage(usage, valid_options)
        sys.exit()

    if "hostport" not in inputs:
        print("--hostport is mandatory")
        brcd_util.full_usage(usage, valid_options)
        sys.exit()

    if "targetname" not in inputs:
        print("--targetname is mandatory")
        brcd_util.full_usage(usage, valid_options)
        sys.exit()

    if "targetport" not in inputs:
        print("--targetport is mandatory")
        brcd_util.full_usage(usage, valid_options)
        sys.exit()

    ret_code, details = zone_allow_pair(
            g_session, ZONE_PREFIX, inputs["hostname"], inputs["hostport"],
            inputs["targetname"], inputs["targetport"], CFG_NAME, False)

    if ret_code > 0:
        print("zone db updated")
    else:
        print("zone db remains")

    print(details)

    pyfos_auth.logout(g_session)


if __name__ == "__main__":
    main(sys.argv[1:])
