# Copyright 2018 Brocade Communications Systems LLC.  All rights reserved.
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

:mod:`pyfos_brocade_extension_ipsec_policy` - PyFOS module for an IPsec policy.
*******************************************************************************
The :mod:`pyfos_brocade_extension_ipsec_policy` module provides REST
support for an extension IPsec policy.
"""
from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type


class extension_ipsec_policy(pyfos_rest_util.rest_object):
    """Class of extension_ipsec_policy

    Important Class Members:

        +--------------------+------------------+---------------------------------+
        | Attribute Name     | Description      |Frequently Used Functions        |
        +====================+==================+=================================+
        |policy-name         |The name of the   |:func:`peek_policy_name`         |
        |                    |IPsec policy.     |:func:`set_policy_name`          |
        +--------------------+------------------+---------------------------------+
        |profile-name        |The profile name  |:func:`peek_profile_name`        |
        |                    |of the policy.    |:func:`set_profile_name`         |
        +--------------------+------------------+---------------------------------+
        |authentication-data |The autentication |:func:`peek_authentication_data` |
        |                    |data of the       |:func:`set_authentication_data`  |
        |                    |policy.           |                                 |
        +--------------------+------------------+---------------------------------+
        |restart-ike-sessions|Restarts the      |:func:`peek_restart_ike_sessions`|
        |                    |IKE session.      |:func:`set_restart_ike_sessions` |
        +--------------------+------------------+---------------------------------+
        |num-ike-sessions    |The total number  |:func:`peek_num_ike_sessions`    |
        |                    |of IKE sessions.  |                                 |
        +--------------------+------------------+---------------------------------+

    *Object Functions*

        .. function:: get()

            Fills the object with values for all the attributes. Once filled,
            the object can be printed using :func:`pyfos_utils.response_print`.

            :param session: The session handler returned
             by :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or success response.

    *Attribute Functions*

        .. function:: peek_policy_name()

            Reads the policy name from an IPsec object.

            :rtype: None on error and a value on success.

        .. function:: peek_profile_name()

            Reads the profile name from an IPsec object.

            :rtype: None on error and a value on success.

        .. function:: peek_authentication_data()

            Reads the authentication data from an IPsec object

            :rtype: None on error and a value on success.

        .. function:: peek_restart_ike_sessions()

            Reads the restart IKE session value from an IPsec object.

            :rtype: None on error and a value on success.

        .. function:: peek_num_ike_sessions()

            Reads the number of IKE sessions for an IPsec object.

            :rtype: None on error and a value on success.

        .. function:: set_policy_name(policyName)

            Sets the policy name in an IPsec object.

            :rtype: A dictionary of errors or success response and a value
             with the policy name as the key.

        .. function:: set_profile_name(profileName)

            Sets the profile name in an IPsec object.

            :rtype: A dictionary of errors or success response and a value
             with the profile name as the key.

        .. function:: set_authentication_data(authData)

            Sets the authentication Data in an Object

            :rtype: A dictionary of errors or success response and a value
             with the authentication data as the key.

        .. function:: set_restart_ike_sessions(restartIkeSession)

            Sets the restart IKE session in an IPsec object.

            :rtype: A dictionary of errors or success response and a value
             with the restart IKE sessions as the key.

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.ipsec,
                         "/rest/running/brocade-extension-ipsec-policy/"
                         "extension-ipsec-policy")
        self.add(pyfos_rest_util.rest_attribute("policy-name",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("profile-name",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("authentication-data",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("num-ike-sessions",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("restart-ike-sessions",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.load(dictvalues, 1)
