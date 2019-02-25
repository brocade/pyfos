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

:mod:`zoning_alias_delete` - PyFOS util for alias delete use case
***********************************************************************************
The :mod:`zoning_alias_delete` supports an alias delete use case.

This module is a standalone script and API that can be used to delete
existing alias(es).

* Inputs:
    * -L=<login>: Login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: IP address.
    * --name=<alias name>: string name of an existing alias.
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
    print("    --name=NAME                  name of alias")
    print("")


def aliasdelete(session, aliases):
    """Delete alisas(es)

    Example usage of the method::

        aliases = [
                    {
                        "alias-name": name,
                    }
                  ]
        result = aliadelete(session, aliases)

    :param session: session returned by login.
    :param aliases: an array of alias to be deleted.
    :rtype: Dictionary of return status matching rest response

    *Use cases*

        Delete an alias.

    """

    new_defined = pyfos_zone.defined_configuration()
    new_defined.set_alias(aliases)
    result = new_defined.delete(session)
    return result


def __aliasdelete(session, name):
    aliases = [
                {"alias-name": name}
              ]
    return aliasdelete(session, aliases)


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

    brcd_zone_util.zone_name_func(session, inputs, usage, __aliasdelete)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
