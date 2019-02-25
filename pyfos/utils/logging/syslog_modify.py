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
:mod:`syslog_modify` - PyFOS util to modify the syslog configuration on \
a switch.
*********************************************************************************
The :mod:`syslog_modify` util provides option to modify the syslog \
configuration parameters on a switch.

This module is a stand-alone script that can be used to modify the syslog
configuration on a switch.

* Input:

| Infrastructure Options:

  | -i,--ipaddr=IPADDR     The IP address of the FOS switch.
  | -L,--login=LOGIN       The login name.
  | -P,--password=PASSWORD The password.
  | -f,--vfid=VFID         The VFID to which the request is \
                            directed [OPTIONAL].
  | -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           Verbose mode [OPTIONAL].

| Util Script Options:

  | --server=The IP address of the server.
  | --port=The port number.
  | --secure-mode=True or false.

* Output:

  * Python dictionary content with RESTCONF response data.

.. function:: modify_syslog_server(session, facility):

        Example Usage of the Method::

            ret = syslog_modify.modify_syslog_server(session, server, port,
                                                     secure_mode)
            print (ret)

        Details::

            val = {
                    "server": server ip address,
                    "port": port number,
                    "secure-mode": true/false
                  }
            syslog_obj = syslog_server()
            syslog_obj.set_server(server)
            syslog_obj.set_secure_mode(secure_mode)
            syslog_obj.set_port(port)

            result = _modify_syslog_server(session, syslog_obj)

        * Input:
                :param session: The session returned by the login.
                :param server: The server IP address.
                :param port: The port number.
                :param secure-mode: True or false.

        * Output:
                :rtype: A dictionary of return status matching the\
                 REST response.

        *Use Cases*

           Modify the syslog configuration.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_logging import syslog_server
from pyfos.utils import brcd_util


def _modify_syslog_server(session, restobject):
    return restobject.patch(session)


def modify_syslog_server(session, server, port, secure_mode):
    val = {
           "server": server,
           "port": port,
           "secure_mode": secure_mode
          }
    syslog_obj = syslog_server(val)
    rc = validate(syslog_obj)
    if rc == 1:
        return None
    result = _modify_syslog_server(session, syslog_obj)
    return result


def validate(syslog_obj):
    if not syslog_obj.peek_server():
        return 1
    return 0


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['server', 'port', 'secure_mode']

    inputs = brcd_util.parse(argv, syslog_server, filters, validate)

    session = brcd_util.getsession(inputs)

    result = _modify_syslog_server(inputs['session'],
                                   inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
