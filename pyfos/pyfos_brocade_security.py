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

:mod:`pyfos_brocade_security` - PyFOS module to provide REST support for\
system security.
************************************************************************************************
The :mod:`pyfos_brocade_security` module provides REST support for \
system security.

"""


from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


class radius_server(pyfos_rest_util.rest_object):
    """This class is used to add, change, read, and delete an AAA
       RADIUS server configuration.

    Important Class Members:

        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | Attribute Name                            | Description                      |Frequently Used Methods                       |
        +===========================================+==================================+==============================================+
        | server                                    | The RADIUS server IP/FQDN.       |:func:`set_server`                            |
        |                                           |                                  |:func:`peek_server`                           |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | port                                      | The RADIUS server port.          |:func:`set_port`                              |
        |                                           |                                  |:func:`peek_port`                             |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | secret                                    | The secret between the switch    |:func:`set_secret`                            |
        |                                           | and the server.                  |:func:`peek_secret`                           |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | timeout                                   | The RADIUS server response       |:func:`set_timeout`                           |
        |                                           | timeout.                         |:func:`peek_timeout`                          |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | authentication                            | The authentication protocol.     |:func:`set_authentication`                    |
        |                                           |                                  |:func:`peek_authentication`                   |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | encryption-type                           | The encryption type.             |:func:`set_encryption_type`                   |
        |                                           |                                  |:func:`peek_encryption_type`                  |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | position                                  | The RADIUS server position.      |:func:`set_position`                          |
        |                                           |                                  |:func:`peek_position`                         |
        +-------------------------------------------+----------------------------------+----------------------------------------------+

    *Object Methods*

        .. staticmethod:: get(session, name=None)

            Returnss a :class:`radius_server` object with the RADIUS server
                                            attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by the \
                :func:`pyfos_auth.login`.
            :rtype: The :class:`radius_server` object, if a name is provided, \
                     or a list of objects if there is more than one. \
                     A dictionary in case of error.

        .. method:: post(session)

            Creates a RADIUS server entry. The required fields are set
            within the object using the attribute's set method.
            This method is used to create a new RADIUS server configuration for
            AAA authentication to a switch.

            Example Usage of the Method to Configure a New AAA RADIUS Server:

            .. code-block:: python

                # initialize the switch object
                radius_obj = pyfos_brocade_security.radius_server()
                # set the server FQDN/ip
                radius_obj.set_server("10.70.12.115")
                # execute HTTP post command to apply the object to the
                # switch connected through session
                radius_obj.post(session)

            :param session: The session handler returned by the \
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

        .. method:: patch(session)

            Edits an existing configuration. The required fields are set within
            the object using the attribute's set method. This method is used to
            modify the existing RADIUS server configuration.

            Example Usage of the Method to Configure Response Timeout:

            .. code-block:: python

                # initialize the switch object
                radius_info = pyfos_brocade_security.radius_server()
                # set the server FQDN/ip
                radius_info.set_server(name)
                # set the response timeout 10
                radius_info.set_timeout(10)
                # execute HTTP patch command to apply the object to the
                # switch connected through session
                radius_info.patch(session)

            *Below is an Example of Combining Object Initialization \
                    and Attribute Sets:*

            .. code-block:: python

                # set the payload
                radius_info = pyfos_brocade_security.radius_server(
                    {"server" : 10.70.12.115,
                    "timeout" : 10})
                result = radius_info.patch(session)
                pyfos_util.response_print(result)

            :param session: The session handler returned by the \
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

        .. method:: delete(session)

            Deletes a RADIUS server entry. The required fields are
            set within the object using attribute's
            set method. This method is used to delete a RADIUS server
            configuration.

            Example Usage of the Method to Delete a RADIUS Configuration:

            .. code-block:: python

                # initialize the switch object
                radius_obj = pyfos_brocade_security.radius_server()
                # set the server FQDN/ip
                radius_obj.set_server("10.70.12.115")
                # execute HTTP delete command to apply the object to the
                # switch connected through session
                radius_obj.delete(session)

    *Attribute Methods*

        .. method:: set_server(name)

            Sets the RADIUS server name in the object.

            :param name: The RADIUS server FQDN/IP to be set within the object
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_server()

            Reads the RADIUS server from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_port(number)

            Sets the RADIUS server port number in the object.

            :param number: The RADIUS server port number to be set within the
                           object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_port()

            Reads the RADIUS server port number from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_secret(secret)

            Sets the RADIUS server secret in the object.

            :param secret: The RADIUS server secret to be set within the object
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_secret()

            Reads the RADIUS server secret from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_timeout(value)

            Sets the RADIUS server response timeout value in the object.

            :param value: The RADIUS server timeout value to be set within the
                          object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_timeout()

            Reads the RADIUS server timeout from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_authentication(protocol)

            Sets the RADIUS server authentication protocol type in the object.

            :param protocol: The RADIUS server authentication protocol type \
                          to be set within the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_authentication()

            Reads the RADIUS server authentication protocol type from the
            object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_encryption_type(encrypt)

            Sets the RADIUS server encryption type in the object.

            :param encrypt: The RADIUS server encryption type to be set within
                            the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_encryption_type()

            Reads the RADIUS server encryption type from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_position(pos)

            Sets the RADIUS server position in the object.

            :param pos: The RADIUS server position to be set within
                            the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_position()

            Reads the RADIUS server position from the object.

            :rtype: A dictionary in case of error or a success response.

        """
    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.radius_server,
                         "/rest/running/brocade-security/radius-server",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "server", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "port", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "secret", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "timeout", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "authentication", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "encryption-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "position", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class tacacs_server(pyfos_rest_util.rest_object):
    """This class is used to add, change, read, and delete an AAA
       TACACS+ server configuration.

    Important Class Members:

        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | Attribute Name                            | Description                      |Frequently Used Methods                       |
        +===========================================+==================================+==============================================+
        | server                                    | The TACACS+ server IP/FQDN.      |:func:`set_server`                            |
        |                                           |                                  |:func:`peek_server`                           |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | port                                      | The TACACS+ server port.         |:func:`set_port`                              |
        |                                           |                                  |:func:`peek_port`                             |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | secret                                    | The secret between the switch    |:func:`set_secret`                            |
        |                                           | and the server.                  |:func:`peek_secret`                           |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | timeout                                   | The TACACS+ server response      |:func:`set_timeout`                           |
        |                                           | timeout.                         |:func:`peek_timeout`                          |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | authentication                            | The authentication protocol.     |:func:`set_authentication`                    |
        |                                           |                                  |:func:`peek_authentication`                   |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | encryption-type                           | The encryption type.             |:func:`set_encryption_type`                   |
        |                                           |                                  |:func:`peek_encryption_type`                  |
        +-------------------------------------------+----------------------------------+----------------------------------------------+
        | position                                  | The TACACS+ server position.     |:func:`set_position`                          |
        |                                           |                                  |:func:`peek_position`                         |
        +-------------------------------------------+----------------------------------+----------------------------------------------+

    *Object Methods*

        .. staticmethod:: get(session, name=None)

            Returns a :class:`tacacs_server` object with TACACS+ Server
            attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: The :class:`tacacs_server` object, if name is provided, \
                or a list of objects if there is more than one. \
                A dictionary in case of error.

        .. method:: post(session)

            Creates a TACACS+ server entry. The required fields are set
            within the object using the attribute's set method.
            This method is used to create a new TACACS+ server configuration
            for AAA authentication to the switch.

            Example Usage of the Method to Configure a New AAA TACACS+ Server:

            .. code-block:: python

                # initialize the switch object
                tacacs_obj = pyfos_brocade_security.tacacs_server()
                # set the server FQDN/ip
                tacacs_obj.set_server("10.70.12.115")
                # execute HTTP post command to apply the object to the
                # switch connected through session
                tacacs_obj.post(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

        .. method:: patch(session)

            Edits an existing configuration. The required fields are set within
            the object using the attribute's set method. This method is used \
            to modify an existing TACACS+ server configuration.

            Example Usage of the Method to Configure a Response Timeout:

            .. code-block:: python

                # initialize the switch object
                tacacs_info = pyfos_brocade_security.tacacs_server()
                # set the server FQDN/ip
                tacacs_info.set_server(name)
                # set the response timeout 10
                tacacs_info.set_timeout(10)
                # execute HTTP patch command to apply the object to the
                # switch connected through session
                tacacs_info.patch(session)

            *Below is an Example of Combining Object Initialization \
                    and Attribute Sets:*

            .. code-block:: python

                # set the payload
                tacacs_info = pyfos_brocade_security.tacacs_server(
                    {"server" : 10.70.12.115,
                    "timeout" : 10})
                result = tacacs_info.patch(session)
                pyfos_util.response_print(result)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

        .. method:: delete(session)

            Deletes a TACACS+ server entry. The required fields are
            set within the object using the attribute's set method. \
            This method is used to delete a TACACS+ server configuration.

            Example Usage of the Method to Delete an TACACS+ Configuration:

            .. code-block:: python

                # initialize the switch object
                tacacs_obj = pyfos_brocade_security.tacacs_server()
                # set the server FQDN/ip
                tacacs_obj.set_server("10.70.12.115")
                # execute HTTP delete command to apply the object to the
                # switch connected through session
                tacacs_obj.delete(session)

    *Attribute Methods*

        .. method:: set_server(name)

            Sets the TACACS+ name in the object.

            :param name: The TACACS+ FQDN/IP to be set within the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_server()

            Reads the TACACS+ server from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_port(number)

            Sets The TACACS+ server port number in the object.

            :param number: The TACACS+ server port number to be set within the
                           object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_port()

            Reads the TACACS+ server port number from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_secret(secret)

            Sets the TACACS+ server secret in the object.

            :param secret: The TACACS+ server secret to be set within \
                           the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_secret()

            Reads the TACACS+ server secret from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_timeout(value)

            Sets the TACACS+ server response timeout value in the object.

            :param value: The TACACS+ server timeout value to be set within the
                          object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_timeout()

            Reads the TACACS+ server timeout from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_authentication(protocol)

            Sets the TACACS+ server authentication protocol type in the object.

            :param protocol: The TACACS+ server authentication protocol type \
                          to be set within the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_authentication()

            Reads the TACACS+ server authentication protocol type from the
            object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_encryption_type(encrypt)

            Sets the TACACS+ server encryption type in the object.

            :param encrypt: The TACACS+ server encryption type to be set within
                            the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_encryption_type()

            Reads the TACACS+ server encryption type from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_position(pos)

            Sets the TACACS+ server position in the object.

            :param pos: The TACACS+ server position to be set within
                            the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_position()

            Reads the TACACS+ server position from the object.

            :rtype: A dictionary in case of error or a success response.

        """
    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.tacacs_server,
                         "/rest/running/brocade-security/tacacs-server",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "server", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "port", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "secret", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "timeout", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "authentication", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "encryption-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "position", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class ldap_server(pyfos_rest_util.rest_object):
    """This class is used to add, change, read, and delete AAA
       LDAP server configuration.

    Important Class Members:

        +-------------------------------------------+----------------------------------+-------------------------------------------+
        | Attribute Name                            | Description                      |Frequently Used Methods                    |
        +===========================================+==================================+===========================================+
        | server                                    | The LDAP server IP/FQDN.         |:func:`set_server`                         |
        |                                           |                                  |:func:`peek_server`                        |
        +-------------------------------------------+----------------------------------+-------------------------------------------+
        | port                                      | The LDAP server port.            |:func:`set_port`                           |
        |                                           |                                  |:func:`peek_port`                          |
        +-------------------------------------------+----------------------------------+-------------------------------------------+
        | timeout                                   | The LDAP server response         |:func:`set_timeout`                        |
        |                                           | timeout.                         |:func:`peek_timeout`                       |
        +-------------------------------------------+----------------------------------+-------------------------------------------+
        | domain                                    | The LDAP server domain name.     |:func:`set_domain`                         |
        |                                           |                                  |:func:`peek_domain`                        |
        +-------------------------------------------+----------------------------------+-------------------------------------------+
        | position                                  | The LDAP server position.        |:func:`set_position`                       |
        |                                           |                                  |:func:`peek_position`                      |
        +-------------------------------------------+----------------------------------+-------------------------------------------+
        | tls-mode                                  | The LDAP server TLS mode.        |:func:`set_tls_mode`                        |
        |                                           |                                  |:func:`peek_tls_mode`                       |
        +-------------------------------------------+----------------------------------+-------------------------------------------+

    *Object Methods*

        .. staticmethod:: get(session, name=None)

            Returns a :class:`ldap_server` object with LDAP Server
                             attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: The :class:`ldap_server` object, if a name is provided, \
                or a list of objects if there is more than one. \
                A dictionary in case of error.

        .. method:: post(session)

            Creates an LDAP server entry. The required fields are set
            within the object using the attribute's set method.
            This method is used to create a new LDAP server configuration for
            AAA authentication to the switch.

            Example Usage of the Method to Configure a New AAA LDAP Server:

            .. code-block:: python

                # initialize the switch object
                ldap_obj = pyfos_brocade_security.ldap_server()
                # set the server FQDN/ip
                ldap_obj.set_server("10.70.12.115")
                # execute HTTP post command to apply the object to the
                # switch connected through session
                ldap_obj.post(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

        .. method:: patch(session)

            Edits an existing configuration. The required fields are set within
            the object using the attribute's set method. This method is used to
            modify the existing LDAP server configuration.

            Example Usage of the Method to Configure the Response Timeout:

            .. code-block:: python

                # initialize the switch object
                ldap_info = pyfos_brocade_security.ldap_server()
                # set the server FQDN/ip
                ldap_info.set_server(name)
                # set the response timeout 10
                ldap_info.set_timeout(10)
                # execute HTTP patch command to apply the object to the
                # switch connected through session
                ldap_info.patch(session)

            *Below is an Example of Combining Object Initialization \
                    and Attribute Sets:*

            .. code-block:: python

                # set the payload
                ldap_info = pyfos_brocade_security.ldap_server(
                    {"server" : 10.70.12.115,
                    "timeout" : 10})
                result = ldap_info.patch(session)
                pyfos_util.response_print(result)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

        .. method:: delete(session)

            Deletes an LDAP server entry. The required fields are
            set within the object using the attribute's
            set method. This method is used to delete an LDAP server
            configuration.

            Example Usage of the Method to Delete an LDAP Configuration:

            .. code-block:: python

                # initialize the switch object
                ldap_obj = pyfos_brocade_security.ldap_server()
                # set the server FQDN/ip
                ldap_obj.set_server("10.70.12.115")
                # execute HTTP delete command to apply the object to the
                # switch connected through session
                ldap_obj.delete(session)

    *Attribute Methods*

        .. method:: set_server(name)

            Sets the LDAP name in the object.

            :param name: The LDAP FQDN/IP to be set within the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_server()

            Reads the LDAP server from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_port(number)

            Sets the LDAP server port number in the object.

            :param number: The LDAP server port number to be set within \
                            the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_port()

            Reads the LDAP server port number from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_timeout(value)

            Sets the LDAP server response timeout value in the object.

            :param value: The LDAP server timeout value to be set within \
                          the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_timeout()

            Reads the LDAP server timeout from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_domain(domain)

            Sets the LDAP server domain name in the object.

            :param domain: The LDAP server domain name to be set within \
                           the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_domain()

            Reads the LDAP server domain name from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_position(pos)

            Sets the LDAP server position in the object.

            :param pos: The LDAP server position to be set within the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_position()

            Reads the LDAP server position from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_tls_mode(tls_mode)

            Sets the LDAP server TLS mode in the object.

            :param tls_mode: The LDAP server TLS mode to be set within the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_tls_mode()

            Reads the LDAP server TLS mode from the object.

            :rtype: A dictionary in case of error or a success response.

        """
    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.ldap_server,
                         "/rest/running/brocade-security/ldap-server",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "server", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "port", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "domain", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "timeout", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "position", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "tls-mode", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class auth_spec(pyfos_rest_util.rest_object):
    """This class configures the authentication mode and displays
       the authentication mode configuration.

    Important Class Members:

        +-------------------------------------------+----------------------------------+------------------------------------------------------+
        | Attribute Name                            | Description                      |Frequently Used Methods                               |
        +===========================================+==================================+======================================================+
        | authentication-mode                       | The authentication mode for      |:func:`set_authentication_mode`                       |
        |                                           | RADIUS, TACACS+, and LDAP.       |:func:`peek_authentication_mode`                      |
        +-------------------------------------------+----------------------------------+------------------------------------------------------+
        | activate-no-log-out                       | A change in the authentication   |:func:`set_activate_no_log_out`                       |
        |                                           | mechanism.                       |:func:`peek_activate_no_log_out`                      |
        +-------------------------------------------+----------------------------------+------------------------------------------------------+
        | primary-auth-log-messages                 | The log messages for             |:func:`set_primary_auth_log_messages`                 |
        |                                           | authentication failure.          |:func:`peek_primary_auth_log_messages`                |
        +-------------------------------------------+----------------------------------+------------------------------------------------------+

    *Object Methods*

        .. staticmethod:: get(session, name=None)

            Returns a :class:`auth_spec` object with authentication
                             configuration attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: The :class:`auth_spec` object or dictionary in case \
                     of error.

        .. method:: patch(session)

            Replaces an existing configuration authentication mode.
            The required fields are set within the object using the attribute's
            set method. This method is used to modify the existing
            authentication mode configuration.

            Example Usage of the Method to Configure the Response radiuslocal:

            .. code-block:: python

                # initialize the switch object
                server_info = pyfos_brocade_security.auth_spec()
                # set the mode of authentication
                server_info.set_authentication_mode("radiuslocal")
                # execute HTTP patch command to apply the object to the
                # switch connected through session
                server_info.patch(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

    *Attribute Methods*

        .. method:: set_authentication_mode(mode)

            Sets the authentication mode in the object.

            :param mode: The authentication mode to be set within the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_authentication_mode()

            Reads the authentication mode from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_activate_no_log_out(bool)

            Sets the authentication mechanism to enable or disable in \
             the object.

            :param bool: The authentication mechanism to be set within \
                         the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_activate_no_log_out()

            Reads the authentication mechanism from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_primary_auth_log_messages(bool)

            Enables or disables log messages in the object.

            :param bool: The log message enabled or disabled within \
                          the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_primary_auth_log_messages()

            Reads the log message status from the object.

            :rtype: A dictionary in case of error or a success response.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.auth_spec,
                         "/rest/running/brocade-security/auth-spec",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "authentication-mode", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "activate-no-log-out", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "primary-auth-log-messages", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class ipfilter_policy(pyfos_rest_util.rest_object):
    """This class provides the ipfilter policy information and also can
       configure the ipfilter policies.

    Important Class Members:

        +-------------------------------------------+----------------------------------+----------------------------------------------------------+
        | Attribute Name                            | Description                      |Frequently Used Methods                                   |
        +===========================================+==================================+==========================================================+
        | name                                      | The policy name.                 |:func:`set_name`                                          |
        |                                           |                                  |:func:`peek_name`                                         |
        +-------------------------------------------+----------------------------------+----------------------------------------------------------+
        | ip-version                                | The policy IP version            |:func:`set_ip_version`                                    |
        |                                           |  (IPv4/IPv6).                    |:func:`peek_ip_version`                                   |
        +-------------------------------------------+----------------------------------+----------------------------------------------------------+
        | is-policy-active                          | Indicates the status of          |:func:`peek_is_policy_active`                             |
        |                                           | the policy (Active/Defined).     |                                                          |
        +-------------------------------------------+----------------------------------+----------------------------------------------------------+
        | is-default-policy                         | Indicates the default or user    |:func:`peek_is_default_policy`                            |
        |                                           | defined policy.                  |                                                          |
        +-------------------------------------------+----------------------------------+----------------------------------------------------------+
        | action                                    | The IPfilter action (commit,     |:func:`set_action`                                        |
        |                                           | save, activate, and clone).      |                                                          |
        +-------------------------------------------+----------------------------------+----------------------------------------------------------+
        | clone-destination-policy-name             | The destination policy name when |:func:`set_clone_destination_policy_name`                 |
        |                                           | using the clone action.          |:func:`peek_clone_destination_policy_name`                |
        +-------------------------------------------+----------------------------------+----------------------------------------------------------+

    *Object Methods*

        .. staticmethod:: get(session)

            Returns a :class:`ipfilter_policy` object with the IPfilter
                             policy attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes are accessed through peek methods.

            Example Usage of the Method to Get IP Filter Policies:

            .. code-block:: python

               # initialize the switch object
               ipfilter_obj=pyfos_brocade_security.ipfilter_policy.get(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: The :class:`ipfilter_policy` object if a name is given or \
                a list of objects if there are more than one. A dictionary in \
                case of error.

        .. method:: post(session)

            Creates an IP filter policy entry. The required fields are set
            within the object using attribute's set method.
            This method is used to create a new IP filter policy configuration.

            Example Usage of the Method to Configure a New IP filter Policy:

            .. code-block:: python

                # initialize the switch object
                ipfilter_obj = pyfos_brocade_security.ipfilter_policy()
                # set the policy name
                ipfilter_obj.set_name("mypolicy")
                # set the ip version
                ipfilter_obj.set_ip_version("IPv4")
                # execute HTTP post command to apply the object to the
                # switch connected through session
                ipfilter_obj.post(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

        .. method:: patch(session)

            The required fields are set within the object using attribute's set
            method. This method is used to perform actions such as commit,
            save, activate the policy, and clone.

            Example Usage of the Method to Clone an IP Filter Policy:

            .. code-block:: python

                # initialize the switch object
                ipfilter_info = pyfos_brocade_security.ipfilter_policy()
                # set the action to perform
                ipfilter_info.set_action("clone")
                # set the source policy name
                ipfilter_info.set_name("default_ipv4")
                # set the destination policy name
                ipfilter_info.set_clone_destination_policy_name("myclone")
                # execute HTTP patch command to apply the object to the
                # switch connected through session
                ipfilter_info.patch(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

        .. method:: delete(session)

            Deletes an IP filter policy. The required fields are
            set within the object using attribute's
            set method. This method is used to delete an IP filter policy
            configuration.

            Example Usage of the Method to Delete an IP Filter Policy
            configuration:

            .. code-block:: python

                # initialize the switch object
                ipfilter_obj = pyfos_brocade_security.ipfilter_policy()
                # set the policy name to delete
                ipfilter_obj.set_name("mypolicy")
                # execute HTTP delete command to apply the object to the
                # switch connected through session
                ipfilter_obj.delete(session)

    *Attribute Methods*

        .. method:: set_name(name)

            Sets policy name in the object.

            :param name: The policy name to be set within the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_name()

            Reads the IP filter policy name from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_ip_version(version)

            Sets the policy IP version in the object.

            :param version: The policy IP version (IPv4/IPv6) to be set within \
                            the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_ip_version()

            Reads the policy IP version from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_is_policy_active()

            Reads the status of the policy from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_is_default_policy()

            Reads whether it is a default or user-defined policy from \
            the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_action(ops)

            Sets the action to perform in the object.

            :param ops: The IP filter action to be set within the object
                   supported operations: clone, save, activate and
                   commit-and-activate.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_clone_destination_policy_name("myclone")

            Sets the destination policy name for the clone action in \
            the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_clone_destination_policy_name()

            Reads the destination policy name from the object.

            :rtype: A dictionary in case of error or a success response.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.ipfilter_policy,
                         "/rest/running/brocade-security/ipfilter-policy",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "ip-version", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "is-policy-active", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "is-default-policy", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "action", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "clone-destination-policy-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class ipfilter_rule(pyfos_rest_util.rest_object):
    """This class provides the IP filter rule information and also can configure
       an IP filter rule.

    Important Class Members:

        +-------------------------------------------+----------------------------------+----------------------------------------------------+
        | Attribute Name                            | Description                      |Frequently Used Methods                             |
        +===========================================+==================================+====================================================+
        | policy-name                               | The policy name.                 |:func:`set_policy_name`                             |
        |                                           |                                  |:func:`peek_policy_name`                            |
        +-------------------------------------------+----------------------------------+----------------------------------------------------+
        | index                                     | The rule number.                 |:func:`set_index`                                   |
        |                                           |                                  |:func:`peek_index`                                  |
        +-------------------------------------------+----------------------------------+----------------------------------------------------+
        | source-ip                                 | The source IP address.           |:func:`set_source_ip`                               |
        |                                           |                                  |:func:`peek_source_ip`                              |
        +-------------------------------------------+----------------------------------+----------------------------------------------------+
        | destination-start-port                    | The destination start port.      |:func:`set_destination_start_port`                  |
        |                                           |                                  |:func:`peek_destination_start_port`                 |
        +-------------------------------------------+----------------------------------+----------------------------------------------------+
        | destination-end-port                      | The destination end port.        |:func:`set_destination_end_port`                    |
        |                                           |                                  |:func:`peek_destination_end_port`                   |
        +-------------------------------------------+----------------------------------+----------------------------------------------------+
        | protocol                                  | The protocol type.               |:func:`set_protocol`                                |
        |                                           |                                  |:func:`peek_protocol`                               |
        +-------------------------------------------+----------------------------------+----------------------------------------------------+
        | permission                                | The permission (permitor deny).  |:func:`set_permission`                              |
        |                                           |                                  |:func:`peek_permission`                             |
        +-------------------------------------------+----------------------------------+----------------------------------------------------+
        | traffic-type                              | The traffic type (INPUT          |:func:`set_traffic_type`                            |
        |                                           | or FORWARD).                     |:func:`peek_traffic_type`                           |
        +-------------------------------------------+----------------------------------+----------------------------------------------------+
        | destination-ip                            | The destination IP address.      |:func:`set_destination_ip`                          |
        |                                           |                                  |:func:`peek_destination_ip`                         |
        +-------------------------------------------+----------------------------------+----------------------------------------------------+

    *Object Methods*

        .. staticmethod:: get(session, name=None)

            Returns a :class:`ipfilter_rule` object filled with IP filter
                             rule attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A :class:`ipfilter_rule` object or a dictionary in case of
                            error.

        .. method:: post(session)

            Creates an IP filter rule entry. The required fields are set
            within the object using attribute's set method.
            This method is used to create a new IP filter rule.

            Example Usage of the Method to Configure a New IP Filter Rule:

            .. code-block:: python

                # initialize the switch object
                ipfilter_obj = pyfos_brocade_security.ipfilter_rule()
                # set the policy name
                ipfilter_obj.set_policy_name("mypolicy")
                # set the ip version
                ipfilter_obj.set_index(1)
                ipfilter_obj.set_source_ip(1.1.1.1)
                ipfilter_obj.set_destination_start_port(23)
                ipfilter_obj.set_protocol(tcp)
                ipfilter_obj.set_permission("permit")
                # execute HTTP post command to apply the object to the
                # switch connected through session
                ipfilter_obj.post(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

        .. method:: delete(session)

            Deletes an IP filter rule. The required fields are
            set within the object using attribute's
            set method. This method is used to delete an IP filter rule
            configuration.

            Example Usage of the Method to Delete an IP Filter Rule
            configuration:

            .. code-block:: python

                # initialize the switch object
                ipfilter_obj = pyfos_brocade_security.ipfilter_rule()
                # set the policy name to delete
                ipfilter_obj.set_policy_name("mypolicy")
                ipfilter_obj.set_index(1)
                # execute HTTP delete command to apply the object to the
                # switch connected through session
                ipfilter_obj.delete(session)

    *Attribute Methods*

        .. method:: set_policy_name(name)

            Sets the policy name in the object.

            :param name: The policy name to be set within the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_policy_name()

            Reads the IP filter policy from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_index(index)

            Sets the rule number in the object.

            :param index: The rule number to be set within the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_index()

            Reads the rule number from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_source_ip(ip)

            Sets the source IP address in the object.

            :param ip: The source IP address to be set within the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_source_ip()

            Reads the source IP address from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_destination_start_port(port)

            Sets the destination start port in the object.

            :param port: The destination start port to be set within \
                         the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_destination_start_port()

            Reads the destination start port from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_destination_end_port(port)

            Sets the destination end port in the object.

            :param port: The destination end port to be set within the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_destination_end_port()

            Reads the destination end port from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_protocol(type)

            Sets the protocol type in the object.

            :param type: The protocol type to be set within the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_protocol()

            Reads the protocol type from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_permission(type)

            Sets the permission type in the object.

            :param type: The permission type to be set within the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_permission()

            Reads the permission type from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_traffic_type(type)

            Sets the traffic type in the object.

            :param type: The traffic type to be set within the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_traffic_type()

            Reads the traffic type from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_destination_ip(ip)

            Sets the destination IP address in the object.

            :param ip: The destination IP address to be set within the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_destination_ip()

            Reads the destination IP address from the object.

            :rtype: A dictionary in case of error or a success response.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.ipfilter_rule,
                         "/rest/running/brocade-security/ipfilter-rule",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "policy-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "index", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "source-ip", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "destination-start-port", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "destination-end-port", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "protocol", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "permission", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "traffic-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "destination-ip", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class sec_crypto_cfg(pyfos_rest_util.rest_object):
    """Class to display active cryptographic configurations.

    Important Class Members:

        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+
        | Attribute Name                                 | Description                      |Frequently Used Methods                                              |
        +================================================+==================================+=====================================================================+
        | ssh-cipher                                     | The SSH cipher configuration.    |:func:`peek_ssh_cipher`                                              |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+
        | ssh-kex                                        | The SSH kex configuration.       |:func:`peek_ssh_kex`                                                 |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+
        | ssh-mac                                        | The SSH mac configuration.       |:func:`peek_ssh_mac`                                                 |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+
        | https-cipher                                   | The HTTPS cipher configuration.  |:func:`peek_https_cipher`                                            |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+
        | radius-cipher                                  | The RADIUS cipher configuration. |:func:`peek_radius_cipher`                                           |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+
        | ldap-cipher                                    | The LDAP cipher configuration.   |:func:`peek_ldap_cipher`                                             |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+
        | syslog-cipher                                  | The Syslog cipher configuration. |:func:`peek_syslog_cipher`                                           |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+
        | https-tls-protocol                             | The TLS Protocol version         |:func:`peek_ttps_tls_protocol`                                       |
        |                                                | for HTTPS.                       |                                                                     |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+
        | radius-tls-protocol                            | The TLS protocol version         |:func:`peek_radius_tls_protocol`                                     |
        |                                                | for RADIUS.                      |                                                                     |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+
        | ldap-tls-protocol                              | The TLS protocol version for     |:func:`peek_ldap_tls_protocol`                                       |
        |                                                | for LDAP.                        |                                                                     |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+
        | syslog-tls-protocol                            | The TLS protocol version         |:func:`peek_syslog_tls_protocol`                                     |
        |                                                | for SYSLOG.                      |                                                                     |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+
        | x509v3-validation-mode                         | The X509 validation mode         |:func:`peek_x509v3_validation_mode`                                  |
        |                                                | selection.                       |                                                                     |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+

    *Object Methods*

        .. staticmethod:: get()

            Returns a :class:`sec_crypto_cfg` object filled with cryptographic
                      attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A :class:`sec_crypto_cfg` object or a dictionary in case of
                            error.

    *Attribute Methods*

        .. method:: peek_ssh_cipher()

            Reads the SSH cipher algorithm from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_ssh_kex()

            Reads the SSH kex algorithm from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_ssh_mac()

            Reads the SSH MAC algorithm from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_https_cipher()

            Reads the https cipher algorithm from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_radius_cipher()

            Reads the RADIUS cipher algorithm from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_ldap_cipher()

            Reads the LDAP cipher algorithm from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_syslog_cipher()

            Reads the syslog cipher algorithm from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_https_tls_protocol()

            Reads the TLS protocol version for https from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_radius_tls_protocol()

            Reads the TLS protocol version for RADIUS from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_ldap_tls_protocol()

            Reads the TLS protocol version for LDAP from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_syslog_tls_protocol()

            Reads the TLS protocol version for syslog from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_x509v3_validation_mode()

            Reads the X509 validation mode selection from the object.

            :rtype: A dictionary in case of error or a success response.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.sec_crypto_cfg,
                         "/rest/running/brocade-security/sec-crypto-cfg",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "ssh-cipher", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "ssh-kex", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "ssh-mac", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "https-cipher", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "radius-cipher", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "ldap-cipher", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "syslog-cipher", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "https-tls-protocol", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "radius-tls-protocol", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "ldap-tls-protocol", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "syslog-tls-protocol", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "x509v3-validation-mode", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.load(dictvalues, 1)


class sec_crypto_cfg_template(pyfos_rest_util.rest_object):
    """Class for cryptographic template display.

    Important Class Members:

        +------------------------------------------------+----------------------------------+--------------------------------------------------------+
        | Attribute Name                                 | Description                      |Frequently Used Methods                                 |
        +================================================+==================================+========================================================+
        | name                                           | The template name.               |:func:`peek_name`                                       |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------+
        | template                                       | The template content.            |:func:`peek_template`                                   |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------+

    *Object Methods*

        .. staticmethod:: get(session, name=None)
            Returns a :class:`sec_crypto_cfg_template` object filled with
                             template contents.

            Each object can be printed using :func:`pyfos_util.response_print`.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A :class:`sec_crypto_cfg_template` object if name is given
               or list of objects if name is None.
               A dictionary in case of error.

    *Attribute Methods*
        .. method:: peek_name()

            Reads the template name from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_template()

            Reads the template content from the object.

            :rtype: A dictionary in case of error or a success response.
    """
    def __init__(self, dictvalues={}):
        super().__init__(
            pyfos_rest_util.rest_obj_type.sec_crypto_cfg_template,
            "/rest/running/brocade-security/sec-crypto-cfg-template",
            version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "template", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.load(dictvalues, 1)


class sec_crypto_cfg_template_action(pyfos_rest_util.rest_object):
    """ This class provides the cryptographic template configurations and
       operations.

    Important Class Members:

        +------------------------------------------------+----------------------------------+--------------------------------------------------------+
        | Attribute Name                                 | Description                      |Frequently Used Methods                                 |
        +================================================+==================================+========================================================+
        | template-name                                  | The template name.               |:func:`set_template_name`                               |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------+
        | action                                         | Sets the crypto action.          |:func:`set_action`                                      |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-user-name                               | Sets the remote user login name. |:func:`set_remote_user_name`                            |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-host-ip                                 | Sets the remote host IP address. |:func:`set_remote_host_ip`                              |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-user-password                           | Sets the remote user password.   |:func:`set_remote_user_password`                        |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-directory                               | The remote directory file path.  |:func:`set_remote_directory`                            |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------+
        | file-transfer-protocol-type                    | Sets the file transfer           |:func:`set_file_transfer_protocol_type`                 |
        |                                                | protocol type.                   |                                                        |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------+

    *Object Methods*

        .. method:: patch(session)

            The required fields are set within the object using attribute's
            set method. This method is used to set the import or export  \
            cryptographic template, which is configured in the host machine, \
            verify and apply template.

            Example Usage of the Method to Apply Cipher Configuration:

            .. code-block:: python

                # initialize the switch object
                crypto_info = pyfos_brocade_security.sec_crypto_cfg_template()
                # set the action to perform
                crypto_info.set_action("apply")
                # set the template name
                crypto_info.set_template_name("default_generic")
                # execute HTTP patch command to apply the object to the
                # switch connected through session
                crypto_info.patch(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

        .. method:: delete(session)

            Deletes a user-defined template. The required fields are
            set within the object using attribute's set method.
            This command is used to delete a user-defined template.

            Example Usage of the Method to Delete a User-defined Template:

                # initialize the switch object
                crypto_obj = pyfos_brocade_security.sec_crypto_cfg_template()
                # set the template name
                crypto_obj.set_template_name("mytemplate")
                crypto_obj.delete(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

    *Attribute Methods*

        .. method:: set_template_name(name)

            Sets the template  name in the object.

            :param name: The default template name to be set within the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: set_action(ops)

            Sets the seccryptographic action in the object.

            :param ops: The seccryptographic action to be set within \
                        the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: set_remote_user_name(loginname)

            Sets the remote user login name in the object.

            :param loginname: The remote user login name name to be set \
                              within the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: set_remote_host_ip(ip)

            Sets the remote user IP address in the object.

            :param ip: The remote user IP address to be set within the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: set_remote_user_password(passwd)

            Sets the remote user password in the object.

            :param passwd: The remote user password to be set within \
                           the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: set_remote_directory(template_file)

            Sets the template file path in the object.

            :param template_file: The template file path to be set within \
                                  the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: set_file_transfer_protocol_type(protocol)

            Sets the file transfer protocol in the object.

            :param protocol: The file transfer protocol to be set within \
                             the object.
            :rtype: A dictionary in case of error or a success response.

        """

    def __init__(self, dictvalues={}):
        super().__init__(
            pyfos_rest_util.rest_obj_type.sec_crypto_cfg_template_action,
            "/rest/running/brocade-security/sec-crypto-cfg-template-action",
            version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "template-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "action", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "remote-user-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "remote-host-ip", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "remote-user-password", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "remote-directory", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "file-transfer-protocol-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class ldap_role_map(pyfos_rest_util.rest_object):
    """Class of LDAP Role mapping configuration.

    Important Class Members:

        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | Attribute Name                    | Description                   |Frequently Used Methods                                |
        +===================================+===============================+=======================================================+
        | ldap-role                         | The LDAP role to be mapped    |:func:`set_ldap_role`                                  |
        |                                   | to a switch role.             |:func:`peek_ldap_role`                                 |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | switch-role                       | The switch role to which the  |:func:`set_switch_role`                                |
        |                                   | LDAP role is mapped.          |:func:`peek_switch_role`                               |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | home-virtual-fabric               | The home VF ID.               |:func:`set_home_virtual_fabric`                        |
        |                                   |                               |:func:`peek_home_virtual_fabric`                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | chassis-access-role               | The chassis-level role.       |:func:`set_chassis_access_role`                        |
        |                                   |                               |:func:`peek_chassis_access_role`                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+

    *Object Methods*

        .. method:: get(session)

            Returns a :class`ldap_role_map`
            object with values for all the attributes.
            The object can be printed using :func:`pyfos_utils.response_print`.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or an
                :class:`ldap_role_map` object.

        .. method:: post(session)

            Creates an entry. The required fields are set within the object \
            using attribute's set method.  This command is used to create
            an ldap_map_role.

            Example Usage of the Method to Create a New Configuration::

                ldap_cfg_obj =
                    pyfos_ldapcfg.ldap_role_map()
                ldap_cfg_obj.set_ldap_role("ldapRole")
                ldap_cfg_obj.set_switch_role("switchRole")
                ldap_cfg_obj.post(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

        .. method:: patch()

            Modifies an LDAP configuration such as vf-list, vf-role-list, \
            and so on. The required fields are set within the object using
            the attribute's set method.

            Example Usage of the Method to Modify an Existing LDAP \
            Role Configuration::

                ldap_cfg_obj =
                    pyfos_ldapcfg.ldap_role_map()
                ldap_cfg_obj.set_ldap_role("ldapRole")
                ldap_cfg_obj.set_chassis_access_role("admin")
                ldap_cfg_obj.set_home_virtual_fabric(128)
                ldap_cfg_obj.patch(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

        .. method:: delete()

            Deletes an LDAP role mapping. The required fields are
            set within the object using attribute's set method.
            This command is used to delete an LDAP role mapping.

            Example Usage of the Method to Delete an Existing LDAP Role Map::

               ldap_cfg_obj =
                    pyfos_ldapcfg.ldap_role_map()
                ldap_cfg_obj.set_ldap_role("ldapRole")
                ldap_cfg_obj.delete(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

    *Attribute Methods*

        .. method:: set_ldap_role(role)

           Sets the LDAP role in the object

            :param role: The LDAP role to be mapped to a switch role.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_ldap_role()

            Reads the LDAP role from the object.

            :rtype: None or ldap_role.

        .. method:: set_switch_role(role)

                Sets the switch role in the object.

            :param role: The switch role to which the LDAP role is mapped.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_switch_role()

            Reads the switch role from the object.

            :rtype: None or switch_role.

        .. method:: set_home_virtual_fabric(fcid)

                Sets the home virtual fabric in the object.

            :param fcid: The default virtual fabric switch context.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_home_virtual_fabric()

            Reads the home virtual fabric from the object.

            :rtype: None or home_virtual_fabric.

        .. method:: set_chassis_access_role(role)

                Sets the chassis access role in the object.

            :param role: The chassis level role.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_chassis_access_role()

            Reads the chassis access role from the object.

            :rtype: None or chassis_access_role.

       """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.ldap_role_map,
                         "/rest/running/brocade-security/ldap-role-map")

        self.add(pyfos_rest_util.rest_attribute(
            "ldap-role", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "switch-role", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "home-virtual-fabric", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "chassis-access-role", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class password_cfg(pyfos_rest_util.rest_object):
    """Class of password configuration.
                Important Class Members:

        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | Attribute Name                    | Description                   |Frequently Used Methods                                |
        +===================================+===============================+=======================================================+
        | minimum-length                    | The minimum length of the     |:func:`set_minimum_length`                             |
        |                                   | password.                     |:func:`peek_minimum_length`                            |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | character-set                     | The minimum criteria on the   |:func:`set_character_set`                              |
        |                                   | character set.                |:func:`peek_character_set`                             |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | user-name-allowed                 | Enable or disable username is |:func:`set_user_name_allowed`                          |
        |                                   | allowed in the password.      |:func:`peek_user_name_allowed`                         |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | minimum-lower-case-character      | The minimum number of         |:func:`set_minimum_lower_case_character`               |
        |                                   | lowercase alphabetic          |:func:`peek_minimum_lower_case_character`              |
        |                                   | characters.                   |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | minimum-upper-case-character      | The minimum number of         |:func:`set_minimum_upper_case_character`               |
        |                                   | uppercase alphabetic          |:func:`peek_minimum_upper_case_character`              |
        |                                   | characters.                   |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | minimum-numeric-character         | The minimum number of digits. |:func:`set_minimum_numeric_character`                  |
        |                                   |                               |:func:`peek_minimum_numeric_character`                 |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | minimum-special-character         | The minimum number of         |:func:`set_minimum_special_character`                  |
        |                                   | punctuation characters.       |:func:`peek_minimum_special_character`                 |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | past-password-history             | The number of past password   |:func:`set_past_password_history`                      |
        |                                   | values that are disallowed.   |:func:`peek_past_password_history`                     |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | minimum-password-age              | The minimum number of days    |:func:`set_minimum_password_age`                       |
        |                                   | before which a password       |:func:`peek_minimum_password_age`                      |
        |                                   | cannot be modified.           |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | maximum-password-age              | The maximum number of days    |:func:`set_maximum_password_age`                       |
        |                                   | after which the password      |:func:`peek_maximum_password_age`                      |
        |                                   | should be modified.           |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | warn-on-expire                    | The number of days prior to   |:func:`set_warn_on_expire`                             |
        |                                   | password expiration when the  |:func:`peek_warn_on_expire`                            |
        |                                   | user should be warned.        |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | lock-out-threshold                | The number of time user can   |:func:`set_lock_out_threshold`                         |
        |                                   | give the incorrect password.  |:func:`peek_lock_out_threshold`                        |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | lock-out-duration                 | The lockout duration          |:func:`set_lock_out_duration`                          |
        |                                   | in minutes.                   |:func:`peek_lock_out_duration`                         |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | admin-lock-out-enabled            | Enables or disables admin     |:func:`set_admin_lock_out_enabled`                     |
        |                                   | lockout.                      |:func:`peek_admin_lock_out_enabled`                    |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | repeat-character-limit            | The length of the character   |:func:`set_repeat_character_limit`                     |
        |                                   | sequences.                    |:func:`peek_repeat_character_limit`                    |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | sequence-character-limit          | The length of sequential      |:func:`set_sequence_character_limit`                   |
        |                                   | character sequences.          |:func:`peek_sequence_character_limit`                  |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | password-config-changed           | Indicates whether it is the   |:func:`peek_password_config_changed`                   |
        |                                   | account default               |                                                       |
        |                                   | configuration.                |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | reverse-user-name-allowed         | Allows or disallows the       |:func:`set_reverse_user_name_allowed`                  |
        |                                   | reverse username in           |:func:`peek_reverse_user_name_allowed`                 |
        |                                   | the password.                 |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | hash-type                         | The hash type.                |:func:`set_hash_type`                                  |
        |                                   |                               |:func:`peek_hash_type`                                 |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | manual-hash-enabled               | Enables or disables manual    |:func:`set_manual_hash_enabled`                        |
        |                                   | hash.                         |:func:`peek_manual_hash_enabled`                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | enforce-expire                    | Expires the password for      |:func:`set_enforce_expire`                             |
        |                                   | the user.                     |:func:`peek_enforce_expire`                            |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | minimum-difference                | The number of character       |:func:`set_minimum_difference`                         |
        |                                   | differences expected between  |:func:`peek_minimum_difference`                        |
        |                                   | the old and new password.     |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | password-action                   | The password configuration    |:func:`set_password_action`                            |
        |                                   | action.                       |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+

       *Object Methods*
        .. method:: get(session)

            Returns a :class`password_cfg`
            object with values for all the attributes.
            The object can be printed using :func:`pyfos_utils.response_print`.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a
                :class:`password_cfg` object.

        .. method:: patch()

            Modifies the password configuration.
            The required fields are set within the object using attribute's
            set method.

            Example Usage of the Method to Modify the Global Password
            Configuration::

                password_obj =
                    pyfos_password_cfg.password_cfg()
                password_obj.set_password_action("global-config")
                password_obj.set_minimum_length(10)
                password_obj.set_user_name_allowed(0)
                password_obj.patch(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

        .. method:: delete(session)

            Deletes a user-defined password configuration.
            The fields are set within the object using attribute's
            set method. This command is used to delete a \
            password configuration.

            Example Usage of the Method to Delete a Password Configuration::

                password_obj =
                    pyfos_password_cfg.password_cfg()
                password_obj.set_password_action("delete-all")
                password_obj.delete(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

       *Attribute Methods*

        .. method:: set_minimum_length(length)

                Sets the minimum length of the password in the object.

            :param length: The minimum length of the password.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_minimum_length()

            Reads the minimum length of the password from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_character_set(criteria)

                Sets the minimum criteria for the password of the object.

            :param criteria: The minimum criteria on the password.
            :rtype: A dictionary in case of error or a success response.

        .. method::peek_character_set()

            Reads the minimum criteria from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_minimum_length()

            Reads the minimum criteria from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_user_name_allowed(bool)

                Sets whether enabling or disabling the username is allowed on \
                the object.

            :param bool: Whether enabling or disabling the username is allowed.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_user_name_allowed()

            Reads whether the username is allowed in password from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_minimum_lower_case_character(number)

                Sets the minimum lowercase characters to the object.

            :param number: The minimum number of lowercase characters.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_minimum_lower_case_character()

            Reads the minimum number of lowercase characters from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_minimum_upper_case_character(number)

                Sets minimum uppercase character to the object

            :param number: minimum number of uppercase character
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_minimum_upper_case_character()

            Reads minimum number of uppercase character from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_minimum_numeric_character(number)

                Sets the minimum digits to the object.

            :param number: The minimum number of digits.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_minimum_numeric_character()

            Reads the minimum number of digits from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_minimum_special_character(number)

                Sets the minimum punctuation characters to the object.

            :param number: The minimum number of punctuation characters.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_minimum_special_character()

            Reads the minimum number of punctuation characters from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_past_password_history(number)

                Sets the number of past passwords disallowed to the object.

            :param number: The number of past passwords disallowed.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_past_password_history()

            Reads the number of past passwords disallowed from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_minimum_password_age(number)

                Sets the minimum number of days that must elapse before a \
                password can be changed.

            :param number: The minimum number of days that must elapse before \
                           a password can be changed.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_minimum_password_age()

            Reads the minimum number of days that must elapse before a \
            password can be changed.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_maximum_password_age(number)

                Sets the maximum number of days that can elapse before a \
                password can be changed.

            :param number: The maximum number of days that can elapse before \
                           a password can be changed.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_maximum_password_age()

            Reads the maximum number of days that can elapse before a \
            password can be changed.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_warn_on_expire(number)

                Sets the number of days prior to password expiration to \
                the object.

            :param number: The number of days prior to password expiration.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_warn_on_expire()

            Reads the number of days prior to password expiration from \
            the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_lock_out_threshold(times)

                Sets the number of times a user can specify an incorrect \
                password to the object.

            :param times: The number of times a user can specify an \
                          incorrect password.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_lock_out_threshold()

            Reads the number of times a user can specify an incorrect password
            from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_lock_out_duration(times)

                Sets the time, in minutes, after which a previously locked
                account automatically unlocks to the object.

            :param times: The time, in minutes, after which a previously locked
                          account automatically unlocks.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_lock_out_duration()

            Reads time, in minutes, after which a previously locked
            account automatically unlocks from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_admin_lock_out_enabled(bool)

                Enables or disables admin lockout to the object.

            :param bool: Enable or disable admin lockout.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_admin_lock_out_enabled()

            Reads the admin lockout status from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_repeat_character_limit(length)

                Sets the length of repeated character sequences to the object.

            :param length: The length of repeated character sequences.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_repeat_character_limit(length)

            Reads the length of repeated character sequences from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_sequence_character_limit(length)

                Sets the length of sequential character sequences to \
                the object.

            :param length: The length of sequential character sequences.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_sequence_character_limit()

            Reads the length of sequential character sequences from \
            the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_password_config_changed()

            Reads the status of the user-defined configuration or the default
            configuration from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_reverse_user_name_allowed(bool)

                Enables or disables use of reverse username in the password \
                to the object.

            :param bool: Enables or disables use of reverse username.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_reverse_user_name_allowed()

            Reads the status of reverse username allowed from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_hash_type(hash)

                Sets the hash type to the object.

            :param hash: The hash type for the password.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_hash_type()

            Reads the hash type from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_manual_hash_enabled(bool)

                Enables or disables manual hash to the object.

            :param bool: Enables or disables manual hash type change.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_manual_hash_enabled()

            Reads the status of the manual hash type change from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_enforce_expire(bool)

                Enables or disables password expiration for the user
                to the object.

            :param bool: Enables or disables password expiration.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_enforce_expire()

            Reads the status of password expiration for the user
            from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_password_action(ops)

                Sets the password action to be performed to the object.

            :param ops: The password action to be performed.
            :rtype: A dictionary in case of error or a success response.

        .. method:: set_minimum_difference(value)

                Sets the minimum difference expected between the old and new
                password.

            :param value: The minimum difference between old and new passwords.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_minimum_difference()

            Reads the value of the minimum difference between old and new \
            passwords from the object.

            :rtype: A dictionary in case of error or a success response.
       """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.password_cfg,
                         "/rest/running/brocade-security/password-cfg")

        self.add(pyfos_rest_util.rest_attribute(
            "minimum-length", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "character-set", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "user-name-allowed", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "minimum-lower-case-character", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "minimum-upper-case-character", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "minimum-numeric-character", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "minimum-special-character", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "past-password-history", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "minimum-password-age", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "maximum-password-age", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "warn-on-expire", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "lock-out-threshold", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "lock-out-duration", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "admin-lock-out-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "repeat-character-limit", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "sequence-character-limit", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "password-config-changed", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "reverse-user-name-allowed", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "hash-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "manual-hash-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "enforce-expire", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "minimum-difference", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "password-action", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class user_specific_password_cfg(pyfos_rest_util.rest_object):
    """Class of user specific password configuration
                Important Class Members:

        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | Attribute Name                    | Description                   |Frequently Used Methods                                |
        +===================================+===============================+=======================================================+
        | user-name                         | The username.                 |:func:`set_user_name`                                  |
        |                                   |                               |:func:`peek_user_name`                                 |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | minimum-password-age              | The minimum number of days    |:func:`set_minimum_password_age`                       |
        |                                   | that must elapse before a     |:func:`peek_minimum_password_age`                      |
        |                                   | password can be changed.      |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | maximum-password-age              | The maximum number of days    |:func:`set_maximum_password_age`                       |
        |                                   | that can elapse before a      |:func:`peek_maximum_password_age`                      |
        |                                   | password can be changed.      |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | warn-on-expire                    | The number of days prior to   |:func:`set_warn_on_expire`                             |
        |                                   | password expiration that a    |:func:`peek_warn_on_expire`                            |
        |                                   | that a warning about password |                                                       |
        |                                   | expiration displays.          |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | enforce-expire                    | Enables or disables password  |:func:`set_enforce_expire`                             |
        |                                   | expiration for user.          |:func:`peek_enforce_expire`                            |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | hash-type                         | The hash type.                |:func:`set_hash_type`                                  |
        |                                   |                               |:func:`peek_hash_type`                                 |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+

       *Object Methods*
        .. method:: get(session)

            Returns a :class`user_specific_password_cfg`
            object with values for all the attributes.
            The object can be printed using :func:`pyfos_utils.response_print`.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a
                :class:`user_specific_password_cfg` object.

        .. method:: post(session)

            Creates a password configuration for a specific user.
            The fields are set within the object using attribute's set
            method. This command is used to create a password configuration
            for a specific user.

            Example Usage of the Method to Create a New Configuration::

                password_obj =
                    pyfos_password_cfg.password_cfg()
                password_obj.set_user_name("mytestuser")
                password_obj.set_minimum_password_age(10)
                password_obj.set_maximum_password_age(20)
                password_obj.set_warn_on_expire(5)
                password_obj.post(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

        .. method:: patch()

            Modifies a user's specific password configuration.
            The fields are set within the object using attribute's
            set method.

            Example Usage of the Method to Modify a User's Password \
            Configuration::

                password_obj =
                    pyfos_password_cfg.password_cfg()
                password_obj.set_minimum_length(10)
                password_obj.set_maximum_length(20)
                password_obj.patch(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

        .. method:: delete(session)

            Deletes a user-defined password configuration.
            The fields are set within the object using attribute's
            set method. This command is used to delete a user-defined \
            password configuration.

            Example Usage of the Method to Delete a User-defined Password
            Configuration::

                password_obj =
                    pyfos_password_cfg.password_cfg()
                password_obj.set_user_name("mytestuser")
                password_obj.delete(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

       *Attribute Methods*

        .. method:: set_user_name(name)

           Sets the username in the object.

            :param name: The username for the password configuration.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_user_name

            Reads the username from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_minimum_password_age(number)

                Sets the minimum number of days that must elapse before a \
                password can be changed.

            :param number: The minimum number of days that must elapse before \
                           a password can be changed.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_minimum_password_age()

            Reads the minimum number of days that must elapse before a \
            password can be changed from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_maximum_password_age(number)

                Sets the maximum number of days that can elapse before a \
                password can be changed.

            :param number: The maximum number of days before password \
                           expiration.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_maximum_password_age()

            Reads the maximum number of days before password expiration \
            from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_warn_on_expire(number)

                Sets the number of days prior to password expiration to \
                the object.

            :param number: number of days
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_warn_on_expire()

            Reads the number of days prior to password expiration that a \
            warning about password expiration displays from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_hash_type(hash)

                Sets the hash type to the object.

            :param hash: The hash type for the password.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_hash_type()

            Reads the hash type from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_enforce_expire(bool)

                Enables or disables password expiration for the user
                to the object.

            :param bool: Enables or disables password expiration.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_enforce_expire()

            Reads the status of the password expiration for the user
            from the object.

            :rtype: A dictionary in case of error or a success response.

       """

    def __init__(self, dictvalues={}):
        super().__init__(
            pyfos_rest_util.rest_obj_type.user_specific_password_cfg,
            "/rest/running/brocade-security/user-specific-password-cfg")

        self.add(pyfos_rest_util.rest_attribute(
            "user-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "minimum-password-age", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "maximum-password-age", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "warn-on-expire", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "hash-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "enforce-expire", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class user_config(pyfos_rest_util.rest_object):
    """Class of user configuration.
               Important Class Members:

        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | Attribute Name                    | Description                   |Frequently Used Methods                                |
        +===================================+===============================+=======================================================+
        | name                              | The name of the user account. |:func:`set_name`                                       |
        |                                   |                               |:func:`peek_name`                                      |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | password                          | The user account password.    |:func:`set_password`                                   |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | role                              | The user's role name.         |:func:`set_role`                                       |
        |                                   |                               |:func:`peek_role`                                      |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | account-description               | The account description.      |:func:`set_account_description`                        |
        |                                   |                               |:func:`peek_account_description`                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | account-enabled                   | Indicates the user's account  |:func:`set_account_enabled`                            |
        |                                   | status.                       |:func:`peek_account_enabled`                           |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | password-change-enforced          | Enables or disables enforcing |:func:`set_password_change_enforced`                   |
        |                                   |  password change during       |:func:`peek_password_change_enforced`                  |
        |                                   |  login.                       |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | account-locked                    | Unlocks the user account if   |:func:`set_account_locked`                             |
        |                                   | already locked.               |:func:`peek_account_locked`                            |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | access-start-time                 | The access start time for     |:func:`set_access_start_time`                          |
        |                                   | the account.                  |:func:`peek_access_start_time`                         |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | access-end-time                   | The access end time for       |:func:`set_access_end_time`                            |
        |                                   | the account.                  |:func:`peek_access_end_time`                           |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | home-virtual-fabric               | The home Virtual Fabric for   |:func:`set_home_virtual_fabric`                        |
        |                                   | the account/                  |:func:`peek_home_virtual_fabric`                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | chassis-access-role               | The chassis access role name. |:func:`set_chassis_access_role`                        |
        |                                   |                               |:func:`peek_chassis_access_role`                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | virtual-fabric-role-id-list/      | The Virtual Fabric role       |:func:`set_virtual_fabric_role_id_list_role_id`        |
        |              role-id              | name list.                    |:func:`peek_virtual_fabric_role_id_list_role_id`       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+

       *Attribute Methods*

        .. staticmethod:: get(session, name=None)

            Returns a :class:`user_config` object filled with user config
                             attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A :class:`user_config` object if the name is given or list \
                    of objects if there is more than one. A dictionary in case \
                    of error.

        .. method:: post(session)

            Creates a user account. The fields are set
            within the object using attribute's set method.
            This method is used to create a new user account configuration.

            Example Usage of the Method to Configure a New User Account:

            .. code-block:: python

                # initialize the user config object
                user_obj = pyfos_brocade_security.user_config()
                user_obj.set_name("myuser")
                user_obj.set_role("admin")
                user_obj.set_password("bXlsaWZlMTk4OSM=");
                user_obj.set_account_description("new user")
                # execute HTTP post command to apply the object to the
                # switch connected through session
                user_obj.post(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

        .. method:: patch(session)

            Replaces an existing configuration. The fields are set within
            the object using attribute's set method. This method is used to
            modifying the existing user account configuration.

            Example Usage of the Method to Configure the Response Timeout:

            .. code-block:: python

                # initialize the user config object
                user_info = pyfos_brocade_security.user_config()
                user_info.set_name("myuser")
                user_info.set_account_enabled(1)
                user_info.set_password_change_enforced(0)
                # execute HTTP patch command to apply the object to the
                # switch connected through session
                user_info.patch(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

        .. method:: delete(session)

            Deletes a user account. The fields are
            set within the object using attribute's
            set method. This method is used to delete a user account
            configuration.

            Example Usage of the Method to Delete a User Account:

            .. code-block:: python

                # initialize the user config object
                user_obj = pyfos_brocade_security.user_config()
                user_obj.set_name("myuser")
                # execute HTTP delete command to apply the object to the
                # switch connected through session
                user_obj.delete(session)

       *Attribute Methods*

        .. method:: set_name(name)

           Sets the user account name in the object.

            :param name: The user account name to be set within the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_name()

            Reads the user account name from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_password(pass)

           Sets the user account password in the object.

            :param pass: The user account password to be set within the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: set_role(role)

           Sets the user role in the object.

            :param role: The user role to be set within the object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_role()

            Reads the user role from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_account_description(message)

           Sets the user account description in the object.

            :param message: The user account description to be set within the
                            object.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_account_description()

            Reads the user account description from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_account_enabled(bool)

           Enables or disables user account in the object.

            :param bool: Enables or disables the user account.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_account_enabled()

            Reads the status of user account from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_password_change_enforced(bool)

           Enables or disables password change during login in the object.

            :param bool: Enables or disables password change durning login.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_password_change_enforced()

            Reads status password change during login from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_account_locked(bool)

           Unlocks the user account if already locked in the object.

            :param bool: Unlocks the user account.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_account_locked()

            Reads the locked or unlocked status of user accountfrom the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_access_start_time(time)

           Sets the user access start time in the object.

            :param time: The user access start time.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_access_start_time()

            Reads the user access start time from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_access_end_time(time)

           Sets the user access end time in the object.

            :param time: The user access end time.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_access_end_time()

            Reads the user access end time from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_home_virtual_fabric(fid)

           Sets the user account home FID in the object

            :param fid: The user account home FID.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_home_virtual_fabric()

            Reads the user account home FID from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_chassis_access_role(role)

           Sets the chassis access role in the object.

            :param role: The chassis access role.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_chassis_access_role()

            Reads the chassis access role from the object.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_virtual_fabric_role_id_list_role_id(roles)

           Sets the virtual fabric roles in the object.

            :param roles: The virtual fabric role and ID.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_virtual_fabric_role_id_list_role_id()

            Reads the virtual fabric role and ID from the object.

            :rtype: A dictionary in case of error or a success response.

       """
    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.user_config,
                         "/rest/running/brocade-security/user-config")

        self.add(pyfos_rest_util.rest_attribute(
            "name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "password", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "role", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "account-description", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "account-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "password-change-enforced", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "account-locked", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "access-start-time", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "access-end-time", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "home-virtual-fabric", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "chassis-access-role", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "virtual-fabric-role-id-list", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "role-id", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["virtual-fabric-role-id-list"])

        self.load(dictvalues, 1)


class sshutil(pyfos_rest_util.rest_object):
    """ This class provides methods to manage
    and configure public and private key pairs in a switch.

    Important Class Members:

        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | Attribute Name                                 | Description                      |Frequently Used Methods                                  |
        +================================================+==================================+=========================================================+
        | allow-user-name                                | The username.                    |:func:`set_allow_user_name`                              |
        |                                                |                                  |:func:`peek_allow_user_name`                             |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | rekey-interval                                 | The rekey interval duration.     |:func:`set_rekey_interval`                               |
        |                                                |                                  |:func:`peek_rekey_interval`                              |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+

    *Object Methods*

        .. method:: get()

            Returns a :class:`sshutil`
            object with values for all the attributes.
            The object can be printed using :func:`pyfos_utils.response_print`.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a
                :class:`sshutil` object.

        .. method:: patch()

            Replaces entry members. The fields are set within the object
            using attribute's set method. This command is used to
            import public key from remote host to switch or
            export public key from switch to a remote host.

            Example Usage of the Method to Export a Public Key:

            .. code-block:: python

                sshutil_obj =
                    pyfos_brocade_security.sshutil()
                sshutil_obj.export_public_key("10.70.4.109", "/root/ca",
                                                   "root", "pray4green")
                sshutil_obj.patch(session)

            Example Usage of the Method to Import a Public Key:

            .. code-block:: python

                sshutil_obj =
                    pyfos_brocade_security.sshutil()
                sshutil_obj.import_export_key("test","10.70.4.109", "/root/ca",
                                                "key.pub","root", "pray4green")
                sshutil_obj.patch(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

    *Attribute Methods*

        .. method:: set_allow_user_name("user")

            Sets the username in the object.

            :param pgid: Allows the username.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_allow_user_name()

            Reads whether the username is allowed in the object.

            :rtype: None or the PGID.

        .. method:: set_rekey_interval(int)

             Sets the rekey interval duration in the object.

            :param interval: The rekey interval duration.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_rekey_interval()

            Reads the rekey interval duration in the object.

            :rtype: None or the multiple fabric name monitoring mode status.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.sshutil,
                         "/rest/running/brocade-security/sshutil",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "allow-user-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "rekey-interval", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class sshutil_key(pyfos_rest_util.rest_object):
    """ This class provides methods/options to manage
    and configure public and private key pairs in a switch.

    Important Class Members:

        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | Attribute Name                                 | Description                      |Frequently Used Methods                                  |
        +================================================+==================================+=========================================================+
        | key-type                                       | The key type.                    |:func:`set_key_type`                                     |
        |                                                |                                  |:func:`peek_key_type`                                    |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | passphrase                                     | The passphrase for the key.      |:func:`set_passphrase`                                   |
        |                                                |                                  |:func:`peek_passphrase`                                  |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | algorithm-type                                 | The algorithm type.              |:func:`set_algorithm_type`                               |
        |                                                |                                  |:func:`peek_algorithm_type`                              |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | size                                           | The size.                        |:func:`peek_size`                                        |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | fingerprint                                    | The fingerprint.                 |:func:`peek_fingerprint`                                 |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+

    *Object Methods*

        .. method:: get()

            Returns a :class:`sshutilkey`
            object with values for all the attributes.
            The object can be printed using :func:`pyfos_utils.response_print`.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a
                :class:`sshutil` object.

        .. method:: post()

            Creates an entry or adds members. The fields are set
            within the object using attribute's set method.
            This method is used to create a host key or
            public and private key pair.

            Example Usage of the Method to Create a New Host Key:

            .. code-block:: python

                sshutil_obj =
                    pyfos_brocade_security.sshutilkey()
                sshutil_obj.generate_public_key("rsa", "fibranne")
                sshutil_obj.generate_host_key("rsa")
                sshutil_obj.post(session)

            The example above generates a public/private key pair and
            host key with and RSA algorithm.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

        .. method:: delete()

            Deletes an entry or entry members. The fields are
            set within the object using attribute's
            set method. This command is used to delete public key(s),
            private key, delknownhost(s), or hostkey.

            Example Usage of the Method to Delete a Public Key:

            .. code-block:: python

                sshutil_obj =
                    pyfos_brocade_security.sshutilkey()
                sshutil_obj.delete_public_keys("user")
                sshutil_obj.delete_host_keys("user")
                sshutil_obj.delete(session)

            Example Usage of the Method to Delete a Private Key:

            .. code-block:: python

                sshutil_obj =
                    pyfos_brocade_security.sshutilkey()
                sshutil_obj.delete_private_key("user")
                sshutil_obj.delete(session)

            Example Usage of the Method to Delete a Host Key:

            .. code-block:: python

                sshutil_obj =
                    pyfos_brocade_security.sshutilkey()
                sshutil_obj.delete_host_key("rsa")
                sshutil_obj.delete(session)

            Example Usage of the Method to Delete a Known Host:

    *Attribute Methods*

        .. method:: set_key_type("type")

            Sets the key type in the object.

            :param pgid: The key type (public-private-key or host-key).
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_key_type()

            Reads the key type from the object.

            :rtype: None or the PGID.

        .. method:: set_passphrase(password)

             Sets the passphrase for key generation in the object.

            :param password: The password for key generation.
            :rtype: A dictionary in case of error or a success response.

        .. method:: set_algorithm_type(type)

             Sets the algorithm type in the object.

            :param algorithm type: The algorithm type (rsa, dsa, or ecdsa).
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_size()

            Reads the size in the object.

            :rtype: None or the multiple fabric name monitoring mode status.

        .. method:: peek_fingerprint()

             Reads the fingerprint in the object

            :param operation: The fingerprint.
            :rtype: A dictionary in case of error or a success response.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.sshutil_key,
                         "/rest/running/brocade-security/sshutil-key",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "key-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "algorithm-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "passphrase", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "size", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "fingerprint", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.load(dictvalues, 1)


class sshutil_public_key_action(pyfos_rest_util.rest_object):
    """ This class provides methods to manage and configure
    public and private key pairs in a switch.

    Important Class Members:

        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | Attribute Name                                 | Description                      |Frequently Used Methods                                  |
        +================================================+==================================+=========================================================+
        | user-name                                      | The username.                    |:func:`set_user_name`                                    |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | public-key-name                                | The public key name.             |:func:`set_public_key_name`                              |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | remote-host-ip                                 | The username for the             |:func:`set_remote_host_ip`                               |
        |                                                | remote host.                     |                                                         |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | remote-directory                               | The directory in remote host.    |:func:`set_remote_dir`                                   |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | remote-user-name                               | The username for the host.       |:func:`set_remote_user_name`                             |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | remote-user-password                           | The remote user's password.      |:func:`set_remote_user_password`                         |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | algorithm-type                                 | The algorithm type.              |:func:`set_algorithm_type`                               |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | action                                         | The sshutil operations.          |:func:`set_action`                                       |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+

    *Object Methods*

        .. method:: patch()

            Replaces entry members. The fields are set within the object
            using attribute's set method. This command is used to
            import public key from remote host to switch,
            export public key from switch to a remote host.

            Example Usage of the Method to Export a Public Key:

            .. code-block:: python

                sshutil_obj =
                    pyfos_brocade_security.sshutil()
                sshutil_obj.export_public_key("10.70.4.109", "/root/ca",
                                                   "root", "pray4green")
                sshutil_obj.patch(session)

            Example Usage of the Method to Import a Public Key:

            .. code-block:: python

                sshutil_obj =
                    pyfos_brocade_security.sshutil()
                sshutil_obj.import_export_key("test","10.70.4.109","/root/ca",
                                                "key.pub","root","pray4green")
                sshutil_obj.patch(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

    *Attribute Methods*

        .. method:: set_user_name("user")

            Sets the username in the object.

            :param pgid: The username.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_user_name()

            Reads the username in the object.

            :rtype: None or the PGID.

        .. method:: set_public_key_name(name)

            Sets the public key name in the object.

            :param name: The name of the public key.
            :rtype: A dictionary in case of error or a success response.

        .. method:: set_remote_host_ip(ip)

            Sets the remote host IP address in the object.

            :param ip: The IP address of the remote host.
            :rtype: A dictionary in case of error or a success response.

        .. method:: set_remote_dir(location)

            Sets a remote directory path in the object.

            :param location: The directory path in remote host.
            :rtype: A dictionary in case of error or a success response.

        .. method:: set_remote_user_name(username)

            Sets the remote host's username in the object.

            :param user name: The username for authenticating the remote host.
            :rtype: A dictionary in case of error or a success response.

        .. method:: set_remote_user_password(password)

             Sets the remote host's user password in the object.

            :param password: The password for the remote host.
            :rtype: A dictionary in case of error or a success response.

        .. method:: set_algorithm_type(type)

             Sets the algorithm type in the object.

            :param algorithm type: The algorithm type.
            :rtype: A dictionary in case of error or a success response.

        .. method:: set_action(type)

             Sets an action in the object.

            :param operation: action
            :rtype: A dictionary in case of error or a success response.

        """

    def __init__(self, dictvalues={}):
        super().__init__(
            pyfos_rest_util.rest_obj_type.sshutil,
            "/rest/running/brocade-security/sshutil-public-key-action",
            version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "user-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "public-key-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "remote-host-ip", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "remote-user-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "remote-user-password", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "remote-directory", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "algorithm-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "action", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class sshutil_public_key(pyfos_rest_util.rest_object):
    """ This class provides methods to manage
    and configure public and private key pairs in a switch.

    Important Class Members:

        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | Attribute Name                                 | Description                      |Frequently Used Methods                                  |
        +================================================+==================================+=========================================================+
        | user-name                                      | The username.                    |:func:`set_user_name`                                    |
        |                                                |                                  |:func:`peek_user_name`                                   |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | public-key                                     | The public key.                  |:func:`set_public_key`                                   |
        |                                                |                                  |:func:`peek_public_key`                                  |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+

    *Object Methods*

        .. method:: get()

            Returns a :class:`sshutil_public_key`
            object with values for all the attributes.
            The object can be printed using :func:`pyfos_utils.response_print`.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a
                :class:`sshutil` object.

        .. method:: delete()

            Deletes an entry or entry members. The fields are
            set within the object using attribute's
            set method. This command is used to delete public key(s), a
            private key, delknownhost(s) or a host key.

            Example Usage of the Method to Delete a Public Key:

            .. code-block:: python

                sshutil_obj =
                    pyfos_brocade_security.sshutil_public_key()
                sshutil_obj.delete_public_keys("user")
                sshutil_obj.delete(session)

    *Attribute Methods*

        .. method:: set_user_name("user")

            Sets the username in the object.

            :param pgid: The username.
            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_user_name()

            Reads the username in the object.

            :rtype: None or the PGID.

        .. method:: peek_public_key()

            Reads the public key in the object.

            :param name: The public key.
            :rtype: A dictionary in case of error or a success response.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.sshutil_public_key,
                         "/rest/running/brocade-security/sshutil-public-key",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "user-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "public-key", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class password(pyfos_rest_util.rest_object):
    """This class provides methods to change password.

    Important Class Members:

        +------------------------------------------------+----------------------------------+----------------------------------------------------------------+
        | Attribute Name                                 | Description                      |Frequently Used Methods                                         |
        +================================================+==================================+================================================================+
        | user-name                          | The name of the user to change password.     |:func:`set_user_name`                                           |
        |                                                |                                  |:func:`peek_user_name`                                          |
        +------------------------------------------------+----------------------------------+----------------------------------------------------------------+
        | old-password                       | The current password.                        |:func:`set_old_password`                                        |
        |                                                |                                  |:func:`peek_old_password`                                       |
        +------------------------------------------------+----------------------------------+----------------------------------------------------------------+
        | new-password                       | The new password.                            |:func:`set_new_password`                                        |
        |                                                |                                  |:func:`peek_new_password`                                       |
        +------------------------------------------------+----------------------------------+----------------------------------------------------------------+

    *Object Methods*

        .. method:: patch()

            Replaces entry members. The fields are set within the object
            using attribute's set method. This command is used to
            change a user password.

            Example Usage of the Method to Change a Password:

            .. code-block:: python

                passwd_obj =
                    pyfos_brocade_security.password()
                passwd_obj.change_password(username)
                passwd_obj.patch(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

    *Attribute Methods*

        .. method:: change_password(username, old_password, new_password)

            Changes the password for the specified user.

            :param username: Changes the password.
            :rtype: A dictionary in case of error or a success response.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.password,
                         "/rest/running/brocade-security/password",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "user-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "old-password", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "new-password", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


# class security-certificate-management(pyfos_rest_util.rest_object):
class security_certificate(pyfos_rest_util.rest_object):
    """This class provides options to display and configure certificates.

    Important Class Members:

        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | Attribute Name                                 | Description                       |Frequently Used Methods                      |
        +================================================+===================================+=============================================+
        | certificate-entity                             | The certificate entity (CSR,      |:func:`set_certificate_entity`               |
        |                                                | switch, or CA certificate.        |:func:`peek_certificate_entity`              |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | certificate-type                               | The certificate types             |:func:`peek_certificate_type`                |
        |                                                | (commoncert, https, radius, ldap, |:func:`set_certificate_type`                 |
        |                                                | or syslog).                       |                                             |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | certificate                                    | The certificate.                  |:func:`peek_certificate`                     |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | certificate-hexdump                            | The certificate in hex format.    |:func:`peek_certificate_hexdump`             |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+

    *Object Methods*

        .. method:: get(session)

            Returns a :class:`seccertmgmt_show` object or a list of objects
            filled with the certificate attributes. If certificate entity
            and certificate type is specified, a certificate matching the name
            of the certificate entity and type is returned or an empty object
            is returned if no match is found.

            Each object can be printed using :func:`pyfos_util.response_print`.
            and individual attributes accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A :class:`seccertmgmt` object to get a object or
                a list of objects if there are more than one.

    *Attribute Methods*

        .. method:: set_certificate_entity(cert)

            Sets the certificate entity in the object.

            :param cert: The certificate entity to be set within the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_certificate_entity()

            Reads the certificate entity in the object.

            :rtype: The certificate entity.

        .. method:: set_certificate_type(cert)

            Sets the certificate type in the object.

            :param cert type: The certificate type to be set within the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_certificate_type()

            Reads the certificate type in the object.

            :rtype: The certificate type.

        .. method:: peek_certificate()

            Gets the certificate in the object.

            :rtype: None or a certificate.

        .. method:: peek_certificate_hexdump()

            Gets the certificate in hex format in the object.

            :rtype: None or the certificate in hex format.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.security_certificate,
                         "/rest/running/brocade-security/security-certificate",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "certificate-entity", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "certificate-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "certificate", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "certificate-hexdump", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)
# class security-certificate-generate(pyfos_rest_util.rest_object):


class security_certificate_generate(pyfos_rest_util.rest_object):
    """This class provides options to display and configure certificates.

    Important Class Members:

        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | Attribute Name                                 | Description                       |Frequently Used Methods                      |
        +================================================+===================================+=============================================+
        | certificate-entity                             | The certificate entity (CSR,      |:func:`set_certificate_entity`               |
        |                                                | switch, or CA certificate.        |                                             |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | certificate-type                               | The certificate types             |:func:`set_certificate_type`                 |
        |                                                | (commoncert, https, radius, ldap, |                                             |
        |                                                | or syslog).                       |                                             |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | algorithm-type                                 | The algorithm type (rsa, dsa,     |:func:`set_algorithm_type`                   |
        |                                                | or ecdsa).                        |                                             |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | key-size                                       | The size of the key.              |:func:`set_key_size`                         |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | hash-type                                      | The hash type.                    |:func:`set_hash_type`                        |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | years                                          | The certificate validity.         |:func:`peek_years`                           |
        |                                                |                                   |:func:`set_years`                            |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | country-name                                   | The country name.                 |:func:`set_country_name`                     |
        |                                                | Only needed to generate a CSR.    |:func:`peek_country_name`                    |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | state-name                                     | The state name.                   |:func:`set_state_name`                       |
        |                                                | Only needed to generate a CSR.    |:func:`peek_state_name`                      |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | locality-name                                  | The locality name.                |:func:`set_locality_name`                    |
        |                                                | Only needed to generate a CSR.    |:func:`peek_locality_name`                   |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | organization-name                              | The organization name.            |:func:`set_organization_name`                |
        |                                                | Only needed to generate a CSR.    |:func:`peek_organization_name`               |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | unit-name                                      | The unit name.                    |:func:`set_unit_name`                        |
        |                                                | Only needed to generate a CSR.    |:func:`peek_unit_name`                       |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | domain-name                                    | The domain name.                  |:func:`set_domain_name`                      |
        |                                                | Only needed to generate a CSR.    |:func:`peek_domain_name`                     |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | keypair-tag                                    | The unique name to identify the   |:func:`set_keypair_tag`                      |
        |                                                | local extension certificate       |                                             |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+


        .. method:: get(session)

            Returns a :class:`security_certificate_generate` object or a list
            of objects filled with the certificate attributes. If a
            certificate entity and certificate type is specified, a certificate
            matching the name of the certificate entity and type is returned or
            an empty object is returned if no match is found.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A :class:`seccertmgmt` object to get a object or
                a list of objects if there are more than one.

        .. method:: post(session)

            Generates a certificate. This method is used
            to create a specified certificate.

            Example Usage of the Method to Create a New Certificate::

                # initialize the System Security object
                seccertmgmt =
                        pyfos_brocade_security.security_certificate_generate();
                # Generate a https certificate
                security_certificate_generate.generate("cert", "https")
                result = security_certificate_generate.post(session)


            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

    *Attribute Methods*

        .. method:: set_certificate_entity(cert)

            Sets the certificate entity in the object.

            :param cert: The certificate entity to be set within the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_certificate_entity()

            Reads the certificate entity in the object.

            :rtype: certificate entity

        .. method:: set_certificate_type(cert)

            Sets the certificate type in the object.

            :param cert type: The certificate type to be set within the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_certificate_type()

            Reads the certificate type in the object.

            :rtype: certificate type

        .. method:: set_algorithm_type(algo)

            Sets the algorithm type in the object.

            :param algo: The algorithm type to be set within the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_algorithm_type()

            Reads the algorithm type in the object.

            :rtype: algorithm type

        .. method:: set_key_size(size)

            Sets the size of the key in the object.

            :param size: The size of the key.
            :rtype: None or a dictionary of error information.

        .. method:: peek_key_size()

            Gets the size of the key in the object.

            :rtype: None or the key size.

        .. method:: set_hash_type(hash_type)

            Sets the hash type in the object.

            :param hash_type: The hash type.
            :rtype: None or a dictionary of error information.

        .. method:: peek_hash_type()

            Gets the hash type in the object.

            :rtype: None or a hash type.

        .. method:: peek_years()

            Gets the years in the object.

            :rtype: None or the years.

        .. method:: set_years(years)

            Sets the years in the object.

            :param years: The years.
            :rtype: None or a dictionary of error information.

        .. method:: peek_certificate()

            Gets the certificate in the object.

            :rtype: None or a certificate.

        .. method:: peek_country_name()

            Gets the country name in the object.

            :rtype: None or the country name.

        .. method:: set_country_name(country_name)

            Sets the country name in the object.

            :param country_name: The country name.
            :rtype: None or a dictionary of error information.

        .. method:: peek_state_name()

            Gets the state name in the object.

            :rtype: None or the state name.

        .. method:: set_state_name(state_name)

            Sets the state name in the object.

            :param state_name: The state name.
            :rtype: None or a dictionary of error information.

        .. method:: peek_locality_name()

            Gets the locality name in the object.

            :rtype: None or the locality name.

        .. method:: set_locality_name(locality_name)

            Sets the locality name in the object.

            :param locality_name: The locality name.
            :rtype: None or a dictionary of error information.

        .. method:: peek_organization_name()

            Gets the organization name in the object.

            :rtype: None or the organization name.

        .. method:: set_organization_name(organization_name)

            Sets the organization name in the object.

            :param organization_name: The organization name.
            :rtype: None or a dictionary of error information.

        .. method:: peek_unit_name()

            Gets the unit name in the object.

            :rtype: None or the unit name.

        .. method:: set_unit_name(unit_name)

            Sets the unit name in the object.

            :param unit_name: The unit name.
            :rtype: None or a dictionary of error information.

        .. method:: peek_domain_name()

            Gets the domain name in the object.

            :rtype: None or the domain name.

        .. method:: set_domain_name(domain_name)

            Sets the domain name in the object.

            :param domain_name: The domain name.
            :rtype: None or a dictionary of error information.

        .. method:: set_keypair_tag(keypair-tag)

            Sets the unique user defined name for Extension local certificate.

            :param keypair-tag: The unique name to create a CSR/certificate.
            :rtype: A dictionary in case of error or a success response.

        """

    def __init__(self, dictvalues={}):
        super().__init__(
            pyfos_rest_util.rest_obj_type.security_certificate_generate,
            "/rest/running/brocade-security/security-certificate-generate",
            version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "certificate-entity", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "certificate-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "algorithm-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "key-size", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "hash-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "years", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "country-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "state-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "locality-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "organization-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "unit-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "domain-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "keypair-tag", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_900_and_ABOVE))

        self.load(dictvalues, 1)
# class security-certificate-management(pyfos_rest_util.rest_object):


class security_certificate_action(pyfos_rest_util.rest_object):
    """This class provides options to display and configure certificates.

    Important Class Members:

        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | Attribute Name                                 | Description                       |Frequently Used Methods                      |
        +================================================+===================================+=============================================+
        | certificate-entity                             | The certificate entity (CSR,      |:func:`set_certificate_entity`               |
        |                                                | switch, or CA certificate.        |                                             |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | certificate-type                               | The certificate types             |:func:`set_certificate_type`                 |
        |                                                | (commoncert, https, radius, ldap, |                                             |
        |                                                | or syslog).                       |                                             |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | certificate-name                               | The certificate name.             |:func:`set_certificate_name`                 |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | operation                                      | The operation.                    |:func:`set_operation`                        |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | protocol                                       | The protocol used for import      |:func:`set_protocol`                         |
        |                                                | or export.                        |                                             |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | remote-host-ip                                 | The remote host IP address for    |:func:`set_remote_host_ip`                   |
        |                                                | import or export.                 |                                             |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | remote-directory                               | The directory in remote host.     |:func:`set_remote_dir`                       |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | remote-user-name                               | The username for the remote host. |:func:`set_remote_user_name`                 |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | remote-user-password                           | The password for the remote host. |:func:`set_remote_user_password`             |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | ca-certificate                                 | The CA filename for extension     |:func:`set_ca_certificate`                   |
        |                                                | certificate import                |                                             |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | keypair-tag                                    | The unique name to identify the   |:func:`set_keypair_tag`                      |
        |                                                | local extension certificate       |                                             |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+

    *Object Methods*

        .. method:: set(session)

            Returns a :class:`security_certificate_action` object or a list of
            objects filled with the certificate attributes. If a certificate
            entity and certificate type is specified, a certificate matching
            the name of the certificate entity and type is returned or an empty
            object is returned if no match is found.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A :class:`seccertmgmt` object to get a object or
                a list of objects if there are more than one.

        .. method:: patch(session)

            Imports or exports the certificate or CSR to and from a
            remote server. This method imports or exports a
            specified certifiate to or from a switch. This certificate
            overwrites any existing certificate already present
            in the switch. Also, this method is used to send a signing
            request (CSR) from the switch to a remote server.

            *Below is an example using individual sets:*

            .. code-block:: python

                # initialize the System Security object
                seccertmgmt =
                          pyfos_brocade_security.security_certificate_action();
                # export a CSR to remote server
                seccertmgmt.import("csr","commoncert","10.70.4.1","ca","root")
                seccertmgmt.export("cert","commoncert","10.70.4.1","ca","root")
                # execute HTTP patch method to apply the object to the
                # switch connected through session
                seccertmgmt.patch(session)


            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

        .. method:: delete(session)

            Deletes a certificate.
            This method is used to remove or clear the specified certificate.

            Example Usage of the Method to Delete a Certificate::

                # initialize the System Security object
                seccertmgmt = pyfos_brocade_security.seccertmgmt();
                # delete a certificate
                seccertmgmt.delete("cert", "https")
                result = seccertmgmt.delete(session)


            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary in case of error or a success response.

    *Attribute Methods*

        .. method:: set_certificate_entity(cert)

            Sets the certificate entity in the object.

            :param cert: The certificate entity to be set within the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_certificate_entity()

            Reads the certificate entity in the object.

            :rtype: The certificate entity.

        .. method:: set_certificate_type(cert)

            Sets the certificate type in the object.

            :param cert type: the certificate type to be set within the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_certificate_type()

            Reads the certificate type in the object.

            :rtype: The certificate type.

        .. method:: peek_certificate_name()

            Gets the certificate name in the object.

            :rtype: None or the certificate name.

        .. method:: set_certificate_name(cert_name)

            Sets the certificate name type in the object.

            :param cert_name: the certificate name
            :rtype: None or a dictionary of error information.

        .. method:: peek_operation()

            Gets the certificate operation in the object.

            :rtype: None or the certificate operation.

        .. method:: set_operation()

            Sets the certificate operation in the object.

            :rtype: None or the certificate operation.

        .. method:: set_remote_host_ip(ip)

            Sets the remote host ip address object

            :param ip: The IP address of the remote host.
            :rtype: A dictionary in case of error or a success response.

        .. method:: set_remote_dir(location)

            Sets a remote directory path in the object.

            :param location: The directory path in remote host.
            :rtype: A dictionary in case of error or a success response.

        .. method:: set_remote_user_name(username)

            Sets the remote host's username in the object.

            :param user name: The username for authenticating the remote host.
            :rtype: A dictionary in case of error or a success response.

        .. method:: set_remote_user_password(password)

             Sets the remote host's user password in the object.

            :param password: The password for remote host.
            :rtype: A dictionary in case of error or a success response.

        .. method:: set_keypair_tag(keypair-tag)

            Sets the unique user defined name for Extension local certificate.

            :param keypair-tag: The unique name to create a CSR/certificate.
            :rtype: A dictionary in case of error or a success response.

        .. method:: set_ca_certificate(ca-certificate)

             Sets the CA certificate name for import of Extension certificate.

            :param password: The password for remote host.
            :rtype: A dictionary in case of error or a success response.
        """

    def __init__(self, dictvalues={}):
        super().__init__(
            pyfos_rest_util.rest_obj_type.security_certificate_action,
            "/rest/running/brocade-security/security-certificate-action",
            version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "certificate-entity", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "certificate-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "operation", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "certificate-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "protocol", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "remote-host-ip", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "remote-user-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "remote-user-password", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "remote-directory", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "ca-certificate", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_900_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute(
            "keypair-tag", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
            version.VER_RANGE_900_and_ABOVE))

        self.load(dictvalues, 1)


class security_certificate_extension(pyfos_rest_util.rest_object):
    """This class provides options to display and configure certificates.

    Important Class Members:

        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | Attribute Name                                 | Description                       |Frequently Used Methods                      |
        +================================================+===================================+=============================================+
        | certificate-entity                             | The certificate entity (CSR,      |:func:`set_certificate_entity`               |
        |                                                | switch, or CA certificate.        |:func:`peek_certificate_entity`              |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | certificate                                    | The certificate.                  |:func:`peek_certificate`                     |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | certificate-hexdump                            | The certificate in hex format.    |:func:`peek_certificate_hexdump`             |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | certificate-name                               | The name of extension certificate |:func:`peek_certificate_name`                |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | keypair-tag                                    | The unique name to identify the   |:func:`peek_keypair_tag`                     |
        |                                                | local extension certificate       |                                             |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | local-certificate                              | The certificate is local for an   |:func:`peek_local_certificate`               |
        |                                                | extension switch or not           |                                             |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+

    *Object Methods*

        .. method:: get(session)

            Returns a :class:`seccertmgmt_show` object or a list of objects
            filled with the certificate attributes. If certificate entity
            and certificate type is specified, a certificate matching the name
            of the certificate entity and type is returned or an empty object
            is returned if no match is found.

            Each object can be printed using :func:`pyfos_util.response_print`.
            and individual attributes accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A :class:`seccertmgmt` object to get a object or
                a list of objects if there are more than one.

    *Attribute Methods*

        .. method:: set_certificate_entity(cert)

            Sets the certificate entity in the object.

            :param cert: The certificate entity to be set within the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_certificate_entity()

            Reads the certificate entity in the object.

            :rtype: The certificate entity.

        .. method:: peek_certificate()

            Gets the certificate in the object.

            :rtype: None or a certificate.

        .. method:: peek_certificate_hexdump()

            Gets the certificate in hex format in the object.

            :rtype: None or the certificate in hex format.

        .. method:: peek_keypair_tag()

            gets the unique user defined name for Extension local certificate.

            :rtype: None or keypair-tag.

        .. method:: peek_certificate_name()

             Gets the certificate name.

            :rtype: None or certitifcate name.

        .. method:: peek_local_certificate()

             Gets if its a local certificate.

            :rtype: None or true/false.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.security_certificate_extension,
                         "/rest/running/brocade-security/security-certificate-extension",
                         version.VER_RANGE_900_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "certificate-entity", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "certificate", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "certificate-hexdump", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "local-certificate", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "keypair-tag", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "certificate-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.load(dictvalues, 1)
