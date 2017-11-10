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

:mod:`switch_config_apply` - PyFOS util for specific config op use case.
***********************************************************************************
The :mod:`switch_config_apply` provides for specific config op use case.

This module is a standalone script that can be used to apply saved
configuration files to the switch. Any drift will be reset to the
saved value.

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
    * List of attributes that changed.

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
    print('switch_config_apply.py -i <ipaddr> -c <path>')


def apply_to_object_help(
        session, pyfos_class, pyfos_object, old_object_in_dict, diffs):
    patch_object = pyfos_class()
    # find if any keys and populate with the current values
    object_keys = []
    for key in pyfos_object.namekeys():
        if pyfos_object.is_key_attrib(key):
            object_keys.append(key)
    base_id = old_object_in_dict[pyfos_object.getcontainer()]
    for key in object_keys:
        # print(object.getattribute(key).getuservalue())
        patch_object.getattribute(key).setuservalue(
            pyfos_object.getattribute(key).getuservalue())
        base_id = base_id[key]
        # print(base_id)
        # print(patch_object.getattribute(key).getuservalue())

    changed = False
    for key, value in diffs.items():
        for key, value in diffs[pyfos_object.getcontainer()].items():
            if pyfos_object.getattribute(key).getisconfig():
                patch_object.getattribute(key).setvalue(
                    old_object_in_dict[pyfos_object.getcontainer()][key])
                # print(patch_object.getattribute(key).getuservalue())
                print("\t", base_id, key, "reverted from", value, "to",
                      patch_object.getattribute(key).getuservalue())
                changed = True
            else:
                print("\t", base_id, "read-only", key, "remains at", value)

    if changed:
        result = patch_object.patch(session)
        print(pyfos_class.__name__, "patch result:", result)


def apply_to_object(session, dir_name, pyfos_class):
    pyfos_object = pyfos_class.get(session)
    current_object_in_dict = json.loads(
            json.dumps(
                pyfos_object, cls=pyfos_util.json_encoder,
                sort_keys=True, indent=4))
    fp = open(dir_name + "/" + pyfos_class.__name__, 'r')
    old_object_in_dict = json.load(fp)
    fp.close()
    diffs = jsondiff.diff(old_object_in_dict, current_object_in_dict)
    if len(diffs) == 0:
        print(pyfos_class.__name__ + " has not drifted")
    else:
        print(pyfos_class.__name__ + " diff(s) are:")
        apply_to_object_help(
                session, pyfos_class, pyfos_object, old_object_in_dict, diffs)


def apply_to_object_list(session, dir_name, pyfos_class):
    pyfos_object = pyfos_class.get(session)
    current_object_in_dict = json.loads(
            json.dumps(
                pyfos_object, cls=pyfos_util.json_encoder,
                sort_keys=True, indent=4))
    fp = open(dir_name + "/" + pyfos_class.__name__, 'r')
    old_object_in_dict = json.load(fp)
    fp.close()
    diffs = jsondiff.diff(old_object_in_dict, current_object_in_dict)
    if len(diffs) == 0:
        print(pyfos_class.__name__ + " has not drifted")
    else:
        print(pyfos_class.__name__ + " diff(s) are:")
        for key, value in diffs.items():
            apply_to_object_help(
                    session, pyfos_class, pyfos_object[key],
                    old_object_in_dict[key], value)


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

    apply_to_object(session, dir_name, pyfos_switch.fibrechannel_switch)
    apply_to_object_list(session, dir_name, pyfos_switchfcport.fibrechannel)
    apply_to_object(session, dir_name, pyfos_zone.defined_configuration)
    apply_to_object(session, dir_name, pyfos_zone.effective_configuration)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
