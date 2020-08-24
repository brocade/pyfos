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


# extension_ipsec_policy_modify.py(pyGen v1.0.0)


"""

:mod:`extension_ipsec_policy_modify` - PyFOS util to modify for\
 extension_ipsec_policy
******************************************************************************\
*******************************************************************************
The:mod:`extension_ipsec_policy_modify` PyFOS util to modify for\
 extension_ipsec_policy


Represents IPsec policy defined on extension blade or system.

extension_ipsec_policy_modify: usage

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
    * --profile-name=PROFILE-NAME: Specifies the IPsec profile to use with the\
      IPSec policy. Valid values for profile name are 'preshared' and 'pki'.
    * --policy-name=POLICY-NAME: Specifies  the name for the IPsec policy. The\
      IPsec policy name can be up to 31 characters long and cannot contain\
      certain special characters and keywords such as 'all' and 'none'.
    * --restart-ike-sessions=RESTART-IKE-SESSIONS: Write-only leaf, will not\
      be returned in GET request. Set it to 1 to restart all inactive IKE\
      sessions for this policy in PATCH request.
    * --authentication-data=AUTHENTICATION-DATA: Specifies the\
      authentication-data depending on the profile used:  For 'preshared'\
      profile, this field specifies the preshared-key to be used for\
      authentication. This operand is required with shared-key\
      authentication. Preshared key length should have minimum length of 16\
      characters and maximum length of 64 characters.  For 'pki' profile,\
      this field specifies the local key pair name to use for IKE\
      authentication. This operand is required with PKI profile. Key pair\
      name length should have minimum length of 1 character and maximum\
      length of 32 characters.  Authentication data will returned as a zero\
      length string for read operations on policies with 'preshared'\
      profile.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: extension_ipsec_policy_modify.modify_extension_ipsec_policy(\
session, profile_name, policy_name, restart_ike_sessions,\
authentication_data)

    *Modify extension_ipsec_policy*

    Example Usage of the Method::

            ret =\
 extension_ipsec_policy_modify.modify_extension_ipsec_policy(session,\
 profile_name, policy_name, restart_ike_sessions, authentication_data)
            print(ret)

    Details::

        extension_ipsec_policyObj = extension_ipsec_policy()
        extension_ipsec_policyObj.set_profile_name(profile_name)
        extension_ipsec_policyObj.set_policy_name(policy_name)
       \
 extension_ipsec_policyObj.set_restart_ike_sessions(restart_ike_sessions)
        extension_ipsec_policyObj.set_authentication_data(authentication_data)
        ret = _modify_extension_ipsec_policy(session,\
 extension_ipsec_policyObj)
        print(ret)

    **Inputs**

    :param session: The session returned by the login.
    :param profile_name: Specifies the IPsec profile to use with the IPSec\
      policy. Valid values for profile name are 'preshared' and 'pki'.
    :param policy_name: Specifies  the name for the IPsec policy. The IPsec\
      policy name can be up to 31 characters long and cannot contain certain\
      special characters and keywords such as 'all' and 'none'.
    :param restart_ike_sessions: Write-only leaf, will not be returned in GET\
      request. Set it to 1 to restart all inactive IKE sessions for this\
      policy in PATCH request.
    :param authentication_data: Specifies the authentication-data depending on\
      the profile used:  For 'preshared' profile, this field specifies the\
      preshared-key to be used for authentication. This operand is required\
      with shared-key authentication. Preshared key length should have\
      minimum length of 16 characters and maximum length of 64 characters. \
      For 'pki' profile, this field specifies the local key pair name to use\
      for IKE authentication. This operand is required with PKI profile. Key\
      pair name length should have minimum length of 1 character and maximum\
      length of 32 characters.  Authentication data will returned as a zero\
      length string for read operations on policies with 'preshared'\
      profile.

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


def _modify_extension_ipsec_policy(session, extension_ipsec_policyObj):
    return extension_ipsec_policyObj.patch(session)


def modify_extension_ipsec_policy(session, profile_name=None,
                                  policy_name=None,
                                  restart_ike_sessions=None,
                                  authentication_data=None):
    extension_ipsec_policyObj = extension_ipsec_policy()
    extension_ipsec_policyObj.set_profile_name(profile_name)
    extension_ipsec_policyObj.set_policy_name(policy_name)
    extension_ipsec_policyObj.set_restart_ike_sessions(restart_ike_sessions)
    extension_ipsec_policyObj.set_authentication_data(authentication_data)
    return _modify_extension_ipsec_policy(session, extension_ipsec_policyObj)


def validate(extension_ipsec_policyObj):
    if extension_ipsec_policyObj.peek_policy_name() is None or\
       (extension_ipsec_policyObj.peek_restart_ike_sessions() is None and
        (extension_ipsec_policyObj.peek_profile_name() is None or
         extension_ipsec_policyObj.peek_authentication_data() is None)):
        return 1
    return 0


def main(argv):
    filters = ["profile_name", "policy_name", "restart_ike_sessions",
               "authentication_data"]
    inputs = brcd_util.parse(argv, extension_ipsec_policy, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _modify_extension_ipsec_policy(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
