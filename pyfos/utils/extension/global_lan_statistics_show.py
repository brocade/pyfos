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


# global_lan_statistics_show.py(pyGen v1.0.0)


"""

:mod:`global_lan_statistics_show` - PyFOS util to show for\
 global_lan_statistics
******************************************************************************\
*******************************************************************************
The:mod:`global_lan_statistics_show` PyFOS util to show for\
 global_lan_statistics


Represents global LAN DP statistics for extension blade or system.

global_lan_statistics_show: usage

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
    * --dp-id=DP-ID: Extension Data Path Processor ID. Based on platform\
      either it will have a single DP or dual DP. In case of single DP only\
      DP0 is supported, and in case of dual DP both DP0 and DP1 are\
      supported  0 : DP0 1 : DP1.
    * --slot=SLOT: In case of non-chassis system, the slot number is always 0.\
      In case of chassis system, it is the slot number of chassis in which\
      the extension blade is inserted in. In case of chassis, slot number is\
      non-zero value.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: global_lan_statistics_show.show_global_lan_statistics(session,\
dp_id, slot)

    *Show global_lan_statistics*

    Example Usage of the Method::

            ret =\
 global_lan_statistics_show.show_global_lan_statistics(session, dp_id, slot)
            print(ret)

    Details::

        global_lan_statisticsObj = global_lan_statistics()
        global_lan_statisticsObj.set_dp_id(dp_id)
        global_lan_statisticsObj.set_slot(slot)
        ret = _show_global_lan_statistics(session, global_lan_statisticsObj)
        print(ret)

    **Inputs**

    :param session: The session returned by the login.
    :param dp_id: Extension Data Path Processor ID. Based on platform either\
      it will have a single DP or dual DP. In case of single DP only DP0 is\
      supported, and in case of dual DP both DP0 and DP1 are supported  0 :\
      DP0 1 : DP1.
    :param slot: In case of non-chassis system, the slot number is always 0.\
      In case of chassis system, it is the slot number of chassis in which\
      the extension blade is inserted in. In case of chassis, slot number is\
      non-zero value.

    **Output**

    :rtype: None or one/more instance of class global_lan_statistics on\
    Success  or a dictionary with error.

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_extension import global_lan_statistics

from pyfos.utils import brcd_util
# End module imports


def _show_global_lan_statistics(session, global_lan_statisticsObj):
    objlist = global_lan_statistics.get(session)
    global_lan_statisticslist = list()
    if isinstance(objlist, global_lan_statistics):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if global_lan_statisticsObj.peek_dp_id() is not None and\
               global_lan_statisticsObj.peek_dp_id() !=\
               objlist[i].peek_dp_id():
                continue
            if global_lan_statisticsObj.peek_slot() is not None and\
               global_lan_statisticsObj.peek_slot() !=\
               objlist[i].peek_slot():
                continue
            global_lan_statisticslist.append(objlist[i])
    else:
        return objlist
    return global_lan_statisticslist


def show_global_lan_statistics(session, dp_id=None, slot=None):
    global_lan_statisticsObj = global_lan_statistics()
    global_lan_statisticsObj.set_dp_id(dp_id)
    global_lan_statisticsObj.set_slot(slot)
    return _show_global_lan_statistics(session, global_lan_statisticsObj)


def validate(global_lan_statisticsObj):
    if global_lan_statisticsObj.peek_dp_id() is None or\
       global_lan_statisticsObj.peek_slot() is None:
        return 0
    return 0


def main(argv):
    filters = ["dp_id", "slot"]
    inputs = brcd_util.parse(argv, global_lan_statistics, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _show_global_lan_statistics(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
