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

:mod:`gigabitethernet_speed_set` - PyFOS util to set GE port speed.
*******************************************************************************
The :mod:`gigabitethernet_speed_set` Util is used to set speed of GE port.

This module is a stand-alone script that can be used to set the
switch GE port speed on an extension platform.

gigabitethernet_speed_set.py: Usage

* Infrastructure options:
    * -i,--ipaddr=IPADDR: IP address of FOS switch.
    * -L,--login=LOGIN: Login name.
    * -P,--password=PASSWORD: Password.
    * -f,--vfid=VFID: VFID to which the request is directed.
    * -s,--secured=MODE: HTTPS mode "self" or "CA"[Optional].
    * -v,--verbose: Verbose mode[Optional].

* Util scripts options:
    * -n,--name=NAME: Set name.
    *    --speed=VALUE: Set speed.

* Outputs:
    * Python dictionary content with RESTCONF response data.

.. function:: gigabitethernet_speed_set.set_port_speed(session,\
name, speed)

    *Modify extension gigabitethernet speed*

        Example usage of the method::

            ret = gigabitethernet_speed_set.set_port_speed(session,
            name, speed)
            print (ret)

        Details::
                gigabitethernet = gigabitethernet()
                gigabitethernet.set_name(name)
                gigabitethernet.set_speed(speed)

                result = gigabitethernet.patch(session)

        * Inputs:
            :param session: Session returned by login.
            :param name: Gigabitethernet port name expressed as slot/port.
            :param speed: Speed for the GE port to be set.

        * Outputs:
            :rtype: Dictionary of return status matching rest response.

        *Use cases*

         Modify extension gigabitethernet port speed to 1G or 10G.
"""


import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_gigabitethernet import gigabitethernet
import sys
import pyfos.utils.brcd_util as brcd_util


isHttps = "0"


def _set_port_speed(session, rest_obj):
    result = rest_obj.patch(session)
    return (result)


def set_port_speed(session, name, speed):
    geObject = gigabitethernet()
    geObject.set_name(name)
    geObject.set_speed(speed)
    result = _set_port_speed(session, geObject)
    return (result)


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
