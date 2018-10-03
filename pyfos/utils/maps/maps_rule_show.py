#!/usr/bin/env python3

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
:mod:`maps_rule_show` - PyFOS util to display MAPS rule
***************************************************************\
*********************************

* input:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

* Util scripts options:

* output:

    If rule name is entered, then the content of the rule
        will be displayed.
    Else all the rules present in the switch and its contents
        will be displayed.
"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_maps import rule
import pyfos.utils.brcd_util as brcd_util


def show_rule(session, rule_obj):
    name = rule_obj.peek_name()
    result = rule_obj.get(session, name)
    return result


def main(argv):

    filters = ['name']
    inputs = brcd_util.parse(argv, rule, filters)
    rule_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)
    result = show_rule(session, rule_obj)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
