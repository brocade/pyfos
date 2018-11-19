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

:mod:`pyfos_vobject` - PyFOS module to test versioning functionality.
*********************************************************************************************************
The :mod:`pyfos_vobject` PyFOS module to test versioning functionality.
"""
from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type

VER_820 = "8.2.0"
VER_82a = "8.2.0a"
VER_821 = "8.2.1"
VER_822 = "8.2.2"

VER_RANGE_820_to_820a = {'START': "8.2.0", 'END': "8.2.0a"}
VER_RANGE_820_to_821 = {'START': "8.2.0", 'END': "8.2.1"}
VER_RANGE_820_to_822 = {'START': "8.2.0", 'END': "8.2.2"}

VER_RANGE_820_and_ABOVE = {'START': "8.2.0", 'END': "9999.9999.9"}
VER_RANGE_820a_and_ABOVE = {'START': "8.2.0a", 'END': "9999.9999.9"}
VER_RANGE_821_and_ABOVE = {'START': "8.2.1", 'END': "9999.9999.9"}
VER_RANGE_822_and_ABOVE = {'START': "8.2.2", 'END': "9999.9999.9"}


class vobject(pyfos_rest_util.rest_object):
    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.ipif,
                         "/rest/running/brocade-interface/vobject")
        # Leaf Attributes
        self.add(pyfos_rest_util.rest_attribute("a", pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY, VER_RANGE_820_to_820a))
        self.add(pyfos_rest_util.rest_attribute("b", pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY, VER_RANGE_820a_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute("c", pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY, VER_RANGE_821_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute("d", pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
                 VER_RANGE_822_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute("e", pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG, VER_RANGE_820_to_820a))
        self.add(pyfos_rest_util.rest_attribute("f", pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
                 VER_RANGE_822_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute("g", pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
                 VER_RANGE_822_and_ABOVE))
        # Container Attribute
        self.add(pyfos_rest_util.rest_attribute("container",
                 pyfos_type.type_str, dict(),
                 pyfos_rest_util.REST_ATTRIBUTE_CONTAINER_LIST,
                 VER_RANGE_820_and_ABOVE))
        self.add(pyfos_rest_util.rest_attribute("Starting820a",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY,
                 VER_RANGE_820a_and_ABOVE),
                 ['container'])
        self.add(pyfos_rest_util.rest_attribute("Starting821",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_KEY,
                 VER_RANGE_821_and_ABOVE),
                 ['container'])
        self.add(pyfos_rest_util.rest_attribute("Starting822",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
                 VER_RANGE_822_and_ABOVE),
                 ['container'])
        self.add(pyfos_rest_util.rest_attribute("upto820a",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
                 VER_RANGE_820_to_820a),
                 ['container'])
        self.add(pyfos_rest_util.rest_attribute("upto822",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG,
                 VER_RANGE_820_to_822), ['container'])
        self.add(pyfos_rest_util.rest_attribute("upto821",
                 pyfos_type.type_str, None,
                 pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG,
                 VER_RANGE_820_to_821), ['container'])
        self.add(pyfos_rest_util.rest_attribute("Default",
                 pyfos_type.type_str, "123",
                 pyfos_rest_util.REST_ATTRIBUTE_CONFIG))
        self.load(dictvalues, 1)
