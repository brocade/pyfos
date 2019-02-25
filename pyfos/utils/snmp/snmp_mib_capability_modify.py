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

:mod:`snmp_mib_capability_modify` - PyFOS util for updating snmp mib capability
*******************************************************************************
The :mod:`snmp_mib_capability_modify` provides option to modify snmp mib
capability attributes

This module can be used to modify the mib state to enable or disable.

* inputs:

|  Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

|  Util scripts options:

  | --mib-name=MIB-NAME    MIB name
  | --mib-state=MIB-STATE   Indicates the MIB state is enabled <true/false>

* outputs:

    * Status of the mib capability patch operation

.. function:: mib_cap_obj.set_is_mib_enabled_state(state)

    * Configures mib capability state

        Example usage of the method::

            ret = mib_cap_obj.set_is_mib_enabled_state(state)
            print (ret)

        Details::

            mib_cap_obj = mib_capability()
            if state is not None:
                ret = mib_cap_obj.set_is_mib_enabled_state(state)

            result = _set_snmp_mib_capability(session, mib_cap_obj)

        * inputs:
            :param session: session returned by login.
            :param state: mib state (enabled / disabled)

        * outputs:
            :rtype: dictionary of return status matching rest response

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_snmp import mib_capability


def _set_snmp_mib_capability(session, restobject):
    return restobject.patch(session)


def _set_mib_enabled_state(session, state):
    mib_cap_obj = mib_capability()
    if state is not None:
        mib_cap_obj.set_is_mib_enabled_state(state)
    result = _set_snmp_mib_capability(session, mib_cap_obj)
    return result


def validate(mib_cap_obj):
    if (mib_cap_obj.peek_mib_name() is None and
       mib_cap_obj.peek_is_mib_enabled_state() is None):
        return 1
    return 0


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['mib_name', 'is_mib_enabled_state']

    inputs = brcd_util.parse(argv, mib_capability, filters, validate)

    session = brcd_util.getsession(inputs)

    result = _set_snmp_mib_capability(inputs['session'], inputs['utilobject'])
    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
