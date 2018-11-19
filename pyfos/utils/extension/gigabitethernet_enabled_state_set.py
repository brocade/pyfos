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

:mod:`gigabitethernet_enabled_state_set` - PyFOS util to set the GE_Port state.
***********************************************************************************
The :mod:`gigabitethernet_enabled_state_set` util sets the GE_Port state.

This module is a stand-alone script that can be used to set the\
 GE_Port enabled state on an extension platform.

gigabitethernet_enabled_state_set.py: Usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * -n,--name=NAME: Sets the name.
    * -e,--enabled-state=VALUE: Sets the enabled state.

* Output:
    * Python dictionary content with RESTCONF response data.

.. function:: gigabitethernet_enabled_state_set.port_state_set(\
session, name, enabled)

    *Modify extension gigabitethernet state*

        Example Usage of the Method::

            ret = gigabitethernet_enabled_state_set.port_state_set(
            session, name, enabled)
            print (ret)

        Details::

            gestate = {
                            "name": name,
                            "enabled-state": enabled,
                      }
            gigabitethernet = gigabitethernet(gestate)
            result = gigabitethernet.patch(session)

        * Input:
            :param session: The session returned by the login.
            :param name: The GE_Port name expressed as slot/port.
            :param speed: The speed for the GE _Port to be set.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

         Modify the extension GE_Port state to enabled or disabled.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_gigabitethernet import gigabitethernet
from pyfos.utils import brcd_util

isHttps = "0"


def _set_port_state(session, restobject):
    return restobject.patch(session)


def port_state_set(session, name, enabled):
    value_dict = {'name': name, 'enabled-state': enabled}
    geObject = gigabitethernet(value_dict)
    result = _set_port_state(session, geObject)
    return result


def validate(geObject):
    if geObject.peek_name() is None or \
       geObject.peek_enabled_state() is None:
        return 1
    return 0


def main(argv):
    # myinputs = "-h -i 10.17.3.70 -n 4/17 -e 1"
    # argv = myinputs.split()
    filters = ['name', 'enabled_state']
    inputs = brcd_util.parse(argv, gigabitethernet, filters,
                             validate)
    geObject = inputs['utilobject']
    session = brcd_util.getsession(inputs)
    result = _set_port_state(inputs['session'], geObject)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
