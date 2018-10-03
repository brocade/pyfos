#!/usr/bin/env python3

# Copyright 2017 Brocade Communications Systems LLC.  All rights reserved.
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

:mod:`port_trunk_area_show` - PyFOS util for getting info \
        of a portareatrunk-group.
***********************************************************************************
The :mod:`port_trunk_area_show` - PyFOS util for getting info \
        of a portareatrunk-group.

This module is a standalone script that can be used to get the info of \
        porttrunkarea-group using group
* Infrastructure options:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * -n=<port name>: <slot>/<port> name of the port
    * -u=<user name>: string name to be assigned to switch
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.

* Util scripts options:
    -n,--name=NAME                     Port in slot/port.
    --group=VALUE                group of the porttrunkarea-group

* outputs:
    * Python dictionary content with RESTCONF response data

"""

import pyfos.pyfos_auth as pyfos_auth
from pyfos.pyfos_brocade_fibrechannel_trunk import trunk
import pyfos.pyfos_util as pyfos_util
import sys
import pyfos.utils.brcd_util as brcd_util


def usage():
    print("usage:")
    print('portcfgmirrorport.py -i <ipaddr> --name <name> --enable/--disable')


def main(argv):
    filters = ["group", "source_port"]
    inputs = brcd_util.parse(argv, trunk, filters)

    fcObject = inputs['utilobject']
    if fcObject.peek_group() is None:
        print("Missing group index in inputs:")
        print(inputs['utilusage'])
        sys.exit(1)

    if fcObject.peek_source_port() is None:
        print("Missing source port in inputs:")
        print(inputs['utilusage'])
        sys.exit(1)

    session = brcd_util.getsession(inputs)
    """
    This following code also works. Its better to call object method
    than class method get() and pass the filters.
    keys = [fcObject.peek_group(), fcObject.peek_source_port()]
    result = fcObject.get(session, keys)
    """
    result = fcObject.getInstances(session)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
