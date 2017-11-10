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

:mod:`switch_config_dump` - PyFOS util for specific config op use case.
***********************************************************************************
The :mod:`switch_config_dump` provides for specific config op use case.

This module is a standalone script that can be used to dump
JSON encoded switch configuration files into a timestamped
directory. The resulting directory can be used to monitor drift
or apply to switch.

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.

* outputs:
    * None

"""

import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_zone as pyfos_zone
import pyfos.pyfos_switch as pyfos_switch
import pyfos.pyfos_switchfcport as pyfos_switchfcport
import pyfos.pyfos_fabric as pyfos_fabric
import pyfos.pyfos_util as pyfos_util
import sys
import pyfos.utils.brcd_util as brcd_util
import json
import os
import time


def usage():
    print("usage:")
    print('switch_config_dump.py -i <ipaddr>')


def dump_object(session, dir_name, pyfos_class):
    object = pyfos_class.get(session)
    fp = open(dir_name + "/" + pyfos_class.__name__, 'w')
    fp.write(
            json.dumps(
                object, cls=pyfos_util.json_encoder, sort_keys=True, indent=4))
    fp.close()


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

    dir_name = ("FOS_" + inputs["ipaddr"] + "_" +
                time.strftime("%Y_%m_%d_%H:%M:%S"))
    try:
        os.stat(dir_name)
    except:
        os.mkdir(dir_name)

    dump_object(session, dir_name, pyfos_switch.fibrechannel_switch)
    dump_object(session, dir_name, pyfos_switchfcport.fibrechannel)
    dump_object(session, dir_name, pyfos_fabric.fabric_switch)
    dump_object(session, dir_name, pyfos_zone.defined_configuration)
    dump_object(session, dir_name, pyfos_zone.effective_configuration)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
