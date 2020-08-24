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


# auth_token_manager_show.py(pyGen v1.0.0)


"""

:mod:`auth_token_manager_show` - PyFOS util to show the\
 AuthTokenManager config and token store details.
*******************************************************************************\
*******************************************************************************
The :mod:`auth_token_manager_show` PyFOS util to show the AuthTokenManager\
 config and store details.


AuthTokenManager Display the config and token store details and tokens.

auth_token_manager_show : usage

* Infrastructure Options:
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --config=CONFIG The Configuration for Auth Token Manager to be used.

* Output:
    * Displays the Config and AuthToken store

.. function:: auth_token_manager_show.show_auth_token_manager(config)

    *Show auth_token_manager*

        Example Usage of the Method::

            ret = auth_token_manager_show.show_auth_token_manager(session,\
            config)
            print (ret)

        * Input::
            :param config: The Configuration for Auth Token Manager to be\
              used.

        * Output:

            :rtype: True/False.

"""


# Start utils imports
import sys
from pyfos.pyfos_auth_token import auth_token_manager
from pyfos.utils import brcd_util
# End module imports


def _show_auth_token_manager(auth_token_managerObj):
    return auth_token_managerObj.show()


def show_auth_token_manager(config=None):
    auth_token_managerObj = auth_token_manager(config)
    return _show_auth_token_manager(auth_token_managerObj)


def validate(auth_token_managerObj):
    if auth_token_managerObj.peek_config() is None:
        return 0
    return 0


def main(argv):
    filters = ["config", "ignoreMandatory"]
    inputs = brcd_util.parse(argv, "auth-token-manager", filters, validate)
    restobject = auth_token_manager(inputs['utilobject'].peek_config())
    _show_auth_token_manager(restobject)


if __name__ == "__main__":
    main(sys.argv[1:])
