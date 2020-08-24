#!/usr/bin/env python3


# Copyright © 2019-2020 Broadcom. All rights reserved.
# The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries.
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


# gigabitethernet_statistics_show.py(pyGen v1.0.0)


"""

:mod:`gigabitethernet_statistics_show` - PyFOS util to show for\
 gigabitethernet_statistics
******************************************************************************\
*******************************************************************************
The:mod:`gigabitethernet_statistics_show` PyFOS util to show for\
 gigabitethernet_statistics


A list of interface-related statistics for gigabitethernet port.

gigabitethernet_statistics_show: usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].
    * -a,--authtoken: AuthToken value or AuthTokenManager config\
    file[OPTIONAL].
    * -z,--nosession: Sessionless authentication based login[OPTIONAL].
    * --nocredential: No credential to be sent in the request[OPTIONAL].

* Util Script Options:
    * --name=NAME: The name of the interface.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: gigabitethernet_statistics_show.show_gigabitethernet_statistics(\
session, name)

    *Show gigabitethernet_statistics*

    Example Usage of the Method::

            ret =\
 gigabitethernet_statistics_show.show_gigabitethernet_statistics(session,\
 name)
            print(ret)

    Details::

        gigabitethernet_statisticsObj = gigabitethernet_statistics()
        gigabitethernet_statisticsObj.set_name(name)
        ret = _show_gigabitethernet_statistics(session,\
 gigabitethernet_statisticsObj)
        print(ret)

    **Inputs**

    :param session: The session returned by the login.
    :param name: The name of the interface.

    **Output**

    :rtype: None or one/more instance of class gigabitethernet_statistics on\
    Success  or a dictionary with error.

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_interface import gigabitethernet_statistics

from pyfos.utils import brcd_util
# End module imports


def _show_gigabitethernet_statistics(session, gigabitethernet_statisticsObj):
    objlist = gigabitethernet_statistics.get(session)
    gigabitethernet_statisticslist = list()
    if isinstance(objlist, gigabitethernet_statistics):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if gigabitethernet_statisticsObj.peek_name() is not None and\
               gigabitethernet_statisticsObj.peek_name() !=\
               objlist[i].peek_name():
                continue
            gigabitethernet_statisticslist.append(objlist[i])
    else:
        return objlist
    return gigabitethernet_statisticslist


def show_gigabitethernet_statistics(session, name=None):
    gigabitethernet_statisticsObj = gigabitethernet_statistics()
    gigabitethernet_statisticsObj.set_name(name)
    return _show_gigabitethernet_statistics(session,
                                            gigabitethernet_statisticsObj)


def validate(gigabitethernet_statisticsObj):
    if gigabitethernet_statisticsObj.peek_name() is None:
        return 0
    return 0


def main(argv):
    filters = ["name"]
    inputs = brcd_util.parse(argv, gigabitethernet_statistics, filters,
                             validate)
    session = brcd_util.getsession(inputs)
    result = _show_gigabitethernet_statistics(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
