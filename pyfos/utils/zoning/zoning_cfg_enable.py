#!/usr/bin/env python3

# Copyright 2018 Brocade Communications Systems LLC.  All rights reserved.
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

:mod:`zoning_cfg_enable` - PyFOS util for specific Zoning use case.
***********************************************************************************
The :mod:`zoning_cfg_enable` provides for specific Zoning use case.

This module is a standalone script and API that can be used to enable
Zone DB enforcement with cfg.

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * --name=<cfg name>: string name of an existing cfg
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.

* outputs:
    * Python dictionary content with RESTCONF response data


"""

import sys
from pyfos import pyfos_auth
import pyfos.pyfos_brocade_zone as pyfos_zone
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def usage():
    print("  Script specific options:")
    print("")
    print("    --name=NAME                  name of cfg")
    print("")


def cfgenable(session, cfgname, checksum):
    """Start enforcing Zone DB with cfg specified

    Example usage of the method::

        result = cfgenable(session, cfgname, checksum)

    :param session: session returned by login
    :param cfgname: name of the cfg to be enabled
    :param checksum: database checksum from effective configuration
    :rtype: dictionary of return status matching rest response

    *use cases*

        1. enable cfg

    """

    new_effective = pyfos_zone.effective_configuration()
    new_effective.set_cfg_name(cfgname)
    new_effective.set_checksum(checksum)
    result = new_effective.patch(session)
    return result


def main(argv):
    valid_options = ["name"]
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

    if "name" not in inputs:
        pyfos_auth.logout(session)
        brcd_util.full_usage(usage, valid_options)
        sys.exit()
    name = inputs["name"]

    current_effective = pyfos_zone.effective_configuration.get(session)
    result = cfgenable(session, name, current_effective.peek_checksum())
    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
