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

:mod:`gigabitethernet_show` - PyFOS util to display the GE_Port data.
*******************************************************************************
The :mod:`gigabitethernet_show` util is used to display the GE_Port data.

This module is a stand-alone script that can be used to show the
switch GE_Port speed on an extension platform.

gigabitethernet_show.py: Usage

* Infrastructure options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA"[Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * -n,--name=NAME: Sets the GE_Port name.

* Output:
    * Python dictionary content with RESTCONF response data.

.. function:: gigabitethernet_show.show(session,\
name, speed)

    *Show extension gigabitethernet*

        Example Usage of the Method::

            ret = gigabitethernet_show.show(session,
            name, speed)
            print (ret)

        * Input:
            :param session: The session returned by the login.
            :param name: The GE_Port name expressed as slot/port.

        * Output:
            :rtype: A list of GE_Ports.

        *Use Cases*

         Show the GE_Port.
"""


import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_gigabitethernet import gigabitethernet
from pyfos.utils import brcd_util


def _show(session, geObject):
    objlist = gigabitethernet.get(session)
    gelist = []
    if isinstance(objlist, gigabitethernet):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if geObject.peek_name() is not None and\
               geObject.peek_name() != objlist[i].peek_name():
                continue
            gelist.append(objlist[i])
    else:
        print(objlist)
    return gelist


# pylint: disable=W0613
def show(session, name):
    geObject = gigabitethernet()
    result = _show(session, geObject)
    return result


def main(argv):
    # myinputs = "-i 10.17.3.70 --name 4/17"
    # argv = myinputs.split()
    filters = ['name']
    inputs = brcd_util.parse(argv, gigabitethernet, filters)
    geObject = inputs['utilobject']
    session = brcd_util.getsession(inputs)
    result = _show(session, geObject)
    if len(result) == 0:
        print("No GE interface found.")
    else:
        pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
