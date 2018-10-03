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

:mod:`extension_ipsec_policy_show` - PyFOS util for Displaying IPsec policy.
***********************************************************************************
The :mod:`extension_ipsec_policy_show` Util is used to display IPsec policy.

This module is a stand-alone script that can be used to show an extension
ipsec policy.
extension_ipsec_policy_show: Usage

* Infrastructure options :
    * -i,--ipaddr=IPADDR: IP address of FOS switch.
    * -L,--login=LOGIN: Login name.
    * -P,--password=PASSWORD: Password.
    * -f,--vfid=VFID: VFID to which the request is directed.
    * -s,--secured=MODE: HTTPS mode "self" or "CA".
    * -v,--verbose: Verbose mode.
* Script specific options:
    *    --policy-name: Set policy-name.


* Outputs:
    * Python dictionary content with RESTCONF response data.

.. function:: extensionipsecpolicyshow.show_extension_ipsec_policy(session\
, name, profile, auth)

    *show extension ipsec policy*

        Example usage of the method::

          ret =
          extensionipsecpolicyshow.show_extension_ipsec_policy(session,
          name, profile, auth)
          print (ret)

        Details::

          "extension-ipsec-policy": {
              "authentication-data": "1111111111111111111111111111",
              "policy-name": "mynewipsecpolicy",
              "profile-name": "preshared"
          }
          result =
          extensionipsecpolicyshow._show_extension_ipsec_policy(session,
          restobject)

        * Inputs:
            :param session: Session returned by login.
            :param name: Ipsec policy name.
            :param profile: Ipsec profile name.
            :param auth: Authentication data.

        * Outputs:
            :rtype: Dictionary of return status matching rest response.

        *Use cases*

         Show ipsec policy.

"""


import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_extension_ipsec_policy import extension_ipsec_policy
import sys
import pyfos.utils.brcd_util as brcd_util

isHttps = "0"


def _show_extension_ipsec_policy(session, ipsecobj):
    result = extension_ipsec_policy.get(session, ipsecobj.peek_policy_name())
    return result


def show_extension_ipsec_policy(session, name, profile, auth):
    value_dict = {'name': name, 'profile-name': profile,
                  'authentication-data': auth}
    ipsecobject = extension_ipsec_policy(value_dict)
    result = _show_extension_ipsec_policy(session, ipsecobject)
    return result


def main(argv):
    # myinput = str("--policy-name=testipsecpolicy")
    # argv = myinput.split()
    inputs = brcd_util.parse(argv, extension_ipsec_policy, ['policy_name'])
    ipsecobject = inputs['utilobject']
    session = brcd_util.getsession(inputs)
    result = _show_extension_ipsec_policy(session, ipsecobject)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
