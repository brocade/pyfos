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

:mod:`chassis_name_set` - PyFOS util to set user friendly name to chassis.
***********************************************************************************
The :mod:`chassis_name_set` provides option to configure name
to chassis.

This module can be used to set name to chassis.

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

| Util scripts options:

|      --user-name=<username>        set "user friendly name to chassis"

* outputs:
    * Python dictionary content with RESTCONF response data.

.. function:: chassis_name_set.set_user_name(session, name)

    * Set the user friendly name to chassis.

        Example usage of the method::

            ret = chassis_name_set.set_user_name(session,
                      name)
            print (ret)

        Details:

            chassis_obj = chassis()
            chassis_obj.set_user_name(name)
            return chassis_obj.patch(session)

        * inputs:
            :param session: session returned by login.
            :param name: User friendly name to chassis.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Set the user friendly name to chassis.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_chassis import chassis
from pyfos.utils import brcd_util


def set_user_name(session, name):
    chassis_obj = chassis()
    chassis_obj.set_chassis_user_friendly_name(name)
    return chassis_obj.patch(session)


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['chassis_user_friendly_name']
    inputs = brcd_util.parse(argv, chassis, filters)

    chassis_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    if chassis_obj.peek_chassis_user_friendly_name() is None:
        print("Missing input(s)")
        print(inputs['utilusage'])
        sys.exit()

    result = set_user_name(inputs['session'],
                           chassis_obj.peek_chassis_user_friendly_name())
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
