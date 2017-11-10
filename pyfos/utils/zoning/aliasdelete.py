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

:mod:`aliasdelete` - PyFOS util for alias delete use case
***********************************************************************************
The :mod:`aliasdelete` supports alias delete use case

This module is a standalone script and API that can be used to delete
existing alias(es).

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * -n=<alias name>: string name of an existing alias
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.

* outputs:
    * Python dictionary content with RESTCONF response data

"""


import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_zone as pyfos_zone
import pyfos.utils.brcd_util as brcd_util
import pyfos.utils.brcd_zone_util as brcd_zone_util
import sys

isHttps = "0"


def usage():
    print("usage:")
    print('aliasdelete.py -i <ipaddr> -n <name>')


def aliasdelete(session, aliases):
    """Delete alisas(es)

    Example usage of the method::

        aliases = [
                    {
                        "alias-name": name,
                    }
                  ]
        result = aliadelete(session, aliases)

    :param session: session returned by login
    :param aliases: an array of alias to be deleted
    :rtype: dictionary of return status matching rest response

    *use cases*

        1. delete an alias

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

    brcd_zone_util.zone_name_func(session, inputs, usage, __aliasdelete)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
