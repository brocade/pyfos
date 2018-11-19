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

:mod:`pyfos_brocade_logging` - PyFOS module to provide REST \
support for configuring the logging facilities in the FC switch.
******************************************************************\
******************************************************************
The :mod:`pyfos_brocade_logging` module provides a REST support for \
the FC switch logging facilities.
"""

from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


class raslog(pyfos_rest_util.rest_object):
    """Class of configurable parameters of RASLog

    Important Class Members:

        +------------------+--------------------+-----------------------------+
        | Attribute name   | Description        |Frequently used methods      |
        +==================+====================+=============================+
        | message-id       | The message ID     |:meth:`peek_message_id`      |
        |                  | of the RASLog.     |                             |
        +------------------+--------------------+-----------------------------+
        | message-text     | The message text   |:meth:`peek_message_text`    |
        |                  | of the RASLog      |                             |
        +------------------+--------------------+-----------------------------+
        | message-enabled  | The message status |:meth:`set_message_enabled`  |
        |                  | of the RASLog.     |:meth:`peek_message_enabled` |
        +------------------+--------------------+-----------------------------+
        | message-flooded  | The message status |:meth:`peek_message_flooded` |
        |                  | of the RASLog.     |                             |
        +------------------+--------------------+-----------------------------+
        | syslog-enabled   | The syslog status  |:meth:`set_syslog_enabled`   |
        |                  | the RASLog.        |:meth:`peek_syslog_enabled`  |
        +------------------+--------------------+-----------------------------+
        | current-severity | The severity level |:meth:`set_current_severity` |
        |                  | the RASLog         |:meth:`peek_current_severity`|
        +------------------+--------------------+-----------------------------+
        | default-severity | Default severity   |:meth:`peek_default_severity`|
        |                  | of the RASLog.     |                             |
        +------------------+--------------------+-----------------------------+

    *Object Methods*

        .. method:: get(session)

            Returns a :class:`raslog` object with attributes from RASLog.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a
                :class:`raslog` object.

        .. method:: patch(session)

            Apply the configurable attribute(s) within the object to RASLog.

            *Below is an Example Using Individual Sets:*

            .. code-block:: python

                # initialize the raslog object
                raslog_obj = pyfos_brocade_logging.raslog()
                # set the message-id attribute to enable the
                # wwn based pid on the raslog
                raslog_obj.set_message_enabled(true)
                # execute HTTP patch command to apply the object to the
                # raslog connected through session
                raslog_obj.patch(session)

            *Below is an Example of Combining Object \
                    Initialization and Attribute Sets:*

            .. code-block:: python

                # initialize the raslog object and
                # set the enable-state attribute
                raslog_obj = pyfos_brocade_logging.raslog(
                    {"message-enabled" : true})
                # execute HTTP patch command to apply the object to the
                # raslog connected through session
                raslog_obj.patch(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or success information.

    *Attribute Methods*

        .. method:: peek_message_id()

            Reads the message ID of the RASLog in the object.

            :rtype: The message ID.

        .. method:: peek_message_text()

            Reads the message description in the RASLog object.

            :rtype: A text description of the RASLog.

        .. method:: set_message_enabled(flag)

            Sets the RASLog message object.

            :param flag: The message status flag within the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_message_enabled()

            Reads the message status in the object.

            :rtype: None or the status of the RASLog.

        .. method:: peek_message_flooded()

            Reads the message flooded status in the object.

            :rtype: None or the status of the RASLog.

        .. method:: set_syslog_enabled(flag)

            Sets the RASLog message object for syslog.

            :param flag: The syslog status flag within the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_syslog_enabled()

            Reads the message syslog status in the object.

            :rtype: None or the syslog status of the RASLog.

        .. method:: set_current_severity(value)

            Sets the severity of RASLog message object.

            :param value: The severity value within the object.
            :rtype: None or a dictionary of error information.

        .. method:: peek_current_severity()

            Reads the severity in the object.

            :rtype: None or the severity of the RASLog.

        .. method:: peek_default_severity()

            Reads the default severity in the object.

            :rtype: None or the default severity of the RASLog.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.raslog,
                         "/rest/running/brocade-logging/raslog",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "message-id", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "message-text", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "message-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "syslog-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "message-flooded", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "current-severity", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "default-severity", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.load(dictvalues, 1)


class raslog_module(pyfos_rest_util.rest_object):
    """Class of configurable parameters of all RASLog of a FOS module.

    Important class members:

        +----------------+----------------------+------------------------+
        | Attribute Name | Description          |Frequently Used Methods |
        +================+======================+========================+
        | module-id      | The module ID        |:meth:`peek_module_id`  |
        |                | of the RASLog.       |                        |
        +----------------+----------------------+------------------------+
        | log-enabled    | The status of all    |:meth:`set_log_enabled` |
        |                | RASLog in the FOS    |                        |
        |                | module.              |                        |
        +----------------+----------------------+------------------------+

    *Object Methods*

        .. method:: get(session)

            Returns a :class:`raslog_module` object with attributes from
            the RASLog module.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of error or a
                :class:`raslog_module` object.

        .. method:: patch(session)

            Apply configurable attribute(s) within the object to RASLog module.

            *Below is an Example Using Individual Sets:*

            .. code-block:: python

                # initialize the raslog_module object
                raslog_module_obj = pyfos_brocade_logging.raslog_module()
                # set the module-id attribute to enable the
                # wwn based pid on the raslog_module
                raslog_module_obj.set_log_enabled(true)
                # execute HTTP patch command to apply the object to the
                # raslog_module connected through session
                raslog_module_obj.patch(session)

            *Below is an Example of Combining Object \
                    Initialization and Attribute Sets:*

            .. code-block:: python

                # initialize the raslog_module object and
                # set the enable-state attribute
                raslog_module_obj = pyfos_brocade_logging.raslog_module(
                    {"log-enabled" : true})
                # execute HTTP patch command to apply the object to the
                # raslog_module connected through session
                raslog_module_obj.patch(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or success information.

    *Attribute Methods*

        .. method:: peek_module_id()

            Reads the module ID of RASLog module in the object.

            :rtype: The module ID.

        .. method:: set_log_enabled(flag)

            Sets the RASLog module in the object.

            :param flag: The message status flag for all messages in the module
                         within the object.
            :rtype: None or a dictionary of error information.

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.raslog_module,
                         "/rest/running/brocade-logging/raslog-module",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "module-id", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "log-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class log_quiet_control(pyfos_rest_util.rest_object):
    """
    Class of configurable parameters of the log quiet control.

    Important Class Members:

        +----------------+-------------------+----------------------------+
        | Attribute Name | Description       |Frequently Used Methods     |
        +================+===================+============================+
        | log-type       | The identifier for|:meth:`peek_log_type`       |
        |                | the log type.     |                            |
        +----------------+-------------------+----------------------------+
        | quiet-enabled  | The quiet status  |:meth:`set_quiet_enabled`   |
        |                | of the log type.  |:meth:`peek_quiet_enabled`  |
        +----------------+-------------------+----------------------------+
        | start-time     | The quiet start   |:meth:`set_start_time`      |
        |                | time of the log   |:meth:`peek_start_time`     |
        |                | type.             |                            |
        +----------------+-------------------+----------------------------+
        | end-time       | The quiet end     |:meth:`set_end_time`        |
        |                | time of the log   |:meth:`peek_end_time`       |
        |                | type.             |                            |
        +----------------+-------------------+----------------------------+
        | days-of-week   | The quiet days of |:meth:`set_days_of_week_day`|
        |                | the log type.     |:meth:`peek_days_of_week`   |
        +----------------+-------------------+----------------------------+

    *Object Methods*

        .. method:: get(session)

            Returns a :class:`log_quiet_control` object with attributes
            from log quiet control.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a
                :class:`log_quiet_control` object.

        .. method:: patch(session)

            Apply configurable attribute(s) within the object to
            log quiet control.

            *Below is an Example Using Individual Sets:*

            .. code-block:: python

                # initialize the log_quiet_control object
                obj = pyfos_brocade_logging.log_quiet_control()
                # set the log-type attribute to enable the
                # wwn based pid on the log_quiet_control
                obj.set_keep_alive_period(true)
                # execute HTTP patch command to apply the object to the
                # log_quiet_control connected through session
                obj.patch(session)

            *Below is an Example of Combining Object \
                    Initialization and Attribute Sets:*

            .. code-block:: python

                # initialize the log_quiet_control object and
                # set the enable attribute
                obj = pyfos_brocade_logging.log_quiet_control(
                    {"quiet-enabled" : true})
                # execute HTTP patch command to apply the object to the
                # log_quiet_control connected through session
                obj.patch(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`
            :rtype: a dictionary of error or success information

    *Attribute Methods*

        .. method:: peek_log_type()

            Reads the message ID of the log quiet control in the object.

            :rtype: The message ID.

        .. method:: set_quiet_enabled(flag)

            Sets the log quiet control object.

            :param flag: The quiet flag of the log within the switch.
            :rtype: None or a dictionary of error information.

        .. method:: peek_quiet_enabled()

            Reads the quiet status in the object.

            :rtype: None or the status of the log quiet control.

        .. method:: set_start_time(value)

            Sets the start time of log quiet control object.

            :param value: The start time period in hh:mm to quiet the logs \
                          within the switch.
            :rtype: None or a dictionary of error information.

        .. method:: peek_start_time()

            Reads the start time in the object.

            :rtype: None or the start time of the log quiet control.

        .. method:: set_end_time(value)

            Sets the end time of log quiet control object.

            :param value: The end time period in hh:mm to quiet the logs within
                          the switch.
            :rtype: None or a dictionary of error information.

        .. method:: peek_end_time()

            Reads the end time in the object.

            :rtype: None or the end time of the log quiet control.

        .. method:: set_days_of_week_day(value)

            Sets the quiet days of log quiet control object.

            :param value: The day to quiet the logs within the switch.
            :rtype: None or a dictionary of error information.

        .. method:: peek_days_of_week()

            Reads the quiet days in the object.

            :rtype: None or the quiet days set for the log quiet control.

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.log_quiet_control,
                         "/rest/running/brocade-logging/log-quiet-control",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "log-type", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "quiet-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "start-time", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "end-time", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "days-of-week", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "day", pyfos_type.type_str,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["days-of-week"])

        self.load(dictvalues, 1)


class log_setting(pyfos_rest_util.rest_object):
    """
    Class of configurable parameters of the log control.

    Important Class Members:

        +---------------------+-----------+----------------------------------+
        |Attribute Name       |Description|Frequently Used Methods           |
        +=====================+===========+==================================+
        |keep-alive-period    |The log    |:meth:`set_keep_alive_period`     |
        |                     |keepalive  |:meth:`peek_keep_alive_period`    |
        |                     |period.    |                                  |
        +---------------------+-----------+----------------------------------+
        |syslog-facility-level|The syslog |:meth:`peek_syslog_facility_level`|
        |                     |facility   |:meth:`set_syslog_facility_level` |
        |                     |level.     |                                  |
        +---------------------+-----------+----------------------------------+

    *Object Methods*

        .. method:: get(session)

            Returns a :class:`log_setting` object with attributes from
            the log setting.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes can be accessed through peek methods.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a
                :class:`log_setting` object.

        .. method:: patch(session)

            Apply configurable attribute(s) within the object to the \
            log setting.

            *Below is an Example Using Individual Sets:*

            .. code-block:: python

                # initialize the log_setting object
                log_setting_obj = pyfos_brocade_logging.log_setting()
                # set the log-type attribute to enable the
                # wwn based pid on the log_setting
                log_setting_obj.set_keep_alive_period(value)
                # execute HTTP patch command to apply the object to the
                # log_setting connected through session
                log_setting_obj.patch(session)

            *Below is an Example of Combining Object \
                    Initialization and Attribute Sets:*

            .. code-block:: python

                # initialize the log_setting object and
                # set the enable attribute
                log_setting_obj = pyfos_brocade_logging.log_setting(
                    {"keep-alive-period" : 24})
                # execute HTTP patch command to apply the object to the
                # log_setting connected through session
                log_setting_obj.patch(session)

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or success information.

    *Attribute Methods*

        .. method:: peek_keep_alive_period()

            Reads the message ID of log setting in the object.

            :rtype: The message ID.

        .. method:: set_keep_alive_period(value)

            Sets the log setting object.

            :param value: The keepalive period.
            :rtype: None or a dictionary of error information.

        .. method:: peek_syslog_facility_level()

            Reads the syslog facility level in the object.

            :rtype: None or the syslog facility level.

        .. method:: set_syslog_facility_level(level)

            Sets the syslog facility level.

            :param: The facility level.
            :rtype: A dictionary of errors or a success response.
    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.log_setting,
                         "/rest/running/brocade-logging/log-setting",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
                "keep-alive-period", pyfos_type.type_int,
                None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
               "syslog-facility-level", pyfos_type.type_str,
               None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class audit(pyfos_rest_util.rest_object):

    """ This class provides methods or options to retrieve and configure
        audit logging.


    Important Class Members:

        +-----------------+-------+-------------------------------------------+
        | Attribute Name  | Desc. |Frequently Used Methods                    |
        +=================+=======+===========================================+
        | audit-enabled   | Audit |:meth:`peek_audit_enabled`                 |
        |                 | flag. |:meth:`set_audit_enabled`                  |
        +-----------------+-------+-------------------------------------------+
        | severity-level  | Severe|:meth:`peek_severity_level`                |
        |                 | level.|:meth:`set_severity_level`                 |
        +-----------------+-------+-------------------------------------------+
        |filter-class-list| Class |:meth:`peek_filter_class_list_filter_class`|
        |/filter-class    | list. |:meth:`set_filter_class_list_filter_class` |
        +-----------------+-------+-------------------------------------------+

    *Object Methods*

        .. method:: get(session)
            Returns a :class:`audit` object or a list of objects \
            with attributes gathered from auditcfg.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes can be accessed through peek methods.

        .. method:: patch(session)

               Apply configurable attribute(s) within the object to audit.

               *Below is an Example Using Individual Sets:*

            .. code-block:: python

                # initialize the audit object
                audit_obj = pyfos_brocade_logging.audit()
                # set audit enabled to true
                audit_obj.set_audit_enabled(true)
                # set the severity level to info
                audit_obj.set_severity_level(info)
                audit_obj.patch(session)

                :param session: The session handler returned by the audit
                :func:`pyfos_auth.login`.
                :rtype: A dictionary of errors or success information.

    *Attribute Methods*

        .. method:: set_audit_enabled(enable/disable)

            Sets the audit log enabled flag to true or false (disabled)
            in the object.

            :param enable/disable: True to enable and false to disable \
                                    audit logs.
            :rtype: A dictionary of errors or success response.

        .. method:: peek_audit_enabled()

            Reads the audit log enabled state in the object.

            :rtype: True or false.

        .. method:: set_severity_level(level)

            Sets the level of severity in the object.

            :param level: The valid severity level (info, warning, \
                           critical, error)
            :rtype: A dictionary of errors or a success response.

        .. method:: peek_severity_level()

            Reads the severity level in the object.

            :rtype: The level of severity of the audit log.

        .. method:: set_filter_class_list_filter_class(filter_class_list)

            Sets the filter class list in the object.

            :param level: The valid filter class list (security, \
            configuration, zone, firmware, fabric, ls, cli, maps).
            :rtype: A dictionary of errors or a success response.

        .. method:: peek_filter_class_list_filter_class()

            Reads the filter class list in the object.

            :rtype: The filter class list of audit logs.

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.audit,
                         "/rest/running/brocade-logging/audit",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "audit-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "severity-level", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "filter-class-list", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "filter-class", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["filter-class-list"])

        self.load(dictvalues, 1)


class syslog_server(pyfos_rest_util.rest_object):
    """ This class provides methods and options to retrieve, configure, modify,
        and delete syslog.

    Important Class Members:

        +----------------+--------------------+------------------------+
        | Attribute Name | Description        |Frequently Used Methods |
        +================+====================+========================+
        | server         | The syslog server  |:meth:`peek_server`     |
        |                | name.              |:meth:`set_server`      |
        +----------------+--------------------+------------------------+
        | port           | The port syslog    |:meth:`peek_port`       |
        |                | server.            |:meth:`set_port`        |
        +----------------+--------------------+------------------------+
        | secure-mode    | The secure mode    |:meth:`peek_secure_mode`|
        |                | using TLS protocol.|:meth:`set_secure_mode` |
        +----------------+--------------------+------------------------+


    *Object Methods*

      .. method:: get(session)
          Returns a :class:`syslog_server` object or list of objects with \
          syslog server attributes.

          Each object can be printed using :func:`pyfos_util.response_print`\
          and individual attributes can be accessed through peek methods.

      .. method:: post(session)

          Add members to a list attribute of the object. This method is used to \
          add syslog servers.

          Example Usage of the Method to Configure a new Syslog Server:

          # initialize the syslog server object
          syslog_server_obj = pyfos_brocade_logging.syslog_server()
          # set the IP address of server
          syslog_server_obj.set_server("10.10.10.10")

          :param session: The session handler returned by
             :func:`pyfos_auth.login`.
          :rtype: A dictionary of errors or a success response.

      .. method:: patch(session)

             Apply configurable attribute(s) within the object to the \
              syslog server.

             *Below is an Example Using Individual Sets:*

          .. code-block:: python

              # initialize the syslog server object
              syslog_server_obj = pyfos_brocade_logging.syslog_server()
              # set the IP address of server
              syslog_server_obj.set_server("10.10.10.10")
              # set the port number
              syslog_server_obj.set_port("1234")
              # set secure mode to true
              syslog_server_obj.set_secure_mode(true)
              syslog_server_obj.patch(session)

              :param session: The session handler returned by
                  :func:`pyfos_auth.login`.
              :rtype: A dictionary of errors or a success response.

      .. method:: delete(session)

             Delete members from a list attribute of the object. This method
              deletes the configured syslog server.

              Example Usage of the Method to Create New Mappings:

          .. code-block:: python

              # initialize the syslog server object
              syslog_server_obj = pyfos_brocade_logging.syslog_server()
              # set the IP address of server
              syslog_server_obj.set_server("10.10.10.10")
              # delete the syslog server
              syslog_server_obj.delete(session)

    *Attribute Methods*

        .. method:: set_server(server)

            Sets the server in the object.

            :param server: The IPv4 or IPv6 address or the DNS name of the \
                            syslog server.
            :rtype: A dictionary of errors or a success response.

        .. method:: peek_server()

            Reads the syslog server in the object.

            :rtype: The IP address or DNS name of the server.

        .. method:: set_port(port)

            Sets the port number in the object.

            :param port: The port number of the syslog server.
            :rtype: A dictionary of errors or a success response.

        .. method:: peek_port()

            Reads the port number in the object.

            :rtype: The port number in the object.

        .. method:: set_secure_mode(true\\/false)

            Sets the secure mode in the object

            :param true\\/false: True enables secure mode and false disables it.
            :rtype: A dictionary of errors or a success response.

        .. method:: peek_secure_mode()

            Reads the secure mode in the object.

            :rtype: The secure mode (true or false).

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.syslog,
                         "/rest/running/brocade-logging/syslog-server",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "server", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "port", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "secure-mode", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)
