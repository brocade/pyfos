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

:mod:`snmp_trap_capability_modify` - PyFOS util to modify snmp trap capability
******************************************************************************
The :mod:`snmp_trap_capability_modify` provides option to modify snmp
trap capability attributes

This module can be used to modify trap state and severity level.

* inputs:

|  Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

|  Util scripts options:

  | --trap-name=TRAP-NAME    Trap name
  | --trap-state=TRAP-STATE  Indicates the Trap state is enabled <true/false>
  | --severity=SEVERITY      Trap severity level[OPTIONAL]

* outputs:

    * Status of the trap capability patch operation

.. function:: trap_cap_obj.set_is_trap_enabled_state(state)

    * Configures trap capability state

        Example usage of the method::

            ret = trap_cap_obj.set_is_trap_enabled_state(state)
            print (ret)

        Details::

            trap_cap_obj = trap_capability()
            trap_cap_obj.set_is_trap_enabled_state(state)
            if state is not None:
                ret = trap_cap_obj.set_is_trap_enabled_state(state)

            result = _set_snmp_trap_capability(session, trap_cap_obj)

        * inputs:
            :param session: session returned by login.
            :param state: trap state (enabled / disabled)

        * outputs:
            :rtype: dictionary of return status matching rest response

.. function:: trap_cap_obj.set_severity(severity)

    * Configures severity level for swEventTrap

        Example usage of the method::

            ret = trap_cap_obj.set_severity(severity)
            print (ret)

        Details::

            trap_cap_obj = trap_capability()
            trap_cap_obj.set_severity(severity)
            if severity is not None:
                ret = trap_cap_obj.set_severity(severity)

            result = _set_snmp_trap_capability(session, trap_cap_obj)

        * inputs:
            :param session: session returned by login.
            :param everity: severity level of swEventTrap

        * outputs:
            :rtype: dictionary of return status matching rest response

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_snmp import trap_capability


def _set_snmp_trap_capability(session, restobject):
    return restobject.patch(session)


def _set_trap_enabled_state(session, state):
    trap_cap_obj = trap_capability()
    if state is not None:
        trap_cap_obj.set_is_trap_enabled_state(state)
    result = _set_snmp_trap_capability(session, trap_cap_obj)
    return result


def _set_severity(session, severity):
    trap_cap_obj = trap_capability()
    if severity is not None:
        trap_cap_obj.set_severity(severity)
    result = _set_snmp_trap_capability(session, trap_cap_obj)
    return result


def validate(trap_cap_obj):
    sev_level_list = ['none', 'critical', 'error', 'warning',
                      'informational', 'debug']
    if (trap_cap_obj.peek_trap_name() is None and
            trap_cap_obj.peek_is_trap_enabled_state() is None):
        return 1
    sev_level = trap_cap_obj.peek_severity()

    if (sev_level is not None and sev_level not in sev_level_list):
        return 1
    return 0
#    if (sev_level != "none" and sev_level != "critical" and
#            sev_level != "error" and sev_level != "warning" and
#            sev_level != "informational" and sev_level != "debug"):
#        return 1
#    return 0


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['trap_name', 'is_trap_enabled_state', 'severity']

    inputs = brcd_util.parse(argv, trap_capability, filters, validate)

    session = brcd_util.getsession(inputs)

    result = _set_snmp_trap_capability(inputs['session'], inputs['utilobject'])
    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
