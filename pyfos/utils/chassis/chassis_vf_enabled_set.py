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

:mod:`chassis_vf_enabled_set` - PyFOS util to set VF enabled state to chassis.
***********************************************************************************
The :mod:`chassis_vf_enabled_set` sets the VF enabled state to chassis.

This module is a stand-alone script that can be used to set the\
 VF enabled state.

chassis_vf_enabled_set.py: Usage

* Inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       Login name.
|   -P,--password=PASSWORD Password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           Verbose mode[OPTIONAL].

| Util scripts options:
|   --vf-enabled=VALUE     Set VF enabled-state (enable=true, disable=false).

* Outputs:
    * Python dictionary content with RESTCONF response data.


.. function:: chassis_vf_enabled_set.set_vf_enabled(session, enabled)

    * Set the VF enabled state to chassis.

        Example usage of the method::

            ret = chassis_vf_enabled_set.set_vf_enabled(session,
                      enabled)
            print (ret)

        Details::

            vfstate = {
                            "vf-enabled": enabled,
                      }
            chassis_obj = chassis(vfstate)
            return chassis_obj.patch(session)

        * Inputs:
            :param session: Session returned by login.
            :param enabled: VF enabled state to be set in chassis.

        * Outputs:
            :rtype: Dictionary of return status matching rest response.

        *Use cases*

         Modify chassis VF enabled state to enabled or disabled.


"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_chassis import chassis
import pyfos.utils.brcd_util as brcd_util


def _set_vf_enabled_state(session, restobject):
    return restobject.patch(session)


def set_vf_enabled(session, enabled):
    value_dict = {'vf-enabled': enabled}
    chassis_obj = chassis(value_dict)
    result = _set_vf_enabled_state(session, chassis_obj)
    return result


def validate(chassis_obj):
    if chassis_obj.peek_vf_enabled() is None:
            return 1
    return 0


def main(argv):
    filters = ['vf_enabled']
    inputs = brcd_util.parse(argv, chassis, filters, validate)

    chassis_obj = inputs['utilobject']
    session = brcd_util.getsession(inputs)
    result = _set_vf_enabled_state(inputs['session'], chassis_obj)

    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
