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


# switch_lacp_system_priority_set.py(pyGen v1.0.0)


"""

:mod:`switch_lacp_system_priority_set` - PyFOS util to modify for\
fibrechannel_switch
******************************************************************************\
*******************************************************************************
The :mod:`switch_lacp_system_priority_set` PyFOS util to modify for\
fibrechannel_switch


Switch state parameters. Requests can also be made using a query that\
specifies the vf-id of the fabric. This request also provides the switch\
state parameters.

switch_lacp_system_priority_set : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --name=NAME The switch world wide name (WWN).
    * --lacp-system-priority=LACP-SYSTEM-PRIORITY Set the system priority of\
      this switch. This priority is used for determining the system that is\
      responsible for resolving conflicts in the choice of aggregation\
      groups. A lower numerical value has a higher priority.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function::\
switch_lacp_system_priority_set.modify_fibrechannel_switch(session, name,\
lacp_system_priority)

    *Modify fibrechannel_switch*

        Example Usage of the Method::

            ret =\
            switch_lacp_system_priority_set.modify_fibrechannel_switch(\
            session, name, lacp_system_priority)
            print (ret)

        Details::

            fibrechannel_switchObj = fibrechannel_switch()
            fibrechannel_switchObj.set_name(name)
            fibrechannel_switchObj.set_lacp_system_priority(\
            lacp_system_priority)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param name: The switch world wide name (WWN).
            :param lacp_system_priority: Set the system priority of this\
              switch. This priority is used for determining the system that\
              is responsible for resolving conflicts in the choice of\
              aggregation groups. A lower numerical value has a higher\
              priority.

        * Output:

            :rtype: Dictionary of response

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_fibrechannel_switch import fibrechannel_switch
from pyfos.utils import brcd_util
# End module imports


def _modify_fibrechannel_switch(session, fibrechannel_switchObj):
    return fibrechannel_switchObj.patch(session)


def modify_fibrechannel_switch(session, name=None, lacp_system_priority=None):
    fibrechannel_switchObj = fibrechannel_switch()
    fibrechannel_switchObj.set_name(name)
    fibrechannel_switchObj.set_lacp_system_priority(lacp_system_priority)
    return _modify_fibrechannel_switch(session, fibrechannel_switchObj)


def validate(fibrechannel_switchObj):
    if fibrechannel_switchObj.peek_name() is None or\
       fibrechannel_switchObj.peek_lacp_system_priority() is None:
        return 1
    return 0


def main(argv):
    filters = ["name", "lacp_system_priority"]
    inputs = brcd_util.parse(argv, fibrechannel_switch, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _modify_fibrechannel_switch(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
