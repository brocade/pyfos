#!/usr/bin/env python3

# Copyright 2021 Brocade Communications Systems LLC.  All rights reserved.
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
:mod:`pyfos_brocade_supportlink` - PyFOS module to provide REST support \
for supportlink.
******************************************************************\
****************************************
The :mod:`pyfos_brocade_supportlink` module provides REST support \
for supportlink.

"""

from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


class supportlink_profile(pyfos_rest_util.rest_object):

    """
        Supportlink profile provides information on profile.

    Important Class Members:

        +-------------------------------+----------------------------------+----------------------------------------------+
        | Attribute Name                | Description                      |Frequently Used Methods                       |
        +===============================+==================================+==============================================+
        | server                        | IP address or DNS name of server |:func:`set_server`                            |
        |                               |                                  |:func:`peek_server`                           |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | port                          | HTTPS port of server             |:func:`set_port`                              |
        |                               |                                  |:func:`peek_port`                             |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | user-name                     | user name of account in server   |:func:`set_user_name`                         |
        |                               |                                  |:func:`peek_user_name`                        |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | start-date                    | start date of operation          |:func:`set_start_date`                        |
        |                               |                                  |:func:`peek_start_date`                       |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | start-time                    | start time of operation          |:func:`set_start_time`                        |
        |                               |                                  |:func:`peek_start_time`                       |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | end-time-period               | end time period from start time  |:func:`set_end_time_period`                   |
        |                               |                                  |:func:`peek_end_time_period`                  |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | retry-time                    | retry time afterfail of operation|:func:`set_retry_time`                        |
        |                               |                                  |:func:`peek_retry_time`                       |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | period                        | frequency of operation           |:func:`set_period`                            |
        |                               |                                  |:func:`peek_period`                           |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | collection-time               | collection time                  |:func:`set_collection_time`                   |
        |                               |                                  |:func:`peek_collection_time`                  |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | group-tag                     | custom group tag                 |:func:`set_group_tag`                         |
        |                               |                                  |:func:`peek_group_tag`                        |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | proxy-server                  | IP address or DNS name of proxy  |:func:`set_proxy_server`                      |
        |                               |                                  |:func:`peek_proxy_server`                     |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | proxy-port                    | HTTPS port of proxy server       |:func:`set_proxy_port`                        |
        |                               |                                  |:func:`peek_proxy_port`                       |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | proxy-user                    | user name of account in proxy    |:func:`set_proxy_user`                        |
        |                               |                                  |:func:`peek_proxy_user`                       |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | proxy-password                | proxy password                   |:func:`set_proxy_password`                    |
        |                               |                                  |:func:`peek_proxy_password`                   |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | proxy-protocol                | protocol used in proxy           |:func:`set_proxy_protocol`                    |
        |                               |                                  |:func:`peek_proxy_protocol`                   |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | supportlink-enabled           | supportlink feature true/false   |:func:`set_supportlink_enabled`               |
        |                               |                                  |:func:`peek_supportlink_enabled`              |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | random-start-time             | switch upload time               |:func:`peek_random_start_time`                |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | next_collection_time          | next collection time             |:func:`peek_next_collection_time`             |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | next_service_start_time       | next upload time                 |:func:`peek_next_service_start_time`          |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | next_service_retry_time       | next upload retry time           |:func:`peek_next_service_retry_time`          |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | last_collection_time          | last successful collection time  |:func:`peek_last_collection_time`             |
        +-------------------------------+----------------------------------+----------------------------------------------+
        | last_upload_time              | last successful upload time      |:func:`peek_last_upload_time`                 |
        +-------------------------------+----------------------------------+----------------------------------------------+

    *Object Methods*

        .. staticmethod:: get(session)

            Returns a :class:`credit_stall_dashboard` object.
            Returns the credit stall dashboard information.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A :class:`credit_stall_dashboard` object. \
                    A dictionary in case of error.

        .. method:: patch(session)

            Replace entry members. Fields involved are set
            within the object using
            attribute's set method. This command is used to
            update config parameters of the supportlink.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

    *Attribute Methods*

        .. method:: set_server()

            Sets the IP address or DNS name of the server.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_server()

            Returns the IP address or DNS name of the server.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_port()

            Sets the HTTPS port of the server.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_port()

            Returns the HTTPS port of the server.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_user_name()

            Sets the user name of account in server.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_user_name()

            Returns the user name of account in server.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_start_date()

            Sets the start date of operation.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_start_date()

            Returns the start date of operation.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_start_time()

            Sets the start time of operation.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_start_time()

            Returns the start time of operation.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_end_time_period()

            Sets the end time period form the start time.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_end_time_period()

            Returns the end time period form the start time.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_retry_time()

            Sets the retry time.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_retry_time()

            Returns the retry time.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_period()

            Sets the period/frequency of operation.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_period()

            Returns the period/frequency of operation.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_collection_time()

            Sets the collection time of operation.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_collection_time()

            Returns the collection time of operation.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_group_tag()

            Sets the custom group tag.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_group_tag()

            Returns the custom group tag.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_proxy_server()

            Sets the IP address or DNS name of proxy server.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_proxy_server()

            Returns the IP address or DNS name of proxy server.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_proxy_port()

            Sets the HTTPS port of proxy server.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_proxy_port()

            Returns the HTTPS port of proxy server.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_proxy_user()

            Sets the user name of account in proxy server.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_proxy_user()

            Returns the user name of account in proxy server.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_proxy_password()

            Sets the proxy password.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_proxy_password()

            Returns the proxy password.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_proxy_protocol()

            Sets the type of proxy protocol used.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_proxy_protocol()

            Returns the type of proxy protocol used.

            :rtype: A dictionary in case of error or a success response.

        .. method:: set_supportlink_enabled()

            Sets the enable/disable status of the supportlink feature.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_supportlink_enabled()

            Returns the enable/disable status of the supportlink feature.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_random_start_time()

            Returns the random upload time calculated.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_next_collection_time()

            Returns the next collection time.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_next_service_start_time()

            Returns the next upload time.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_next_service_retry_time()

            Returns the next upload retry time.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_last_collection_time()

            Returns the last successful collection time.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_last_upload_time()

            Returns the last successful upload time.

            :rtype: A dictionary in case of error or a success response.

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.supportlink_profile,
                         "/rest/running/brocade-supportlink/supportlink-profile",
                         version.VER_RANGE_900_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "supportlink-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "server", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "port", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "user-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "period", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "start-time", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "start-date", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "collection-time", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "retry-time", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "end-time-period", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "random-start-time", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "next-collection-time", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "next-service-start-time", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "next-service-retry-time", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "last-collection-time", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "last-upload-time", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "proxy-server", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "proxy-port", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "proxy-user", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "proxy-password", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "proxy-protocol", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.add(pyfos_rest_util.rest_attribute(
            "group-tag", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class supportlink_history(pyfos_rest_util.rest_object):

    """Class of supportlink_history

    *Description supportlink_history*

        The supportLink history is used to retrieve the failures occurred
        during the inventory upload operations.

    Important class members of supportlink_history:

        +--------------------------+---------------------------------+-------------------------------------------------+
        | Attribute Name           | Description                     |  Frequently Used Methods                        |
        +==========================+=================================+=================================================+
        | server                   | SupportLink destination         | :func:`peek_server`                             |
        |                          | server address or domain        |                                                 |
        |                          | name.                           |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | error-code               | It indicates the exact          | :func:`peek_error_code`                         |
        |                          | failure occurred during         |                                                 |
        |                          | supportLink upload operation.   |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | error-message            | The error message provides      | :func:`peek_error_message`                      |
        |                          | the reason for the              |                                                 |
        |                          | supportLink upload operation    |                                                 |
        |                          | failures.                       |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | port                     | The HTTPS port number of the    | :func:`peek_port`                               |
        |                          | destination server.             |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | time-stamp               | The time when supportLink       | :func:`peek_time_stamp`                         |
        |                          | upload operation failed.        |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | index                    | The index of the specific       | :func:`peek_index`                              |
        |                          | upload failure entry and it     |                                                 |
        |                          | is used as a label for this     |                                                 |
        |                          | object.                         |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+

    *Object functions for supportlink_history*

    .. function:: get()

        Get the instances of class "supportlink_history from switch. The
         object can be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for supportlink_history*

        .. function:: peek_server()

            Reads the value assigned to server in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_error_code()

            Reads the value assigned to error-code in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_error_message()

            Reads the value assigned to error-message in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_port()

            Reads the value assigned to port in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_time_stamp()

            Reads the value assigned to time-stamp in the object.

            :rtype: None on error and a value on success.


        .. function:: peek_index()

            Reads the value assigned to index in the object.

            :rtype: None on error and a value on success.


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-supportlink" +\
                 "/supportlink-history"
        clstype = pyfos_rest_util.rest_obj_type.supportlink_history
        clsver = version.VER_RANGE_900_and_ABOVE
        super().__init__(clstype, clsuri, clsver)

        self.add(pyfos_rest_util.rest_attribute("server", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("error-code",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("error-message",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("port", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("time-stamp",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("index", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.load(dictvalues, 1)
