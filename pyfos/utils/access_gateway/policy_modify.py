#!/usr/bin/env python3

# Copyright 2018 Brocade Communications Systems LLC.  All rights reserved.
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

:mod:`policy_modify` - PyFOS util to enable/disable policies.
****************************************************************************
The :mod:`policy_modify` provides option to enable/disable the policies.

This module can be used to enable AG policies like port-group policy,
auto policy.

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

| Util scripts options:

|      --port-group=PORT-GROUP     Port group policy <0|1>
|      --auto=AUTO                 Auto policy <0|1>

* outputs:
    * Status of the policy modify operation

..function:: policy_modify.modify_policy(session, port_group_enabled,
auto_enabled)

    * Enable/Disable a policy

        Example usage of the method::

           ret = policy_modify.modify_policy(session, 1, None)
           print (ret)

        Details::

            policy_obj = policy()
            if port_group_enabled is None and
               auto_enabled is None:
               return
            if port_group_enabled is not None:
               policy_obj.set_port_group_policy_enabled(port_group_enabled)
            if auto_enabled is not None:
               policy_obj.set_auto_policy_enabled(auto_enabled)

            result = _modify_policy(session, policy_obj)
            print (ret)

        * inputs:
            :param session: session returned by login.
            :param port_group_enabled: 1 (Enable)/0 (Disable) Port Group policy
            :param auto_enabled: 1 (Enable)/0 (Disable) Auto policy

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Enable/Disable port-group policy
        2. Enable/Disable auto policy

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_access_gateway import policy


def _modify_policy(session, restobject):
    return restobject.patch(session)


def modify_policy(session, port_group_enabled, auto_enabled):
    policy_obj = policy()
    if (port_group_enabled is None and
       auto_enabled is None):
        return 1
    if port_group_enabled is not None:
        policy_obj.set_port_group_policy_enabled(port_group_enabled)
    if auto_enabled is not None:
        policy_obj.set_auto_policy_enabled(auto_enabled)

    result = _modify_policy(session, policy_obj)
    return result


def validate(policy_obj):
    if (policy_obj.peek_port_group_policy_enabled() is None and
            policy_obj.peek_auto_policy_enabled() is None):
        return 1

    if (policy_obj.peek_port_group_policy_enabled() is not None and
            policy_obj.peek_auto_policy_enabled() is not None):
        print("Port group and Auto cannot be modified simultaneously")
        policy_obj.showusage()
        sys.exit(1)
    return 0


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    inputs = brcd_util.parse(argv, policy, None, validate)

    session = brcd_util.getsession(inputs)

    # pyfos_util.response_print(inputs['utilobject'].displaycustomcli())
    result = _modify_policy(inputs['session'], inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
