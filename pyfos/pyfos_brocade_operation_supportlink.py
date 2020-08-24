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

:mod:`pyfos_brocade_operation_supportlink` - PyFOS module for the supportlink \
 operation.
******************************************************************************\
***********
The :mod:`pyfos_brocade_operation_supportlink` module provides REST support for
 the supportlink operation.

"""

from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as ver


class supportlink(pyfos_rest_util.rest_object):
    """Class of the supportlink Operation

    Important Class Members:

        +--------------------+---------------------------------------+---------------------------------------+
        | Attribute Name     | Description                           |Frequently Used Methods                |
        +====================+=======================================+=======================================+
        | action             |Type of action - default/collect/send. |:func:`set_action`                     |
        +--------------------+---------------------------------------+---------------------------------------+

    *Object Methods*

        .. method:: post()

            Configures supportlink. The required fields are set
            within the object using the attribute's set method.
            This method is used to trigger the supportlink operation in the \
            switch.

            Example Usage of the Method to Post the Supportlink Operation:

            .. code-block:: python

                ss_obj =
                    pyfos_brocade_operation_supportlink.supportlink()
                ss_obj.set_action("default")
                ss_obj.post(session)

            The above example triggers the supportlink operation.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

    *Attribute Methods*

        .. method:: set_action()

            Sets the action type in the object.

            :param action: The action type of the remote server.
            :rtype: A dictionary of errors or a success response.

        """
    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.rpc_supportlink,
                         "/rest/operations/supportlink",
                         ver.VER_RANGE_821_and_ABOVE, 1, "supportlink")
        self.add(pyfos_rest_util.rest_attribute("action",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.load(dictvalues, 1)
