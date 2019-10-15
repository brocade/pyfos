#!/usr/bin/env python3

# Copyright © 2018 Broadcom. All Rights Reserved. The term “Broadcom” refers to
# Broadcom Inc. and/or its subsidiaries.
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

:mod:`pyfos_brocade_operation_license` - PyFOS module for the license \
 operation.
******************************************************************************\
***********
The :mod:`pyfos_brocade_operation_license` module provides REST support for
 the license operation.

"""

from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as ver


class license(pyfos_rest_util.rest_object):
    """Class of the license Operation

    Important Class Members:

        +---------------------------+-------------------------------+---------------------------------------+
        | Attribute Name            | Description                   |Frequently Used Methods                |
        +===========================+===============================+=======================================+
        | name                      |license name.                  |:func:`set_name`                       |
        +---------------------------+-------------------------------+---------------------------------------+
        | action                    |install or remove license.     |:func:`set_action`                     |
        +---------------------------+-------------------------------+---------------------------------------+

    *Object Methods*

        .. method:: post()

            Configures license. The required fields are set
            within the object using the attribute's set method.

            Example Usage of the Method to Post the license Operation:

            .. code-block:: python

                license_obj =
                    pyfos_brocade_operation_license.license()
                license_obj.set_action("install")
                license_obj.set_name("XYZLICENSEKEY")
                license_obj.post(session)

            The above example triggers the license install operation.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

    *Attribute Methods*

        .. method:: set_name()

            Sets license name.

            :param name: license name.
            :rtype: A dictionary of errors or a success response.

        .. method:: set_action()

            Sets action to install or remove.

            :param action: install or remove.
            :rtype: A dictionary of errors or a success response.

        """
    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.rpc_license,
                         "/rest/operations/license",
                         ver.VER_RANGE_820_ABOVE, 1, "license-parameters")
        self.add(pyfos_rest_util.rest_attribute("name",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("action",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.load(dictvalues, 1)
