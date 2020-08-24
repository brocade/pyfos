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

:mod:`maps_fpi_profile_patch` - PyFOS util to update FPI profile.
*******************************************************************************

This script is used to update a FPI profile.

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

    --name                                              Specifies FPI\
                                                        profile name.
    --performance-impact-transmit-queue-latency         TXQL latency\
                                                        in msec
    --performance-impact-credit-zero-percentage-1-sec   credit-zero\
                        buffer stats threshold percentage in 1-second
    --performance-impact-credit-zero-percentage-5-sec   credit-zero\
                        buffer stats threshold percentage in 5-second
    --performance-impact-credit-zero-percentage-10-sec  credit-zero\
                        buffer stats threshold percentage in 10-second
    --frame-loss-transmit-queue-latency                 frame loss FPI\
                        state is due to frame transmit timeout or TXQL

* Output:

    * A success response or a dictionary in case of error.

"""


import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_maps import fpi_profile
from pyfos.utils import brcd_util


def main(argv):

    filters = ["name", "performance_impact_transmit_queue_latency",
               "performance_impact_credit_zero_percentage_1_sec",
               "performance_impact_credit_zero_percentage_5_sec",
               "performance_impact_credit_zero_percentage_10_sec",
               "frame_loss_transmit_queue_latency"]

    inputs = brcd_util.parse(argv, fpi_profile, filters)

    maps_obj = inputs['utilobject']
    if maps_obj.peek_name() is None:
        print("Missing command line options")
        print(inputs['utilusage'])
        exit(1)

    # Login to switch
    session = brcd_util.getsession(inputs)

    result = maps_obj.patch(session)
    pyfos_util.response_print(result)

    # Log out
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
