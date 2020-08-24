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


# auth_token_reset_default_config.py(pyGen v1.0.0)


"""

:mod:`auth_token_reset_default_config` - PyFOS util to reset default\
store for AuthTokenManager.
******************************************************************************\
*******************************************************************************
The :mod:`auth_token_reset_default_config` PyFOS util to reset default\
store for AuthTokenManager.


AuthTokenManager operation to reset the config store to default store

auth_token_reset_default_config : usage

* Infrastructure Options:
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --config=CONFIG The Configuration for Auth Token Manager to be used.

* Output:
    * Python dictionary content with RESTCONF response data.


.. function::\
auth_token_reset_default_config.reset_auth_token_manager(session, config,\
reset_default)

    *Modify auth_token_manager*

        Example Usage of the Method::

            ret =\
            auth_token_reset_default_config.reset_auth_token_manager(\
            config=None)
            print (ret)

        Details::

            auth_token_managerObj =\
            brcd_util.pseudodictrestobject("auth-token-manager")
            auth_token_managerObj.set_config(config)
            ret = _reset_auth_token_manager(auth_token_managerObj)
            print (ret)

        * Input::

            None

        * Output:

            :rtype: Dictionary of response

"""


# Start utils imports
import sys
from pyfos import pyfos_util
from pyfos.pyfos_auth_token import auth_token_manager
from pyfos.utils import brcd_util
# End module imports


def _reset_auth_token_manager(auth_token_managerObj):
    restobject = auth_token_manager(auth_token_managerObj.peek_config())
    return restobject.resetUserDefaultStore()


def reset_auth_token_manager():
    auth_token_managerObj = \
                          brcd_util.pseudodictrestobject("auth-token-manager")
    return _reset_auth_token_manager(auth_token_managerObj)


def validate(auth_token_managerObj):
    if auth_token_managerObj.peek_config() is None:
        return 0
    return 0


def main(argv):
    filters = ["ignoreMandatory"]
    inputs = brcd_util.parse(argv, "auth-token-manager", filters, validate)
    result = _reset_auth_token_manager(inputs['utilobject'])
    pyfos_util.response_print(result)


if __name__ == "__main__":
    main(sys.argv[1:])
