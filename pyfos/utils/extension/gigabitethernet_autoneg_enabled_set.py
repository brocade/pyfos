#!/usr/bin/env python3


# Copyright © 2019-2020 Broadcom. All rights reserved.
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


# gigabitethernet_autoneg_enabled_set.py(pyGen v1.0.0)


"""

:mod:`gigabitethernet_autoneg_enabled_set` - PyFOS util to modify for\
 gigabitethernet
******************************************************************************\
*******************************************************************************
The:mod:`gigabitethernet_autoneg_enabled_set` PyFOS util to modify for\
 gigabitethernet


The list of gigabitethernet interfaces on the device. System-controlled\
 interfaces created by the system are always present in this list, whether\
 they are configured or not.

gigabitethernet_autoneg_enabled_set: usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].
    * -a,--authtoken: AuthToken value or AuthTokenManager config\
    file[OPTIONAL].
    * -z,--nosession: Sessionless authentication based login[OPTIONAL].
    * --nocredential: No credential to be sent in the request[OPTIONAL].

* Util Script Options:
    * --name=NAME: The name of the interface.
    * --auto-negotiation-enabled=AUTO-NEGOTIATION-ENABLED: Auto-negotiation is\
      enabled by default in 1G mode. In 10G mode it is disabled and not\
      supported. When the port is set for 1G mode, you can disable\
      auto-negotiation. In case of chassis system if the slot is powered off\
      or in faulty state then the leaf will be skipped in display. \
      Supported values:  true : Auto negotiation mode for GE port is\
      enabled.  false : Auto negotiation mode for GE port is disabled.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: gigabitethernet_autoneg_enabled_set.modify_gigabitethernet(\
session, name, auto_negotiation_enabled)

    *Modify gigabitethernet*

    Example Usage of the Method::

            ret =\
 gigabitethernet_autoneg_enabled_set.modify_gigabitethernet(session, name,\
 auto_negotiation_enabled)
            print(ret)

    Details::

        gigabitethernetObj = gigabitethernet()
        gigabitethernetObj.set_name(name)
       \
 gigabitethernetObj.set_auto_negotiation_enabled(auto_negotiation_enabled)
        ret = _modify_gigabitethernet(session, gigabitethernetObj)
        print(ret)

    **Inputs**

    :param session: The session returned by the login.
    :param name: The name of the interface.
    :param auto_negotiation_enabled: Auto-negotiation is enabled by default in\
      1G mode. In 10G mode it is disabled and not supported. When the port\
      is set for 1G mode, you can disable auto-negotiation. In case of\
      chassis system if the slot is powered off or in faulty state then the\
      leaf will be skipped in display.  Supported values:  true : Auto\
      negotiation mode for GE port is enabled.  false : Auto negotiation\
      mode for GE port is disabled.

    **Output**

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


def modify_gigabitethernet(session, name=None, auto_negotiation_enabled=None):
    gigabitethernetObj = gigabitethernet()
    gigabitethernetObj.set_name(name)
    gigabitethernetObj.set_auto_negotiation_enabled(auto_negotiation_enabled)
    return _modify_gigabitethernet(session, gigabitethernetObj)


def validate(gigabitethernetObj):
    if gigabitethernetObj.peek_name() is None or\
       gigabitethernetObj.peek_auto_negotiation_enabled() is None:
        return 1
    return 0


def main(argv):
    filters = ["name", "auto_negotiation_enabled"]
    inputs = brcd_util.parse(argv, gigabitethernet, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _modify_gigabitethernet(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
