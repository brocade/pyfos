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


# dp_hcl_status_show.py(pyGen v1.0.0)


"""

:mod:`dp_hcl_status_show` - PyFOS util to show for dp_hcl_status
*******************************************************************************
The:mod:`dp_hcl_status_show` PyFOS util to show for dp_hcl_status


Represents the HCL status on extension datapath process.

dp_hcl_status_show: usage

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
    * --ip-hcl-stage=IP-HCL-STAGE: The current DP HCL stage for IP protocol.
    * --firmware-version=FIRMWARE-VERSION: A human readable string identifying\
      the firmware version running on the datapath process of the\
      switch/blade.
    * --dp-id=DP-ID: Extension Data Path Processor ID. Based on platform\
      either it will have a single DP or dual DP. In case of single DP only\
      DP0 is supported, and in case of dual DP both DP0 and DP1 are\
      supported  0 : DP0 1 : DP1.
    * --slot=SLOT: The slot number of for the datapath processor.
    * --state=STATE: The current DP HCL state
    * --svi-swapped=SVI-SWAPPED: Is the SVI swapped for HCL processing
    * --dp-communication-status=DP-COMMUNICATION-STATUS: The current state of\
      DP-DP communication
    * --status=STATUS: The current DP status.
    * --fc-hcl-stage=FC-HCL-STAGE: The current DP HCL stage for FC protocol.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: dp_hcl_status_show.show_dp_hcl_status(session, ip_hcl_stage,\
firmware_version, dp_id, slot, state, svi_swapped, dp_communication_status,\
status, fc_hcl_stage)

    *Show dp_hcl_status*

    Example Usage of the Method::

            ret = dp_hcl_status_show.show_dp_hcl_status(session, ip_hcl_stage,\
 firmware_version, dp_id, slot, state, svi_swapped, dp_communication_status,\
 status, fc_hcl_stage)
            print(ret)

    Details::

        dp_hcl_statusObj = dp_hcl_status()
        dp_hcl_statusObj.set_ip_hcl_stage(ip_hcl_stage)
        dp_hcl_statusObj.set_firmware_version(firmware_version)
        dp_hcl_statusObj.set_dp_id(dp_id)
        dp_hcl_statusObj.set_slot(slot)
        dp_hcl_statusObj.set_state(state)
        dp_hcl_statusObj.set_svi_swapped(svi_swapped)
        dp_hcl_statusObj.set_dp_communication_status(dp_communication_status)
        dp_hcl_statusObj.set_status(status)
        dp_hcl_statusObj.set_fc_hcl_stage(fc_hcl_stage)
        ret = _show_dp_hcl_status(session, dp_hcl_statusObj)
        print(ret)

    **Inputs**

    :param session: The session returned by the login.
    :param ip_hcl_stage: The current DP HCL stage for IP protocol.
    :param firmware_version: A human readable string identifying the firmware\
      version running on the datapath process of the switch/blade.
    :param dp_id: Extension Data Path Processor ID. Based on platform either\
      it will have a single DP or dual DP. In case of single DP only DP0 is\
      supported, and in case of dual DP both DP0 and DP1 are supported  0 :\
      DP0 1 : DP1.
    :param slot: The slot number of for the datapath processor.
    :param state: The current DP HCL state
    :param svi_swapped: Is the SVI swapped for HCL processing
    :param dp_communication_status: The current state of DP-DP communication
    :param status: The current DP status.
    :param fc_hcl_stage: The current DP HCL stage for FC protocol.

    **Output**

    :rtype: None or one/more instance of class dp_hcl_status on Success  or a\
    dictionary with error.

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_extension import dp_hcl_status

from pyfos.utils import brcd_util
# End module imports


def _show_dp_hcl_status(session, dp_hcl_statusObj):
    objlist = dp_hcl_status.get(session)
    dp_hcl_statuslist = list()
    if isinstance(objlist, dp_hcl_status):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if dp_hcl_statusObj.peek_ip_hcl_stage() is not None and\
               dp_hcl_statusObj.peek_ip_hcl_stage() !=\
               objlist[i].peek_ip_hcl_stage():
                continue
            if dp_hcl_statusObj.peek_firmware_version() is not None and\
               dp_hcl_statusObj.peek_firmware_version() !=\
               objlist[i].peek_firmware_version():
                continue
            if dp_hcl_statusObj.peek_dp_id() is not None and\
               dp_hcl_statusObj.peek_dp_id() != objlist[i].peek_dp_id():
                continue
            if dp_hcl_statusObj.peek_slot() is not None and\
               dp_hcl_statusObj.peek_slot() != objlist[i].peek_slot():
                continue
            if dp_hcl_statusObj.peek_state() is not None and\
               dp_hcl_statusObj.peek_state() != objlist[i].peek_state():
                continue
            if dp_hcl_statusObj.peek_svi_swapped() is not None and\
               dp_hcl_statusObj.peek_svi_swapped() !=\
               objlist[i].peek_svi_swapped():
                continue
            if dp_hcl_statusObj.peek_dp_communication_status() is not None and\
               dp_hcl_statusObj.peek_dp_communication_status() !=\
               objlist[i].peek_dp_communication_status():
                continue
            if dp_hcl_statusObj.peek_status() is not None and\
               dp_hcl_statusObj.peek_status() != objlist[i].peek_status():
                continue
            if dp_hcl_statusObj.peek_fc_hcl_stage() is not None and\
               dp_hcl_statusObj.peek_fc_hcl_stage() !=\
               objlist[i].peek_fc_hcl_stage():
                continue
            dp_hcl_statuslist.append(objlist[i])
    else:
        return objlist
    return dp_hcl_statuslist


def show_dp_hcl_status(session, ip_hcl_stage=None, firmware_version=None,
                       dp_id=None, slot=None, state=None, svi_swapped=None,
                       dp_communication_status=None, status=None,
                       fc_hcl_stage=None):
    dp_hcl_statusObj = dp_hcl_status()
    dp_hcl_statusObj.set_ip_hcl_stage(ip_hcl_stage)
    dp_hcl_statusObj.set_firmware_version(firmware_version)
    dp_hcl_statusObj.set_dp_id(dp_id)
    dp_hcl_statusObj.set_slot(slot)
    dp_hcl_statusObj.set_state(state)
    dp_hcl_statusObj.set_svi_swapped(svi_swapped)
    dp_hcl_statusObj.set_dp_communication_status(dp_communication_status)
    dp_hcl_statusObj.set_status(status)
    dp_hcl_statusObj.set_fc_hcl_stage(fc_hcl_stage)
    return _show_dp_hcl_status(session, dp_hcl_statusObj)


def validate(dp_hcl_statusObj):
    if dp_hcl_statusObj.peek_ip_hcl_stage() is None or\
       dp_hcl_statusObj.peek_firmware_version() is None or\
       dp_hcl_statusObj.peek_dp_id() is None or dp_hcl_statusObj.peek_slot()\
       is None or dp_hcl_statusObj.peek_state() is None or\
       dp_hcl_statusObj.peek_svi_swapped() is None or\
       dp_hcl_statusObj.peek_dp_communication_status() is None or\
       dp_hcl_statusObj.peek_status() is None or\
       dp_hcl_statusObj.peek_fc_hcl_stage() is None:
        return 0
    return 0


def main(argv):
    filters = ["ip_hcl_stage", "firmware_version", "dp_id", "slot", "state",
               "svi_swapped", "dp_communication_status", "status",
               "fc_hcl_stage"]
    inputs = brcd_util.parse(argv, dp_hcl_status, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _show_dp_hcl_status(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
