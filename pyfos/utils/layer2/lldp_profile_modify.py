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


# lldp_profile_modify.py(pyGen v1.0.0)


"""

:mod:`lldp_profile_modify` - PyFOS util to modify for lldp_profile
*******************************************************************************
The :mod:`lldp_profile_modify` PyFOS util to modify for lldp_profile


The LLDP profile.

lldp_profile_modify : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --name=NAME The LLDP profile name.
    * --multiplier=MULTIPLIER The LLDP timeout multiplier value of the LLDP\
      profile. Multiplier value -1 indicates that it will be derived from\
      lldp global multiplier value.
    * --tx-interval=TX-INTERVAL The Transmit interval value of the LLDP\
      profile. Tx-interval value -1 indicates that it will be derived from\
      lldp global tx-interval value.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: lldp_profile_modify.modify_lldp_profile(session, name,\
multiplier, tx_interval)

    *Modify lldp_profile*

        Example Usage of the Method::

            ret = lldp_profile_modify.modify_lldp_profile(session, name,\
            multiplier, tx_interval)
            print (ret)

        Details::

            lldp_profileObj = lldp_profile()
            lldp_profileObj.set_name(name)
            lldp_profileObj.set_multiplier(multiplier)
            lldp_profileObj.set_tx_interval(tx_interval)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param name: The LLDP profile name.
            :param multiplier: The LLDP timeout multiplier value of the LLDP\
              profile. Multiplier value -1 indicates that it will be derived\
              from lldp global multiplier value.
            :param tx_interval: The Transmit interval value of the LLDP\
              profile. Tx-interval value -1 indicates that it will be\
              derived from lldp global tx-interval value.

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


def _modify_lldp_profile(session, lldp_profileObj):
    return lldp_profileObj.patch(session)


def modify_lldp_profile(session, name=None, multiplier=None, tx_interval=None):
    lldp_profileObj = lldp_profile()
    lldp_profileObj.set_name(name)
    lldp_profileObj.set_multiplier(multiplier)
    lldp_profileObj.set_tx_interval(tx_interval)
    return _modify_lldp_profile(session, lldp_profileObj)


def validate(lldp_profileObj):
    if not lldp_profileObj.peek_name():
        return 1

    if lldp_profileObj.peek_multiplier() is None and\
       lldp_profileObj.peek_tx_interval() is None:
        return 1
    return 0


def main(argv):
    filters = ["name", "multiplier", "tx_interval"]
    inputs = brcd_util.parse(argv, lldp_profile, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _modify_lldp_profile(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
