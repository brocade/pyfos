
# Copyright 2018 Brocade Communications Systems, Inc.  All rights reserved.
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

:mod:`pyfos_brocade_module_version` - PyFOS module to provide \
module level version information for all the supported modules.
**************************************************************************\
**************************************************************************
The :mod:`pyfos_brocade_module_version` provides the REST support for module version.

"""

from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


# pylint: disable=W0622
class module_version(pyfos_rest_util.rest_object):
    """Class of module version

    Important class members:


        +---------------------------+------------------------------+----------------------------------------------------------+
        | Attribute name            | Description                  |Frequently used methods                                   |
        +===========================+==============================+==========================================================+
        | name                      | It refers to yang module     |:meth:`peek_name`                                         |
        |                           | name                         |                                                          |
        +---------------------------+------------------------------+----------------------------------------------------------+
        | version                   | Yang module version in the   |:meth:`peek_version`                                      |
        |                           | format of x.y.z.             |                                                          |
        +---------------------------+------------------------------+----------------------------------------------------------+
        | uri                       | Uniform                      |:meth:`peek_uri`                                          |
        |                           | Resource Identifier (URI)    |                                                          |
        |                           | of a module.                 |                                                          |
        +---------------------------+------------------------------+----------------------------------------------------------+
        | objects                   | List of all the supported    |:meth:`peek_objects`                                      |
        |                           | objects from this module.    |                                                          |
        +---------------------------+------------------------------+----------------------------------------------------------+

    *Object methods*

        .. classmethod:: get(session)

            Returns a :class:`module_version` object filled with attributes
            gathered throuth the session passed in. Each object can be printed
            using :func:`pyfos_util.response_print`.

            :param session: session handler returned by
                :func:`utils.brcd_util.getsession`
            :rtype: a :class:`module-version` object

    *Attribute methods*

        .. method:: peek_name()

            Represents the module name.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_version()

            Represents the module version.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_objects()

            Returns the supported objects for this module.

            :rtype: A dictionary in case of error or a success response.

        .. method:: peek_uri()

            Returns this module uri.

            :rtype: A dictionary in case of error or a success response.

    """
    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.module_version,
                         "/rest/brocade-module-version",
                         version.VER_RANGE_821b_and_ABOVE,
                         0, "module")

        self.add(pyfos_rest_util.rest_attribute("name",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("version",
                 pyfos_type.type_na, dict(),
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute("object",
                 pyfos_type.type_na, None,
                 pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST), ["objects"])
        self.add(pyfos_rest_util.rest_attribute("uri",
                 pyfos_type.type_int, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.load(dictvalues, 1)
