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

:mod:`gigabitethernet_speed_set` - PyFOS util to set GE_Port speed.
*******************************************************************************
The :mod:`gigabitethernet_speed_set` util is used to set GE_Port speed.

This module is a stand-alone script that can be used to set the
switch GE_Port speed on an extension platform.

gigabitethernet_speed_set.py: Usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * -n,--name=NAME: Sets the name.
    *    --speed=VALUE: Sets the speed.

* Output:
    * Python dictionary content with RESTCONF response data.

.. function:: gigabitethernet_speed_set.set_port_speed(session,\
name, speed)

    *Modify extension gigabitethernet speed*

        Example Usage of the Method::

            ret = gigabitethernet_speed_set.set_port_speed(session,
            name, speed)
            print (ret)

        Details::
                gigabitethernet = gigabitethernet()
                gigabitethernet.set_name(name)
                gigabitethernet.set_speed(speed)

                result = gigabitethernet.patch(session)

        * Input:
            :param session: The session returned by the login.
            :param name: The GE_Port name expressed as slot/port.
            :param speed: The speed at which to set the GE_Port.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

         Modify the extension GE_Port speed to 1G or 10G.
"""


import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_gigabitethernet import gigabitethernet
from pyfos.utils import brcd_util


isHttps = "0"


def _set_port_speed(session, rest_obj):
    result = rest_obj.patch(session)
    return result


def set_port_speed(session, name, speed):
    geObject = gigabitethernet()
    geObject.set_name(name)
    geObject.set_speed(speed)
    result = _set_port_speed(session, geObject)
    return result


def validate(geObject):
    if geObject.peek_name() is None or \
       geObject.peek_speed() is None:
        return 1
    return 0


def main(argv):
    # myinputs = "-h -i 10.17.3.70 --name 4/17 --speed 10000000000"
    # myinputs = "-h -i 10.17.3.70  --speed 1000000000 -n 4/17"
    # myinputs = "--name 4/17 --speed 1000000000"
    # myinputs = "-i 10.17.3.70 --name 4/17"
    # argv = myinputs.split()
    filters = ['name', 'speed']
    inputs = brcd_util.parse(argv, gigabitethernet, filters,
                             validate)
    session = brcd_util.getsession(inputs)

    result = _set_port_speed(inputs['session'], inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
