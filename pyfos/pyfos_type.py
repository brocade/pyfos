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


class pyfos_type():
    type_na = 0
    type_int = 1
    type_wwn = 2
    type_str = 3
    type_bool = 4
    type_ip_addr = 5
    type_ipv6_addr = 6
    type_zoning_name = 7
    type_domain_port = 8

    def __init__(self, pyfos_type):
        self.pyfos_type = pyfos_type

    def get_type(self):
        return self.pyfos_type

    def vaildate_set(self, value):
        return True

    def __validate_peek_help(self, cur_type, value):
        if value is None:
            return True, None
        elif cur_type == pyfos_type.type_int:
            cur_value = int(value)
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
            cur_value = str(value)
            if isinstance(cur_value, str):
                return True, cur_value
        elif cur_type == pyfos_type.type_bool:
            cur_value = bool(value)
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
        else:
            return False, None

    def validate_peek(self, value):
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
    yang_leaf = 0x00010000
    yang_container = 0x00020000
    yang_list = 0x00040000
    yang_leaf_list = 0x00080000


class rest_yang_config():
    yang_key = 0x01000000
    yang_config = 0x02000000
    yang_not_config = 0x02000000
    yang_mandatory = 0x04000000
