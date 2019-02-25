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

:mod:`time_zone_set` - PyFOS util to set the time zone.
*******************************************************************************
The :mod:`time_zone_set` util sets the time zone.

This module is a stand-alone script and API that can be used to set the time \
zone by the time zone name and the off-set value.

* Input:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     The IP address of the FOS switch.
|   -L,--login=LOGIN       The login name.
|   -P,--password=PASSWORD The password.
|   -f,--vfid=VFID         The VFID to which the request is \
                            directed [OPTIONAL].
|   -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           Verbose mode [OPTIONAL].

* Util Script Options:
    --gmt_offset_hours     Sets the GMT hours offset value.
    --gmt_offset_minutes   Sets the GMT minutes offset value.

* Output:
    * Displays the system time zone details.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_time import time_zone
from pyfos.utils import brcd_util


def main(argv):
    filters = ["gmt_offset_hours", "gmt_offset_minutes"]
    inputs = brcd_util.parse(argv, time_zone, filters)

    tz_obj = inputs['utilobject']
    if tz_obj.peek_gmt_offset_hours() is None:
        print("Missing command line options")
        print(inputs['utilusage'])
        exit(1)

    # Login to switch
    session = brcd_util.getsession(inputs)

    result = tz_obj.patch(session)
    pyfos_util.response_print(result)

    # Log out
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
