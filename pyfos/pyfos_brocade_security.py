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
System Security.
************************************************************************************************
The :mod:`pyfos_brocade_security` module provides REST support for \
System Security.

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

            Return a :class:`radius_server` object with RADIUS server
                                            attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by the \
                :func:`pyfos_auth.login`.
            :rtype: The :class:`radius_server` object, if name is provided, \
                     or list of objects if there is more than one. \
                     A dictionary in case of error.

        .. method:: post(session)

            Create a RADIUS server entry. The required fields are set
            within the object using the attribute's set method.
            This method is used to create a new RADIUS server configuration for
            AAA authentication to a switch.

            Example Usage of the Method to Configure a New AAA RADIUS server:

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
            :rtype: A dictionary of errors or a success response.

        .. method:: patch(session)

            Edit an existing configuration. The required fields are set within
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

            Delete a RADIUS server entry. Fields involved are
            set within the object using attribute's
            set method. This method is used to delete a RADIUS server
            configuration.

            Example usage of the method to delete an RADIUS configuration:

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

            Sets the RADIUS name in the object.

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

            :param protocol: the RADIUS server authentication protocol type \
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

            Return a :class:`tacacs_server` object with TACACS+ Server
            attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: The :class:`tacacs_server` object, if name is provided, \
                or a list of objects if there is more than one. \
                A dictionary in case of error.

        .. method:: post(session)

            Create a TACACS+ server entry. The required fields are set
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
            :rtype: A dictionary of errors or a success response.

        .. method:: patch(session)

            Edit an existing configuration. The required fields are set within
            the object using the attribute's set method. This method is used \
            to modify the existing TACACS+ server configuration.

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

            Delete a TACACS+ server entry. The required fields are
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

    *Object Methods*

        .. staticmethod:: get(session, name=None)

            Return a :class:`ldap_server` object with LDAP Server
                             attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: The :class:`ldap_server` object, if name is provided, \
                or a list of objects if there is more than one. \
                A dictionary in case of error.

        .. method:: post(session)

            Create an LDAP server entry. The required fields are set
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
            :rtype: A dictionary of errors or a success response.

        .. method:: patch(session)

            Edit an existing configuration. The required fields are set within
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

            Delete an LDAP server entry. The required fields are
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

            :param name: the LDAP FQDN/IP to be set within the object.
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

        self.load(dictvalues, 1)


