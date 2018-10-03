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

:mod:`time_zone_show` - PyFOS util to set and show time zone information.
*******************************************************************************
The :mod:`time_zone_show` supports 'tstimezone' CLI use case.

This module is a standalone script and API that can be used to display
and set time zone by both time zone name and off-set value.

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

* outputs:
    * display system time zone details.

"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_time import time_zone
import pyfos.utils.brcd_util as brcd_util


def main(argv):
    filters = []
    inputs = brcd_util.parse(argv, time_zone, filters)

    # Login to switch
    session = brcd_util.getsession(inputs)

    # Print Time Zone attributes
    ts_attributes = time_zone.get(inputs['session'])
    pyfos_util.response_print(ts_attributes)

    # Log out
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
