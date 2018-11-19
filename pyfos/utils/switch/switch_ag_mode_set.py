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

:mod:`switch_ag_mode_set` - PyFOS util to enable or disable AG mode
*******************************************************************************
The :mod:`switch_ag_mode_set` provides option to enable and disable
the AG mode.

This module can be used to enable and disable the Access Gateway(AG) mode.
The switch must be in disabled state before enabling or disabling AG mode.

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

| Util scripts options:

|      --ag-mode=VALUE     set ag-mode (enable = 3, disable = 1)

* outputs:
    * Status of the AG enable/disable operation.

.. function:: switch_ag_mode_set.set_ag_mode(session, ag_mode)

    * Enable/Disable the Access Gateway(AG) mode.

        Example usage of the method::

            ret = switch_ag_mode_set.set_ag_mode(session, ag_mode)
            print (ret)

        Details::

            sw_obj = fibrechannel_switch()
            current_sw = fibrechannel_switch.get(session)

            sw_obj.set_name(current_sw.peek_name())
            sw_obj.set_ag_mode(ag_mode)
            return sw_obj.patch(session)

        * inputs:
            :param session: session returned by login.
            :param ag_mode: AG mode value (Enable = 3, Disable = 1)

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Enable AG mode
        2. Disable AG mode
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_fibrechannel_switch import fibrechannel_switch
from pyfos.utils import brcd_util


def set_ag_mode(session, ag_mode):
    sw_obj = fibrechannel_switch()
    current_sw = fibrechannel_switch.get(session)
    if pyfos_util.is_failed_resp(current_sw):
        return current_sw

    sw_obj.set_name(current_sw.peek_name())
    sw_obj.set_ag_mode(ag_mode)
    # print(settings_obj)
    return sw_obj.patch(session)


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['ag_mode']
    inputs = brcd_util.parse(argv, fibrechannel_switch, filters)

    sw_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    if sw_obj.peek_ag_mode() is None:
        print("Missing input(s)")
        sys.exit()

    # pyfos_util.response_print(inputs['utilobject'].displaycustomcli())
    result = set_ag_mode(inputs['session'],
                         sw_obj.peek_ag_mode())
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