class auth_spec(pyfos_rest_util.rest_object):
    """This class configures the authentication mode and displays
       the authentication mode configuration.

    Important Class Members:

        +-------------------------------------------+----------------------------------+------------------------------------------------------+
        | Attribute name                            | Description                      |Frequently used methods                               |
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

            Sets the log messages enable or disable value in the object.

            :param bool: The log message enable or disable to be set within \
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

            Example Usage of the method to get ipfilter policies:

            .. code-block:: python

               # initialize the switch object
               ipfilter_obj=pyfos_brocade_security.ipfilter_policy.get(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: :class:`ipfilter_policy` object if name is given or list of
                objects if there are more than one. Dictionary in case of error

        .. method:: post(session)

            Create an ipfilter policy entry. Fields involved are set
            within the object using attribute's set method.
            This method is used to create a new ipfilter policy configuration.

            Example usage of the method to configure a new ipfilter policy:

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

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

        .. method:: patch(session)

            Fields involved are set within the object using attribute's set
            method. This method is used to perform actions such as commit,
            save, activate the policy, clone.

            Example usage of the method to perform clone operation:

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

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary in case of error or success response

        .. method:: delete(session)

            Delete an ipfilter policy. Fields involved are
            set within the object using attribute's
            set method. This method is used to delete an ipfilter policy
            configuration.

            Example usage of the method to delete an ipfilter policy
            configuration:

            .. code-block:: python

                # initialize the switch object
                ipfilter_obj = pyfos_brocade_security.ipfilter_policy()
                # set the policy name to delete
                ipfilter_obj.set_name("mypolicy")
                # execute HTTP delete command to apply the object to the
                # switch connected through session
                ipfilter_obj.delete(session)

    *Attribute methods*

        .. method:: set_name(name)

            Sets policy name in the object.

            :param name: policy name to be set within the object
            :rtype: dictionary in case of error or success response

        .. method:: peek_name()

            Reads the ipfilter policy name from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_ip_version(version)

            Sets policy ip version in the object.

            :param version: policy ip version (ipv4/ipv6) to be set within the
                            object

            :rtype: dictionary in case of error or success response

        .. method:: peek_ip_version()

            Reads the policy ip version from the object.

            :rtype: dictionary in case of error or success response

        .. method:: peek_is_policy_active()

            Reads the status of the policy from the object.

            :rtype: dictionary in case of error or success response

        .. method:: peek_is_default_policy()

            Reads whether default or user defined policy from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_action(ops)

            Sets the action to perform in the object.

            :param ops: ipfilter action to be set within the object
                   supported operations: clone, save, activate and
                   commit-and-activate

            :rtype: dictionary in case of error or success response

        .. method:: set_clone_destination_policy_name("myclone")

            Sets the destination policy name for the clone action in the object

            :rtype: dictionary in case of error or success response

        .. method:: peek_clone_destination_policy_name()

            Reads the destination policy name from the object.

            :rtype: dictionary in case of error or success response

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
    """This class provides the ipfilter rule information and also can configure
       the ipfilter rule.

    Important class members:

        +-------------------------------------------+----------------------------------+----------------------------------------------------+
        | Attribute name                            | Description                      |Frequently used methods                             |
        +===========================================+==================================+====================================================+
        | policy-name                               | Policy name                      |:func:`set_policy_name`                             |
        |                                           |                                  |:func:`peek_policy_name`                            |
        +-------------------------------------------+----------------------------------+----------------------------------------------------+
        | index                                     | Rule number                      |:func:`set_index`                                   |
        |                                           |                                  |:func:`peek_index`                                  |
        +-------------------------------------------+----------------------------------+----------------------------------------------------+
        | source-ip                                 | Source IP                        |:func:`set_source_ip`                               |
        |                                           |                                  |:func:`peek_source_ip`                              |
        +-------------------------------------------+----------------------------------+----------------------------------------------------+
        | destination-start-port                    | Destination start port           |:func:`set_destination_start_port`                  |
        |                                           |                                  |:func:`peek_destination_start_port`                 |
        +-------------------------------------------+----------------------------------+----------------------------------------------------+
        | destination-end-port                      | Destination end port             |:func:`set_destination_end_port`                    |
        |                                           |                                  |:func:`peek_destination_end_port`                   |
        +-------------------------------------------+----------------------------------+----------------------------------------------------+
        | protocol                                  | Protocol type                    |:func:`set_protocol`                                |
        |                                           |                                  |:func:`peek_protocol`                               |
        +-------------------------------------------+----------------------------------+----------------------------------------------------+
        | permission                                | Permission permit/deny           |:func:`set_permission`                              |
        |                                           |                                  |:func:`peek_permission`                             |
        +-------------------------------------------+----------------------------------+----------------------------------------------------+
        | traffic-type                              | Traffic type INPUT/FORWARD       |:func:`set_traffic_type`                            |
        |                                           |                                  |:func:`peek_traffic_type`                           |
        +-------------------------------------------+----------------------------------+----------------------------------------------------+
        | destination-ip                            | Destination IP                   |:func:`set_destination_ip`                          |
        |                                           |                                  |:func:`peek_destination_ip`                         |
        +-------------------------------------------+----------------------------------+----------------------------------------------------+

    *Object methods*

        .. staticmethod:: get(session, name=None)

            Return a :class:`ipfilter_rule` object filled with Ipfilter
                             rule attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: :class:`ipfilter_rule` object or dictionary in case of
                            error

        .. method:: post(session)

            Create an ipfilter rule entry. Fields involved are set
            within the object using attribute's set method.
            This method is used to create a new ipfilter rule.

            Example usage of the method to configure a new ipfilter rule:

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

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

        .. method:: delete(session)

            Delete an ipfilter rule. Fields involved are
            set within the object using attribute's
            set method. This method is used to delete a ipfilter rule
            configuration.

            Example usage of the method to delete an ipfilter rule
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

    *Attribute methods*

        .. method:: set_policy_name(name)

            Sets policy name in the object.

            :param name: policy name to be set within the object
            :rtype: dictionary in case of error or success response

        .. method:: peek_policy_name()

            Reads the ipfilter policy from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_index(index)

            Sets rule number in the object.

            :param index: rule number to be set within the object

            :rtype: dictionary in case of error or success response

        .. method:: peek_index()

            Reads the rule number from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_source_ip(ip)

            Sets source ip address in the object.

            :param ip: source ip to be set within the object

            :rtype: dictionary in case of error or success response

        .. method:: peek_source_ip()

            Reads the source ip from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_destination_start_port(port)

            Sets destination start port in the object.

            :param port: destination start port to be set within the object

            :rtype: dictionary in case of error or success response

        .. method:: peek_destination_start_port()

            Reads the destination start port from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_destination_end_port(port)

            Sets destination end port in the object.

            :param port: destination end port to be set within the object

            :rtype: dictionary in case of error or success response

        .. method:: peek_destination_end_port()

            Reads the destination end port from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_protocol(type)

            Sets protocol type in the object.

            :param type: protocol type to be set within the object

            :rtype: dictionary in case of error or success response

        .. method:: peek_protocol()

            Reads the protocol type from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_permission(type)

            Sets permission type in the object.

            :param type: permission type to be set within the object

            :rtype: dictionary in case of error or success response

        .. method:: peek_permission()

            Reads the permission type from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_traffic_type(type)

            Sets traffic type in the object.

            :param type: traffic type to be set within the object

            :rtype: dictionary in case of error or success response

        .. method:: peek_traffic_type()

            Reads the traffic type from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_destination_ip(ip)

            Sets destination ip address in the object.

            :param ip: destination ip to be set within the object

            :rtype: dictionary in case of error or success response

        .. method:: peek_destination_ip()

            Reads the destination ip from the object.

            :rtype: dictionary in case of error or success response

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

    Important class members:

        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+
        | Attribute name                                 | Description                      |Frequently used methods                                              |
        +================================================+==================================+=====================================================================+
        | ssh-cipher					 | SSH cipher configuration         |:func:`peek_ssh_cipher`					          |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+
        | ssh-kex				         | SSH kex configuration            |:func:`peek_ssh_kex`				                  |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+
        | ssh-mac				         | SSH mac configuration            |:func:`peek_ssh_mac`				                  |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+
        | https-cipher			                 | HTTPS cipher configuration       |:func:`peek_https_cipher`			                          |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+
        | radius-cipher    	                         | Radius cipher configuration      |:func:`peek_radius_cipher`		                                  |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+
        | ldap-cipher	                                 | Ldap cipher configuration        |:func:`peek_ldap_cipher`  		                                  |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+
        | syslog-cipher 	                         | Syslog cipher configuration      |:func:`peek_syslog_cipher`		                                  |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+
        | https-tls-protocol		                 | TLS Protocol version for HTTPS   |:func:`peek_ttps_tls_protocol`      	                          |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+
        | radius-tls-protocol  		                 | TLS Protocol version for RADIUS  |:func:`peek_radius_tls_protocol`                       		  |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+
        | ldap-tls-protocol    		                 | TLS Protocol version for LDAP    |:func:`peek_ldap_tls_protocol`                             	  |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+
        | syslog-tls-protocol		                 | TLS Protocol version for SYSLOG  |:func:`peek_syslog_tls_protocol`                            	  |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+
        | x509v3-validation-mode                         | X509 validation mode selection   |:func:`peek_x509v3_validation_mode`                                  |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------------------+

    *Object methods*

        .. staticmethod:: get()

            Return a :class:`sec_crypto_cfg` object filled with cryptographic
                      attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: :class:`sec_crypto_cfg` object or dictionary in case of
                            error.

    *Attribute methods*

        .. method:: peek_ssh_cipher()

            Reads ssh cipher algorithm from the object.

            :rtype: dictionary in case of error or success response

        .. method:: peek_ssh_kex()

            Reads ssh kex algorithm from the object.

            :rtype: dictionary in case of error or success response

        .. method:: peek_ssh_mac()

            Reads ssh mac algorithm from the object.

            :rtype: dictionary in case of error or success response

        .. method:: peek_https_cipher()

            Reads https cipher algorithm from the object.

            :rtype: dictionary in case of error or success response

        .. method:: peek_radius_cipher()

            Reads radius cipher algorithm from the object.

            :rtype: dictionary in case of error or success response

        .. method:: peek_ldap_cipher()

            Reads ldap cipher algorithm from the object.

            :rtype: dictionary in case of error or success response

        .. method:: peek_syslog_cipher()

            Reads syslog cipher algorithm from the object.

            :rtype: dictionary in case of error or success response

        .. method:: peek_https_tls_protocol()

            Reads TLS protocol version for https from the object.

            :rtype: dictionary in case of error or success response

        .. method:: peek_radius_tls_protocol()

            Reads TLS protocol version for radius from the object.

            :rtype: dictionary in case of error or success response

        .. method:: peek_ldap_tls_protocol()

            Reads TLS protocol version for ldap from the object.

            :rtype: dictionary in case of error or success response

        .. method:: peek_syslog_tls_protocol()

            Reads TLS protocol version for syslog from the object.

            :rtype: dictionary in case of error or success response

        .. method:: peek_x509v3_validation_mode()

            Reads X509 validation mode selection from the object.

            :rtype: dictionary in case of error or success response

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

    Important class members:

        +------------------------------------------------+----------------------------------+--------------------------------------------------------+
        | Attribute name                                 | Description                      |Frequently used methods                                 |
        +================================================+==================================+========================================================+
        | name                                           | Template name                    |:func:`peek_name`                                       |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------+
        | template                                       | Template Content                 |:func:`peek_template`                                   |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------+

    *Object methods*

        .. staticmethod:: get(session, name=None)
            Return a :class:`sec_crypto_cfg_template` object filled with
                             template contents.

            Each object can be printed using :func:`pyfos_util.response_print`

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: :class:`sec_crypto_cfg_template` object if name is given or
               list of objects if name is None. Dictionary in case of error.

    *Attribute methods*
        .. method:: peek_name()

            Reads the template name from the object.

            :rtype: dictionary in case of error or success response

        .. method:: peek_template()

            Reads the template content from the object.

            :rtype: dictionary in case of error or success response
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
    """This class provides the cryptographic template configurations and
       operations.

    Important class members:

        +------------------------------------------------+----------------------------------+--------------------------------------------------------+
        | Attribute name                                 | Description                      |Frequently used methods                                 |
        +================================================+==================================+========================================================+
        | template-name                                  | Template name                    |:func:`set_template_name`                               |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------+
        | action                                         | Set crypto action                |:func:`set_action`                                      |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-user-name                               | Set remote user login name       |:func:`set_remote_user_name`                            |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-host-ip                                 | Set remote host ip               |:func:`set_remote_host_ip`                              |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-user-password                           | Set remote user password         |:func:`set_remote_user_password`                        |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------+
        | remote-directory                               | Remote directory file path       |:func:`set_remote_directory`                            |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------+
        | file-transfer-protocol-type                    | Set file transfer protocol type  |:func:`set_file_transfer_protocol_type`                 |
        +------------------------------------------------+----------------------------------+--------------------------------------------------------+

    *Object methods*

        .. method:: patch(session)

            Fields involved are set within the object using attribute's
            set method. This method is used to set import/export cryptographic
            template which is configured in host machine, verify and apply
            template.

            Example usage of the method to apply cipher configuration:

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

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary in case of error or success response

        .. method:: delete(session)

            Delete a user defined template. Fields involved are
            set within the object using attribute's
            set method. This command is used to delete user defined template

            Example usage of the method to delete a user defined template:

                # initialize the switch object
                crypto_obj = pyfos_brocade_security.sec_crypto_cfg_template()
                # set the template name
                crypto_obj.set_template_name("mytemplate")
                crypto_obj.delete(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

    *Attribute methods*

        .. method:: set_template_name(name)

            Sets template  name in the object.

            :param name: default template name to be set within the object
            :rtype: dictionary in case of error or success response

        .. method:: set_action(ops)

            Sets seccryptographic action in the object.

            :param ops: seccryptographic action to be set within the object
            :rtype: dictionary in case of error or success response

        .. method:: set_remote_user_name(loginname)

            Sets remote user login name in the object.

            :param loginname: remote user login name name to be set within the
                              object
            :rtype: dictionary in case of error or success response

        .. method:: set_remote_host_ip(ip)

            Sets remote user ip in the object.

            :param ip: remote user ip to be set within the object
            :rtype: dictionary in case of error or success response

        .. method:: set_remote_user_password(passwd)

            Sets remote user password in the object.

            :param passwd: remote user password to be set within the object
            :rtype: dictionary in case of error or success response

        .. method:: set_remote_directory(template_file)

            Sets the template file path in the object.

            :param template_file: template file path to be set within the
                                  object
            :rtype: dictionary in case of error or success response

        .. method:: set_file_transfer_protocol_type(protocol)

            Sets file transfer protocol in the object.

            :param protocol: file transfer protocol to be set within the object
            :rtype: dictionary in case of error or success response

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
    """Class of LDAP Role mapping configuration
               Important class members:

    Important class members:

        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | Attribute name                    | Description                   |Frequstly used methods                                 |
        +===================================+===============================+=======================================================+
        | ldap-role                         | LDAP role to be mapped to     |:func:`set_ldap_role`                                  |
        |                                   | a switch role                 |:func:`peek_ldap_role`                                 |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | switch-role                       | switch role to which the LDAP |:func:`set_switch_role`                                |
        |                                   | role is mapped.               |:func:`peek_switch_role`                               |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | home-virtual-fabric               | home VF ID                    |:func:`set_home_virtual_fabric`                        |
        |                                   |                               |:func:`peek_home_virtual_fabric`                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | chassis-access-role               | chassis level role            |:func:`set_chassis_access_role`                        |
        |                                   |                               |:func:`peek_chassis_access_role`                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+

    *Object methods*

        .. method:: get(session)

            Return :class`ldap_role_map`
            object with values for all the attributes.
            The object can be printed using :func:`pyfos_utils.response_print`

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or
                :class:`ldap_role_map` object

        .. method:: post(session)

            Create an entry. Fields involved are set within the object using
            attribute's set method.  This command is used to create
            a ldap_map_role.

            Example usage of the method to create a new cfg::

                ldap_cfg_obj =
                    pyfos_ldapcfg.ldap_role_map()
                ldap_cfg_obj.set_ldap_role("ldapRole")
                ldap_cfg_obj.set_switch_role("switchRole")
                ldap_cfg_obj.post(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

        .. method:: patch()

            To modify ldap configuration such as vf-list, vf-role-list etc.
            Fields involved are set within the object using
            attribute's set method.

            Example usage of the method to modify existing ldaprole cfg::

                ldap_cfg_obj =
                    pyfos_ldapcfg.ldap_role_map()
                ldap_cfg_obj.set_ldap_role("ldapRole")
                ldap_cfg_obj.set_chassis_access_role("admin")
                ldap_cfg_obj.set_home_virtual_fabric(128)
                ldap_cfg_obj.patch(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

        .. method:: delete()

            Delete an LDAP role mapping. Fields involved are
            set within the object using attribute's
            set method. This command is used to delete LDAP role mapping.

            Example usage of the method to delete an existing LDAP role map::

               ldap_cfg_obj =
                    pyfos_ldapcfg.ldap_role_map()
                ldap_cfg_obj.set_ldap_role("ldapRole")
                ldap_cfg_obj.delete(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

    *Attribute methods*

        .. method:: set_ldap_role(role)

           Sets ldap role in the object

            :param role: LDAP role to be mapped to a switch role
            :rtype: dictionary of error or success response

        .. method:: peek_ldap_role()

            Reads ldap role from the object.

            :rtype: None or ldap_role

        .. method:: set_switch_role(role)

                Sets switch role in the object

            :param role: switch role to which the  LDAP  role is mapped
            :rtype: dictionary of error or success response

        .. method:: peek_switch_role()

            Reads switch role from the object.

            :rtype: None or switch_role

        .. method:: set_home_virtual_fabric(fcid)

                Sets home virtual fabric in the object

            :param fcid: default virtual fabric switch context
            :rtype: dictionary of error or success response

        .. method:: peek_home_virtual_fabric()

            Reads home virtual fabric from the object.

            :rtype: None or home_virtual_fabric

        .. method:: set_chassis_access_role(role)

                Sets chassis access role in the object

            :param role: chassis level role
            :rtype: dictionary of error or success response

        .. method:: peek_chassis_access_role()

            Reads chassis access role from the object.

            :rtype: None or chassis_access_role

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
    """Class of password configuration
                Important class members:

        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | Attribute name                    | Description                   |Frequstly used methods                                 |
        +===================================+===============================+=======================================================+
        | minimum-length                    | Minimum length of the password|:func:`set_minimum_length`                             |
        |                                   |                               |:func:`peek_minimum_length`                            |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | character-set                     | Minimum criteria on the       |:func:`set_character_set`                              |
        |                                   | character set                 |:func:`peek_character_set`                             |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | user-name-allowed                 | Enable/disable username is    |:func:`set_user_name_allowed`                          |
        |                                   | allowed in the password       |:func:`peek_user_name_allowed`                         |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | minimum-lower-case-character      | Minimum number of lowercase   |:func:`set_minimum_lower_case_character`               |
        |                                   | alphabetic characters         |:func:`peek_minimum_lower_case_character`              |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | minimum-upper-case-character      | Minimum number of uppercase   |:func:`set_minimum_upper_case_character`               |
        |                                   | alphabetic characters         |:func:`peek_minimum_upper_case_character`              |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | minimum-numeric-character         | Minimum number of digits      |:func:`set_minimum_numeric_character`                  |
        |                                   |                               |:func:`peek_minimum_numeric_character`                 |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | minimum-special-character         | Minimum number of punctuation |:func:`set_minimum_special_character`                  |
        |                                   | characters                    |:func:`peek_minimum_special_character`                 |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | past-password-history             | Number of past password value |:func:`set_past_password_history`                      |
        |                                   | that are disallowed           |:func:`peek_past_password_history`                     |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | minimum-password-age              | Minimum number of days before |:func:`set_minimum_password_age`                       |
        |                                   | which password cannot be      |:func:`peek_minimum_password_age`                      |
        |                                   | modified                      |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | maximum-password-age              | Maximum number of days after  |:func:`set_maximum_password_age`                       |
        |                                   | which the password should be  |:func:`peek_maximum_password_age`                      |
        |                                   | modified                      |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | warn-on-expire                    | Number of days prior to       |:func:`set_warn_on_expire`                             |
        |                                   | password expiration when the  |:func:`peek_warn_on_expire`                            |
        |                                   | user should be warned         |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | lock-out-threshold                | Number of time user can give  |:func:`set_lock_out_threshold`                         |
        |                                   | incorrect password            |:func:`peek_lock_out_threshold`                        |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | lock-out-duration                 | Lockout duration in minutes   |:func:`set_lock_out_duration`                          |
        |                                   |                               |:func:`peek_lock_out_duration`                         |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | admin-lock-out-enabled            | Enable/disable admin lockout  |:func:`set_admin_lock_out_enabled`                     |
        |                                   |                               |:func:`peek_admin_lock_out_enabled`                    |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | repeat-character-limit            | Length of the character       |:func:`set_repeat_character_limit`                     |
        |                                   | sequences                     |:func:`peek_repeat_character_limit`                    |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | sequence-character-limit          | Length of sequential character|:func:`set_sequence_character_limit`                   |
        |                                   | sequences                     |:func:`peek_sequence_character_limit`                  |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | password-config-changed           | Indicates account default     |:func:`peek_password_config_changed`                   |
        |                                   | configuration or not          |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | reverse-user-name-allowed         | Allow/disallow reverse user   |:func:`set_reverse_user_name_allowed`                  |
        |                                   | name in password              |:func:`peek_reverse_user_name_allowed`                 |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | hash-type                         | Hash type                     |:func:`set_hash_type`                                  |
        |                                   |                               |:func:`peek_hash_type`                                 |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | manual-hash-enabled               | Enable/disable manual hash    |:func:`set_manual_hash_enabled`                        |
        |                                   |                               |:func:`peek_manual_hash_enabled`                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | enforce-expire                    | Expires the password for user |:func:`set_enforce_expire`                             |
        |                                   |                               |:func:`peek_enforce_expire`                            |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | minimum-difference                | Number of character difference|:func:`set_minimum_difference`                         |
        |                                   | expected between old and new  |:func:`peek_minimum_difference`                        |
        |                                   | password                      |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | password-action                   | Password configuration action |:func:`set_password_action`                            |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+

       *Object methods*
        .. method:: get(session)

            Return :class`password_cfg`
            object with values for all the attributes.
            The object can be printed using :func:`pyfos_utils.response_print`

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or
                :class:`password_cfg` object

        .. method:: patch()

            To modify password configuration.
            Fields involved are set within the object using attribute's
            set method.

            Example usage of the method to modify global password
            configuration::

                password_obj =
                    pyfos_password_cfg.password_cfg()
                password_obj.set_password_action("global-config")
                password_obj.set_minimum_length(10)
                password_obj.set_user_name_allowed(0)
                password_obj.patch(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

        .. method:: delete(session)

            Delete a user defined password configuration.
            Fields involved are set within the object using attribute's
            set method. This command is used to delete password configuration.

            Example usage of the method to delete a password configuration::

                password_obj =
                    pyfos_password_cfg.password_cfg()
                password_obj.set_password_action("delete-all")
                password_obj.delete(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

       *Attribute methods*

        .. method:: set_minimum_length(length)

                Sets minimum length of the password in the object

            :param length: minimum length of the password
            :rtype: dictionary in case of error or success response

        .. method:: peek_minimum_length()

            Reads minimum length of the password from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_character_set(criteria)

                Sets minimum criteria for the password ot the object

            :param criteria: minimum criteria on the password
            :rtype: dictionary in case of error or success response

        .. method::peek_character_set()

            Reads minimum criteria from the object.

            :rtype: dictionary in case of error or success response

        .. method:: peek_minimum_length()

            Reads minimum criteria from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_user_name_allowed(bool)

                Sets enable/disable username allowed to the object

            :param bool: enable/disable username allowed
            :rtype: dictionary in case of error or success response

        .. method:: peek_user_name_allowed()

            Reads username allowed in password or not from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_minimum_lower_case_character(number)

                Sets minimum lowercase character to the object

            :param number: minimum number of lowercase character
            :rtype: dictionary in case of error or success response

        .. method:: peek_minimum_lower_case_character()

            Reads minimum number of lowercase character from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_minimum_upper_case_character(number)

                Sets minimum uppercase character to the object

            :param number: minimum number of uppercase character
            :rtype: dictionary in case of error or success response

        .. method:: peek_minimum_upper_case_character()

            Reads minimum number of uppercase character from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_minimum_numeric_character(number)

                Sets minimum digits to the object

            :param number: minimum number of digits
            :rtype: dictionary in case of error or success response

        .. method:: peek_minimum_numeric_character()

            Reads minimum number of digits from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_minimum_special_character(number)

                Sets minimum punctuational character to the object

            :param number: minimum number of punctuational character
            :rtype: dictionary in case of error or success response

        .. method:: peek_minimum_special_character()

            Reads minimum number of punctuational character from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_past_password_history(number)

                Sets number of past password disallowed to the object

            :param number: number of past password disallowed
            :rtype: dictionary in case of error or success response

        .. method:: peek_past_password_history()

            Reads number of past password disallowed from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_minimum_password_age(number)

                Sets minimum number of days before which the password cannot be
                modified

            :param number: minimum number of days
            :rtype: dictionary in case of error or success response

        .. method:: peek_minimum_password_age()

            Reads minimum number of days of password age from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_maximum_password_age(number)

                Sets maximum number of days after which the password should be
                modified

            :param number: maximum number of days
            :rtype: dictionary in case of error or success response

        .. method:: peek_maximum_password_age()

            Reads maximum number of days of password age from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_warn_on_expire(number)

                Sets number of days prior to password expiration to the object

            :param number: number of days
            :rtype: dictionary in case of error or success response

        .. method:: peek_warn_on_expire()

            Reads number of days prior to password expiration from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_lock_out_threshold(times)

                Sets number of times a user can specify an incorrect password
                 to the object

            :param times: number of times
            :rtype: dictionary in case of error or success response

        .. method:: peek_lock_out_threshold()

            Reads number of times ia user can specify an incorrect password
            from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_lock_out_duration(times)

                Sets the time, in minutes, after which a previously locked
                account automatically unlocks to the object

            :param times: number of minutes
            :rtype: dictionary in case of error or success response

        .. method:: peek_lock_out_duration()

            Reads the minutes for automatically unlocks the locked accout
            from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_admin_lock_out_enabled(bool)

                Sets enable/disable admin lockout to the object

            :param bool: enable/disable admin lockout
            :rtype: dictionary in case of error or success response

        .. method:: peek_admin_lock_out_enabled()

            Reads admin lockout status from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_repeat_character_limit(length)

                Sets length of repeated character sequences to the object

            :param length: length of repeated character sequences
            :rtype: dictionary in case of error or success response

        .. method:: peek_repeat_character_limit(length)

            Reads length of repeated character sequences from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_sequence_character_limit(length)

                Sets length of sequential character sequences to the object

            :param length: length of sequential character sequences
            :rtype: dictionary in case of error or success response

        .. method:: peek_sequence_character_limit()

            Reads length of sequential character sequences from the object.

            :rtype: dictionary in case of error or success response

        .. method:: peek_password_config_changed()

            Reads status of the userdefined configuration or default
            configuration from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_reverse_user_name_allowed(bool)

                Sets enable/disable reverse user name in password to the object

            :param bool: status of the reverse user name
            :rtype: dictionary in case of error or success response

        .. method:: peek_reverse_user_name_allowed()

            Reads status of the reverse user name from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_hash_type(hash)

                Sets hash type to the object

            :param hash: hash type for the password
            :rtype: dictionary in case of error or success response

        .. method:: peek_hash_type()

            Reads hash type from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_manual_hash_enabled(bool)

                Sets enable/disable manual hash to the object

            :param bool: status of the hash type change can be manual or not
            :rtype: dictionary in case of error or success response

        .. method:: peek_manual_hash_enabled()

            Reads status of the hash type change can be manual or not
            from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_enforce_expire(bool)

                Sets enable/disable password expiration for the user
                to the object

            :param bool: enable/disable password expiration
            :rtype: dictionary in case of error or success response

        .. method:: peek_enforce_expire()

            Reads status of the password expiration for the user
            from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_password_action(ops)

                Sets password action to be perform to the object

            :param ops: password action to be perform
            :rtype: dictionary in case of error or success response

        .. method:: set_minimum_difference(value)

                Sets minimum difference expected between the old and new
                password

            :param value: minimum difference between old and new password
            :rtype: dictionary in case of error or success response

        .. method:: peek_minimum_difference()

            Reads the value of minimum difference between old and new password
            from the object.

            :rtype: dictionary in case of error or success response
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
                Important class members:

        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | Attribute name                    | Description                   |Frequstly used methods                                 |
        +===================================+===============================+=======================================================+
        | user-name                         | User Name                     |:func:`set_user_name`                                  |
        |                                   |                               |:func:`peek_user_name`                                 |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | minimum-password-age              | Minimum number of days before |:func:`set_minimum_password_age`                       |
        |                                   | which the password cannot be  |:func:`peek_minimum_password_age`                      |
        |                                   | modified                      |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | maximum-password-age              | Maximum number of days after  |:func:`set_maximum_password_age`                       |
        |                                   | which the password should be  |:func:`peek_maximum_password_age`                      |
        |                                   | modified                      |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | warn-on-expire                    | Number of days prior to       |:func:`set_warn_on_expire`                             |
        |                                   | password expiration           |:func:`peek_warn_on_expire`                            |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | enforce-expire                    | Enable/disable expires the    |:func:`set_enforce_expire`                             |
        |                                   | password for user             |:func:`peek_enforce_expire`                            |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | hash-type                         | Hash type                     |:func:`set_hash_type`                                  |
        |                                   |                               |:func:`peek_hash_type`                                 |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+

       *Object methods*
        .. method:: get(session)

            Return :class`user_specific_password_cfg`
            object with values for all the attributes.
            The object can be printed using :func:`pyfos_utils.response_print`

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or
                :class:`user_specific_password_cfg` object

        .. method:: post(session)

            Create a password configuration for specific user.
            Fields involved are set within the object using attribute's set
            method.  This command is used to create a password configuration
            for specific user.

            Example usage of the method to create a new configuration::

                password_obj =
                    pyfos_password_cfg.password_cfg()
                password_obj.set_user_name("mytestuser")
                password_obj.set_minimum_password_age(10)
                password_obj.set_maximum_password_age(20)
                password_obj.set_warn_on_expire(5)
                password_obj.post(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

        .. method:: patch()

            To modify user specific password configuration.
            Fields involved are set within the object using attribute's
            set method.

            Example usage of the method to modify user password configuration::

                password_obj =
                    pyfos_password_cfg.password_cfg()
                password_obj.set_minimum_length(10)
                password_obj.set_maximum_length(20)
                password_obj.patch(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

        .. method:: delete(session)

            Delete a user defined password configuration.
            Fields involved are set within the object using attribute's
            set method. This command is used to delete password configuration.

            Example usage of the method to delete a user specific password
            configuration::

                password_obj =
                    pyfos_password_cfg.password_cfg()
                password_obj.set_user_name("mytestuser")
                password_obj.delete(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

       *Attribute methods*

        .. method:: set_user_name(name)

           Sets user name in the object

            :param name: user name for the password configuration
            :rtype: dictionary in case of error or success response

        .. method:: peek_user_name

            Reads user name from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_minimum_password_age(number)

                Sets minimum number of days before which the password cannot be
                modified

            :param number: minimum number of days
            :rtype: dictionary in case of error or success response

        .. method:: peek_minimum_password_age()

            Reads minimum number of days of password age from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_maximum_password_age(number)

                Sets maximum number of days after which the password should be
                modified

            :param number: maximum number of days
            :rtype: dictionary in case of error or success response

        .. method:: peek_maximum_password_age()

            Reads maximum number of days of password age from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_warn_on_expire(number)

                Sets number of days prior to password expiration to the object

            :param number: number of days
            :rtype: dictionary in case of error or success response

        .. method:: peek_warn_on_expire()

            Reads number of days prior to password expiration from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_hash_type(hash)

                Sets hash type to the object

            :param hash: hash type for the password
            :rtype: dictionary in case of error or success response

        .. method:: peek_hash_type()

            Reads hash type from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_enforce_expire(bool)

                Sets enable/disable password expiration for the user
                to the object

            :param bool: enable/disable password expiration
            :rtype: dictionary in case of error or success response

        .. method:: peek_enforce_expire()

            Reads status of the password expiration for the user
            from the object.

            :rtype: dictionary in case of error or success response

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
    """Class of user configuration
               Important class members:

        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | Attribute name                    | Description                   |Frequstly used methods                                 |
        +===================================+===============================+=======================================================+
        | name                              | Name of the user account      |:func:`set_name`                                       |
        |                                   |                               |:func:`peek_name`                                      |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | password                          | User account password         |:func:`set_password`                                   |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | role                              | Use role name                 |:func:`set_role`                                       |
        |                                   |                               |:func:`peek_role`                                      |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | account-description               | Account description           |:func:`set_account_description`                        |
        |                                   |                               |:func:`peek_account_description`                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | account-enabled                   | Indicates user account status |:func:`set_account_enabled`                            |
        |                                   |                               |:func:`peek_account_enabled`                           |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | password-change-enforced          | Enable/disable password       |:func:`set_password_change_enforced`                   |
        |                                   | change enforce while login    |:func:`peek_password_change_enforced`                  |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | account-locked                    | Unlocks the user accout if    |:func:`set_account_locked`                             |
        |                                   | it locked already             |:func:`peek_account_locked`                            |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | access-start-time                 | Access start time for account |:func:`set_access_start_time`                          |
        |                                   |                               |:func:`peek_access_start_time`                         |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | access-end-time                   | Access end time for account   |:func:`set_access_end_time`                            |
        |                                   |                               |:func:`peek_access_end_time`                           |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | home-virtual-fabric               | Home Virtual Fabric for       |:func:`set_home_virtual_fabric`                        |
        |                                   | account                       |:func:`peek_home_virtual_fabric`                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | chassis-access-role               | Chassis access role name      |:func:`set_chassis_access_role`                        |
        |                                   |                               |:func:`peek_chassis_access_role`                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | virtual-fabric-role-id-list/      | Virtual Fabric role name list |:func:`set_virtual_fabric_role_id_list_role_id`        |
        |              role-id              |                               |:func:`peek_virtual_fabric_role_id_list_role_id`       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+

       *Attribute methods*

        .. staticmethod:: get(session, name=None)

            Return a :class:`user_config` object filled with user config
                             attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: :class:`user_config` object if name is given or list of
                objects if there are more than one. Dictionary in case of error

        .. method:: post(session)

            Create a user account. Fields involved are set
            within the object using attribute's set method.
            This method is used to create a new user account configuration.

            Example usage of the method to configure a new user account:

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

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

        .. method:: patch(session)

            Replace existing configuration. Fields involved are set within
            the object using attribute's set method. This method is used to
            modifying the existing user account configuration.

            Example usage of the method to configure response timeout:

            .. code-block:: python

                # initialize the user config object
                user_info = pyfos_brocade_security.user_config()
                user_info.set_name("myuser")
                user_info.set_account_enabled(1)
                user_info.set_password_change_enforced(0)
                # execute HTTP patch command to apply the object to the
                # switch connected through session
                user_info.patch(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary in case of error or success response

        .. method:: delete(session)

            Delete a user account. Fields involved are
            set within the object using attribute's
            set method. This method is used to delete a user account
            configuration.

            Example usage of the method to delete a user account:

            .. code-block:: python

                # initialize the user config object
                user_obj = pyfos_brocade_security.user_config()
                user_obj.set_name("myuser")
                # execute HTTP delete command to apply the object to the
                # switch connected through session
                user_obj.delete(session)

       *Attribute methods*

        .. method:: set_name(name)

           Sets user account name in the object

            :param name: User account name to be set within the object
            :rtype: dictionary of error or success response

        .. method:: peek_name()

            Reads user account name from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_password(pass)

           Sets user account password in the object.

            :param pass: user account password to be set within the object
            :rtype: dictionary in case of error or success response

        .. method:: set_role(role)

           Sets user role in the object

            :param role: User role to be set within the object
            :rtype: dictionary of error or success response

        .. method:: peek_role()

            Reads user role from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_account_description(message)

           Sets user account description in the object

            :param message: user account description to be set within the
                            object
            :rtype: dictionary of error or success response

        .. method:: peek_account_description()

            Reads user account description from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_account_enabled(bool)

           Sets enable/disable user account in the object

            :param bool: enable/disable user account to be set within the
                         object
            :rtype: dictionary of error or success response

        .. method:: peek_account_enabled()

            Reads status of user account from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_password_change_enforced(bool)

           Sets enable/disable password change while login in the object

            :param bool: enable/disable password change to be set within the
                         object
            :rtype: dictionary of error or success response

        .. method:: peek_password_change_enforced()

            Reads status password change while login from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_account_locked(bool)

           Sets unlocks user account if already locked in the object

            :param bool: Unlocks user account to be set within the object
            :rtype: dictionary of error or success response

        .. method:: peek_account_locked()

            Reads status of user account about locked/unlocked from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_access_start_time(time)

           Sets user access start time in the object

            :param time: access start time to be set within the object
            :rtype: dictionary of error or success response

        .. method:: peek_access_start_time()

            Reads access start time from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_access_end_time(time)

           Sets user access end time in the object

            :param time: access end time to be set within the object
            :rtype: dictionary of error or success response

        .. method:: peek_access_end_time()

            Reads access end time from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_home_virtual_fabric(fid)

           Sets user account home fid in the object

            :param fid: home fid to be set within the object
            :rtype: dictionary of error or success response

        .. method:: peek_home_virtual_fabric()

            Reads account home fid from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_chassis_access_role(role)

           Sets chassis access role in the object

            :param role: chassis access role to be set within the object
            :rtype: dictionary of error or success response

        .. method:: peek_chassis_access_role()

            Reads chassis access role from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_virtual_fabric_role_id_list_role_id(roles)

           Sets virtual fabric roles in the object

            :param roles: virtual fabric role and id set within the object
            :rtype: dictionary of error or success response

        .. method:: peek_virtual_fabric_role_id_list_role_id()

            Reads virtual fabric role and id from the object.

            :rtype: dictionary in case of error or success response

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
    """ This class provides methods/options to manage
    and configure public and private key pairs in a switch.

    Important class members:

        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | Attribute name                                 | Description                      |Frequently used methods                                  |
        +================================================+==================================+=========================================================+
        | allow-user-name                                | user name                        |:func:`set_allow_user_name`                              |
        |                                                |                                  |:func:`peek_allow_user_name`                             |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | rekey-interval                                 | rekey interval duration          |:func:`set_rekey_interval`                               |
        |                                                |                                  |:func:`peek_rekey_interval`                              |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+

    *Object methods*

        .. method:: get()

            Return :class:`sshutil`
            object with values for all the attributes.
            The object can be printed using :func:`pyfos_utils.response_print`

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or
                :class:`sshutil` object

        .. method:: patch()

            Replace entry members. Fields involved are set within the object
            using attribute's set method. This command is used to
            Import public key from remote host to switch,
            Export public key from switch to a remote host.

            Example usage of the method to export public key:

            .. code-block:: python

                sshutil_obj =
                    pyfos_brocade_security.sshutil()
                sshutil_obj.export_public_key("10.70.4.109", "/root/ca",
                                                   "root", "pray4green")
                sshutil_obj.patch(session)

            Example usage of the method to import public key:

            .. code-block:: python

                sshutil_obj =
                    pyfos_brocade_security.sshutil()
                sshutil_obj.import_export_key("test","10.70.4.109", "/root/ca",
                                                "key.pub","root", "pray4green")
                sshutil_obj.patch(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

    *Attribute methods*

        .. method:: set_allow_user_name("user")

            Sets user name in the object

            :param pgid: allow user name
            :rtype: dictionary of error or success response

        .. method:: peek_allow_user_name()

            Reads allow user name in the object.

            :rtype: None or pgid

        .. method:: set_rekey_interval(int)

             Sets rekey interval duration in the object

            :param interval: rekey interval duration
            :rtype: dictionary of error or success response

        .. method:: peek_rekey_interval()

            Reads rekey interval duration in the object.

            :rtype: None or multiple fabric name monitoring mode status

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

    Important class members:

        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | Attribute name                                 | Description                      |Frequently used methods                                  |
        +================================================+==================================+=========================================================+
        | key-type                                       | key type                         |:func:`set_key_type`                                     |
        |                                                |                                  |:func:`peek_key_type`                                    |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | passphrase                                     | Passphrase for the key           |:func:`set_passphrase`                                   |
        |                                                |                                  |:func:`peek_passphrase`                                  |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | algorithm-type                                 | Algorithm type                   |:func:`set_algorithm_type`                               |
        |                                                |                                  |:func:`peek_algorithm_type`                              |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | size                                           | size                             |:func:`peek_size`                                        |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | fingerprint                                    | fingerprint                      |:func:`peek_fingerprint`                                 |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+

    *Object methods*

        .. method:: get()

            Return :class:`sshutilkey`
            object with values for all the attributes.
            The object can be printed using :func:`pyfos_utils.response_print`

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or
                :class:`sshutil` object

        .. method:: post()

            Create an entry or add members. Fields involved are set
            within the object using attribute's set method.
            This method is used to create a host key or
            public and private key pair.

            Example usage of the method to create a new host key:

            .. code-block:: python

                sshutil_obj =
                    pyfos_brocade_security.sshutilkey()
                sshutil_obj.generate_public_key("rsa", "fibranne")
                sshutil_obj.generate_host_key("rsa")
                sshutil_obj.post(session)

            The above example will generate public/private key pair and
            host key with rsa algorithm.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

        .. method:: delete()

            Delete an entry or entry members. Fields involved are
            set within the object using attribute's
            set method. This command is used to delete public key(s) or
            private key or delknownhost(s) or hostkey.

            Example usage of the method to delete public key:

            .. code-block:: python

                sshutil_obj =
                    pyfos_brocade_security.sshutilkey()
                sshutil_obj.delete_public_keys("user")
                sshutil_obj.delete_host_keys("user")
                sshutil_obj.delete(session)

            Example usage of the method to delete private key:

            .. code-block:: python

                sshutil_obj =
                    pyfos_brocade_security.sshutilkey()
                sshutil_obj.delete_private_key("user")
                sshutil_obj.delete(session)

            Example usage of the method to delete host key:

            .. code-block:: python

                sshutil_obj =
                    pyfos_brocade_security.sshutilkey()
                sshutil_obj.delete_host_key("rsa")
                sshutil_obj.delete(session)

            Example usage of the method to delete known host:

    *Attribute methods*

        .. method:: set_key_type("type")

            Sets key type in the object

            :param pgid: key type(public-private-key or host-key)
            :rtype: dictionary of error or success response

        .. method:: peek_key_type()

            Reads key type in the object.

            :rtype: None or pgid

        .. method:: set_passphrase(password)

             Sets passphrase for key generation in the object

            :param password: password for generating key
            :rtype: dictionary of error or success response

        .. method:: set_algorithm_type(type)

             Sets algorithm type in the object

            :param algorithm type: algorithm type(rsa/dsa/ecdsa)
            :rtype: dictionary of error or success response

        .. method:: peek_size()

            Reads size in the object.

            :rtype: None or multiple fabric name monitoring mode status

        .. method:: peek_fingerprint()

             Reads finger print in the object

            :param operation: finger print
            :rtype: dictionary of error or success response

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
    """ This class provides methods/options to manage
    and configure public and private key pairs in a switch.

    Important class members:

        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | Attribute name                                 | Description                      |Frequently used methods                                  |
        +================================================+==================================+=========================================================+
        | user-name                                      | user name                        |:func:`set_user_name`                                    |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | public-key-name                                | Public key name                  |:func:`set_public_key_name`                              |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | remote-host-ip                                 | user name for the remote host    |:func:`set_remote_host_ip`                               |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | remote-directory                               | Directory in remote host         |:func:`set_remote_dir`                                   |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | remote-user-name                               | user name for the host           |:func:`set_remote_user_name`                             |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | remote-user-password                           | Password for the remote user     |:func:`set_remote_user_password`                         |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | algorithm-type                                 | Algorithm type                   |:func:`set_algorithm_type`                               |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | action                                         | sshutil operations               |:func:`set_action`                                       |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+

    *Object methods*

        .. method:: patch()

            Replace entry members. Fields involved are set within the object
            using attribute's set method. This command is used to
            Import public key from remote host to switch,
            Export public key from switch to a remote host.

            Example usage of the method to export public key:

            .. code-block:: python

                sshutil_obj =
                    pyfos_brocade_security.sshutil()
                sshutil_obj.export_public_key("10.70.4.109", "/root/ca",
                                                   "root", "pray4green")
                sshutil_obj.patch(session)

            Example usage of the method to import public key:

            .. code-block:: python

                sshutil_obj =
                    pyfos_brocade_security.sshutil()
                sshutil_obj.import_export_key("test","10.70.4.109","/root/ca",
                                                "key.pub","root","pray4green")
                sshutil_obj.patch(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

    *Attribute methods*

        .. method:: set_user_name("user")

            Sets user name in the object

            :param pgid: user name
            :rtype: dictionary of error or success response

        .. method:: peek_user_name()

            Reads user name in the object.

            :rtype: None or pgid

        .. method:: set_public_key_name(name)

            Sets public key name in the object

            :param name: name of public key
            :rtype: dictionary of error or success response

        .. method:: set_remote_host_ip(ip)

            Sets remote host ip address object

            :param ip: ip address of the remote host
            :rtype: dictionary of error or success response

        .. method:: set_remote_dir(location)

            Sets a remote directory path object

            :param location: directory path in remote host
            :rtype: dictionary of error or success response

        .. method:: set_remote_user_name(username)

            Sets remote host's user name in the object

            :param user name: user name for authenticating remote host
            :rtype: dictionary of error or success response

        .. method:: set_remote_user_password(password)

             Sets remote host's user password in the object

            :param password: password for remote host
            :rtype: dictionary of error or success response

        .. method:: set_algorithm_type(type)

             Sets algorithm type in the object

            :param algorithm type: algorithm type
            :rtype: dictionary of error or success response

        .. method:: set_action(type)

             Sets action in the object

            :param operation: action
            :rtype: dictionary of error or success response

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
    """ This class provides methods/options to manage
    and configure public and private key pairs in a switch.

    Important class members:

        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | Attribute name                                 | Description                      |Frequently used methods                                  |
        +================================================+==================================+=========================================================+
        | user-name                                      | user name                        |:func:`set_user_name`                                    |
        |                                                |                                  |:func:`peek_user_name`                                   |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+
        | public-key                                     | Public key                       |:func:`set_public_key`                                   |
        |                                                |                                  |:func:`peek_public_key`                                  |
        +------------------------------------------------+----------------------------------+---------------------------------------------------------+

    *Object methods*

        .. method:: get()

            Return :class:`sshutil_public_key`
            object with values for all the attributes.
            The object can be printed using :func:`pyfos_utils.response_print`

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or
                :class:`sshutil` object

        .. method:: delete()

            Delete an entry or entry members. Fields involved are
            set within the object using attribute's
            set method. This command is used to delete public key(s) or
            private key or delknownhost(s) or hostkey.

            Example usage of the method to delete public key:

            .. code-block:: python

                sshutil_obj =
                    pyfos_brocade_security.sshutil_public_key()
                sshutil_obj.delete_public_keys("user")
                sshutil_obj.delete(session)

    *Attribute methods*

        .. method:: set_user_name("user")

            Sets user name in the object

            :param pgid: user name
            :rtype: dictionary of error or success response

        .. method:: peek_user_name()

            Reads user name in the object.

            :rtype: None or pgid

        .. method:: peek_public_key()

            Reads public key in the object

            :param name: public key
            :rtype: dictionary of error or success response

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

    Important class members:

        +------------------------------------------------+----------------------------------+----------------------------------------------------------------+
        | Attribute name                                 | Description                      |Frequently used methods                                         |
        +================================================+==================================+================================================================+
        | user-name                          | name of the user to change password          |:func:`set_user_name`                                           |
        |                                                |                                  |:func:`peek_user_name`                                          |
        +------------------------------------------------+----------------------------------+----------------------------------------------------------------+
        | old-password                       | Current password.                            |:func:`set_old_password`                                        |
        |                                                |                                  |:func:`peek_old_password`                                       |
        +------------------------------------------------+----------------------------------+----------------------------------------------------------------+
        | new-password                       | New password.                                |:func:`set_new_password`                                        |
        |                                                |                                  |:func:`peek_new_password`                                       |
        +------------------------------------------------+----------------------------------+----------------------------------------------------------------+

    *Object methods*

        .. method:: patch()

            Replace entry members. Fields involved are set within the object
            using attribute's set method. This command is used to
            change user password.

            Example usage of the method to change password:

            .. code-block:: python

                passwd_obj =
                    pyfos_brocade_security.password()
                passwd_obj.change_password(username)
                passwd_obj.patch(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

    *Attribute methods*

        .. method:: change_password(username, old_password, new_password)

            Change password for the specified user

            :param username: change password
            :rtype: dictionary of error or success response

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

    Important class members:

        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | Attribute name                                 | Description                       |Frequently used methods                      |
        +================================================+===================================+=============================================+
        | certificate-entity                             | CSR/switch/CA certificate         |:func:`set_certificate_entity`               |
        |                                                |                                   |:func:`peek_certificate_entity`              |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | certificate-type                               | Certificate types (commoncert/    |:func:`peek_certificate_type`                |
        |                                                | https/radius/ldap/syslog)         |:func:`set_certificate_type`                 |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | certificate                                    | Certificate                       |:func:`peek_certificate`                     |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | certificate-hexdump                            | Certificate in hex format         |:func:`peek_certificate_hexdump`             |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+

    *Object methods*

        .. method:: get(session)

            Returns :class:`seccertmgmt_show` object or a list of objects
            filled with certificate attributes gathered. If certificate entity
            and certificate type is given, a certificate matching the name of
            the certificate entity and type is returned or an empty object is
            returned if no match is found.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: a :class:`seccertmgmt` object to get a object or
                a list of objects if there are more than one

    *Attribute methods*

        .. method:: set_certificate_entity(cert)

            Sets certificate entity in the object.

            :param cert: certificate entity to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_certificate_entity()

            Reads certificate entity in the object.

            :rtype: certificate entity

        .. method:: set_certificate_type(cert)

            Sets certificate type in the object.

            :param cert type: certificate type to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_certificate_type()

            Reads certificate type in the object.

            :rtype: certificate type

        .. method:: peek_certificate()

            Gets certificate in the object.

            :rtype: None or certificate

        .. method:: peek_certificate_hexdump()

            Gets certificate(hexa format) in the object.

            :rtype: None or certificate

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

    Important class members:

        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | Attribute name                                 | Description                       |Frequently used methods                      |
        +================================================+===================================+=============================================+
        | certificate-entity                             | CSR/switch/CA certificate         |:func:`set_certificate_entity`               |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | certificate-type                               | Certificate types (commoncert/    |:func:`set_certificate_type`                 |
        |                                                | https/radius/ldap/syslog)         |                                             |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | algorithm-type                                 | Algorithm type (rsa/dsa/ecdsa)    |:func:`set_algorithm_type`                   |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | key-size                                       | Size of the key                   |:func:`set_key_size`                         |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | hash-type                                      | hash type                         |:func:`set_hash_type`                        |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | years                                          | certificate validity              |:func:`peek_years`                           |
        |                                                |                                   |:func:`set_years`                            |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | country-name                                   | Country name                      |:func:`set_country_name`                     |
        |                                                | Needed only for generating CSR    |:func:`peek_country_name`                    |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | state-name                                     | State name                        |:func:`set_state_name`                       |
        |                                                | Needed only for generating CSR    |:func:`peek_state_name`                      |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | locality-name                                  | Locality name                     |:func:`set_locality_name`                    |
        |                                                | Needed only for generating CSR    |:func:`peek_locality_name`                   |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | organization-name                              | Organization name                 |:func:`set_organization_name`                |
        |                                                | Needed only for generating CSR    |:func:`peek_organization_name`               |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | unit-name                                      | Unit name                         |:func:`set_unit_name`                        |
        |                                                | Needed only for generating CSR    |:func:`peek_unit_name`                       |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | domain-name                                    | domain name                       |:func:`set_domain_name`                      |
        |                                                | Needed only for generating CSR    |:func:`peek_domain_name`                     |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+

        .. method:: get(session)

            Returns :class:`security_certificate_generate` object or a list of
            objects filled with certificate attributes gathered. If certificate
            entity and certificate type is given, a certificate matching the
            name of the certificate entity and type is returned or an empty
            object is returned if no match is found.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: a :class:`seccertmgmt` object to get a object or
                a list of objects if there are more than one

        .. method:: post(session)

            Generates certificate. This method is used
            to create a specified certificate.

            Example usage of the method to create a new Certificate::

                # initialize the System Security object
                seccertmgmt =
                        pyfos_brocade_security.security_certificate_generate();
                # Generate a https certificate
                security_certificate_generate.generate("cert", "https")
                result = security_certificate_generate.post(session)


            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

    *Attribute methods*

        .. method:: set_certificate_entity(cert)

            Sets certificate entity in the object.

            :param cert: certificate entity to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_certificate_entity()

            Reads certificate entity in the object.

            :rtype: certificate entity

        .. method:: set_certificate_type(cert)

            Sets certificate type in the object.

            :param cert type: certificate type to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_certificate_type()

            Reads certificate type in the object.

            :rtype: certificate type

        .. method:: set_algorithm_type(algo)

            Sets algorithm type in the object.

            :param algo: algorithm type within the object
            :rtype: None or dictionary of error information

        .. method:: peek_algorithm_type()

            Reads algorithm type in the object.

            :rtype: algorithm type

        .. method:: set_key_size(size)

            Sets size of the key in the object.

            :param size: size of the key
            :rtype: None or dictionary of error information

        .. method:: peek_key_size()

            Gets size of the key in the object.

            :rtype: None or key size

        .. method:: set_hash_type(hash_type)

            Sets hash type in the object.

            :param hash_type: hash type
            :rtype: None or dictionary of error information

        .. method:: peek_hash_type()

            Gets hash type in the object.

            :rtype: None or hash type

        .. method:: peek_years()

            Gets years in the object.

            :rtype: None or years

        .. method:: set_years(years)

            Sets years in the object.

            :param years: years
            :rtype: None or dictionary of error information

        .. method:: peek_certificate()

            Gets certificate in the object.

            :rtype: None or certificate

        .. method:: peek_country_name()

            Gets country name in the object.

            :rtype: None or country name

        .. method:: set_country_name(country_name)

            Sets country name in the object.

            :param country_name: country name
            :rtype: None or dictionary of error information

        .. method:: peek_state_name()

            Gets state name in the object.

            :rtype: None or state name

        .. method:: set_state_name(state_name)

            Sets state name in the object.

            :param state_name: state name
            :rtype: None or dictionary of error information

        .. method:: peek_locality_name()

            Gets locality name in the object.

            :rtype: None or locality name

        .. method:: set_locality_name(locality_name)

            Sets locality name in the object.

            :param locality_name: locality name
            :rtype: None or dictionary of error information

        .. method:: peek_organization_name()

            Gets organization name in the object.

            :rtype: None or organization name

        .. method:: set_organization_name(organization_name)

            Sets organization name in the object.

            :param organization_name: organization name
            :rtype: None or dictionary of error information

        .. method:: peek_unit_name()

            Gets unit name in the object.

            :rtype: None or unit name

        .. method:: set_unit_name(unit_name)

            Sets unit name in the object.

            :param unit_name: unit name
            :rtype: None or dictionary of error information

        .. method:: peek_domain_name()

            Gets domain name in the object.

            :rtype: None or domain name

        .. method:: set_domain_name(domain_name)

            Sets domain name in the object.

            :param domain_name: domain name
            :rtype: None or dictionary of error information

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
            "key-size", pyfos_type.type_int,
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

        self.load(dictvalues, 1)
# class security-certificate-management(pyfos_rest_util.rest_object):


class security_certificate_action(pyfos_rest_util.rest_object):
    """This class provides options to display and configure certificates.

    Important class members:

        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | Attribute name                                 | Description                       |Frequently used methods                      |
        +================================================+===================================+=============================================+
        | certificate-entity                             | CSR/switch/CA certificate         |:func:`set_certificate_entity`               |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | certificate-type                               | Certificate types (commoncert/    |:func:`set_certificate_type`                 |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | certificate-name                               | certificate name                  |:func:`set_certificate_name`                 |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | operation                                      | operation                         |:func:`set_operation`                        |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | protocol                                       | Protocol used for import/export   |:func:`set_protocol`                         |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | remote-host-ip                                 | Remote host ip for import/export  |:func:`set_remote_host_ip`                   |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | remote-directory                               | Directory in remote host          |:func:`set_remote_dir`                       |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | remote-user-name                               | User name for the remote host     |:func:`set_remote_user_name`                 |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+
        | remote-user-password                           | Password for the remote host      |:func:`set_remote_user_password`             |
        +------------------------------------------------+-----------------------------------+---------------------------------------------+

    *Object methods*

        .. method:: set(session)

            Returns :class:`security_certificate_action` object or a list of
            objects filled with certificate attributes gathered. If certificate
            entity and certificate type is given, a certificate matching the
            name of the certificate entity and type is returned or an empty
            object is returned if no match is found.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: a :class:`seccertmgmt` object to get a object or
                a list of objects if there are more than one

        .. method:: patch(session)

            Import or export of certificate or CSR from and to a
            remote server. This method imports or exports a
            specified certifiate from or to
            a switch. This certificate will overwrite
            any existing certificate that is already present in the switch.
            Also, this method is used to send a signing request(CSR) from the
            switch to a remote server.

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


            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: a dictionary of error or success information

        .. method:: delete(session)

            Delete a certificate.
            This method is used to remove/clear specified certificate.

            Example usage of the method to delete certificate::

                # initialize the System Security object
                seccertmgmt = pyfos_brocade_security.seccertmgmt();
                # delete a certificate
                seccertmgmt.delete("cert", "https")
                result = seccertmgmt.delete(session)


            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

    *Attribute methods*

        .. method:: set_certificate_entity(cert)

            Sets certificate entity in the object.

            :param cert: certificate entity to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_certificate_entity()

            Reads certificate entity in the object.

            :rtype: certificate entity

        .. method:: set_certificate_type(cert)

            Sets certificate type in the object.

            :param cert type: certificate type to be set within the object
            :rtype: None or dictionary of error information

        .. method:: peek_certificate_type()

            Reads certificate type in the object.

            :rtype: certificate type

        .. method:: peek_certificate_name()

            Gets certificate name in the object.

            :rtype: None or certificate name

        .. method:: set_certificate_name(cert_name)

            Sets certificate name type in the object.

            :param cert_name: certificate name
            :rtype: None or dictionary of error information

        .. method:: peek_operation()

            Gets certificate operation in the object.

            :rtype: None or certificate operation

        .. method:: set_operation()

            Sets certificate operation in the object.

            :rtype: None or certificate operation

        .. method:: set_remote_host_ip(ip)

            Sets remote host ip address object

            :param ip: ip address of the remote host
            :rtype: dictionary of error or success response

        .. method:: set_remote_dir(location)

            Sets a remote directory path object

            :param location: directory path in remote host
            :rtype: dictionary of error or success response

        .. method:: set_remote_user_name(username)

            Sets remote host's user name in the object

            :param user name: user name for authenticating remote host
            :rtype: dictionary of error or success response

        .. method:: set_remote_user_password(password)

             Sets remote host's user password in the object

            :param password: password for remote host
            :rtype: dictionary of error or success response

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
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "remote-host-ip", pyfos_type.type_str,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "remote-user-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "remote-user-password", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "remote-directory", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)
