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


# auth_token_delete.py(pyGen v1.0.0)


"""

:mod:`auth_token_delete` - PyFOS util to Delete an AuthToken with Manager.
*******************************************************************************
The :mod:`auth_token_delete` PyFOS util to Delete an AuthToken with Manager.


AuthToken Delete from a FOS switch using REST operations.

auth_token_delete : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --config=CONFIG The Configuration for Auth Token Manager to be used.

* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: auth_token_delete.delete_auth_token_manager(session, config,\
delete_auth_token)

    *Modify auth_token_manager*

        Example Usage of the Method::

            ret = auth_token_delete.delete_auth_token_manager(session, config,\
            delete_auth_token)
            print (ret)

        Details::

            auth_token_managerObj =\
            brcd_util.pseudodictrestobject("auth-token-manager")
            auth_token_managerObj.set_config(config)
            ret = _delete_auth_token_manager(session, auth_token_managerObj)
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
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_auth_token import auth_token_manager, auth_token
from pyfos.utils import brcd_util
# End module imports


def _delete_auth_token_manager(session, auth_token_managerObj):
    mytokenmanager = auth_token_manager(auth_token_managerObj.peek_config())
    myauthtoken = mytokenmanager.getToken(session)
    if myauthtoken is None:
        myauthtoken = auth_token(session)
    ret = myauthtoken.delete(session)
    if ret["http-resp-code"] == 204 or ret["http-resp-code"] == 400 and\
       ret["client-errors"]["errors"]["error"]["error-message"] ==\
       "Auth token not present":
        mytokenmanager.removeToken(myauthtoken)
    return ret


def delete_auth_token_manager(session, config=None):
    auth_token_managerObj = \
                          brcd_util.pseudodictrestobject("auth-token-manager")
    auth_token_managerObj.set_config(config)
    return _delete_auth_token_manager(session, auth_token_managerObj)


def validate(auth_token_managerObj):
    if auth_token_managerObj.peek_config() is None:
        return 0
    return 0


def main(argv):
    filters = ["config"]
    inputs = brcd_util.parse(argv, "auth-token-manager", filters, validate)
    session = brcd_util.getsession(inputs)
    result = _delete_auth_token_manager(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
