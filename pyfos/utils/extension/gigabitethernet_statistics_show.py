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

:mod:`gigabitethernet_statistics_show` - PyFOS util for GE Stats.
*******************************************************************************
The :mod:`gigabitethernet_statistics_show` Util is used to display GE Stats.

This module is a stand-alone script that can be used to show the
switch GE port stats on an extension platform.

gigabitethernet_statistics_show.py: Usage

* Infrastructure options:
    * -i,--ipaddr=IPADDR: IP address of FOS switch.
    * -L,--login=LOGIN: Login name.
    * -P,--password=PASSWORD: Password.
    * -f,--vfid=VFID: VFID to which the request is directed.
    * -s,--secured=MODE: HTTPS mode "self" or "CA"[Optioanl].
    * -v,--verbose: Verbose mode[Optional].

* Util scripts options:
    * -n,--name=NAME : Show name

* Outputs:
    * Python dictionary content with RESTCONF response data.

.. function:: gigabitethernet_statistics_show.show(\
session, name, speed)

    *Show extension gigabitethernet statistics*

        Example usage of the method::

            ret = gigabitethernet_statistics_show.show(
            session, name)
            print (ret)

        * Inputs:
            :param session: Session returned by login.
            :param name: GigabitEthernet port name expressed as slot/port.

        * Outputs:
            :rtype: List of GE ports.

        *Use cases*

         Show GigabitEthernet port statistics.
"""


import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_gigabitethernet import \
     gigabitethernet_statistics
import sys
import pyfos.utils.brcd_util as brcd_util


def _show(session, geObject):
    objlist = gigabitethernet_statistics.get(session)
    gelist = []
    if isinstance(objlist, gigabitethernet_statistics):
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


def show(session, name):
    geObject = gigabitethernet_statistics()
    geObject.set_name(name)
    result = _show(session, geObject)
    return (result)


def main(argv):
    # myinputs = "-i 10.17.3.70 --name 4/17"
    # argv = myinputs.split()
    filters = ['name']
    inputs = brcd_util.parse(argv, gigabitethernet_statistics,
                             filters)
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
