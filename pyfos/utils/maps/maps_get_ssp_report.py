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
:mod:`maps_get_ssp_report` - PyFOS util to display the MAPS Switch \
Status Policy report.
*****************************************************************************************

This script displays the MAPS Switch Status Policy report.

* Input:

* Infrastructure Options:

    * -i,--ipaddr=IPADDR     The IP address of the FOS switch.
    * -L,--login=LOGIN       The login name.
    * -P,--password=PASSWORD The password.
    * -f,--vfid=VFID         The VFID to which the request is \
                             directed [OPTIONAL].
    * -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
    * -v,--verbose           Verbose mode [OPTIONAL].

* Util Script Options:

* Output:
    The MAPS Switch Status Policy report.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_maps import switch_status_policy_report
from pyfos.utils import brcd_util


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
