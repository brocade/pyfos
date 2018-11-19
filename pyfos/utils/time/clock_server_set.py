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

:mod:`clock_server_set` - PyFOS util to set one or more external NTP servers.
*******************************************************************************
The :mod:`clock_server_set` supports 'tsclockserver' CLI use case.

This module is a standalone script and API that can be used to set NTP servers.

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

* Util scripts options:
    --ntp_server_address                      Specifing NTP address(es)/LOCL.
                                                e.g:"10.70.12.111;10.70.12.115"

* outputs:
    * success response or dictionary in case of error

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_time import clock_server
from pyfos.utils import brcd_util


def main(argv):
    filters = ["ntp_server_address_server_address"]
    inputs = brcd_util.parse(argv, clock_server, filters)

    ts_obj = inputs['utilobject']
    if ts_obj.peek_ntp_server_address_server_address() == "[]":
        print("Missing command line options")
        print(inputs['utilusage'])
        exit(1)

    # Login to switch
    session = brcd_util.getsession(inputs)
    result = ts_obj.patch(session)
    pyfos_util.response_print(result)

    # Log out
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
