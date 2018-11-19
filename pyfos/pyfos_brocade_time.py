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

:mod:`pyfos_brocade_time` - PyFOS module to provide rest support for time server.
*********************************************************************************
The :mod:`pyfos_brocade_time` provides a REST support for Time Server.

"""

from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


class time_zone(pyfos_rest_util.rest_object):
    """This class provides system time zone information and also can configure the
       time zone by both name and offset values.

    Important class members:

        +--------------------------------+----------------------------------+------------------------------------+
        | Attribute name                 | Description                      |Frequently used methods             |
        +================================+==================================+====================================+
        | name                           | Time zone by name                |:func:`set_name`                    |
        |                                |                                  |:func:`peek_name`                   |
        +--------------------------------+----------------------------------+------------------------------------+
        | gmt-offset-hours               | Hours offset values              |:func:`set_gmt_offset_hours`        |
        |                                |                                  |:func:`peek_gmt_offset_hours`       |
        +--------------------------------+----------------------------------+------------------------------------+
        | gmt-offset-minutes             | Minutes offset values            |:func:`set_gmt_offset_minutes`      |
        |                                |                                  |:func:`peek_gmt_offset_minutes`     |
        +--------------------------------+----------------------------------+------------------------------------+

    *Object methods*

        .. staticmethod:: get(session)

            Return a :class:`time_zone` object filled with TS Time Zone
                             attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                :func:`pyfos_auth.login`

            :rtype: :class:`time_zone` object. Dictionary in case of error.

        .. method:: patch()

            Replace existing configuration. Fields involved are set within
            the object using attribute's set method. This command is used to
            replace the existing time zone configuration.

            Example usage of the method to configure time zone by name:

            .. code-block:: python

                tz_obj = pyfos_brocade_time.time_zone()
                tz_obj.set_name("Africa/Accra")
                tz_obj.patch(session)

            :param session: session handler returned by
                :func:`pyfos_auth.login`
            :rtype: dictionary in case of error or success response

    *Attribute methods*

        .. method:: peek_name()

            Reads time zone name from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_name(name)

            Sets name in the object

            :param name: time zone by name
            :rtype: dictionary in case of error or success response

        .. method:: peek_gmt_offset_hours()

            Reads time zone hours offset value from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_gmt_offset_hours(value)

            Sets value in the object

            :param value: time zone by hours offset
            :rtype: dictionary in case of error or success response

        .. method:: peek_gmt_offset_minutes()

            Reads time zone minutes offset value from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_gmt_offset_minutes(value)

            Sets value in the object

            :param value: time zone by minutes offset
            :rtype: dictionary in case of error or success response

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.time_zone,
                         "/rest/running/brocade-time/time-zone",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "gmt-offset-hours", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "gmt-offset-minutes", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_CONFIG))

        self.load(dictvalues, 1)


class clock_server(pyfos_rest_util.rest_object):
    """This class provides NTP clock server information and also can configure the
       list of NTP clock server or LOCL.

    Important class members:

        +--------------------------------------+----------------------------------+---------------------------------------------------+
        | Attribute name                       | Description                      |Frequently used methods                            |
        +======================================+==================================+===================================================+
        | ntp-server-address/server-address    | NTP server address list or LOCL  |:func:`set_ntp_server_address_server_address`      |
        |                                      |                                  |:func:`peek_ntp_server_address_server_address`     |
        +--------------------------------------+----------------------------------+---------------------------------------------------+
        | active-server                        | Active server address or LOCL    |:func:`peek_active_server`                         |
        +--------------------------------------+----------------------------------+---------------------------------------------------+

    *Object methods*

        .. staticmethod:: get(session)

            Return a :class:`clock_server` object filled with TS
                             Clock Server attributes.

            Each object can be printed using :func:`pyfos_util.response_print`
            and individual attributes accessed through peek methods.

            :param session: session handler returned by
                    :func:`pyfos_auth.login`
            :rtype: :class:`clock_server` object. Dictionary in case of error.

        .. method:: patch()

            Replace existing configuration. Fields involved are set within
            the object using attribute's set method. This command is used to
            replace the existing NTP clock server configuration.

            Example usage of the method to configure ntp clock server:
            .. code-block:: python

             ts_obj = pyfos_brocade_time.clock_server()
             tz_obj.set_ntp_server_address_server-address("1.2.3.4","5.6.7.8")
             tz_obj.patch(session)

            :param session: session handler returned by
                    :func:`pyfos_auth.login`
            :rtype: dictionary in case of error or success response

    *Attribute methods*

        .. method:: peek_ntp_server_address_server_address()

            Reads list or single ntp clock server from the object.

            :rtype: dictionary in case of error or success response

        .. method:: set_ntp_server_address_server_address(name)

            Sets ntp clock server in the object

            :param name: list of server ip's
            :rtype: dictionary in case of error or success response

        .. method:: peek_active_server()

            Reads active ntp clock server from the object.

            :rtype: dictionary in case of error or success response

        """

    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.clock_server,
                         "/rest/running/brocade-time/clock-server",
                         version.VER_RANGE_821_and_ABOVE)

        self.add(pyfos_rest_util.rest_attribute(
            "ntp-server-address", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "server-address", pyfos_type.type_ip_addr,
            None, pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["ntp-server-address"])
        self.add(pyfos_rest_util.rest_attribute(
            "active-server", pyfos_type.type_ip_addr,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.load(dictvalues, 1)
