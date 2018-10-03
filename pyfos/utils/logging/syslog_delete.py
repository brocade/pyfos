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
:mod:`syslog_delete` - PyFOS util to delete syslog configuration on switch.
*********************************************************************************
The :mod:`syslog_delete` provides option to delete the config parameters\
of syslog on switch.

This module is a standalone script that can be used to delete the syslog
configuration on switch.

* inputs:

| Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch.
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

| Util scripts options:

  | --server=<server ip address>

* outputs:
    * Status of delete operation

.. function:: del_syslog_server(session, server)

        Example usage of the method::

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

        * inputs:
                :param session: session returned by login.
                :server: server ip address

        * outputs:
                :rtype: dictionary of return status matching rest response

        *use cases*

                Delete the configured syslog servers.
"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_logging import syslog_server
import pyfos.utils.brcd_util as brcd_util


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
    if (not syslog_obj.peek_server()):
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
