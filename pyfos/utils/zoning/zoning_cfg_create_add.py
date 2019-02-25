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

:mod:`zoning_cfg_create_add` - PyFOS util for specific Zoning use case.
***********************************************************************************
The :mod:`zoning_cfg_create_add` provides for a specific Zoning use case.

This module is a stand-alone script and API that can be used to create new
cfg(s) or add to existing cfg(s).

* Inputs:
    * -L=<login>: Login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: IP address.
    * --name=<cfg name>: string name of new cfg.
    * --members=<member list>: list of members separated by ";".
        Multiple members need to be enclosed by "".
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        a VFID of 128 is assumed.

* Outputs:
    * Python dictionary content with RESTCONF response data.

"""

import sys
from pyfos import pyfos_auth
import pyfos.pyfos_brocade_zone as pyfos_zone
from pyfos.utils import brcd_zone_util
from pyfos.utils import brcd_util


def usage():
    print("  Script specific options:")
    print("")
    print("    --name=NAME                  name of cfg")
    print("    --members=MEMBERS            ; separated list of cfg members")
    print("                                 multiple members enclosed by \"\"")
    print("")


def cfgcreate(session, cfgs):
    """Create new cfg(s) with member(s).

    Example usage of the method::

        cfgs = [
                    {
                        "cfg-name": name,
                        "member-zone": {"zone-name": members}
                    }
                  ]
        result = cfgcreate(session, cfgs)

    :param session: session returned by login
    :param cfgs: an array of cfg and members
    :rtype: dictionary of return status matching rest response

    *Use cases*

        1. Create new CFG(s) with provided member(s).
        2. Add new member(s) to existing CFG(s).

    """

    new_defined = pyfos_zone.defined_configuration()
    new_defined.set_cfg(cfgs)
    result = new_defined.post(session)
    return result


def __cfgcreate(session, name, members):
    cfgs = [
            {"cfg-name": name, "member-zone": {"zone-name": members}}
           ]
    return cfgcreate(session, cfgs)


def main(argv):
    valid_options = ["name", "members"]
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

    brcd_zone_util.zone_name_members_func(session, inputs, usage, __cfgcreate)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
