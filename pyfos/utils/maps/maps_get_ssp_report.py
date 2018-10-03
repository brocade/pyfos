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
:mod:`maps_get_ssp_report` - PyFOS util to display MAPS SSP report
******************************************************************

This script displays MAPS switch status policy report

* input:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

* Util scripts options:

* output:
    Displays MAPS SSP report
"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_maps import switch_status_policy_report
import pyfos.utils.brcd_util as brcd_util


def main(argv):

    filters = []
    inputs = brcd_util.parse(argv, switch_status_policy_report, filters)

    # Login to switch
    session = brcd_util.getsession(inputs)

    # SSP show
    sw_report = switch_status_policy_report.get(inputs['session'])
    pyfos_util.response_print(sw_report)

    # Logout from switch
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
