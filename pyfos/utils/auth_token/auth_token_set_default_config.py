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


# auth_token_set_default_config.py(pyGen v1.0.0)


"""

:mod:`auth_token_set_default_config` - PyFOS util to set the default token\
 store for AuthTokenManager to the user specified one.
******************************************************************************\
*******************************************************************************
The :mod:`auth_token_set_default_config` PyFOS util to set the default token\
 store for AuthTokenManager to the user specified one.


AuthTokenManager operation to set the default token store to custom user one.

auth_token_set_default_config : usage

* Infrastructure Options:
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --config=CONFIG The Configuration for Auth Token Manager to be used.

* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: auth_token_set_default_config.setdefault_auth_token_manager(\
config)

    *Modify auth_token_manager*

        Example Usage of the Method::

            ret =\
            auth_token_set_default_config.setdefault_auth_token_manager(\
            config)
            print (ret)

        Details::

            auth_token_managerObj =\
            brcd_util.pseudodictrestobject("auth-token-manager")
            auth_token_managerObj.set_config(config)
            ret = _setdefault_auth_token_manager(auth_token_managerObj)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param config: The Configuration for Auth Token Manager to be\
              used.

        * Output:

            :rtype: Dictionary of response

"""


# Start utils imports
import sys
from pyfos import pyfos_util
from pyfos.pyfos_auth_token import auth_token_manager
from pyfos.utils import brcd_util
# End module imports


def _setdefault_auth_token_manager(auth_token_managerObj):
    tokenmanager = auth_token_manager(auth_token_managerObj.peek_config())
    return tokenmanager.setUserStoreAsDefaultStore()


def setdefault_auth_token_manager(config):
    auth_token_managerObj = \
                          brcd_util.pseudodictrestobject("auth-token-manager")
    auth_token_managerObj.set_config(config)
    return _setdefault_auth_token_manager(auth_token_managerObj)


def validate(auth_token_managerObj):
    if auth_token_managerObj.peek_config() is None:
        return 1
    return 0


def main(argv):
    filters = ["config", "ignoreMandatory"]
    inputs = brcd_util.parse(argv, "auth-token-manager", filters, validate)
    result = _setdefault_auth_token_manager(inputs['utilobject'])
    pyfos_util.response_print(result)


if __name__ == "__main__":
    main(sys.argv[1:])
