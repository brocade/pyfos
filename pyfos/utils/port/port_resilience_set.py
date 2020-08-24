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

:mod:`port_resilience_set` - PyFOS util for specific port op use case.
***********************************************************************************
The :mod:`port_resilience_set` provides for specific port op use case.

This module is a standalone script that can be used to set/reset/show
resilience state of a port.

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.
    * --enable/--disable

* Util scripts options:
    --name=NAME                               Port in slot/port.

* outputs:
    * Enables the Credit Recovery and Forward Error Correction features on the
    * given port. These features help in increasing the resilience of the port
    * by adding suto corrections or recovery of lost frames on the fibre link.

"""

import sys
import time
from pyfos import pyfos_auth
import pyfos.pyfos_brocade_interface as pyfos_switchfcport
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def usage():
    print("  Util scripts options:\n")
    print("    --name=NAME			 port in slot/port")
    print("    --enable/--disable		 To enable/Disable")

#
#    This function would enable or disable the CR and FEC state
#    of the given port to given value
#


def changeResilienceStateOfPort(session, name, enabled):
    port = pyfos_switchfcport.fibrechannel()
    port.set_name(name)
    port.set_credit_recovery_enabled(enabled)
    port.set_fec_enabled(enabled)
    result = port.patch(session)
    pyfos_util.response_print(result)
    #   Wait for few secs to allow the new value to be negotiated
    time.sleep(3)
    newport = pyfos_switchfcport.fibrechannel.get(session, name)
    return newport


def main(argv):
    valid_options = ["name", "enable", "disable", "show"]
    inputs = brcd_util.generic_input(argv, usage, valid_options)

    session = pyfos_auth.login(inputs["login"], inputs["password"],
                               inputs["ipaddr"], inputs["secured"],
                               verbose=inputs["verbose"])

    if pyfos_auth.is_failed_login(session):
        print("login failed because",
              session.get(pyfos_auth.CREDENTIAL_KEY)
              [pyfos_auth.LOGIN_ERROR_KEY])
        brcd_util.full_usage(usage, valid_options)
        sys.exit()

    brcd_util.exit_register(session)

    vfid = None
    if 'vfid' in inputs:
        vfid = inputs['vfid']

    if vfid is not None:
        pyfos_auth.vfid_set(session, vfid)

    if "name" not in inputs:
        pyfos_auth.logout(session)
        brcd_util.full_usage(usage, valid_options)
        sys.exit()
    name = inputs["name"]

    config = 0

    if "enable" not in inputs and "disable" not in inputs:
        pyfos_auth.logout(session)
        brcd_util.full_usage(usage, valid_options)
        sys.exit()
    if "enable" in inputs and "disable" in inputs:
        pyfos_auth.logout(session)
        brcd_util.full_usage(usage, valid_options)
        sys.exit()
    if "enable" in inputs:
        config = 1
    if "disable" in inputs:
        config = 2

    validport = pyfos_switchfcport.fibrechannel.get(session, name)
    if pyfos_util.is_failed_resp(validport):
        pyfos_util.response_print(validport)
        pyfos_auth.logout(session)
        sys.exit()

    if config in (1, 2):
        if config == 1:
            print("Trying to enable resilience on port ", name)
            newport = changeResilienceStateOfPort(session, name, 1)
        elif config == 2:
            print("Trying to disable the resilience on port ", name)
            newport = changeResilienceStateOfPort(session, name, 0)
    else:
        newport = pyfos_switchfcport.fibrechannel.get(session, name)
        if pyfos_util.is_failed_resp(newport):
            pyfos_util.test_explicit_result_failed(newport)
            sys.exit()

    cr_enabled = newport.peek_credit_recovery_enabled()
    cr_active = newport.peek_credit_recovery_active()

    if ((cr_active == 1) and (cr_enabled == 1)):
        print("Credit Recovery is enabled and active on port ", name)
    elif ((cr_active == 0) and (cr_enabled == 1)):
        print("Credit Recovery is enabled, but not active on port ", name)
    elif cr_enabled == 0:
        print("Credit Recovery is disabled on port ", name)

    fec_enabled = newport.peek_fec_enabled()
    fec_active = newport.peek_fec_active()

    if ((fec_active == 1) and (fec_enabled == 1)):
        print("Forward Error Correction is enabled and active on port ", name)
    elif ((fec_active == 0) and (fec_enabled == 1)):
        print("Forward Error Correction is enabled but \
                                    not active on port ", name)
    elif fec_enabled == 0:
        print("Forward Error Correction is disabled on port ", name)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
