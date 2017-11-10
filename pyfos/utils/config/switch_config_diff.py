#!/usr/bin/env python3

# Copyright 2017 Brocade Communications Systems, Inc.  All rights reserved.
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
The :mod:`switch_config_diff` provides for specific config op use case.

This module is a standalone script that can be used to display
drifted attributes between the current switch configuration and
previously saved config directory.

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * -c=<compare directory>: name of the directory that contains
        JSON encoded switch configuration files
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.

* outputs:
    * List of attributes that drifted.

"""

import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_zone as pyfos_zone
import pyfos.pyfos_switch as pyfos_switch
import pyfos.pyfos_switchfcport as pyfos_switchfcport
import pyfos.pyfos_util as pyfos_util
import sys
import pyfos.utils.brcd_util as brcd_util
import json
import jsondiff


def usage():
    print("usage:")
    print('switch_config_diff.py -i <ipaddr> -c <path>')


def diff_object(session, dir_name, pyfos_class):
    object = pyfos_class.get(session)
    current_object = json.loads(
            json.dumps(
                object, cls=pyfos_util.json_encoder, sort_keys=True, indent=4))
    fp = open(dir_name + "/" + pyfos_class.__name__, 'r')
    old_object = json.load(fp)
    fp.close()
    diffs = jsondiff.diff(old_object, current_object)
    if len(diffs) == 0:
        print(pyfos_class.__name__ + " has not drifted")
    else:
        print(pyfos_class.__name__ + " diff(s) are:")
        for key, value in diffs[object.getcontainer()].items():
            print("\t", key, ":", value)


def diff_object_list(session, dir_name, pyfos_class):
    object = pyfos_class.get(session)
    current_object = json.loads(
            json.dumps(
                object, cls=pyfos_util.json_encoder, sort_keys=True, indent=4))
    fp = open(dir_name + "/" + pyfos_class.__name__, 'r')
    old_object = json.load(fp)
    fp.close()
    diffs = jsondiff.diff(old_object, current_object)
    if len(diffs) == 0:
        print(pyfos_class.__name__ + " has not drifted")
    else:
        print(pyfos_class.__name__ + " diff(s) are:")
        object_keys = []
        for key in object[0].namekeys():
            if object[0].is_key_attrib(key):
                object_keys.append(key)
        for key, value in diffs.items():
            base_id = current_object[key][object[0].getcontainer()]
            for key in object_keys:
                base_id = base_id[key]
            print("\t", base_id, "diff(s) are")
            for key1, value1 in value[object[0].getcontainer()].items():
                print("\t\t", key1, ":", value1)


def main(argv):
    isHttps = "0"

    inputs = brcd_util.generic_input(argv, usage)

    session = pyfos_auth.login(inputs["login"], inputs["password"],
                               inputs["ipaddr"], isHttps)
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

    diff_object(session, dir_name, pyfos_switch.fibrechannel_switch)
    diff_object_list(session, dir_name, pyfos_switchfcport.fibrechannel)
    diff_object(session, dir_name, pyfos_zone.defined_configuration)
    diff_object(session, dir_name, pyfos_zone.effective_configuration)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
