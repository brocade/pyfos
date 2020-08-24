#!/usr/bin/env python3


# Copyright © 2019 Broadcom. All rights reserved.
# The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries.
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


# auth_token_migrate_token.py(pyGen v1.0.0)


"""

:mod:`auth_token_migrate_token` - PyFOS util to Migrate the AuthToken's\
 from AuthTokenManager managed token stores across instances.
******************************************************************************\
*******************************************************************************
The :mod:`auth_token_migrate_token` PyFOS util to Migrate the AuthToken's\
 from AuthTokenManager managed token stores across instances.


AuthTokenManager migration of AuthTokens across differenet managed token stores

auth_token_migrate_token : usage

* Infrastructure Options:
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --config=CONFIG The Configuration for Auth Token Manager to be used.
    * --migrate-config=MIGRATE-CONFIG The Configuration for Auth Token Manager\
      to be used.
* Output:
    * Migrates the AuthToken from the migrate config store.


.. function:: auth_token_migrate_token.migrate_auth_token_manager(\
config, migrate_config)

    *Modify auth_token_manager*

        Example Usage of the Method::

            ret = auth_token_migrate_token.migrate_auth_token_manager(\
            config, migrate_config)
            print (ret)

        Details::

            auth_token_managerObj =\
            brcd_util.pseudodictrestobject("auth_token_manager")
            auth_token_managerObj.set_config(config)
            auth_token_managerObj.set_migrate_config(migrate_config)
            ret = _migrate_auth_token_manager(auth_token_managerObj)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param config: The Configuration for Auth Token Manager to be\
              used.
            :param migrate_config: The Configuration for Auth Token Manager to\
              be used.

        * Output:

            :rtype: True/False

"""


# Start utils imports
import sys
from pyfos.pyfos_auth_token import auth_token_manager
from pyfos.utils import brcd_util
# End module imports


def _migrate_auth_token_manager(auth_token_managerObj):
    ret = True
    dstauthtokenmanager = auth_token_manager(
        auth_token_managerObj.peek_config())
    srcauthtokenmanager = auth_token_manager(
        auth_token_managerObj.peek_migrate_config())
    srcauthtokenmanager.show()
    dstauthtokenmanager.show()

    ret = dstauthtokenmanager.migrate(srcauthtokenmanager)
    # srcauthtokenmanager.show()
    dstauthtokenmanager.show()
    return ret


def migrate_auth_token_manager(config=None, migrate_config=None):
    auth_token_managerObj = \
                          brcd_util.pseudodictrestobject("auth_token_manager")
    auth_token_managerObj.set_config(config)
    auth_token_managerObj.set_migrate_config(migrate_config)
    if validate(auth_token_manager):
        return False
    return _migrate_auth_token_manager(auth_token_managerObj)


def validate(auth_token_managerObj):
    if auth_token_managerObj.peek_migrate_config() is None:
        return 1
    return 0


def main(argv):
    filters = ["config", "migrate_config", "ignoreMandatory"]
    inputs = brcd_util.parse(argv, "auth-token-manager", filters, validate)
    # session = brcd_util.getsession(inputs)
    _migrate_auth_token_manager(inputs['utilobject'])


if __name__ == "__main__":
    main(sys.argv[1:])
