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

If :class:`pyfos_brocade_zone.defined_configuration` is changed,
:func:`cfgsave` is executed
to apply the changes to persistent database. If
:class:`pyfos_brocade_zone.effective_configuration` is changed,
appropriate :func:`cfgenable`, :func:`cfgsave` or
:func:`cfgdisable` is called.

The configuration files are saved by :mod:`switch_config_dump` script.

The configuration files can be in spreadsheet format or in JSON format.
By default, spreadsheet format is used. Name of the spreadsheet is
given without .<vfid>.xlsx file extension for --compare option. For
JSON format configuration files, --json option added to --compare
option and directory name is given instead.

* Inputs:
    * -L=<login>: Login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: IP address.
    * --compare=<compare directory>: name of the directory that
        contains the JSON encoded switch configuration files or
        name of the spreadsheet without .<vfid>.xlsx file extension.

* Outputs:
    * A List of attributes that changed.

"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_brocade_zone as pyfos_zone
import pyfos.pyfos_brocade_fibrechannel_switch as pyfos_switch
import pyfos.pyfos_brocade_fibrechannel as pyfos_switchfcport
import pyfos.utils.brcd_util as brcd_util
import pyfos.utils.zoning.zoning_cfg_save as cfgsave
import pyfos.pyfos_brocade_fibrechannel_logical_switch as fc_ls
import pyfos.pyfos_util as pyfos_util
import switch_config_util
import switch_config_obj


def usage():
    print("  Script specific options:")
    print("")
    print("    --compare=PATH               directory name")
    print("")


def process_apply(session, envelope_name, in_json, template, inputs, vf):
    if vf is 128:
        print("apply to default switch or non-vf")
    else:
        print("apply to VFID", vf)

    pyfos_auth.vfid_set(session, vf)
    if vf is 128:
        vf_based_name = envelope_name
    else:
        vf_based_name = envelope_name + "." + str(vf)

    for obj in switch_config_obj.objects_to_process:
        if obj["obj_name"] == pyfos_switchfcport.fibrechannel and 'template' in inputs and 'reffcport' in inputs:
            switch_config_util.process_object(
                session, vf_based_name, obj, True, True, in_json, template,
                [{"name": inputs['reffcport']}])
        else:
            switch_config_util.process_object(
                session, vf_based_name, obj, True, True, in_json, template)


def main(argv):
    valid_options = ["json", "compare", "template", "reffcport"]
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

    envelope_name = inputs['compare']

    in_json = False
    if 'json' in inputs:
        in_json = True

    template = None
    if 'template' in inputs:
        template = switch_config_util.get_template(inputs['template'])

    result = fc_ls.fibrechannel_logical_switch.get(session)
    if pyfos_util.is_failed_resp(result):
        process_apply(session, envelope_name, in_json, template, inputs, 128)
    else:
        for switch in result:
            process_apply(session, envelope_name, in_json, template, inputs, switch.peek_fabric_id())

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
