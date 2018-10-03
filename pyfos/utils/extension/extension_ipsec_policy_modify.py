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

:mod:`extension_ipsec_policy_modify` - PyFOS util for modifying IPsec policy.
***********************************************************************************
The :mod:`extension_ipsec_policy_modify` Util is used to modify IPsec Policy.

This module is a stand-alone script that can be used to modify an extension
IPsec policy.

extension_ipsec_policy_modify: Usage

* Infrastructure options:
    * -i,--ipaddr=IPADDR: IP address of the FOS switch.
    * -L,--login=LOGIN: Login name.
    * -P,--password=PASSWORD: Password.
    * -f,--vfid=VFID: VFID to which the request is directed.
    * -s,--secured=MODE: HTTPS mode "self" or "CA".
    * -v,--verbose: Verbose mode.

* Script specific options:
    *    --profile-name: Set profile-name.
    *    --restart-ike-sessions: Set restart-ike-sessions.
    *    --policy-name: Set policy-name.
    *    --authentication-data: Set authentication-data.

* Outputs:
    * Python dictionary content with RESTCONF response data.

.. function:: extension_ipsec_policy_modify.modify_extension_ipsec_policy(\
session, name, profile, auth)

    *Create extension ipsec policy*

        Example usage of the method::

          ret =
          extension_ipsec_policy_modify.modify_extension_ipsec_policy(session,
          name, profile, auth, restart_ike)
          print (ret)

        Details::

          "extension-ipsec-policy": {
              "authentication-data": "1111111111111111111111111111",
              "policy-name": "mynewipsecpolicy",
              "profile-name": "preshared",
              "restart_ike-sessions": restart_ike
          }
          result =
          extension_ipsec_policy_modify._modify_extension_ipsec_policy(session,
          restobject)

        * Inputs:
            :param session: Session returned by login.
            :param name: IPsec policy name.
            :param profile: IPsec profile name.
            :param auth: Authentication data.
            :param restart_ike: Need to restart the ike sessions.

        * Outputs:
            :rtype: Dictionary of return status matching rest response.

        *Use cases*

         Create a new ipsec policy.

"""


import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_extension_ipsec_policy import extension_ipsec_policy
import sys
import pyfos.utils.brcd_util as brcd_util

isHttps = "0"


def _modify_extension_ipsec_policy(session, ipsecobj):
    result = ipsecobj.patch(session)
    return result


def modify_extension_ipsec_policy(session, name, profile, auth,
                                  restart_ike=None):
    value_dict = {'name': name, 'profile-name': profile,
                  'authentication-data': auth,
                  'restart-ike-sessions': restart_ike}
    ipsecobject = extension_ipsec_policy(value_dict)
    result = _modify_extension_ipsec_policy(session, ipsecobject)
    return result


def validate(ipsecobject):
    if ipsecobject.peek_policy_name() is None or \
       ipsecobject.peek_authentication_data() is None:
            return 1
    return 0


def main(argv):
    # myinput = str("--policy-name=testipsecpolicy " +
    #               "--authentication-data=1111111111111111111111111111 " +
    #               "--profile-name=preshared -i 10.17.3.70 -L admin " +
    #               "-P password")
    # argv = myinput.split()
    filters = ["policy_name", "profile_name", "authentication_data",
               "restart_ike_sessions"]
    inputs = brcd_util.parse(argv, extension_ipsec_policy, filters, validate)
    ipsecobject = inputs['utilobject']
    session = brcd_util.getsession(inputs)
    result = _modify_extension_ipsec_policy(session, ipsecobject)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
