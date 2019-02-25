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

:mod:`zoning_def_zone` - PyFOS util for specific Zoning use case.
***********************************************************************************
The :mod:`zoning_def_zone` provides for specific Zoning use case.

This module is a standalone script and API that can be used to set
Default Zone mode.

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * --allaccess=<1 or 0>: All access mode enabled or not
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
import pyfos.utils.zoning.zoning_cfg_save as cfgsave
import pyfos.utils.zoning.zoning_cfg_abort as cfgabort


def defzone(session, allaccess):
    """Set Default Zone mode to all access or not

    Example usage of the method::

        result = defzone(session, True)

    :param session: session returned by login
    :param allaccess: boolean to indicate all access enabled or not
    :rtype: dictionary of return status matching rest response

    *use cases*

        1. enable all access
        2. disable all access

    """

    new_effective = pyfos_zone.effective_configuration()
    new_effective.set_default_zone_access(allaccess)
    result = new_effective.patch(session)
    return result


def usage():
    print("  Script specific options:")
    print("")
    print("    --allaccess=MODE             1 or 0")
    print("")


def main(argv):
    valid_options = ["allaccess"]
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

    if "allaccess" not in inputs:
        pyfos_auth.logout(session)
        usage()
        sys.exit()
    allaccess = inputs["allaccess"]

    current_effective = pyfos_zone.effective_configuration.get(session)

    result = defzone(session, allaccess)

    if pyfos_util.is_failed_resp(result):
        pyfos_util.response_print(result)
    else:
        pyfos_util.response_print(result)
        result = cfgsave.cfgsave(session, current_effective.peek_checksum())
        pyfos_util.response_print(result)
        if pyfos_util.is_failed_resp(result):
            print("failed. \n\nAborting transaction.")
            result = cfgabort.cfgabort(session)
            pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
