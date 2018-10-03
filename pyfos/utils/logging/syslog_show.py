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

:mod:`syslog_show` - PyFOS util to show syslog server configuration on switch.
*******************************************************************************
The :mod:`syslog_show` provides option to show the parameters of syslog on a
switch.

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

| Util script options:

  | --server=server-ip   Ip address of the syslog server

* outputs:
    * Syslog server information

.. function:: show_syslog_server(session, server)

        Example usage of the method::

            ret = syslog_show.show_syslog_server(session, server)
            print (ret)

        Details::

            result = syslog_show.show_syslog_server(session, "10.10.10.10")

       * inputs:
            :param session: session returned by login.
            :param server: server ip address.

       * outputs:
            :rtype: Displays the list of configured syslog servers. If the
                  server is specified, displays matching entry if present.

        *use cases*

        1. Retrieve the syslog server information.

"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_logging import syslog_server
import pyfos.utils.brcd_util as brcd_util


def show_syslog_server(session, server):
    syslog_server_obj = syslog_server()
    if server is None:
        return syslog_server_obj.get(session)
    else:
        return syslog_server_obj.get(session, server)


def main(argv):
    filters = ["server"]
    inputs = brcd_util.parse(argv, syslog_server, filters)

    session = brcd_util.getsession(inputs)

    result = show_syslog_server(inputs['session'],
                                inputs['utilobject'].peek_server())
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
            main(sys.argv[1:])
