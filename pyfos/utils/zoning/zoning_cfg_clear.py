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

:mod:`zoning_cfg_clear` - PyFOS util for specific Zoning use case.
***********************************************************************************
The :mod:`zoning_cfg_clear` provides for a specific Zoning use case.

This module is a stand-alone script and API that can be used to clear a Zone DB.

* Inputs:
    * -L=<login>: Login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: IP address.
    * --name=<cfg name>: string name of an existing cfg.
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        a VFID of 128 is assumed.

* Outputs:
    * Python dictionary content with RESTCONF response data.

.. note::
    Internally, the script runs cfgsave after cfgclear.
    Therefore, zoning_cfg_disable.py should normally be executed
    before zoning_cfg_clear.py to avoid unexpected errors.

"""

import sys
from pyfos import pyfos_auth
import pyfos.pyfos_brocade_zone as pyfos_zone
from pyfos import pyfos_util
from pyfos.utils import brcd_util
import pyfos.utils.zoning.zoning_cfg_save as cfgsave
import pyfos.utils.zoning.zoning_cfg_abort as cfgabort


def cfgclear(session):
    """Clear Zone DB

    Example usage of the method::

        result = cfgcleare(session)

    :param session: session returned by login.
    :rtype: dictionary of return status matching rest response.

    *Use cases*

        Clear Zone DB.

    """

    new_effective = pyfos_zone.effective_configuration()
    new_effective.set_cfg_action(pyfos_zone.CFG_ACTION_CLEAR)
    result = new_effective.patch(session)
    return result


def usage():
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
        brcd_util.full_usage(usage, valid_options)
        sys.exit()

    brcd_util.exit_register(session)

    vfid = None
    if 'vfid' in inputs:
        vfid = inputs['vfid']

    if vfid is not None:
        pyfos_auth.vfid_set(session, vfid)

    current_effective = pyfos_zone.effective_configuration.get(session)

    result = cfgclear(session)
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
