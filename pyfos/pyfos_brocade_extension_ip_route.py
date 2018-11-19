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

:mod:`pyfos_brocade_extension_ip_route` - PyFOS module for extension \
IP routes.
********************************************************************************
The :mod:`pyfos_extension_iproute` module provides REST support for
IP route extension objects.
"""
from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type


class extension_ip_route(pyfos_rest_util.rest_object):
    """Class of extension_iproute

    Important Class Members:

        +----------------+--------------+-----------------------------+
        | Attribute Name | Description  |Frequently Used Functions    |
        +================+==============+=============================+
        |name            |The slot/port |:func:`peek_name`            |
        |                |name of the   |:func:`set_name`             |
        |                |GE_Port.      |                             |
        +----------------+--------------+-----------------------------+
        |ip-address      |The IPv4/IPv6 |:func:`peek_ip_address`      |
        |                |address.      |:func:`peek_ip_address`      |
        +----------------+--------------+-----------------------------+
        |dp-id           |The data-path |:func:`peek_dp_id`           |
        |                |processor ID. |:func:`set_dp_id`            |
        |                |              |                             |
        +----------------+--------------+-----------------------------+
        |ip-prefix-length|The IP prefix |:func:`peek_ip_prefix_length`|
        |                |length.       |:func:`set_ip_prefix_length` |
        +----------------+--------------+-----------------------------+
        |ip-gateway      |The IP address|                             |
        |                |of the        |                             |
        |                |gateway.      |                             |
        |                |              |                             |
        +----------------+--------------+-----------------------------+
        |status-flags    |The IP        |:func:`peek_status_flags`    |
        |                |interface     |                             |
        |                |flags.        |                             |
        +----------------+--------------+-----------------------------+

    *Object Functions*

        .. function:: get()

            Fills the object with values for all the attributes. Once filled,
            the object can be printed using :func:`pyfos_utils.response_print`.

            :param session: The session handler returned
             by :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

    *Attribute Functions*

        .. function:: peek_name()

            Reads the name from the object.

            :rtype: None on error and a value on success.

        .. function:: peek_ip_address()

            Reads the IP address from the object.

            :rtype: None on error and a value on success.

        .. function:: peek_dp_id()

            Reads the data-path processor ID from the object.

            :rtype: None on error and a value on success.

        .. function:: peek_ip_prefix_length()

            Reads the IP prefix length from an object.

            :rtype: None on error and a value on success.

        .. function:: peek_ip_gateway()

            Reads the IP gateway from an object.

            :rtype: None on error and a value on success.

        .. function:: peek_status_flags()

            Reads the IP interface flags from an object.

            :rtype: None on error and a value on success.

        .. function:: set_name(name)

            Sets the name in the object.

            :rtype: A dictionary of errors or success response
             and a value with the name as the key.

        .. function:: set_ip_address(ip_address)

            Sets the IP address in the object.

            :rtype: A dictionary of errors or success response
             and a value with "ip-address" as the key.

        .. function:: set_dp_id(dpid)

            Sets the data-path processor ID in the object.

            :rtype: A dictionary of errors or success response and
             a value with the DP ID as the key.

        .. function:: set_ip_prefix_length(prefixlength)

            Sets the IP prefix length in the object.

            :rtype: A dictionary of errors or success response and a value
             with "IP prefix length as the key.

        .. function:: set_ip_gateway(gateway)

            Sets the MTU size in the object.

            :rtype: A dictionary of errors or success response and a value
             with the MTU size as the key.

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
