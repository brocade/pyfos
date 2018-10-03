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

:mod:`configure_dport_mode_modify` - PyFos util to set dport mode of the \
switch.
***********************************************************************************
The :mod:`configure_dport_mode_modify` sets the dport mode of the switch.

This module is a standalone script that can be used to set the dport mode
of the switch.

* Infrastructure options:
    * -i,--ipaddr=IPADDR: IP address of FOS switch.
    * -L,--login=LOGIN: login name.
    * -P,--password=PASSWORD: password.
    * -f,--vfid=VFID: VFID to which the request is directed to.
    * -s,--secured=MODE: HTTPS mode "self" or "CA"[OPTIONAL].
    * -v,--verbose: verbose mode[OPTIONAL].

* Util scripts options:
    * --dynamic-d-port-enabled=DYNAMIC-D-PORT-ENABLED: set given dynamic dport\
            mode
    * --on-demand-d-port-enabled=ON-DEMAND-D-PORT-ENABLED: set on demand dport\
            mode

* outputs:
    * Python dictionary content with RESTCONF response data

..function:: set_dport_mode(session, dynamic_dport_mode,
                                ondemand_dport_mode)

    Example usage of the method::

        ret = configure_dport_mode_modify.set_dport_mode(session,
                dynamic_dport_mode, ondemand_dport_mode)
        print (ret)

    Details::

        result = configure_dport_mode_modify.set_dport_mode(session,
                dynamic_dport_mode, ondemand_dport_mode)

    * inputs:
        :param session: session returned by login
        :param dynamic_dport_mode: Set dynamic D-port mode
        :param ondemand_dport_mode: Set on demand D-port mode

    * outputs:
        :rtype: dictionary of return status matching rest response

    *use cases*

    1. Patch the Dport configuration of the switch

"""

import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
import sys
import pyfos.utils.brcd_util as brcd_util
from pyfos.pyfos_brocade_fibrechannel_configuration import port_configuration


def _set_dport_mode(session, port_cfg_obj):
    # Set parameters
    result = port_cfg_obj.patch(session)
    return result


def _validate_dport_mode(port_cfg_obj):

    # Verify parameters
    dynamic_mode = port_cfg_obj.peek_dynamic_d_port_enabled()
    ondemad_mode = port_cfg_obj.peek_on_demand_d_port_enabled()
    if dynamic_mode is None and ondemad_mode is None:
        print("Missing required option")
        return 1

    # Success
    return 0


def set_dport_mode(session, dynamic_dport_mode, ondemand_dport_mode):
    # Set parameters
    value_dict = {'dynamic-d-port-enabled': dynamic_dport_mode,
                  'on-demand-d-port-enabled': ondemand_dport_mode}
    port_cfg_obj = port_configuration(value_dict)

    # Validate paramters
    rc = _validate_dport_mode(port_cfg_obj)
    if rc == 1:
        # Failed validation
        return None

    # Set  D-port mode
    result = _set_dport_mode(session, port_cfg_obj)
    return result


def main(argv):
    # Parse inputs
    filters = ["dynamic_d_port_enabled", "on_demand_d_port_enabled"]
    inputs = brcd_util.parse(argv, port_configuration, filters,
                             _validate_dport_mode)

    # Get object
    port_cfg_obj = inputs['utilobject']

    # Get session
    session = brcd_util.getsession(inputs)

    # Call function
    result = _set_dport_mode(session, port_cfg_obj)
    if result is None:
        print(inputs['utilusage'])
        sys.exit(1)

    # Print response
    pyfos_util.response_print(result)

    # Log out
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
