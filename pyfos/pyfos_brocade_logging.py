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

:mod:`pyfos_brocade_logging` - PyFOS module to provide rest\
        support for configuring logging facilities in FC switch.
******************************************************************\
******************************************************************
The :mod:`pyfos_brocade_logging` provides a REST support for\
        FC switch logging facilities.

"""

import pyfos.pyfos_rest_util as pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


class raslog(pyfos_rest_util.rest_object):
    """Class of configurable parameters of raslog

    Important class members:

        +------------------+--------------------+-----------------------------+
        | Attribute name   | Description        |Frequently used methods      |
        +==================+====================+=============================+
        | message-id       | The message id     |:meth:`peek_message_id`      |
        |                  | of the raslog      |                             |
        +------------------+--------------------+-----------------------------+
        | message-text     | The message text   |:meth:`peek_message_text`    |
        |                  | of the raslog      |                             |
        +------------------+--------------------+-----------------------------+
        | message-enabled  | The message status |:meth:`set_message_enabled`  |
        |                  | of the raslog      |:meth:`peek_message_enabled` |
        +------------------+--------------------+-----------------------------+
        | message-flooded  | The message status |:meth:`peek_message_flooded` |
        |                  | of the raslog      |                             |
        +------------------+--------------------+-----------------------------+
        | syslog-enabled   | The syslog status  |:meth:`set_syslog_enabled`   |
        |                  | the raslog         |:meth:`peek_syslog_enabled`  |
        +------------------+--------------------+-----------------------------+
        | current-severity | The severity level |:meth:`set_current_severity` |
        |                  | the raslog         |:meth:`peek_current_severity`|
        +------------------+--------------------+-----------------------------+
        | default-severity | Default severity   |:meth:`peek_default_severity`|
        |                  | of the raslog      |                             |
        +------------------+--------------------+-----------------------------+

    *Object methods*

        .. method:: get(session)

            Returns a :class:`raslog` object with attributes from raslog.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or a
                :class:`raslog` object

        .. method:: patch(session)

            Apply configurable attribute(s) within the object to raslog.

            *Below is an example using individual sets:*

            .. code-block:: python

                # initialize the raslog object
                raslog_obj = pyfos_brocade_logging.raslog()
                # set the message-id attribute to enable the
                # wwn based pid on the raslog
                raslog_obj.set_message_enabled(true)
                # execute HTTP patch command to apply the object to the
                # raslog connected through session
                raslog_obj.patch(session)

            *Below is an example of combining object \
                    initialization and attribute sets:*

            .. code-block:: python

                # initialize the raslog object and
                # set the enable-state attribute
                raslog_obj = pyfos_brocade_logging.raslog(
                    {"message-enabled" : true})
                # execute HTTP patch command to apply the object to the
                # raslog connected through session
                raslog_obj.patch(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: a dictionary of error or success information

    *Attribute methods*

        .. method:: peek_message_id()

            Reads the message id of raslog in the object.

            :rtype: message id

        .. method:: peek_message_text()

            Reads Message description in the raslog object.

            :rtype: Text description of the raslog

        .. method:: set_message_enabled(flag)

            Sets the raslog message object.

            :param flag: message status flag within the object
            :rtype: None or dictionary of error information

        .. method:: peek_message_enabled()

            Reads the message status in the object.

            :rtype: None or status of the raslog

        .. method:: peek_message_flooded()

            Reads the message flooded status in the object.

            :rtype: None or status of the raslog

        .. method:: set_syslog_enabled(flag)

            Sets the raslog message object for syslog.

            :param flag: syslog status flag within the object
            :rtype: None or dictionary of error information

        .. method:: peek_syslog_enabled()

            Reads the message syslog status in the object.

            :rtype: None or syslog status of the raslog

        .. method:: set_current_severity(value)

            Sets the severity of raslog message object.

            :param value: severity value within the object
            :rtype: None or dictionary of error information

        .. method:: peek_current_severity()

            Reads the severity in the object.

            :rtype: None or severity of the raslog

        .. method:: peek_default_severity()

            Reads the default severity in the object.

            :rtype: None or default severity of the raslog

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
    """Class of configurable parameters of all raslog of a FOS Module

    Important class members:

        +----------------+----------------------+------------------------+
        | Attribute name | Description          |Frequently used methods |
        +================+======================+========================+
        | module-id      | The module id        |:meth:`peek_module_id`  |
        |                | of the raslog        |                        |
        +----------------+----------------------+------------------------+
        | log-enabled    | The status of all    |:meth:`set_log_enabled` |
        |                | raslogs in FOS Module|                        |
        +----------------+----------------------+------------------------+

    *Object methods*

        .. method:: get(session)

            Returns a :class:`raslog_module` object with attributes from
            raslog_module.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or a
                :class:`raslog_module` object

        .. method:: patch(session)

            Apply configurable attribute(s) within the object to raslog_module.

            *Below is an example using individual sets:*

            .. code-block:: python

                # initialize the raslog_module object
                raslog_module_obj = pyfos_brocade_logging.raslog_module()
                # set the module-id attribute to enable the
                # wwn based pid on the raslog_module
                raslog_module_obj.set_log_enabled(true)
                # execute HTTP patch command to apply the object to the
                # raslog_module connected through session
                raslog_module_obj.patch(session)

            *Below is an example of combining object \
                    initialization and attribute sets:*

            .. code-block:: python

                # initialize the raslog_module object and
                # set the enable-state attribute
                raslog_module_obj = pyfos_brocade_logging.raslog_module(
                    {"log-enabled" : true})
                # execute HTTP patch command to apply the object to the
                # raslog_module connected through session
                raslog_module_obj.patch(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: a dictionary of error or success information

    *Attribute methods*

        .. method:: peek_module_id()

            Reads the module id of raslog_module in the object.

            :rtype: module id

        .. method:: set_log_enabled(flag)

            Sets the raslog_module module object.

            :param flag: message status flag for all messages in tha module
                         within the object
            :rtype: None or dictionary of error information

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
    Class of configurable parameters of log quiet control

    Important class members:

        +----------------+-------------------+----------------------------+
        | Attribute name | Description       |Frequently used methods     |
        +================+===================+============================+
        | log-type       | The identifier for|:meth:`peek_log_type`       |
        |                | log type          |                            |
        +----------------+-------------------+----------------------------+
        | quiet-enabled  | The quiet status  |:meth:`set_quiet_enabled`   |
        |                | of the log type   |:meth:`peek_quiet_enabled`  |
        +----------------+-------------------+----------------------------+
        | start-time     | The quiet start   |:meth:`set_start_time`      |
        |                | time of log type  |:meth:`peek_start_time`     |
        +----------------+-------------------+----------------------------+
        | end-time       | The quiet end     |:meth:`set_end_time`        |
        |                | time of log type  |:meth:`peek_end_time`       |
        +----------------+-------------------+----------------------------+
        | days-of-week   | The quiet days of |:meth:`set_days_of_week_day`|
        |                | the log type      |:meth:`peek_days_of_week`   |
        +----------------+-------------------+----------------------------+

    *Object methods*

        .. method:: get(session)

            Returns a :class:`log_quiet_control` object with attributes
            from log_quiet_control.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or a
                :class:`log_quiet_control` object

        .. method:: patch(session)

            Apply configurable attribute(s) within the object to
            log_quiet_control.

            *Below is an example using individual sets:*

            .. code-block:: python

                # initialize the log_quiet_control object
                obj = pyfos_brocade_logging.log_quiet_control()
                # set the log-type attribute to enable the
                # wwn based pid on the log_quiet_control
                obj.set_keep_alive_period(true)
                # execute HTTP patch command to apply the object to the
                # log_quiet_control connected through session
                obj.patch(session)

            *Below is an example of combining object \
                    initialization and attribute sets:*

            .. code-block:: python

                # initialize the log_quiet_control object and
                # set the enable attribute
                obj = pyfos_brocade_logging.log_quiet_control(
                    {"quiet-enabled" : true})
                # execute HTTP patch command to apply the object to the
                # log_quiet_control connected through session
                obj.patch(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: a dictionary of error or success information

    *Attribute methods*

        .. method:: peek_log_type()

            Reads the message id of log_quiet_control in the object.

            :rtype: message id

        .. method:: set_quiet_enabled(flag)

            Sets the log_quiet_control object.

            :param flag: quiet flag of the log within the switch
            :rtype: None or dictionary of error information

        .. method:: peek_quiet_enabled()

            Reads the quiet status in the object.

            :rtype: None or status of the log_quiet_control

        .. method:: set_start_time(value)

            Sets the start time of log_quiet_control object.

            :param value: start time period in hh:mm to quiet the logs within
                          the switch
            :rtype: None or dictionary of error information

        .. method:: peek_start_time()

            Reads the start-time in the object.

            :rtype: None or start time of the log_quiet_control

        .. method:: set_end_time(value)

            Sets the end time of log_quiet_control object.

            :param value: end time period in hh:mm to quiet the logs within
                          the switch
            :rtype: None or dictionary of error information

        .. method:: peek_end_time()

            Reads the end time in the object.

            :rtype: None or end time of the log_quiet_control

        .. method:: set_days_of_week_day(value)

            Sets the quiet days of log_quiet_control object.

            :param value: day to quiet the logs within the switch
            :rtype: None or dictionary of error information

        .. method:: peek_days_of_week()

            Reads the quiet days in the object.

            :rtype: None or quiet days of the log_quiet_control

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
    Class of configurable parameters of log control

    Important class members:

        +---------------------+-----------+----------------------------------+
        |Attribute name       |Description|Frequently used methods           |
        +=====================+===========+==================================+
        |keep-alive-period    |Log alive  |:meth:`set_keep_alive_period`     |
        |                     |period     |:meth:`peek_keep_alive_period`    |
        +---------------------+-----------+----------------------------------+
        |syslog-facility-level|Syslog     |:meth:`peek_syslog_facility_level`|
        |                     |facility   |:meth:`set_syslog_facility_level` |
        |                     |level      |                                  |
        +---------------------+-----------+----------------------------------+

    *Object methods*

        .. method:: get(session)

            Returns a :class:`log_setting` object with attributes from
            log_setting.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary of error or a
                :class:`log_setting` object

        .. method:: patch(session)

            Apply configurable attribute(s) within the object to log_setting.

            *Below is an example using individual sets:*

            .. code-block:: python

                # initialize the log_setting object
                log_setting_obj = pyfos_brocade_logging.log_setting()
                # set the log-type attribute to enable the
                # wwn based pid on the log_setting
                log_setting_obj.set_keep_alive_period(value)
                # execute HTTP patch command to apply the object to the
                # log_setting connected through session
                log_setting_obj.patch(session)

            *Below is an example of combining object \
                    initialization and attribute sets:*

            .. code-block:: python

                # initialize the log_setting object and
                # set the enable attribute
                log_setting_obj = pyfos_brocade_logging.log_setting(
                    {"keep-alive-period" : 24})
                # execute HTTP patch command to apply the object to the
                # log_setting connected through session
                log_setting_obj.patch(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: a dictionary of error or success information

    *Attribute methods*

        .. method:: peek_keep_alive_period()

            Reads the message id of log_setting in the object.

            :rtype: message id

        .. method:: set_keep_alive_period(value)

            Sets the log_setting object.

            :param value: keep alive period
            :rtype: None or dictionary of error information

        .. method:: peek_syslog_facility_level()

            Reads the syslog facility level in the object

            :rtype: None or syslog facility level

        .. method:: set_syslog_facility_level(level)

            Sets the syslog facility level.

            :param: facility level
            :rtype: dictionary of error or success response
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

    """ This class provides methods/options to retrieve and configure
        audit logging.


    Important class members:

        +-----------------+-------+-------------------------------------------+
        | Attribute name  | Desc. |Frequently used methods                    |
        +=================+=======+===========================================+
        | audit-enabled   | Audit |:meth:`peek_audit_enabled`                 |
        |                 | Flag  |:meth:`set_audit_enabled`                  |
        +-----------------+-------+-------------------------------------------+
        | severity-level  | Severe|:meth:`peek_severity_level`                |
        |                 | Level |:meth:`set_severity_level`                 |
        +-----------------+-------+-------------------------------------------+
        |filter-class-list| Class |:meth:`peek_filter_class_list_filter_class`|
        |/filter-class    | List  |:meth:`set_filter_class_list_filter_class` |
        +-----------------+-------+-------------------------------------------+

    *Object methods*

        .. method:: get(session)
            Returns a :class:`audit` object or a list of objects filled
            with attributes gathered from auditcfg.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

        .. method:: patch(session)

               Apply configurable attribute(s) within the object to audit

               *Below is an example using individual sets:*

            .. code-block:: python

                # initialize the audit object
                audit_obj = pyfos_brocade_logging.audit()
                # set audit enabled to true
                audit_obj.set_audit_enabled(true)
                # set the severity level to info
                audit_obj.set_severity_level(info)
                audit_obj.patch(session)

                :param session: session handler returned by audit
                    :func:`pyfos_auth.login`
                :rtype: a dictionary of error or success information

    *Attribute methods*

        .. method:: set_audit_enabled(enable/disable)

            Sets enabled=true or disabled=false in the object

            :param enable/disable: true to enable and false to disable audit
            :rtype: dictionary of error or success response

        .. method:: peek_audit_enabled()

            Reads audit enabled state in the object.

            :rtype: true or false

        .. method:: set_severity_level(level)

            Sets level of severity in the object

            :param : level: Valid severity level: info,warning,critical,error
            :rtype: dictionary of error or success response

        .. method:: peek_severity_level()

            Reads severtiy level in the object.

            :rtype: level of severity of audit

        .. method:: set_filter_class_list_filter_class(filter_class_list)

            Sets filter class list in the object

            :param : level: Valid filter class list - security,configuration,
            zone,firmware,fabric,ls,cli,maps
            :rtype: dictionary of error or success response

        .. method:: peek_filter_class_list_filter_class()

            Reads filter class list in the object.

            :rtype: filter class list of audit

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.audit,
                         "/rest/running/brocade-logging/audit",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "audit-enabled", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "severity-level",  pyfos_type.type_str,
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
    """ This class provides methods/options to retrieve, configure, modify
        and delete syslog.


    Important class members:

        +----------------+-------------------+------------------------+
        | Attribute name | Description       |Frequently used methods |
        +================+===================+========================+
        | server         | syslog server name|:meth:`peek_server`     |
        |                |                   |:meth:`set_server`      |
        +----------------+-------------------+------------------------+
        | port           | port syslog server|:meth:`peek_port`       |
        |                |                   |:meth:`set_port`        |
        +----------------+-------------------+------------------------+
        | secure-mode    | secure mode       |:meth:`peek_secure_mode`|
        |                | using TLS protocol|:meth:`set_secure_mode` |
        +----------------+-------------------+------------------------+

    *Object methods*

    .. method:: get(session)
        Returns a :class:`syslog_server` object or list of objects filled with
        syslog server attributes.

        Each object can be printed using :func:`pyfos_util.response_print`
        and individual attributes accessed through peek methods.

    .. method:: post(session)

        Add members to a list attribute of the object. This method is used to
        add syslog servers.

        Example usage of the method to configure new syslog server:

        # initialize the syslog server object
        syslog_server_obj = pyfos_brocade_logging.syslog_server()
        # set the IP address of server
        syslog_server_obj.set_server("10.10.10.10")

        :param session: session handler returned by
           :func:`pyfos_auth.login`
        :rtype: dictionary of error or success response

    .. method:: patch(session)

           Apply configurable attribute(s) within the object to syslog_server

           *Below is an example using individual sets:*

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

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: a dictionary of error or success information

    .. method:: delete(session)

            Delete members from a list attribute of the object. This method
            deletes the syslog server configured.

             Example usage of the method to create a new Mappings:

            # initialize the syslog server object
            syslog_server_obj = pyfos_brocade_logging.syslog_server()
            # set the IP address of server
            syslog_server_obj.set_server("10.10.10.10")
            # delete the syslog server
            syslog_server_obj.delete(session)

    *Attribute methods*

        .. method:: set_server(server)

            Sets server in the object

            :param server: IPv4/v6 address or dns name of syslog server
            :rtype: dictionary of error or success response

        .. method:: peek_server()

            Reads syslog server in the object.

            :rtype: server IP address or dns name

        .. method:: set_port(port)

            Sets port number in the object.

            :param port: port number of syslog server
            :rtype: dictionary of error or success response

        .. method:: peek_port()

            Reads port number in the object.

            :rtype: port number in the object

        .. method:: set_secure_mode(true/false)

            Sets secure mode in the object

            :param true/false:true=enables secure mode and false disables it
            :rtype: dictionary of error or success response

        .. method:: peek_secure_mode()

            Reads secure mode in the object.

            :rtype: secure mode true or false

    """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.syslog,
                         "/rest/running/brocade-logging/syslog-server",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "server", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "port",  pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "secure-mode", pyfos_type.type_bool,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)
