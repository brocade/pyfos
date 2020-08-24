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


# pyfos_brocade_extension_ipsec_policy.py(pyGen v1.0.0)


"""

:mod:`pyfos_brocade_extension_ipsec_policy` - PyFOS module Represents\
 IPsec policy defined on extension blade or system.
******************************************************************************\
*******************************************************************************
The:mod:`pyfos_brocade_extension_ipsec_policy` The PyFOS module support\
 Represents IPsec policy defined on extension blade or system.
"""


# Start module imports
from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
# End module imports


class extension_ipsec_policy(pyfos_rest_util.rest_object):

    """Class of extension_ipsec_policy

    *Description extension_ipsec_policy*

        Represents IPsec policy defined on extension blade or system.

    Important class members of extension_ipsec_policy:

        +--------------------------+---------------------------------+-------------------------------------------------+
        | Attribute Name           | Description                     |  Frequently Used Methods                        |
        +==========================+=================================+=================================================+
        | policy-name              | Specifies the name for the      | :func:`peek_policy_name`                        |
        |                          | IPsec policy. The IPsec         | :func:`set_policy_name`                         |
        |                          | policy name can be up to 31     |                                                 |
        |                          | characters long and cannot      |                                                 |
        |                          | contain certain special         |                                                 |
        |                          | characters and keywords such    |                                                 |
        |                          | as 'all' and 'none'.            |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | restart-ike-sessions     | Write-only leaf, will not be    | :func:`peek_restart_ike_sessions`               |
        |                          | returned in GET request. Set    | :func:`set_restart_ike_sessions`                |
        |                          | it to 1 to restart all          |                                                 |
        |                          | inactive IKE sessions for       |                                                 |
        |                          | this policy in PATCH request.   |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | authentication-data      | Specifies the                   | :func:`peek_authentication_data`                |
        |                          | authentication-data depending   | :func:`set_authentication_data`                 |
        |                          | on the profile used: For        |                                                 |
        |                          | 'preshared' profile, this       |                                                 |
        |                          | field specifies the             |                                                 |
        |                          | preshared-key to be used for    |                                                 |
        |                          | authentication. This operand    |                                                 |
        |                          | is required with shared-key     |                                                 |
        |                          | authentication. Preshared key   |                                                 |
        |                          | length should have minimum      |                                                 |
        |                          | length of 16 characters and     |                                                 |
        |                          | maximum length of 64            |                                                 |
        |                          | characters. For 'pki'           |                                                 |
        |                          | profile, this field specifies   |                                                 |
        |                          | the local key pair name to      |                                                 |
        |                          | use for IKE authentication.     |                                                 |
        |                          | This operand is required with   |                                                 |
        |                          | PKI profile. Key pair name      |                                                 |
        |                          | length should have minimum      |                                                 |
        |                          | length of 1 character and       |                                                 |
        |                          | maximum length of 32            |                                                 |
        |                          | characters. Authentication      |                                                 |
        |                          | data will returned as a zero    |                                                 |
        |                          | length string for read          |                                                 |
        |                          | operations on policies with     |                                                 |
        |                          | 'preshared' profile.            |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | profile-name             | Specifies the IPsec profile     | :func:`peek_profile_name`                       |
        |                          | to use with the IPSec policy.   | :func:`set_profile_name`                        |
        |                          | Valid values for profile name   |                                                 |
        |                          | are 'preshared' and 'pki'.      |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | num-ike-sessions         | Number of IKE Sessions.         | :func:`peek_num_ike_sessions`                   |
        +--------------------------+---------------------------------+-------------------------------------------------+

    *Object functions for extension_ipsec_policy*

    .. function:: get()

        Get the instances of class "extension_ipsec_policy from switch. The
         object can be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for extension_ipsec_policy*

        .. function:: peek_policy_name()

            Reads the value assigned to policy-name in the object.

            :rtype: None on error and a value on success.


        .. function:: set_policy_name(value)

            Set the value of policy-name in the object.

            :rtype: A dictionary of error or a success response and a value
             with "policy-name" as the key


        .. function:: peek_restart_ike_sessions()

            Reads the value assigned to restart-ike-sessions in the object.

            :rtype: None on error and a value on success.


        .. function:: set_restart_ike_sessions(value)

            Set the value of restart-ike-sessions in the object.

            :rtype: A dictionary of error or a success response and a value
             with "restart-ike-sessions" as the key


        .. function:: peek_authentication_data()

            Reads the value assigned to authentication-data in the object.

            :rtype: None on error and a value on success.


        .. function:: set_authentication_data(value)

            Set the value of authentication-data in the object.

            :rtype: A dictionary of error or a success response and a value
             with "authentication-data" as the key


        .. function:: peek_profile_name()

            Reads the value assigned to profile-name in the object.

            :rtype: None on error and a value on success.


        .. function:: set_profile_name(value)

            Set the value of profile-name in the object.

            :rtype: A dictionary of error or a success response and a value
             with "profile-name" as the key


        .. function:: peek_num_ike_sessions()

            Reads the value assigned to num-ike-sessions in the object.

            :rtype: None on error and a value on success.


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-extension-ipsec-policy" +\
                 "/extension-ipsec-policy"
        clstype = pyfos_rest_util.rest_obj_type.ipsec
        super().__init__(clstype, clsuri)

        self.add(pyfos_rest_util.rest_attribute("policy-name",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("authentication-data",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("profile-name",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("restart-ike-sessions",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("num-ike-sessions",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.load(dictvalues, 1)
