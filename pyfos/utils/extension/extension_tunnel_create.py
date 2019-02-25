#!/usr/bin/env python3

# Copyright © 2018 Broadcom. All Rights Reserved. The term “Broadcom” refers to
# Broadcom Inc. and/or its subsidiaries.
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

:mod:`extension_tunnel_create` - PyFOS util for creating a tunnel.
********************************************************************************
The :mod:`extension_tunnel_create` util provides tunnel creation functionality.

This module is a stand-alone script that can be used to create an extension
tunnel.

extension_tunnel_create.py: Usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * -n,--name=NAME: Sets the name.
    * -l,--load-level=VALUE: Sets the load level.
    * -f,--fast-write-enabled=VALUE: Enables or disables FastWrite.
    * -c,--compression-tunnel=VALUE: Sets the compression tunnel.
    * -a,--admin-enabled=VALUE: Enables or disables the admin status.
    *    --ipsec-policy=VALUE: Sets the IPsec policy.
    *    --user-friendly-name=VALUE: Sets the user friendly name.
    *    --fc-compression=VALUE: Sets the FC compression.
    *    --ip-compression=VALUE: Sets the IP compression.
    *    --ip-extension=VALUE: Sets the IP extension.

* Output:
    * Python dictionary content with RESTCONF response data.

.. function:: extension_tunnel_create.create_extension_tunnel(session, name)

    *Create an Extension Tunnel*

        Example Usage of the Method::

                ret = extension_tunnel_create.create_extension_tunnel(session,
                name)
                print (ret)

        Details::

            tunnel = {
                            "name": name,
                      }
            result = extension_tunnel_create._create_extension_tunnel(session,
            tunnel)

        * Input:
            :param session: The session returned by the login.
            :param name: Sets the VE_Port name expressed as slot/port.

        * Output:
            :rtype: A dictionary of return statuses matching the REST response.

        *Use Cases*

         Create a new extension tunnel.
"""


import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_extension_tunnel import extension_tunnel
from pyfos.utils import brcd_util

isHttps = "0"


def _create_extension_tunnel(session, tnlobject):
    result = tnlobject.post(session)
    return result


def create_extension_tunnel(session, name):
    value_dict = {'name': name}
    tnlobject = extension_tunnel(value_dict)
    result = _create_extension_tunnel(session, tnlobject)
    return result


def validate(tnlobject):
    if tnlobject.peek_name() is None:
        return 1
    return 0


def main(argv):
    # myinput=str("-i 10.17.3.70  --name 4/19")
    # argv = myinput.split()
    filters = ['name', 'user_friendly_name', 'ipsec_policy', 'load_level',
               'ip_extension', 'fast_write_enabled', 'compression_tunnel',
               'compression_protocol_ip_compression',
               'compression_protocol_fc_compression', 'admin_enabled']
    inputs = brcd_util.parse(argv, extension_tunnel, filters, validate)
    tnlobject = inputs['utilobject']
    session = brcd_util.getsession(inputs)
    result = _create_extension_tunnel(session, tnlobject)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
