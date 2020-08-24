# Copyright © 2018 Broadcom.  All rights reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.
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

:mod:`pyfos_brocade_snmp` - PyFOS module to provide rest support for SNMP.
**************************************************************************
The :mod:`pyfos_brocade_snmp` provides REST support for the SNMP.
"""
from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


class system(pyfos_rest_util.rest_object):
    """This class provides information for the SNMP system configurations.

    Important class members:

        +--------------------------+--------------------------------+---------------------------------------------------+
        | Attribute name           | Description                    |Frequently used methods                            |
        +==========================+================================+===================================================+
        | description              | Texual description of the      |:meth:`set_description`                            |
        |                          | entity                         |:meth:`peek_description`                           |
        +--------------------------+--------------------------------+---------------------------------------------------+
        | location                 | The physical location of       |:meth:`set_location`                               |
        |                          | this node                      |:meth:`peek_location`                              |
        +--------------------------+--------------------------------+---------------------------------------------------+
        | contact                  | The textual identification of  |:meth:`set_contact`                                |
        |			   | the contact person 	    |:meth:`peek_contact`		                |
        +--------------------------+--------------------------------+---------------------------------------------------+
        | informs-enabled          | Indicates if informs is enabled|:meth:`set_informs_enabled`                        |
        |			   | or not                   	    |:meth:`peek_informs_enabled`	                |
        +--------------------------+--------------------------------+---------------------------------------------------+
        | encryption-enabled       | Indicates if the password flag |:meth:`set_encryption_enabled`                     |
        |			   | is enabled or not		    |:meth:`peek_encryption_enabled`	                |
        +--------------------------+--------------------------------+---------------------------------------------------+
        | audit-interval           | Indicates the SNMP audit 	    |:meth:`set_audit_interval`                         |
        |			   | interval          	            |:meth:`peek_audit_interval`                        |
        +--------------------------+--------------------------------+---------------------------------------------------+
        | default-control          | Defaulting the SNMP            |:meth:`set_default_config_default_control`         |
        |			   | configurations		    |                              	                |
        +--------------------------+--------------------------------+---------------------------------------------------+
        | security-get-level       | SNMP GET security level        |:meth:`set_security_get_level`                     |
        |			   |                                |:meth:`peek_security_get_level`                    |
        +--------------------------+--------------------------------+---------------------------------------------------+
        | security-set-level       | SNMP SET security level        |:meth:`set_security_set_level`                     |
        |			   |                                |:meth:`peek_security_set_level`                    |
        +--------------------------+--------------------------------+---------------------------------------------------+
        | snmpv1-enabled           | Indicates if SNMP v1 is enabled|:meth:`set_snmpv1_enabled`                         |
        |			   | or not                   	    |:meth:`peek_snmpv1_enabled`	                |
        +--------------------------+--------------------------------+---------------------------------------------------+

    *Object methods*

        .. classmethod:: get()

            Returns :class:`system`
            object or a list of objects filled with
            SNMP system attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or
                :class:`system` object

        .. method:: patch()

            Replace entry members. Fields involved are set within the object
            using the attribute's set method.

    *Attribute methods*

        .. method:: set_description()

            Set the system description.

            :rtype: dictionary of error or success response.

        .. method:: peek_description()

            Reads system system description of SNMP of the switch.

            :rtype: None or system description of the switch.

        .. method:: set_location()

            Set the system location name.

            :rtype: dictionary of error or success response.

        .. method:: peek_location()

            Reads location name from the object.

            :rtype: None or location name.

        .. method:: set_contact()

            Set the contact person of the switch.

            :rtype: None or contact person of the switch.

        .. method:: peek_contact()

            Reads system contact from the object.

            :rtype: None or system contact.

        .. method:: set_informs_enabled()

            Set the informs enabled flag.

            :rtype: None or informs enabled flag.

        .. method:: peek_informs_enabled()

            Reads informs enabled from the object.

            :rtype: None or informs enabled.

        .. method:: set_encryption_enabled()

            Set the encryption enabled flag.

            :rtype: None or encryption enabled flag.

        .. method:: peek_encryption_enabled()

            Reads encryption enabled from the object.

            :rtype: None or encryption enabled.

        .. method:: set_audit_interval()

            Set the audit interval.

            :rtype: None or audit interval.

        .. method:: peek_audit_interval()

            Reads audit interval from the object.

            :rtype: None or audit interval.

        .. method:: set_default_config_default_control()

            Set the default control.

            :rtype: None or default control.

        .. method:: set_security_level()

            Set the SNMP security level.

            :rtype: None or security level.

        .. method:: peek_security_level()

            Reads SNMP security level from the object.

            :rtype: None or SNMP security level.

        .. method:: set_security_get_level()

            Set the SNMP get security level.

            :rtype: None or SNMP get security level.

        .. method:: peek_security_get_level()

            Reads SNMP get security level from the object.

            :rtype: None or SNMP get security level.

        .. method:: set_security_set_level()

            Set the SNMP set security level.

            :rtype: None or SNMP set security level.

        .. method:: peek_security_set_level()

            Reads SNMP set security level from the object.

            :rtype: None or SNMP set security level.

        .. method:: set_snmpv1_enabled()

            Set the SNMP v1 enabled flag.

            :rtype: None or SNMP v1 enabled flag.

        .. method:: peek_snmpv1_enabled()

            Reads SNMP v1 enabled from the object.

            :rtype: None or SNMP v1 enabled.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.system,
                         "/rest/running/brocade-snmp/system",
                         version.VER_RANGE_821b_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "description", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "location", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "contact", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "informs-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "encryption-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "audit-interval", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "default-config", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "default-control", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["default-config"])
        self.add(pyfos_rest_util.rest_attribute(
            "security-get-level", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "security-set-level", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "snmpv1-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class mib_capability(pyfos_rest_util.rest_object):
    """This class provides information for the SNMP MIB capability.

    Important class members:

        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | Attribute name                    | Description                    | Frequently used methods                               |
        +===================================+================================+=======================================================+
        | mib-name                          | Indicates the MIB name         |:meth:`peek_mib_name`                                  |
        |				    |                                |                     			             |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | is-mib-enabled-state              | Indicates the MIB is enabled / |:meth:`set_is_mib_enabled_state`                       |
        |				    | disabled                       |:meth:`peek_is_mib_enabled_state`	                     |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+

    *Object methods*

        .. classmethod:: get()

            Returns :class:`mib-capability`
            object or a list of objects filled with
            mib capability attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or
                :class:`mib-capability` object

        .. method:: patch()

            Replace entry members. Fields involved are set within the object
            using the attribute's set method.

    *Attribute methods*

        .. method:: peek_mib_name()

            Reads mib name from the object.

            :rtype: None or mib name.

        .. method:: set_is_mib_enabled_state()

            Set the mib state enabled / disabled.

            :rtype: dictionary of error or success response.

        .. method:: peek_is_mib_enabled_state()

            Reads the mib state.

            :rtype: None or mib state.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.mib_capability,
                         "/rest/running/brocade-snmp/mib-capability",
                         version.VER_RANGE_821b_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "mib-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "is-mib-enabled-state", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class trap_capability(pyfos_rest_util.rest_object):
    """This class provides information for the SNMP MIB trap capability.

    Important class members:

        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | Attribute name                    | Description                    | Frequently used methods                               |
        +===================================+================================+=======================================================+
        | trap-name                         | Indicates the SNMP trap name   |:meth:`peek_trap_name`                                 |
        |                                   |                                |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | is_trap-enabled-state             | Indicates the trap is enabled /|:meth:`set_is_trap_enabled_state`                      |
        |                                   | disabled                       |:meth:`peek_is_trap_enabled_state`                     |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | severity                          | Indicates the severity of      |:meth:`set_severity`                                   |
        |                                   | the swEvent trap               |:meth:`peek_severity`                                  |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+

    *Object methods*

        .. classmethod:: get()

            Returns :class:`trap-capability`
            object or a list of objects filled with
            trap capability attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or
                :class:`trap-capability` object

        .. method:: patch()

            Replace entry members. Fields involved are set within the object
            using the attribute's set method.

    *Attribute methods*

        .. method:: peek_trap_name()

            Reads trap name from the object.

            :rtype: None or trap name.

        .. method:: set_is_trap_enabled_state()

            Set the trap state enabled / disabled.

            :rtype: dictionary of error or success response.

        .. method:: peek_is_trap_enabled_state()

            Reads the trap state.

            :rtype: None or trap state.

        .. method:: set_severity ()

            Set the severity value to swEvent trap.

            :rtype: dictionary of error or success response.

        .. method:: peek_severity ()

            Reads severity from the object.

            :rtype: None or severity.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.trap_capability,
                         "/rest/running/brocade-snmp/trap-capability",
                         version.VER_RANGE_821b_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "trap-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "is-trap-enabled-state", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "severity", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class v1_account(pyfos_rest_util.rest_object):
    """This class provides information for the SNMP v1 account.

    Important class members:

        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | Attribute name                    | Description                    | Frequently used methods                               |
        +===================================+================================+=======================================================+
        | index				    | Index of SNMP v1 account       |:meth:`peek_index`                                     |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | community-name                    | Name of the community          |:meth:`set_community_name`                      	     |
        | 				    | 				     |:meth:`peek_community_name`                      	     |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | community-group                   | Community belongs to the group |:meth:`peek_community_group`                           |
        |				    | RO or RW			     |:meth:`set_community_group`			     |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+

    *Object methods*

        .. classmethod:: get()

            Returns :class:`v1-account`
            object or a list of objects filled with
            SNMP v1 account attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or
                :class:`v1-account` object

        .. method:: patch()

            Replace entry members. Fields involved are set within the object
            using the attribute's set method.

    *Attribute methods*

        .. method:: peek_index()

            Reads index of SNMP v1 account entry from the object.

            :rtype: None or index number of SNMP v1 account.

        .. method:: set_community_name()

            Set the community name.

            :rtype: dictionary of error or success response.

        .. method:: peek_community_name()

            Reads community name from the object.

            :rtype: None or community name.

        .. method:: peek_community_group()

            Reads group name of the SNMP v1 account.

            :rtype: None or group name.

        .. method:: set_community_group()

            Set group name of the SNMP v1 account.

            :rtype: dictionary of error or success response.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.v1_account,
                         "/rest/running/brocade-snmp/v1-account",
                         version.VER_RANGE_821b_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "index", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "community-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "community-group", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class v1_trap(pyfos_rest_util.rest_object):
    """This class provides information for SNMP v1 trap notification.

    Important class members:

        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | Attribute name                    | Description                    | Frequently used methods                               |
        +===================================+================================+=======================================================+
        | index                             | Index of SNMP v1 trap account  |:meth:`peek_index`                               	     |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | host				    | IP address of trap recipient   |:meth:`set_host`                          	     |
        |                                   | system			     |:meth:`peek_host`                                      |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | trap-severity-level	            | Specifies the trap recipient   |:meth:`set_trap_severity_level`                        |
        |                                   | severity level                 |:meth:`peek_trap_severity_level`                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | port-number                       | UDP port where SNMP traps will |:meth:`set_port_number`                                |
        |				    | be received		     |:meth:`peek_port_number`			             |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+

    *Object methods*

        .. classmethod:: get()

            Returns :class:`SNMP v1 trap recipients`
            object or a list of objects filled with
            v1 trap attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or
                :class:`v1-trap` object

        .. method:: patch()

            Replace entry members. Fields involved are set within the object
            using the attribute's set method.

    *Attribute methods*

        .. method:: peek_index()

            Reads index of SNMP v1 trap entry from the object.

            :rtype: None or index number of SNMP v1 trap entry.

        .. method:: set_host()

            Set the IP address of trap recipient host.

            :rtype: dictionary of error or success response.

        .. method:: peek_host()

            Reads IP address of the trap recipient host from the object.

            :rtype: None or IP address of the host.

        .. method:: set_trap_severity_level()

            Set the severity level of the trap recipient.

            :rtype: None or severity level of the trap recipient.

        .. method:: peek_trap_severity_level()

            Reads severity level of the trap recipient from the object.

            :rtype: None or severity level of the trap recipient.

        .. method:: set_port_number()

            Set the port number for the trap recipient.

            :rtype: None or success response.

        .. method:: peek_port_number()

            Reads port number from the object.

            :rtype: None or port number.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.v1_trap,
                         "/rest/running/brocade-snmp/v1-trap",
                         version.VER_RANGE_821b_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "index", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "host", pyfos_type.type_ip_addr,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "trap-severity-level", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "port-number", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class v3_account(pyfos_rest_util.rest_object):
    """This class provides information of SNMP v3 user account

    Important class members:

        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | Attribute name                    | Description                    | Frequently used methods                               |
        +===================================+================================+=======================================================+
        | index				    | Index of SNMP v3 user account  |:meth:`peek_index`                                     |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | user-name                         | Name of the SNMP v3 user       |:meth:`set_user_name`                                  |
        |			            |				     |:meth:`peek_user_name`				     |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | user-group                        | SNMP v3 user belongs to the    |:meth:`peek_user_group`                                |
        |				    | group snmpadmin or snmpuser    |							     |
        |				    |				     |:meth:`set_user_group`				     |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | authentication-protocol           | Authentication protocol for    |:meth:`set_authentication_protocol`                    |
        |				    | SNMP v3 user		     |:meth:`peek_authentication_protocol`                   |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | privacy-protocol                  | Privacy protocol for SNMP v3   |:meth:`set_privacy_protocol`                           |
        |				    | user		     	     |:meth:`peek_privacy_protocol`			     |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | authentication-password           | Authentication password for    |:meth:`set_authentication_password`                    |
        |				    | SNMP v3 user		     |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | privacy-password                  | Privacy password for SNMP v3   |:meth:`set_privacy_password`                           |
        |				    | user		     	     |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | manager-engine-id                 | The manager engine-id is used  |:meth:`set_manager_engine_id`                          |
        |				    | to receive  the informs        |:meth:`peek_manager_engine_id`                         |
        |				    | notification                   |                                       		     |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+

    *Object methods*

        .. classmethod:: get()

            Returns :class:`v3-account`
            object or a list of objects filled with
            SNMP v3 account attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or
                :class:`blade` object

        .. method:: patch()

            Replace entry members. Fields involved are set within the object
            using the attribute's set method.

    *Attribute methods*

        .. method:: peek_index()

            Reads index of SNMP v3 user account from the object.

            :rtype: None or index number of SNMP v3 account.

        .. method:: set_user_name()

            Set SNMP V3 user name.

            :rtype: dictionary value of error or success response.

        .. method:: peek_user_name()

            Reads SNMP v3 user name of SNMP v3 account from the object.

            :rtype: None or user name of the SNMP v3 account.

        .. method:: peek_user_group()

            Reads group name of the SNMP v3 user.

            :rtype: None or group of the SNMP v3 user.

        .. method:: set_user_group()

            Set group name of the SNMP v3 user.

            :rtype: dictionary value of error or success response.

        .. method:: set_authentication_protocol()

            Set authentication protocol of the SNMP v3 user.

            :rtype: dictionary value of error or success response.

        .. method:: peek_authentication_protocol()

            Reads authentication protocol of the SNMP v3 user.

            :rtype: None or auth protocol of the SNMP v3 user.

        .. method:: set_privacy_protocol()

            Set privacy protocol of the SNMP v3 user.

            :rtype: dictionary value of error or success response.

        .. method:: peek_privacy_protocol()

            Reads privacy protocol of the SNMP v3 user.

            :rtype: None or privacy protocol of the SNMP v3 user.

        .. method:: set_authentication_password()

            Set authentication password of the SNMP v3 user.

            :rtype: dictionary value of error or success response.

        .. method:: set_privacy_password()

            Set privacy password of the SNMP v3 user.

            :rtype: dictionary value of error or success response.

        .. method:: set_manager_engine_id()

            Set manager engine id.

            :rtype: dictionary value of error or success response.

        .. method:: peek_manager_engine_id()

            Reads engine id of the manager.

            :rtype: None or manager engine id.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.v3_account,
                         "/rest/running/brocade-snmp/v3-account",
                         version.VER_RANGE_821b_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "index", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "user-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "user-group", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "authentication-protocol", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "privacy-protocol", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "authentication-password", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "privacy-password", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "manager-engine-id", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class v3_trap(pyfos_rest_util.rest_object):
    """This class provides information for SNMP v3 trap notification.

    Important class members:

        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | Attribute name                    | Description                    | Frequently used methods                               |
        +===================================+================================+=======================================================+
        | trap-index                        | Defines the label by which     |:meth:`peek_trap_index`                                |
        |				    | this object is known	     |							     |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | usm-index                         | Defines the label by which     |:meth:`peek_usm_index`                                 |
        |				    | this object is known	     |							     |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | host				    | IP address of trap recipient   |:meth:`set_host`                          	     |
        |                                   | system			     |:meth:`peek_host`                                      |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | trap-severity-level	            | Specifies the trap recipient   |:meth:`set_trap_severity_level`                        |
        |                                   | severity level                 |:meth:`peek_trap_severity_level`                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | port-number                       | UDP port where SNMP traps will |:meth:`set_port_number`                                |
        |                                   | be received                    |:meth:`peek_port_number`                               |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | informs-enabled                   | Indicates whether informs is   |:meth:`set_informs_enabled`                            |
        |				    | enabled or not    	     |:meth:`peek_informs_enabled`                           |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+

    *Object methods*

        .. classmethod:: get()

            Returns :class:`SNMP v1 trap recipients`
            object or a list of objects filled with
            v1 trap attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or
                :class:`v3-trap` object

        .. method:: patch()

            Replace entry members. Fields involved are set within the object
            using the attribute's set method.

    *Attribute methods*

        .. method:: peek_trap_index()

            Reads index of SNMP v3 trap entry from the object.

            :rtype: None or index number of SNMP v3 trap entry.

        .. method:: peek_usm_index()

            Reads index of SNMP v3 user entry from the associated object.

            :rtype: None or index number of SNMP v3 user entry.

        .. method:: set_host()

            Set IP address of the trap recipient host.

            :rtype: dictionary value of error or success response.

        .. method:: peek_host()

            Reads IP address of the trap recipient host from the object.

            :rtype: None or IP address of the host.

        .. method:: set_trap_severity_level()

            Set severity level of the trap recipient.

            :rtype: dictionary value of error or success response.

        .. method:: peek_trap_severity_level()

            Reads severity level of the trap recipient from the object.

            :rtype: None or severity level of the trap recipient.

        .. method:: set_port_number()

            Set port number of the trap recipient.

            :rtype: dictionary value of error or success response.

        .. method:: peek_port_number()

            Reads port number from the object.

            :rtype: None or port number.

        .. method:: set_informs_enabled()

            Set  informs enabled flag of the object.

            :rtype: dictionary value of error or success response.

        .. method:: peek_informs_enabled()

            Reads informs enabled flag from the object.

            :rtype: None or informs enabled flag value.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.v3_trap,
                         "/rest/running/brocade-snmp/v3-trap",
                         version.VER_RANGE_821b_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "trap-index", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "usm-index", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "host", pyfos_type.type_ip_addr,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "trap-severity-level", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "port-number", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "informs-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class access_control(pyfos_rest_util.rest_object):
    """This class provides information for SNMP access control.

    Important class members:

        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | Attribute name                    | Description                    | Frequently used methods                               |
        +===================================+================================+=======================================================+
        | index                             | Defines the label by which this|:meth:`peek_index`                               	     |
        |				    | object is known		     |							     |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | host				    | The subnet area of the access  |:meth:`peek_host`                          	     |
        |                                   | host			     |:meth:`set_host`                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | access-level	    		    | The access level of SNMP access|:meth:`peek_access_level`                              |
        |                                   | control entry	   	     |:meth:`set_access_level`                               |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+

    *Object methods*

        .. classmethod:: get()

            Returns :class:`SNMP access contorl list` object.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or
                :class:`access-control` object

        .. method:: patch()

            Replace entry members. Fields involved are set within the object
            using the attribute's set method.

    *Attribute methods*

        .. method:: peek_index()

            Reads index of SNMP access control entry from the object.

            :rtype: None or index number of SNMP access control list entry.

        .. method:: set_host()

            Set the IP address of host for the SNMP access control list.

            :rtype: dictionary of error or success response.

        .. method:: peek_host()

            Reads IP address of the subnet area of the access host from
                  the object.

            :rtype: None or IP address of the host.

        .. method:: set_access_level()

            Set access contol level.

            :rtype: dictionary value of error or success response.


        .. method:: peek_access_level()

            Reads access level of SNMP access control entry from the object.

            :rtype: None or SNMP access level of SNMP access control entry.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.access_control,
                         "/rest/running/brocade-snmp/access-control",
                         version.VER_RANGE_821b_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "index", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "host", pyfos_type.type_ip_addr,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "access-level", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)
