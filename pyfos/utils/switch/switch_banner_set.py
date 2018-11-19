#!/usr/bin/env python3

# Copyright © 2018 Broadcom.  All rights reserved. The term "Broadcom"
# refers to Broadcom Inc. and/or its subsidiaries.
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

:mod:`switch_banner_set` - PyFOS util for specific switch op use case.
***********************************************************************************
The :mod:`switch_banner_set` provides for a specific switch op use case.

This module is a stand-alone script that can be used to set a banner string.

* Inputs:
    * -L=<login>: Login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: IP address.
    * --banner=<banner message>: banner message to be assigned to a switch.
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
       a  VFID of 128 is assumed.

* Outputs:
    * Python dictionary content with RESTCONF response data.

"""

import sys
from pyfos import pyfos_auth
import pyfos.pyfos_brocade_fibrechannel_switch as pyfos_switch
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def usage():
    print("  Script specific options:")
    print("")
    print("    --banner=MESSAGE              banner string")
    print("")


def main(argv):
    valid_options = ["banner"]
    inputs = brcd_util.generic_input(argv, usage, valid_options)

    session = pyfos_auth.login(inputs["login"], inputs["password"],
                               inputs["ipaddr"], inputs["secured"],
                               verbose=inputs["verbose"])
    if pyfos_auth.is_failed_login(session):
        print("login failed because",
              session.get(pyfos_auth.CREDENTIAL_KEY)
              [pyfos_auth.LOGIN_ERROR_KEY])
        usage()
        sys.exit()

    brcd_util.exit_register(session)

    vfid = None
    if 'vfid' in inputs:
        vfid = inputs['vfid']

    if vfid is not None:
        pyfos_auth.vfid_set(session, vfid)

    if "banner" not in inputs:
        usage()
        sys.exit()
    banner = inputs["banner"]

    current_switch = pyfos_switch.fibrechannel_switch.get(session)

    switch = pyfos_switch.fibrechannel_switch()
    name = current_switch.peek_name()
    switch.set_name(name)
    switch.set_banner(banner)
    result = switch.patch(session)
    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
