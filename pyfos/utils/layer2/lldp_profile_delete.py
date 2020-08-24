#!/usr/bin/env python3


# Copyright © 2019 Broadcom. All rights reserved.
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


# lldp_profile_delete.py(pyGen v1.0.0)


"""

:mod:`lldp_profile_delete` - PyFOS util to delete for lldp_profile
*******************************************************************************
The :mod:`lldp_profile_delete` PyFOS util to delete for lldp_profile


The LLDP profile.

lldp_profile_delete : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --name=NAME The LLDP profile name.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: lldp_profile_delete.delete_lldp_profile(session, name)

    *Delete lldp_profile*

        Example Usage of the Method::

            ret = lldp_profile_delete.delete_lldp_profile(session, name)
            print (ret)

        Details::

            lldp_profileObj = lldp_profile()
            lldp_profileObj.set_name(name)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param name: The LLDP profile name.

        * Output:

            :rtype: Dictionary of response

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_lldp import lldp_profile
from pyfos.utils import brcd_util
# End module imports


def _delete_lldp_profile(session, lldp_profileObj):
    return lldp_profileObj.delete(session)


def delete_lldp_profile(session, name=None):
    lldp_profileObj = lldp_profile()
    lldp_profileObj.set_name(name)
    return _delete_lldp_profile(session, lldp_profileObj)


def validate(lldp_profileObj):
    if lldp_profileObj.peek_name() is None:
        return 1
    return 0


def main(argv):
    filters = ["name"]
    inputs = brcd_util.parse(argv, lldp_profile, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _delete_lldp_profile(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
