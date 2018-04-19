#!/usr/bin/env python3

# Copyright © 2018 Broadcom. All rights reserved. The term "Broadcom"
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

:mod:`switch_config_apply` - PyFOS util for specific config op use case.
***********************************************************************************
The :mod:`switch_config_apply` provides for a specific config op use case.

This module is a stand-alone script that can be used to apply saved
configuration files to the switch. Any drift will be reset to the
saved value.

* Inputs:
    * -L=<login>: Login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: IP address.
    * --compare=<compare directory>: name of the directory that contains
        the JSON encoded switch configuration files.
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        a VFID of 128 is assumed.

* Outputs:
    * A List of attributes that changed.

"""

import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_brocade_zone as pyfos_zone
import pyfos.pyfos_brocade_fibrechannel_switch as pyfos_switch
import pyfos.pyfos_brocade_fibrechannel as pyfos_switchfcport
import sys
import pyfos.utils.brcd_util as brcd_util
import switch_config_util
import pyfos.utils.zoning.zoning_cfg_save as cfgsave


def usage():
    print("  Script specific options:")
    print("")
    print("    --compare=PATH               directory name")
    print("")


def main(argv):
    valid_options = ["compare", "template", "reffcport"]
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

    if 'compare' not in inputs or inputs['compare'] is None:
        usage()
        sys.exit()

    dir_name = inputs['compare']

    template = None
    if 'template' in inputs:
        template = switch_config_util.get_template(inputs['template'])

    switch_config_util.process_object(
            session, dir_name, pyfos_switch.fibrechannel_switch,
            False, template)
    if 'template' in inputs and 'reffcport' in inputs:
        switch_config_util.process_object(
                session, dir_name, pyfos_switchfcport.fibrechannel,
                False, template,
                [{"name": inputs['reffcport']}])
    else:
        switch_config_util.process_object(
                session, dir_name, pyfos_switchfcport.fibrechannel,
                False, template)
    switch_config_util.process_object(
            session, dir_name, pyfos_zone.defined_configuration,
            False, template)
    current_effective = pyfos_zone.effective_configuration.get(session)
    cfgsave.cfgsave(session, current_effective.peek_checksum())

    switch_config_util.process_object(
            session, dir_name, pyfos_zone.effective_configuration,
            False, template)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
