#!/usr/bin/env python3


# Copyright © 2019-2020 Broadcom. All rights reserved.
# The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries.
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


# pyfos_brocade_extension_ip_route.py(pyGen v1.0.0)


"""

:mod:`pyfos_brocade_extension_ip_route` - PyFOS module Represents static\
 IP route on the IP interface defined on extension blade or system.
******************************************************************************\
*******************************************************************************
The:mod:`pyfos_brocade_extension_ip_route` The PyFOS module support\
 Represents static IP route on the IP interface defined on extension blade\
 or system.
"""


# Start module imports
from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
# End module imports


class extension_ip_route(pyfos_rest_util.rest_object):

    """Class of extension_ip_route

    *Description extension_ip_route*

        Represents static IP route on the IP interface defined on extension
        blade or system.

    Important class members of extension_ip_route:

        +--------------------------+---------------------------------+-------------------------------------------------+
        | Attribute Name           | Description                     |  Frequently Used Methods                        |
        +==========================+=================================+=================================================+
        | dp-id                    | Extension Data Path Processor   | :func:`peek_dp_id`                              |
        |                          | ID associated with the IP       | :func:`set_dp_id`                               |
        |                          | Route. Based on platform        |                                                 |
        |                          | either it will have a single    |                                                 |
        |                          | DP or dual DP. In case of       |                                                 |
        |                          | single DP only DP0 is           |                                                 |
        |                          | supported, and in case of       |                                                 |
        |                          | dual DP both DP0 and DP1 are    |                                                 |
        |                          | supported. 0 : DP0 1 : DP1      |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | ip-prefix-length         | The prefix length operator      | :func:`peek_ip_prefix_length`                   |
        |                          | for the destination IP          | :func:`set_ip_prefix_length`                    |
        |                          | address. Once set, prefix       |                                                 |
        |                          | length can not be changed.      |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | name                     | The name of the interface.      | :func:`peek_name`                               |
        |                          |                                 | :func:`set_name`                                |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | ip-address               | Specifies the destination       | :func:`peek_ip_address`                         |
        |                          | IPv4/IPv6 address.              | :func:`set_ip_address`                          |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | ip-gateway               | Specifies the IP address of     | :func:`peek_ip_gateway`                         |
        |                          | an IP router that can route     | :func:`set_ip_gateway`                          |
        |                          | packets to the destination IP   |                                                 |
        |                          | address. The gateway address    |                                                 |
        |                          | must be on the same IP subnet   |                                                 |
        |                          | as one of the port IP           |                                                 |
        |                          | addresses. This operand is      |                                                 |
        |                          | optional with IPv6 addresses.   |                                                 |
        |                          | Once set, IP gateway can not    |                                                 |
        |                          | changed.                        |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+
        | status-flags             | Iproute Flags:  U = Usable G    | :func:`peek_status_flags`                       |
        |                          | = Gateway H = Host C =          |                                                 |
        |                          | Created (Interface) S =         |                                                 |
        |                          | Static L = LinkLayer            |                                                 |
        +--------------------------+---------------------------------+-------------------------------------------------+

    *Object functions for extension_ip_route*

    .. function:: get()

        Get the instances of class "extension_ip_route from switch. The object
         can be printed using :func:`pyfos_utils.response_print`.

        :param session: The session handler returned by
         :func:`pyfos_auth.login`.

        :rtype: A dictionary of errors or a success response.


    *Class functions for extension_ip_route*

        .. function:: peek_dp_id()

            Reads the value assigned to dp-id in the object.

            :rtype: None on error and a value on success.


        .. function:: set_dp_id(value)

            Set the value of dp-id in the object.

            :rtype: A dictionary of error or a success response and a value
             with "dp-id" as the key


        .. function:: peek_ip_prefix_length()

            Reads the value assigned to ip-prefix-length in the object.

            :rtype: None on error and a value on success.


        .. function:: set_ip_prefix_length(value)

            Set the value of ip-prefix-length in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ip-prefix-length" as the key


        .. function:: peek_name()

            Reads the value assigned to name in the object.

            :rtype: None on error and a value on success.


        .. function:: set_name(value)

            Set the value of name in the object.

            :rtype: A dictionary of error or a success response and a value
             with "name" as the key


        .. function:: peek_ip_address()

            Reads the value assigned to ip-address in the object.

            :rtype: None on error and a value on success.


        .. function:: set_ip_address(value)

            Set the value of ip-address in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ip-address" as the key


        .. function:: peek_ip_gateway()

            Reads the value assigned to ip-gateway in the object.

            :rtype: None on error and a value on success.


        .. function:: set_ip_gateway(value)

            Set the value of ip-gateway in the object.

            :rtype: A dictionary of error or a success response and a value
             with "ip-gateway" as the key


        .. function:: peek_status_flags()

            Reads the value assigned to status-flags in the object.

            :rtype: None on error and a value on success.


    """

    def __init__(self, dictvalues=None):

        clsuri = "/rest" + "/running" + "/brocade-extension-ip-route" +\
                 "/extension-ip-route"
        clstype = pyfos_rest_util.rest_obj_type.iproute
        super().__init__(clstype, clsuri)

        self.add(pyfos_rest_util.rest_attribute("dp-id", pyfos_type.type_int,
                 None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("ip-prefix-length",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("name", pyfos_type.type_str,
                 None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("ip-address",
                 pyfos_type.type_ip_addr, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute("ip-gateway",
                 pyfos_type.type_ip_addr, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG_MANDATORY))
        self.add(pyfos_rest_util.rest_attribute("status-flags",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.load(dictvalues, 1)
