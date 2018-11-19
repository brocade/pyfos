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

:mod:`configure_dport_mode_modify` - PyFOS util to set the D_Port mode of the \
switch.
**************************************************************************************
The :mod:`configure_dport_mode_modify` util sets the D_Port mode of the switch.

This module is a stand-alone script that can be used to set the D_Port mode
of the switch.

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [OPTIONAL].
    * -v,--verbose: Verbose mode [OPTIONAL].

* Util Script Options:
    * --dynamic-d-port-enabled=DYNAMIC-D-PORT-ENABLED: Sets the given dynamic\
 D_Port mode.
    * --on-demand-d-port-enabled=ON-DEMAND-D-PORT-ENABLED: Sets the on-demand\
            D_Port mode.

* Output:
    * Python dictionary content with RESTCONF response data.

..function:: set_dport_mode(session, dynamic_dport_mode,
                                ondemand_dport_mode)

    Example Usage of the Method::

        ret = configure_dport_mode_modify.set_dport_mode(session,
                dynamic_dport_mode, ondemand_dport_mode)
        print (ret)

    Details::

        result = configure_dport_mode_modify.set_dport_mode(session,
                dynamic_dport_mode, ondemand_dport_mode)

    * Input:
        :param session: The session returned by login.
        :param dynamic_dport_mode: Sets the dynamic D_Port mode.
        :param ondemand_dport_mode: Sets the on-demand D_Port mode.

    * Output:
        :rtype: A dictionary of return status matching the REST response.

    *Use Cases*

    1. Patch the D_Port configuration of the switch.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
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
