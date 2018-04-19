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

:mod:`pyfos_brocade_extension_ip_route` - PyFOS module for Extension IP Route.
******************************************************************************
The :mod:`pyfos_extension_iproute` provides a REST support for
IP Route Extension objects.
"""
import pyfos.pyfos_rest_util as pyfos_rest_util
from pyfos.pyfos_type import pyfos_type


class extension_ip_route(pyfos_rest_util.rest_object):
    """Class of extension_iproute

    Important class members:

        +-------------------------------+-------------------------------+---------------------------------------+
        | Attribute name                | Description                   |Frequently used functions              |
        +===============================+===============================+=======================================+
        | name                          | The slot/port name of GE port |:func:`peek_name`                      |
        +-------------------------------+-------------------------------+---------------------------------------+
        | name                          | The slot/port name of GE port |:func:`set_name`                       |
        +-------------------------------+-------------------------------+---------------------------------------+
        | ip-address                    | The IPv4/IPv6 address         |:func:`peek_ip_address`                |
        +-------------------------------+-------------------------------+---------------------------------------+
        | ip-address                    | The IPv4/IPv6 address         |:func:`set_ip_address`                 |
        +-------------------------------+-------------------------------+---------------------------------------+
        | dp-id                         | Data-path Processor ID        |:func:`peek_dp_id`                     |
        +-------------------------------+-------------------------------+---------------------------------------+
        | dp-id                         | Data-path Processor ID        |:func:`set_dp_id`                      |
        +-------------------------------+-------------------------------+---------------------------------------+
        | ip-prefix-length              | The prefix length of IP       |:func:`peek_ip_prefix_length`          |
        +-------------------------------+-------------------------------+---------------------------------------+
        | ip-prefix-length              | The prefix length of IP       |:func:`set_ip_prefix_length`           |
        +-------------------------------+-------------------------------+---------------------------------------+
        | ip-gateway                    | The IP Address Gateway        |:func:`peek_ip_gateway`                |
        +-------------------------------+-------------------------------+---------------------------------------+
        | ip-gateway                    | The IP Address Gateway        |:func:`set_ip_gateway`                 |
        +-------------------------------+-------------------------------+---------------------------------------+
        | status-flags                  | IP Interface Flags            |:func:`peek_status_flags`              |
        +-------------------------------+-------------------------------+---------------------------------------+

    *Object functions*

        .. function:: get()

            Fill the object with values for all the attributes. Once filled,
            the object can be printed using :func:`pyfos_utils.response_print`

            :param session: session handler returned
             by :func:`pyfos_auth.login`
            :rtype: dictionary of error or success response

    *Attribute functions*

        .. function:: peek_name()

            Reads name from the object.

            :rtype: None on error and value on success

        .. function:: peek_ip_address()

            Reads IP Address from the object.

            :rtype: None on error and value on success

        .. function:: peek_dp_id()

            Reads the Data-path Processor ID from the Object

            :rtype: None on error and value on success

        .. function:: peek_ip_prefix_length()

            Reads the IP prefix length from an object.

            :rtype: None on error and value on success

        .. function:: peek_ip_gateway()

            Reads IP Gateway from an object.

            :rtype: None on error and value on success

        .. function:: peek_status_flags()

            Reads IP interface flags from an object.

            :rtype: None on error and value on success

        .. function:: set_name(name)

            Set the name in the object.

            :rtype: dictionary of error or success response
             and value with "name" as key

        .. function:: set_ip_address(ip_address)

            Set the IP Address in the object.

            :rtype: dictionary of error or success response
             and value with "ip-address" as key

        .. function:: set_dp_id(dpid)

            Set the Data-path Processor ID in the Object

            :rtype: dictionary of error or success response and
             value with "dp-id" as key

        .. function:: set_ip_prefix_length(prefixlength)

            Set the IP prefix length in the object.

            :rtype: dictionary of error or success response and value
             with "ip-prefix-length" as key

        .. function:: set_ip_gateway(gateway)

            Set the mtu size in the object.

            :rtype: dictionary of error or success response and value
             with "mtu-size" as key

        """
    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.iproute,
                         "/rest/running/brocade-extension-ip-route"
                         "/extension-ip-route")
        self.add(pyfos_rest_util.rest_attribute("name",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("ip-address",
                 pyfos_type.type_ip_addr, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("dp-id",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("ip-prefix-length",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("ip-gateway",
                 pyfos_type.type_ip_addr, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG_MANDATORY))
        self.add(pyfos_rest_util.rest_attribute("status-flags",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.load(dictvalues, 1)
