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

:mod:`zone_allow_pair` - PyFOS util for specific Zoning use case.
***********************************************************************************
The :mod:`zone_allow_pair` provides for specific Zoning use case.

This module is a standalone script and API that can be used to create a Zone
between a pair of host/target without having to go through Zone DB
management of creating Zones, adding to CFG, enabling CFG, etc. The script
will create a new zone using host and target name along with a
prefix, add port WWNs to the newly create Zone, add to the current CFG or
create a new CFG to add the newly create Zone, & enable the CFG.

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * --hostname=<hostname>: string name of the host or host port
    * --hostport=<WWN>: PWWN of the host
    * --targetname=<targetname>: string name of the target or target port
    * --targetport=<WWN>: PWWN of the target
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.

* outputs:
    * Indicate if Zone DB has been changed or not due to the execution
    * Python dictionary content with details string descriptions

"""


import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_zone as pyfos_zone
import pyfos.pyfos_util as pyfos_util
import pyfos.utils.brcd_util as brcd_util
import inspect
import sys

isHttps = "0"
session = None
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
    print("usage:")
    print('zone_allow_pair.py -i <ipaddr>'
          ' --hostname=<hostname> --hostport=<host port wwn> '
          ' --targetname=<targetname> --targetport=<target port wwn>')


def zonename_get(prefix, hostname, targetname):
    return (prefix + hostname + "_" + targetname)


def zone_allow_pair(session, prefix, hostname, hostport,
                    targetname, targetport, if_no_cfg, checkmode):
    """Create/add a pair of host and target to a tuple Zone

    Example usage of the method to create a new tuple zone with a pair::

        ret_code, result = zone_allow_pair.zone_allow_pair(
            session, "az__pz__", "myhost", "11:22:33:44:55:66:77:88",
            "mytarget", "88:77:66:55:44:33:22:11", "cfg_if_there_is_non", True)
        if ret_code > 0:
            print ("zone db changed", result)
        else:
            print ("zone db didn't change", result)

    :param session: session returned by login
    :param prefix: prefix for the peer Zone name
    :param hostname: string name of the host
    :param hostport: WWN of the host port
    :param targetname: string name of the target
    :param targetport: WWN of the target port
    :param if_no_cfg: CFG name to be used if there are no enabled CFG
    :param checkmode: indicate if Zone DB is to be updated or
        return status only
    :rtype: return code and dictionary of status description

    *use cases*

        1. pass in host/target pair to create tuple zone
        2. pass in host/target pair to create tuple zone

    """

    cfgname = if_no_cfg
    zonename = zonename_get(prefix, hostname, targetname)
    cfgmem = [zonename]
    zonemem = [hostport, targetport]

    prezonedb = pyfos_zone.effective_configuration.get(session)
    if pyfos_util.is_failed_resp(prezonedb):
        return (RET_ERR, {"line": inspect.currentframe().f_lineno,
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
                return (RET_ERR, {"line": inspect.currentframe().f_lineno,
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
                return (RET_ERR, {"line": inspect.currentframe().f_lineno,
                                  "error": result})

            new_effective = pyfos_zone.effective_configuration()
            new_effective.set_cfg_name(cfgname)
            checksum = prezonedb.peek_checksum()
            new_effective.set_checksum(checksum)
            result = new_effective.patch(session)
            if pyfos_util.is_failed_resp(result):
                return (RET_ERR, {"line": inspect.currentframe().f_lineno,
                                  "error": result})

            return (RET_ZONE_CREATED_ADDED_TO_NEW_CFG,
                    {"return_str": zonename +
                     " created and added to new cfg of " + cfgname})
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
                     " and effective in " + found_in_cfg})
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
                    return (RET_ERR, {"line": inspect.currentframe().f_lineno,
                                      "error": result})

                new_effective = pyfos_zone.effective_configuration()
                new_effective.set_cfg_name(prezonedb.peek_cfg_name())
                checksum = prezonedb.peek_checksum()
                new_effective.set_checksum(checksum)
                result = new_effective.patch(session)
                if pyfos_util.is_failed_resp(result):
                    return (RET_ERR, {"line": inspect.currentframe().f_lineno,
                                      "error": result})

                return (RET_ZONE_CREATED_ADDED_TO_CFG,
                        {"return_str": zonename +
                         " created and added to existing cfg of " +
                         prezonedb.peek_cfg_name()})


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

    ret_code, details = zone_allow_pair(
            session, ZONE_PREFIX, inputs["hostname"], inputs["hostport"],
            inputs["targetname"], inputs["targetport"], CFG_NAME, False)

    if ret_code > 0:
        print("zone db updated")
    else:
        print("zone db remains")

    print(details)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
