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


# pod_license_show.py(pyGen v1.0.0)


"""

:mod:`pod_license_show` - PyFOS util to show for\
ports_on_demand_license_info
******************************************************************************\
*******************************************************************************
The :mod:`pod_license_show` PyFOS util to show for\
ports_on_demand_license_info


Contains information related to ports-on-demand license reservations.

pod_license_show : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: pod_license_show.show_ports_on_demand_license_info(session)

    *Show ports_on_demand_license_info*

        Example Usage of the Method::

            ret = pod_license_show.show_ports_on_demand_license_info(session)
            print (ret)

        Details::

            ports_on_demand_license_infoObj = ports_on_demand_license_info()
            print (ret)

        * Input::

            :param session: The session returned by the login.

        * Output:

            :rtype: None or more instance of class\
            ports_on_demand_license_info on Success  or a dictionary with\
            error.

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_license import ports_on_demand_license_info

from pyfos.utils import brcd_util
# End module imports


def _show_ports_on_demand_license_info(session,
                                       ports_on_demand_license_infoObj):
    objlist = ports_on_demand_license_info.get(session)
    ports_on_demand_license_infolist = list()
    if isinstance(objlist, ports_on_demand_license_info):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            ports_on_demand_license_infolist.append(objlist[i])
    else:
        return (objlist)
    return ports_on_demand_license_infolist


def show_ports_on_demand_license_info(session):
    ports_on_demand_license_infoObj = ports_on_demand_license_info()
    return _show_ports_on_demand_license_info(session,
                                              ports_on_demand_license_infoObj
                                              )


def validate(ports_on_demand_license_infoObj):
    return 0


def main(argv):
    filters = []
    inputs = brcd_util.parse(argv, ports_on_demand_license_info, filters,
                             validate)
    session = brcd_util.getsession(inputs)
    result = _show_ports_on_demand_license_info(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
