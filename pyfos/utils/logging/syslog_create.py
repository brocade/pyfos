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

:mod:`syslog_create` PyFOS util to create syslog server configuration on\
 switch.
***************************************************************************\
**********
The :mod:`syslog_create` provides option to create the config parameters of\
syslog server on a switch.

This module is a standalone script that can be used to display the syslog
server configuration on a switch.

* inputs:

| Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch.
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

| Util scripts options:

  | --server=server ip address
  | --port=port number
  | --secure_mode=true | false

* outputs:
    * Status of create/add syslog server operation

.. function:: create_syslog_server(session, server, port, secure_mode)

        Example usage of the method::

              ret = syslog_create.create_syslog_server(session, server,\
                                                          port, secure_mode)
              print (ret)

        Details::

                val = {
                       "server": server ip address,
                       "port": port number,
                       "secure-mode": true/false

                      }
                syslog_obj = syslog_server(val)
                result = _create_syslog_server(session, syslog_obj)
                return result

        * inputs:
                :param session: session returned by login.
                :param server: server ip.
                :param port: port number.
                :param secure-mode: true/false.

        * outputs:
                :rtype: dictionary of return status matching rest response

        *use cases*
           Add syslog server

"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_logging import syslog_server
import pyfos.utils.brcd_util as brcd_util


def _create_syslog_server(session, restobject):
    return restobject.post(session)


def create_syslog_server(session, server, port, secure_mode):

    syslog_obj = syslog_server()

    if (not syslog_obj.peek_server()):
        return

    if (syslog_obj.peek_secure_mode() is not None):
        syslog_obj.set_secure_mode(secure_mode)
    if (syslog_obj.peek_port() is not None):
        syslog_obj.set_port(port)

    result = _create_syslog_server(session, syslog_obj)
    return result


def validate(syslog_obj):
    if (not syslog_obj.peek_server()):
        return 1
    elif (syslog_obj.peek_port() is not None and
          not syslog_obj.peek_secure_mode()):
            return 1
    else:
        return 0


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['server', 'port', 'secure_mode']

    inputs = brcd_util.parse(argv, syslog_server, filters, validate)

    session = brcd_util.getsession(inputs)

    result = _create_syslog_server(inputs['session'],
                                   inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
