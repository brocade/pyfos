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


# lldp_gigabitethernet_modify.py(pyGen v1.0.0)


"""

:mod:`lldp_gigabitethernet_modify` - PyFOS util to modify for\
gigabitethernet
******************************************************************************\
*******************************************************************************
The :mod:`lldp_gigabitethernet_modify` PyFOS util to modify for\
gigabitethernet


The list of gigabitethernet interfaces on the device. System-controlled\
interfaces created by the system are always present in this list, whether\
they are configured or not.

lldp_gigabitethernet_modify : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --name=NAME The name of the interface.
    * --lldp-profile=LLDP-PROFILE LLDP profile name configured on the port.\
      Blank lldp-profile means LLDP profile is not configured on this port.\
      In such case, lldp global parameters are in use for this port. To\
      configure a new profile or change existing profile on the port, user\
      should perform a PATCH operation with the profile name. To remove the\
      profile from the port, user should perform a PATCH operation with NULL\
      string.
    * --lldp-enabled-state=LLDP-ENABLED-STATE LLDP state of the port Possible\
      values are:  true  - LLDP is enabled on the port  false  - LLDP is\
      disabled on the port
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: lldp_gigabitethernet_modify.modify_gigabitethernet(session,\
name, lldp_profile, lldp_enabled_state)

    *Modify gigabitethernet*

        Example Usage of the Method::

            ret = lldp_gigabitethernet_modify.modify_gigabitethernet(session,\
            name, lldp_profile, lldp_enabled_state)
            print (ret)

        Details::

            gigabitethernetObj = gigabitethernet()
            gigabitethernetObj.set_name(name)
            gigabitethernetObj.set_lldp_profile(lldp_profile)
            gigabitethernetObj.set_lldp_enabled_state(lldp_enabled_state)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param name: The name of the interface.
            :param lldp_profile: LLDP profile name configured on the port.\
              Blank lldp-profile means LLDP profile is not configured on\
              this port. In such case, lldp global parameters are in use for\
              this port. To configure a new profile or change existing\
              profile on the port, user should perform a PATCH operation\
              with the profile name. To remove the profile from the port,\
              user should perform a PATCH operation with NULL string.
            :param lldp_enabled_state: LLDP state of the port Possible values\
              are:  true  - LLDP is enabled on the port  false  - LLDP is\
              disabled on the port

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


def modify_gigabitethernet(session, name=None, lldp_profile=None,
                           lldp_enabled_state=None):
    gigabitethernetObj = gigabitethernet()
    gigabitethernetObj.set_name(name)
    gigabitethernetObj.set_lldp_profile(lldp_profile)
    gigabitethernetObj.set_lldp_enabled_state(lldp_enabled_state)
    return _modify_gigabitethernet(session, gigabitethernetObj)


def validate(gigabitethernetObj):
    if gigabitethernetObj.peek_name() is None:
        return 1

    if gigabitethernetObj.peek_lldp_profile() is None and\
       gigabitethernetObj.peek_lldp_enabled_state() is None:
        return 1
    return 0


def main(argv):
    filters = ["name", "lldp_profile", "lldp_enabled_state"]
    inputs = brcd_util.parse(argv, gigabitethernet, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _modify_gigabitethernet(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
