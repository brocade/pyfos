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

:mod:`maps_config_patch` - PyFOS util for maps config
*******************************************************************

This script is used to configure MAPS config like email addresses,
relay config etc...
Note: For updating maps-config class any one attribute is mandatory

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

* Util scripts options:
    --action               global actions list (separated by ";")
    --decommission-cfg     decommision behaviour
    --recipient-address    list of to email addresses
    --sender-address       sender email address
    --domain-name          domain name
    --relay-ip-address     relay configuration
    --test-email-subject   test email subject
    --test-email-body      test email body

* outputs:
    * success response or dictionary in case of error.

"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_maps import maps_config
import pyfos.utils.brcd_util as brcd_util


def main(argv):

    filters = ["actions_action", "decommission_cfg", "sender_address",
               "recipient_address_list_recipient_address", "domain_name",
               "relay_ip_address", "test_email_subject",
               "test_email_body"]

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
