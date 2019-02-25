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

:mod:`chassis_vf_enabled_set` - PyFOS util to set the VF-enabled state \
on a chassis.
*************************************************************************************
The :mod:`chassis_vf_enabled_set` util sets the VF-enabled state \
on a chassis.

This module is a stand-alone script that can be used to set the\
 VF-enabled state.

chassis_vf_enabled_set.py: Usage

* Input:

| Infrastructure Options:

  | -i,--ipaddr=IPADDR     The IP address of the FOS switch.
  | -L,--login=LOGIN       The login name.
  | -P,--password=PASSWORD The password.
  | -f,--vfid=VFID         The VFID to which the request is \
                            directed [OPTIONAL].
  | -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           Verbose mode [OPTIONAL].

| Util Script Options:

|   --vf-enabled=VALUE     Sets the VF-enabled state (enable=true, \
                            disable=false).

* Output:
    * Python dictionary content with RESTCONF response data.

.. function:: chassis_vf_enabled_set.set_vf_enabled(session, enabled)

    * Sets the VF-enabled state on a chassis.

        Example Usage of the Method::

            ret = chassis_vf_enabled_set.set_vf_enabled(session,
                      enabled)
            print (ret)

        Details::

            vfstate = {
                            "vf-enabled": enabled,
                      }
            chassis_obj = chassis(vfstate)
            return chassis_obj.patch(session)

        * Input:
            :param session: The session returned by the login.
            :param enabled: The VF-enabled state to be set in the chassis.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

         Enable or disable the chassis VF-enabled state.


"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_chassis import chassis
from pyfos.utils import brcd_util


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
