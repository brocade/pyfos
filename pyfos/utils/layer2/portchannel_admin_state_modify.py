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


# portchannel_admin_state_modify.py(pyGen v1.0.0)


"""

:mod:`portchannel_admin_state_modify` - PyFOS util to modify for\
portchannel
******************************************************************************\
*******************************************************************************
The :mod:`portchannel_admin_state_modify` PyFOS util to modify for\
portchannel


The list of portchannel interfaces on the switch, their related configuration\
and operational state.

portchannel_admin_state_modify : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --name=NAME The portchannel name.
    * --admin-state-enabled=ADMIN-STATE-ENABLED Indicates the admin state of\
      the portchannel.  The possible values are: false : portchannel is \
      disabled. true  : portchannel is enabled.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: portchannel_admin_state_modify.modify_portchannel(session, name,\
admin_state_enabled)

    *Modify portchannel*

        Example Usage of the Method::

            ret = portchannel_admin_state_modify.modify_portchannel(session,\
            name, admin_state_enabled)
            print (ret)

        Details::

            portchannelObj = portchannel()
            portchannelObj.set_name(name)
            portchannelObj.set_admin_state_enabled(admin_state_enabled)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param name: The portchannel name.
            :param admin_state_enabled: Indicates the admin state of the\
              portchannel.  The possible values are: false : portchannel is \
              disabled. true  : portchannel is enabled.

        * Output:

            :rtype: Dictionary of response

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_interface import portchannel
from pyfos.utils import brcd_util
# End module imports


def _modify_portchannel(session, portchannelObj):
    return portchannelObj.patch(session)


def modify_portchannel(session, name=None, admin_state_enabled=None):
    portchannelObj = portchannel()
    portchannelObj.set_name(name)
    portchannelObj.set_admin_state_enabled(admin_state_enabled)
    return _modify_portchannel(session, portchannelObj)


def validate(portchannelObj):
    if portchannelObj.peek_name() is None or\
       portchannelObj.peek_admin_state_enabled() is None:
        return 1
    return 0


def main(argv):
    filters = ["name", "admin_state_enabled"]
    inputs = brcd_util.parse(argv, portchannel, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _modify_portchannel(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
