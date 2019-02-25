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

:mod:`syslog_show` - PyFOS util to show the syslog server configuration\
 on a switch.
**************************************************************************************
The :mod:`syslog_show` util provides the option to show the syslog parameters \
on a switch.

This module is a stand-alone script that can be used to display the syslog
server configuration on a switch.

* Input:

| Infrastructure options:

  | -i,--ipaddr=IPADDR     The IP address of the FOS switch.
  | -L,--login=LOGIN       The login name.
  | -P,--password=PASSWORD The password.
  | -f,--vfid=VFID         The VFID to which the request is \
                            directed [OPTIONAL].
  | -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           Verbose mode [OPTIONAL].

| Util Script Options:

  | --server=server-ip:   The IP address of the syslog server.

* Output:
    * Syslog server information.

.. function:: show_syslog_server(session, server)

        Example Usage of the Method::

            ret = syslog_show.show_syslog_server(session, server)
            print (ret)

        Details::

            result = syslog_show.show_syslog_server(session, "10.10.10.10")

       * Input:
            :param session: The session returned by the login.
            :param server: The server IP address.

       * Output:
            :rtype: A list of configured syslog servers. If the
                  server is specified, displays a matching entry, if present.

        *Use Cases*

        1. Retrieve the syslog server information.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_logging import syslog_server
from pyfos.utils import brcd_util


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
