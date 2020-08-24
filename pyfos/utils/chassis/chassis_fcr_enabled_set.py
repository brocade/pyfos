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


# chassis_fcr_enabled_set.py(pyGen v1.0.0)


"""

:mod:`chassis_fcr_enabled_set` - PyFOS util to modify FCR state for chassis
*******************************************************************************
The :mod:`chassis_fcr_enabled_set` PyFOS util to modify FCR state for chassis


The complete details of the chassis.

chassis_fcr_enabled_set : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --fcr-enabled=FCR-ENABLED Indicates whether FCR is enabled or not.      \
      true  : enabled      false : disabled
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: chassis_fcr_enabled_set.modify_chassis(session, fcr_enabled)

    *Modify chassis*

        Example Usage of the Method::

            ret = chassis_fcr_enabled_set.modify_chassis(session, fcr_enabled)
            print (ret)

        Details::

            chassisObj = chassis()
            chassisObj.set_fcr_enabled(fcr_enabled)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param fcr_enabled: Indicates whether FCR is enabled or not.      \
              true  : enabled      false : disabled

        * Output:

            :rtype: Dictionary of response

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_chassis import chassis

from pyfos.utils import brcd_util
# End module imports


def _modify_chassis(session, chassisObj):
    return chassisObj.patch(session)


def modify_chassis(session, fcr_enabled=None):
    chassisObj = chassis()
    chassisObj.set_fcr_enabled(fcr_enabled)
    return _modify_chassis(session, chassisObj)


def validate(chassisObj):
    if chassisObj.peek_fcr_enabled() is None:
        return 1
    return 0


def main(argv):
    filters = ["fcr_enabled"]
    inputs = brcd_util.parse(argv, chassis, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _modify_chassis(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
