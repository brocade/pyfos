#!/usr/bin/env python3


# Copyright © 2019 Broadcom. All rights reserved.
# The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries.
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


# portchannel_member_timeout_set.py(pyGen v1.0.0)


"""

:mod:`portchannel_member_timeout_set` - PyFOS util to modify for\
gigabitethernet
******************************************************************************\
*******************************************************************************
The :mod:`portchannel_member_timeout_set` PyFOS util to modify for\
gigabitethernet


The list of gigabitethernet interfaces on the device. System-controlled\
interfaces created by the system are always present in this list, whether\
they are configured or not.

portchannel_member_timeout_set : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --name=NAME The name of the interface.
    * --portchannel-member-timeout=PORTCHANNEL-MEMBER-TIMEOUT The dynamic\
      portchannel member timeout of the gigabit-ethernet interface. default\
      long.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: portchannel_member_timeout_set.modify_gigabitethernet(session,\
name, portchannel_member_timeout)

    *Modify gigabitethernet*

        Example Usage of the Method::

            ret =\
            portchannel_member_timeout_set.modify_gigabitethernet(session,\
            name, portchannel_member_timeout)
            print (ret)

        Details::

            gigabitethernetObj = gigabitethernet()
            gigabitethernetObj.set_name(name)
            gigabitethernetObj.set_portchannel_member_timeout(\
            portchannel_member_timeout)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param name: The name of the interface.
            :param portchannel_member_timeout: The dynamic portchannel member\
              timeout of the gigabit-ethernet interface. default long.

        * Output:

            :rtype: Dictionary of response

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_interface import gigabitethernet
from pyfos.utils import brcd_util
# End module imports


def _modify_gigabitethernet(session, gigabitethernetObj):
    return gigabitethernetObj.patch(session)


def modify_gigabitethernet(session, name=None,
                           portchannel_member_timeout=None):
    gigabitethernetObj = gigabitethernet()
    gigabitethernetObj.set_name(name)
    gigabitethernetObj.set_portchannel_member_timeout(
                       portchannel_member_timeout)
    return _modify_gigabitethernet(session, gigabitethernetObj)


def validate(gigabitethernetObj):
    if gigabitethernetObj.peek_name() is None or\
       gigabitethernetObj.peek_portchannel_member_timeout() is None:
        return 1
    return 0


def main(argv):
    filters = ["name", "portchannel_member_timeout"]
    inputs = brcd_util.parse(argv, gigabitethernet, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _modify_gigabitethernet(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
