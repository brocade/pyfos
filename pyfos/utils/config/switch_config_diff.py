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

:mod:`switch_config_diff` - PyFOS util for specific config op use case.
***********************************************************************************
The :mod:`switch_config_diff` provides for a specific config op use case.

This module is a stand-alone script that can be used to display
drifted attributes between the current switch configuration and a previously
saved configuration files.

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
    * --compare=<compare directory>: Name of the directory that contains
       the  JSON encoded switch configuration files.

* Outputs:
    * List of attributes that have drifted.

"""

import sys
import switch_config_util
import switch_config_obj
from pyfos import pyfos_auth
import pyfos.pyfos_brocade_fibrechannel as pyfos_switchfcport
from pyfos.utils import brcd_util
from pyfos.manager.pyfos_config_manager import config_manager


def usage():
    print("  Script specific options:")
    print("")
    print("    --compare=PATH               directory name")
    print("")


def process_diff(session, envelope_name, in_json, template, inputs, vf):
    if vf == 128:
        print("processing diff for default switch or non-vf")
    else:
        print("processing diff for VFID", vf)

    pyfos_auth.vfid_set(session, vf)
    if vf == 128:
        vf_based_name = envelope_name
    else:
        vf_based_name = envelope_name + "." + str(vf)

    for obj in switch_config_obj.objects_to_process:
        if obj["obj_name"] == pyfos_switchfcport.fibrechannel and 'template' in inputs and 'reffcport' in inputs:
            switch_config_util.process_object(
                session, vf_based_name, obj, True, False, in_json, template,
                [{"name": inputs['reffcport']}])
        else:
            switch_config_util.process_object(
                session, vf_based_name, obj, True, False, in_json, template)


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
        in_json = inputs['json']

    # template = None
    # if 'template' in inputs:
    #    template = switch_config_util.get_template(inputs['template'])

    if in_json:
        fmtfile = 'JSON'
        fmtobj = 'json'
        # ext = '.json'
    else:
        fmtfile = 'XLSX'
        fmtobj = 'attributes'
        # ext = '.xlsx'
    mgr = config_manager(fmtfile, fmtobj)
    mgr.handlediff(envelope_name, session)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
