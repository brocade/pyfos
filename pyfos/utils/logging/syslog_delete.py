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
:mod:`syslog_delete` - PyFOS util to delete the syslog configuration on\
 a switch.
*********************************************************************************
The :mod:`syslog_delete` util provides the option to delete the syslog \
configuration parameters of syslog on a switch.

This module is a stand-alone script that can be used to delete the syslog
configuration on a switch.

* Input:

| Infrastructure Options:

  | -i,--ipaddr=IPADDR     The IP address of the FOS switch.
  | -L,--login=LOGIN       The login name.
  | -P,--password=PASSWORD The password.
  | -f,--vfid=VFID         The VFID to which the request is \
                            directed [OPTIONAL].
  | -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           Verbose mode[OPTIONAL].

| Util Script Options:

  | --server=<server IP address>

* Output:
    * Status of the delete operation.

.. function:: del_syslog_server(session, server)

        Example Usage of the Method::

               ret = syslog_delete.del_syslog_server(session, server)
               print (ret)

        Details::

                val = {
                        "server": server-ip
                      }

                syslog_obj = syslog_server()
                syslog_obj.set_server(server)

                result = _del_syslog_server(session, syslog_obj)
                return result

        * Input:
                :param session: The session returned by the login.
                :server: The server IP address.

        * Output:
                :rtype: A dictionary of return status matching the\
                 REST response.

        *Use Cases*

                Delete the configured syslog servers.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_logging import syslog_server
from pyfos.utils import brcd_util


def _del_syslog_server(session, restobject):
    return restobject.delete(session)


def del_syslog_server(session, server):
    val = {
           "server": server
          }
    syslog_obj = syslog_server(val)

    result = _del_syslog_server(session, syslog_obj)
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

    result = _del_syslog_server(inputs['session'],
                                inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
