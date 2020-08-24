#!/usr/bin/env python3

# Copyright 2019 Brocade Communications Systems LLC.  All rights reserved.
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

:mod:`zoning_fabric_lock_show` - PyFOS util to show zone fabric locking \
information.
***************************************************************************************
The :mod:`zoning_fabric_lock_show` provides the user a way to display
zone fabric locking information.

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.

* outputs:
    * Python dictionary content with RESTCONF response data

"""

import sys
from pyfos import pyfos_auth
import pyfos.pyfos_brocade_zone as pyfos_zone
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def usage():
    print("")


def main(argv):

    valid_options = []
    inputs = brcd_util.generic_input(argv, usage, valid_options)

    session = brcd_util.getsession(inputs)
    fabric_lock = pyfos_zone.fabric_lock.get(session)
    pyfos_util.response_print(fabric_lock)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
