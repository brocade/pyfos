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
:mod:`maps_group_show` - PyFOS util to display MAPS Policy
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
    --name                 specify group name

* output:

    If Group name is entered, then all the Group information will be displayed.
    Else all the groups present in the switch will be displayed.
"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_maps import group
import pyfos.utils.brcd_util as brcd_util


def show_group(session, group_object):
    name = group_object.peek_name()
    result = group_object.get(session, name)
    return result


def main(argv):

    filters = ['name']
    inputs = brcd_util.parse(argv, group, filters)
    group_object = inputs['utilobject']

    session = brcd_util.getsession(inputs)
    result = show_group(session, group_object)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
