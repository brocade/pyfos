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

:mod:`monitoring_system_matrix` - PyFOS util to list all MS in MAPS
************************************************************************

This script is used to display MAPS monitoring systems and its supported
values.

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

* Util scripts options:

* outputs:
    * displays all monitoring systems present in MAPS

"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_maps import monitoring_system_matrix
import pyfos.utils.brcd_util as brcd_util


def main(argv):
    filters = []
    inputs = brcd_util.parse(argv, monitoring_system_matrix, filters)

    # Login to switch
    session = brcd_util.getsession(inputs)

    # Print Radius Server attributes
    ms_output = monitoring_system_matrix.get(inputs['session'])
    pyfos_util.response_print(ms_output)

    # Logout from switch
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
