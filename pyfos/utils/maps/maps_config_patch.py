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

:mod:`maps_config_patch` - PyFOS util for MAPS configuration.
*******************************************************************

This script is used to configure MAPS such as email addresses and
relay configuration.
Note: For updating maps-config class, any one attribute in the
Util Script Options is mandatory.

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
    --actions-action       Sets one or more global actions (separated by ";").
    --decommission-cfg     Sets the decommision behavior.
    --recipient-address    Sets one or more email addresses in the "to" list.
    --sender-address       Sets the sender email address.
    --domain-name          Sets the domain name.
    --relay-ip-address     Sets the relay configuration.
    --test-email-subject   Sets the test email subject.
    --test-email-body      Sets the test email body.
    --quiet-time           Sets the global quiet time.
    --f-port-fpi-profile   Sets the F-Port FPI profile.
    --e-port-fpi-profile   Sets the E-Port FPI profile.

* Output:
    * A success response or a dictionary in case of error.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_maps import maps_config
from pyfos.utils import brcd_util


def main(argv):

    filters = ["actions_action", "decommission_cfg", "sender_address",
               "recipient_address_list_recipient_address", "domain_name",
               "relay_ip_address", "test_email_subject",
               "test_email_body", "quiet_time",
               "f_port_fpi_profile", "e_port_fpi_profile"]

    inputs = brcd_util.parse(argv, maps_config, filters)

    maps_config_obj = inputs['utilobject']

    # Login to switch
    session = brcd_util.getsession(inputs)

    result = maps_config_obj.patch(session)
    pyfos_util.response_print(result)

    # Log out
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
