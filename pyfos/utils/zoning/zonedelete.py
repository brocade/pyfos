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

:mod:`zonedelete` - PyFOS util for specific Zoning use case.
***********************************************************************************
The :mod:`zonedelete` provides for specific Zoning use case.

This module is a standalone script and API that can be used to delete
existing Zone(s).

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * -n=<zonename>: string name of an existing Zone.
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.

* outputs:
    * Python dictionary content with RESTCONF response data

"""

import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_zone as pyfos_zone
import sys
import pyfos.utils.brcd_util as brcd_util
import pyfos.utils.brcd_zone_util as brcd_zone_util

isHttps = "0"


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
    print("usage:")
    print('zonedelete.py -i <ipaddr> -n <name>')


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

    brcd_zone_util.zone_name_func(session, inputs, usage, __zonedelete)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
