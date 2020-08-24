#!/usr/bin/env python3


# Copyright © 2019-2020 Broadcom. All rights reserved.
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


# extension_ipsec_policy_delete.py(pyGen v1.0.0)


"""

:mod:`extension_ipsec_policy_delete` - PyFOS util to delete for\
 extension_ipsec_policy
******************************************************************************\
*******************************************************************************
The:mod:`extension_ipsec_policy_delete` PyFOS util to delete for\
 extension_ipsec_policy


Represents IPsec policy defined on extension blade or system.

extension_ipsec_policy_delete: usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].
    * -a,--authtoken: AuthToken value or AuthTokenManager config\
    file[OPTIONAL].
    * -z,--nosession: Sessionless authentication based login[OPTIONAL].
    * --nocredential: No credential to be sent in the request[OPTIONAL].

* Util Script Options:
    * --policy-name=POLICY-NAME: Specifies  the name for the IPsec policy. The\
      IPsec policy name can be up to 31 characters long and cannot contain\
      certain special characters and keywords such as 'all' and 'none'.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: extension_ipsec_policy_delete.delete_extension_ipsec_policy(\
session, policy_name)

    *Delete extension_ipsec_policy*

    Example Usage of the Method::

            ret =\
 extension_ipsec_policy_delete.delete_extension_ipsec_policy(session,\
 policy_name)
            print(ret)

    Details::

        extension_ipsec_policyObj = extension_ipsec_policy()
        extension_ipsec_policyObj.set_policy_name(policy_name)
        ret = _delete_extension_ipsec_policy(session,\
 extension_ipsec_policyObj)
        print(ret)

    **Inputs**

    :param session: The session returned by the login.
    :param policy_name: Specifies  the name for the IPsec policy. The IPsec\
      policy name can be up to 31 characters long and cannot contain certain\
      special characters and keywords such as 'all' and 'none'.

    **Output**

    :rtype: Dictionary of response

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_extension_ipsec_policy import extension_ipsec_policy

from pyfos.utils import brcd_util
# End module imports


def _delete_extension_ipsec_policy(session, extension_ipsec_policyObj):
    return extension_ipsec_policyObj.delete(session)


def delete_extension_ipsec_policy(session, policy_name=None):
    extension_ipsec_policyObj = extension_ipsec_policy()
    extension_ipsec_policyObj.set_policy_name(policy_name)
    return _delete_extension_ipsec_policy(session, extension_ipsec_policyObj)


def validate(extension_ipsec_policyObj):
    if extension_ipsec_policyObj.peek_policy_name() is None:
        return 1
    return 0


def main(argv):
    filters = ["policy_name"]
    inputs = brcd_util.parse(argv, extension_ipsec_policy, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _delete_extension_ipsec_policy(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
