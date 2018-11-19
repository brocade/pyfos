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

:mod:`logical_switch_show` - PyFOS util to display Logical switch configuration
********************************************************************************
The :mod:`logical_switch_show` displays Logical switch configuration.

This module is a standalone script and API that can be used to display
logical switch configuration with specified VFID. If no VFID is given,
configuration of all logical switches are displayed.
logical switch configuration with specified Fabric ID. If no Fabric ID is
given, configuration of all logical switches are displayed.

* inputs:

| Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch.
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID of LS context to which the request is \
                           directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

| Util scripts options:

  | --fabric-id=FABRIC-ID  Fabric ID of logical switch this action is targeting

* outputs:
    * Logical switch information of specified Fabric ID. When Fabric ID is
      not provided, all existing logical switches will be displayed.

.. function:: logical_switch_show.show_logical_switch(session, fid)

    * Display the logical-switches configured.

        Example usage of the method::

            # Example 1: Display all the logical-switches
            ret = logical_switch_show.show_logical_switch(session, None)
            print (ret)

            # Example 2: Display a specific logical-switch 1
            ret = logical_switch_show.show_logical_switch(session, 1)
            print (ret)

        Details::

            lswitch_obj = fibrechannel_logical_switch()
            if fid is None: # All logical-switches
                result = lswitch_obj.get(session, None)
            else:
                result = lswitch_obj.get(session, fid)

        * inputs:
            :param session: session returned by login.
            :param fid: Specific fabric ID or None for all fabrics.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Retrieve the VF logical-switch information.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_fibrechannel_logical_switch \
    import fibrechannel_logical_switch


def show_logical_switch(session, vfid):
    ls_object = fibrechannel_logical_switch()
    if vfid is None:
        result = ls_object.get(session, None)
    else:
        result = ls_object.get(session, vfid)
    return result


def main(argv):
    filters = ['fabric_id']
    inputs = brcd_util.parse(argv, fibrechannel_logical_switch, filters)
    session = brcd_util.getsession(inputs)

    vfid = None
    ls_obj = inputs['utilobject']
    vfid = ls_obj.peek_fabric_id()

    result = show_logical_switch(session, vfid)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
