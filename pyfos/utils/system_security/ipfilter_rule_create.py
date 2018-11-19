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

:mod:`ipfilter_rule_create` - PyFOS util to create ipfilter rule
*******************************************************************************
The :mod:`ipfilter_rule_create` supports 'ipfilter' CLI use case.

This module is a standalone script and API that can be used to create a
ipfilter rule

* inputs:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     IP address of FOS switch.
|   -L,--login=LOGIN       login name.
|   -P,--password=PASSWORD password.
|   -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
|   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           verbose mode[OPTIONAL].

* Util scripts options:
    --policy-name                            set ipfilter policy name
    --index                                  set ipfilter rule index
    --source-ip                              set source ip address
    --destination-start-port                 set destination start port number
    --protocol                               set protocol type
    --permission                             set permission type


* outputs:
    * success response or dictionary in case of error.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_security import ipfilter_rule
from pyfos.utils import brcd_util


def main(argv):
    filters = ["policy_name", "index",
               "source_ip", "destination_start_port",
               "protocol", "permission"]
    inputs = brcd_util.parse(argv, ipfilter_rule, filters)

    ipfilter_obj = inputs['utilobject']
    if (ipfilter_obj.peek_policy_name() is None or
            ipfilter_obj.peek_index() is None or
            ipfilter_obj.peek_source_ip() is None or
            ipfilter_obj.peek_destination_start_port() is None or
            ipfilter_obj.peek_protocol() is None or
            ipfilter_obj.peek_permission() is None):
        print("Missing command line options")
        print(inputs['utilusage'])
        exit(1)

    # Login to switch
    session = brcd_util.getsession(inputs)

    result = ipfilter_obj.post(session)
    pyfos_util.response_print(result)

    # Log out
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
