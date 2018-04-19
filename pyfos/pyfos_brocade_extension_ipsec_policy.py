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

:mod:`pyfos_brocade_extension_ipsec_policy` - PyFOS module for IPSec Policy.
*******************************************************************************
The :mod:`pyfos_brocade_extension_ipsec_policy` provides a REST
support for Extension IPSec Policy.
"""
import pyfos.pyfos_rest_util as pyfos_rest_util
from pyfos.pyfos_type import pyfos_type


class extension_ipsec_policy(pyfos_rest_util.rest_object):
    """Class of extension_ipsec_policy

    Important class members:

        +-------------------------------+-------------------------------+---------------------------------------+
        | Attribute name                | Description                   |Frequently used functions              |
        +===============================+===============================+=======================================+
        | policy-name                   | The name of the ipsec policy  |:func:`peek_policy_name`               |
        +-------------------------------+-------------------------------+---------------------------------------+
        | policy-name                   | The name of the ipsec policy  |:func:`set_policy_name`                |
        +-------------------------------+-------------------------------+---------------------------------------+
        | profile-name                  | The profile name of policy    |:func:`peek_profile_name`              |
        +-------------------------------+-------------------------------+---------------------------------------+
        | profile-name                  | The profile name of policy    |:func:`set_profile_name`               |
        +-------------------------------+-------------------------------+---------------------------------------+
        | authentication-data           | Autentication data of policy  |:func:`peek_authentication_data`       |
        +-------------------------------+-------------------------------+---------------------------------------+
        | authentication-data           | Autentication data of policy  |:func:`set_authentication_data`        |
        +-------------------------------+-------------------------------+---------------------------------------+
        | restart-ike-sessions          | restart the ike session       |:func:`peek_restart_ike_sessions`      |
        +-------------------------------+-------------------------------+---------------------------------------+
        | restart-ike-sessions          | restart the ike session       |:func:`set_restart_ike_sessions`       |
        +-------------------------------+-------------------------------+---------------------------------------+
        | num-ike-sessions              | Total IKE sessions            |:func:`peek_num_ike_sessions`          |
        +-------------------------------+-------------------------------+---------------------------------------+

    *Object functions*

        .. function:: get()

            Fill the object with values for all the attributes. Once filled,
            the object can be printed using :func:`pyfos_utils.response_print`

            :param session: session handler returned
             by :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

    *Attribute functions*

        .. function:: peek_policy_name()

            Reads the policy name from an ipsec object.

            :rtype: None on error and value on success

        .. function:: peek_profile_name()

            Reads the profile name from an ipsec object.

            :rtype: None on error and value on success

        .. function:: peek_authentication_data()

            Reads the authentication data from an ipsec Object

            :rtype: None on error and value on success

        .. function:: peek_restart_ike_sessions()

            Reads the restart ike seesion value from an ipsec object.

            :rtype: None on error and value on success

        .. function:: peek_num_ike_sessions()

            Reads num of IKE sessions for an ipsec object.

            :rtype: None on error and value on success

        .. function:: set_policy_name(policyName)

            Set the policy name in an ipsec object.

            :rtype: dictionary of error or success response and value
             with "policy-name" as key

        .. function:: set_profile_name(profileName)

            Set the profile name in an ipsec object.

            :rtype: dictionary of error or success response and value with
             "profile-name" as key

        .. function:: set_authentication_data(authData)

            Set the authentication Data in an Object

            :rtype: dictionary of error or success response and value
             with "authentication-data" as key

        .. function:: set_restart_ike_sessions(restartIkeSession)

            Set the restart ike session in an ipsec object.

            :rtype: dictionary of error or success response and value
             with "restart-ike-sessions" as key

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
