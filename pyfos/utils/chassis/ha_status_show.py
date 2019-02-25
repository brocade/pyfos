#!/usr/bin/env python3
#
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

:mod:`ha_status_show` - PyFOS util to display the HA status of the switch.
***********************************************************************************
The :mod:`ha_status_show` displays the HA status of the switch.

This module is a stand-alone script that can be used to display the HA status \
of the switch.


| Infrastructure Options:

    * -L=<login>: The login ID. If not provided, an interactive
        prompt will request one.
    * -P=<password>: The password. If not provided, an interactive
        prompt will request one.
    * -i=<IP address>: The IP address.
    * -n=<port name>: The <slot>/<port> name of the port.
    * -u=<user name>: The string name to be assigned to the switch.
    * -f=<VFID>: The VFID or -1 if VF is disabled. If unspecified,
        a VFID of 128 is assumed.

* Output:
    * Python dictionary content with RESTCONF response data.

"""
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_chassis import ha_status
from pyfos.utils import brcd_util


def show_ha_status(session):
    ha_status_obj = ha_status()
    result = ha_status_obj.get(session)
    return result


def main(argv):

    filters = []
    inputs = brcd_util.parse(argv, ha_status, filters)

    session = brcd_util.getsession(inputs)

    result = show_ha_status(inputs['session'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
