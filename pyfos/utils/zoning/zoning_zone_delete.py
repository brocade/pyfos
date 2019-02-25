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

:mod:`zoning_zone_delete` - PyFOS util for specific Zoning use case.
***********************************************************************************
The :mod:`zoning_zone_delete` provides for specific Zoning use case.

This module is a standalone script and API that can be used to delete
existing Zone(s).

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * --name=<zonename>: string name of an existing Zone.
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.

* outputs:
    * Python dictionary content with RESTCONF response data

"""

import sys
from pyfos import pyfos_auth
import pyfos.pyfos_brocade_zone as pyfos_zone
from pyfos.utils import brcd_util
from pyfos.utils import brcd_zone_util


def zonedelete(session, zones):
    """Delete an existing Zone(s)

    Example usage of the method::

        zones = [
                    {
                        "zone-name": name,
                    }
               ]
        result = zonedelete(session, zones)

    :param session: session returned by login
    :param zones: an array of zone and new members
    :rtype: dictionary of return status matching rest response

    *use cases*

        1. Delete an existing Zone(s)

    """

    new_defined = pyfos_zone.defined_configuration()
    new_defined.set_zone(zones)
    result = new_defined.delete(session)
    return result


def __zonedelete(session, name):
    zones = [
                {"zone-name": name}
            ]
    return zonedelete(session, zones)


def usage():
    print("  Script specific options:")
    print("")
    print("    --name=NAME                  name of zone")
    print("")


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

    brcd_zone_util.zone_name_func(session, inputs, usage, __zonedelete)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
