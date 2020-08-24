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

:mod:`pyfos_type` - PyFOS module for :class:`pyfos_rest_util.rest_attribute`\
 to associate correct data type and yang type informations in pyfos along\
 with support for correct data type conversion and validations support for\
 *peek_* and *set_* methods.
******************************************************************************\
******************************************************************************\
******************************************************************************\
******************************************************************************\
*******************************************************************************
The :mod:`pyfos_type` PyFOS module to identify and associate the data type
and yang type informations for :class:`pyfos_rest_util.rest_attribute`.

"""


class pyfos_type():
    """
    class for management of all data types supported for PyFOS class
    :class:`pyfos_rest_util.rest_attribute` types.The class also support
    type conversion and validation to known data types using different
    functions like :func:`validate_peek` and  :func:`validate_peek_help`.

    * PyFOS type enum table:

        +----------------------+-------------------------------+--------------------------------------------------------------+
        |  PyFOS type enum     |  Supported Input value        |  Description and details of the enum type                    |
        +======================+===============================+==============================================================+
        |  *type_na*           |  python None/dict/list        |  Specifies leaf type for composite type like yang container, |
        |                      |                               |  list or leaf list. Also for leaf type where no validations  |
        |                      |                               |  needed.                                                     |
        +----------------------+-------------------------------+--------------------------------------------------------------+
        |  *type_int*          |  Integer input values         |  Specifies leaf type which takes integer input values the    |
        |                      |                               |  yang zero based counters, integer values bound by range etc |
        +----------------------+-------------------------------+--------------------------------------------------------------+
        | *type_wwn*           |  string equivalent wwn        |  Specifies leaf type which takes yang wwn input values str   |
        +----------------------+-------------------------------+--------------------------------------------------------------+
        | *type_str*           |  string input value           |  Specifies leaf type which takes string input values.        |
        +----------------------+-------------------------------+--------------------------------------------------------------+
        | *type_bool*          |  True/False or 0/1            |  Specifies boolean leaf type and can use python boolean or   |
        |                      |                               |  integer equivalent value  for the same 1:True 0:False       |
        +----------------------+-------------------------------+--------------------------------------------------------------+
        | *type_ip_addr*       |  string input in IP v4/v6     |  Specifies leaf type which represents an IPv4/IPv6 addr      |
        +----------------------+-------------------------------+--------------------------------------------------------------+
        | *type_ipv6_addr*     |  string input in IP v6        |  Specifies leaf type which represents an IPV6 addr           |
        +----------------------+-------------------------------+--------------------------------------------------------------+
        | *type_zoning_name*   |  string input value           |  Specifies leaf type which takes string input confirming to  |
        |                      |                               |  zoning rules/checks                                         |
        +----------------------+-------------------------------+--------------------------------------------------------------+
        | *type_domain_port*   |  Integer input values         |  Specifies leaf type which takes integer port values.        |
        +----------------------+-------------------------------+--------------------------------------------------------------+
        | *type_float*         |  float input values           |  Specifies leaf type which takes float input values.         |
        +----------------------+-------------------------------+--------------------------------------------------------------+
        |  type_hex_str        |  String input values for HEX  |  Specifies leaf type which takes hex input value             |
        +----------------------+-------------------------------+--------------------------------------------------------------+

    """

    type_na = 0
    type_int = 1
    type_wwn = 2
    type_str = 3
    type_bool = 4
    type_ip_addr = 5
    type_ipv6_addr = 6
    type_zoning_name = 7
    type_domain_port = 8
    type_float = 9
    type_hex_str = 10

    def __init__(self, my_pyfos_type):
        self.pyfos_type = my_pyfos_type

    def get_type(self):
        """Get the pyfos type value from the class object"""
        return self.pyfos_type

    def get_type_str(self):
        """Get the string equivalent enum value"""
        if self.pyfos_type == pyfos_type.type_na:
            return "na"
        elif self.pyfos_type == pyfos_type.type_int:
            return "int"
        elif self.pyfos_type == pyfos_type.type_wwn:
            return "wwn"
        elif self.pyfos_type == pyfos_type.type_str:
            return "str"
        elif self.pyfos_type == pyfos_type.type_bool:
            return "bool"
        elif self.pyfos_type == pyfos_type.type_ip_addr:
            return "ipv4"
        elif self.pyfos_type == pyfos_type.type_ipv6_addr:
            return "ipv6"
        elif self.pyfos_type == pyfos_type.type_zoning_name:
            return "zoning_name"
        elif self.pyfos_type == pyfos_type.type_domain_port:
            return "domain_port"
        elif self.pyfos_type == pyfos_type.type_float:
            return "float"
        elif self.pyfos_type == pyfos_type.type_hex_str:
            return "hex_str"
        else:
            return "unknown"

    def validate_set(self):
        """ Validate set for :class:`pyfos_rest_util.rest_attribute`"""
        return True

    def __validate_peek_help(self, cur_type, value):
        return self.validate_peek_help(cur_type, value)

    def validate_peek_help(self, cur_type, value):
        """
        Function for validation and also conversion of input data
        value into the correct data type equivalent. This function is common
        and is used for both *peek_* and *set_* variants setters and getters
        alike for :class:`pyfos_rest_util.rest_attribute`
        """
        if value is None:
            return True, None
        elif cur_type == pyfos_type.type_int:
            try:
                cur_value = int(value)
            except ValueError as err:
                print("Incorrect ", self.get_type_str(), "(value:", value,
                      " type", type(value), ")", err)
                return False, None
            except TypeError as err:
                print("Incorrect ", self.get_type_str(), "(value:", value,
                      " type", type(value), ")", err)
                return False, None
            if isinstance(cur_value, int):
                return True, cur_value
        elif cur_type == pyfos_type.type_wwn:
            cur_value = str(value)
            if isinstance(cur_value, str):
                return True, cur_value
        elif cur_type == pyfos_type.type_wwn:
            cur_value = str(value)
            if isinstance(cur_value, str):
                return True, cur_value
        elif cur_type == pyfos_type.type_str:
            if not isinstance(value, str):
                print("Incorrect ", self.get_type_str(), "(value:", value,
                      " type", type(value), ")")
                return False, None
            cur_value = str(value)
            if isinstance(cur_value, str):
                return True, cur_value
        elif cur_type == pyfos_type.type_bool:
            if value in ("True", True, "true", "1"):
                cur_value = True
            elif value in ("False", False, "false", "0"):
                cur_value = False
            else:
                print("Incorrect ", self.get_type_str(), "(value:", value,
                      " type", type(value), ")")
                return False, None
            if isinstance(cur_value, bool):
                return True, cur_value
        elif cur_type == pyfos_type.type_ip_addr:
            cur_value = str(value)
            if isinstance(cur_value, str):
                return True, cur_value
        elif cur_type == pyfos_type.type_zoning_name:
            cur_value = str(value)
            if isinstance(cur_value, str):
                return True, cur_value
        elif cur_type == pyfos_type.type_domain_port:
            cur_value = str(value)
            if isinstance(cur_value, str):
                return True, cur_value
        elif cur_type == pyfos_type.type_ipv6_addr:
            cur_value = str(value)
            if isinstance(cur_value, str):
                return True, cur_value
        elif cur_type == pyfos_type.type_na:
            return True, value
        elif cur_type == pyfos_type.type_float:
            try:
                cur_value = float(value)
            except ValueError as err:
                print("Incorrect ", self.get_type_str(), "(value:", value,
                      " type", type(value), ")", err)
                return False, None
            except TypeError as err:
                print("Incorrect ", self.get_type_str(), "(value:", value,
                      " type", type(value), ")", err)
                return False, None
            if isinstance(cur_value, float):
                return True, cur_value
        elif cur_type == pyfos_type.type_hex_str:
            cur_value = str(value)
            if isinstance(cur_value, str):
                return True, cur_value
        else:
            return False, None

        print("Incorrect ", self.get_type_str(), "(value:", value, " type",
              type(value), ")")
        return False, None

    def validate_peek(self, value):
        """Wrapper for helper function :func:`validate_peek_help` for
        validation and also conversion of input data value into the correct
        data type equivalent. This function is used for *peek_* method of
        :class:`pyfos_rest_util.rest_attribute` """
        if isinstance(self.pyfos_type, list):
            for cur_type in self.pyfos_type:
                correct_type, cast_value = self.__validate_peek_help(cur_type,
                                                                     value)
                if correct_type is True:
                    return correct_type, cast_value
            return False, None
        else:
            return self.__validate_peek_help(self.pyfos_type, value)


class rest_yang_type():
    """
    class rest_yang_type indicates the yang equivalent attribute type
    information for pyfos class :class:`pyfos_rest_util.rest_attribute`
    like *container*, *list*, *leaf*, *leaf list*.

    * yang_leaf: The pyfos attribute is a leaf in the yang.
    * yang_container: The pyfos attribute is a container in the yang.
    * yang_list: The pyfos attribute is a list in the yang.
    * yang_leaf_list: The pyfos attribute is a leaf list in the yang

    """
    yang_leaf = 0x00010000
    yang_container = 0x00020000
    yang_list = 0x00040000
    yang_leaf_list = 0x00080000


class rest_yang_config():
    """
    class rest_yang_config indicates the yang attributes associated with
    pyfos class :class:`pyfos_rest_util.rest_attribute` like *key*,
    *config*, *mandatory* etc.


    * yang_leaf: The pyfos rest_attribute is only a leaf in the yang.
    * yang_key: The pyfos attribute is a key in the yang.
    * yang_config: The pyfos attribute is a config in the yang.
    * yang_not_config: The pyfos attribute is not for configuration in yang.
    * yanf_mandatory: The pyfos attribute is mandatory in yang.

    """
    yang_leaf = 0x00010000
    yang_key = 0x01000000
    yang_config = 0x02000000
    yang_not_config = 0x02000000
    yang_mandatory = 0x04000000
