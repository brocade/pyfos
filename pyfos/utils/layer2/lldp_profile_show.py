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


# lldp_profile_show.py(pyGen v1.0.0)


"""

:mod:`lldp_profile_show` - PyFOS util to show for lldp_profile
*******************************************************************************
The :mod:`lldp_profile_show` PyFOS util to show for lldp_profile


The LLDP profile.

lldp_profile_show : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --tx-interval=TX-INTERVAL The Transmit interval value of the LLDP\
      profile. Tx-interval value -1 indicates that it will be derived from\
      lldp global tx-interval value.
    * --name=NAME The LLDP profile name.
    * --multiplier=MULTIPLIER The LLDP timeout multiplier value of the LLDP\
      profile. Multiplier value -1 indicates that it will be derived from\
      lldp global multiplier value.
    * --tlv=TLV List of enabled TLVs for the LLDP profile. Empty enabled-tlvs\
      indicates that the tlvs will be derived from lldp global\
      optional-tlvs.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: lldp_profile_show.show_lldp_profile(session, tx_interval, name,\
multiplier, enabled_tlvs_tlv)

    *Show lldp_profile*

        Example Usage of the Method::

            ret = lldp_profile_show.show_lldp_profile(session, tx_interval,\
            name, multiplier, enabled_tlvs_tlv)
            print (ret)

        Details::

            lldp_profileObj = lldp_profile()
            lldp_profileObj.set_tx_interval(tx_interval)
            lldp_profileObj.set_name(name)
            lldp_profileObj.set_multiplier(multiplier)
            lldp_profileObj.set_enabled_tlvs_tlv(enabled_tlvs_tlv)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param tx_interval: The Transmit interval value of the LLDP\
              profile. Tx-interval value -1 indicates that it will be\
              derived from lldp global tx-interval value.
            :param name: The LLDP profile name.
            :param multiplier: The LLDP timeout multiplier value of the LLDP\
              profile. Multiplier value -1 indicates that it will be derived\
              from lldp global multiplier value.
            :param enabled_tlvs_tlv: List of enabled TLVs for the LLDP\
              profile. Empty enabled-tlvs indicates that the tlvs will be\
              derived from lldp global optional-tlvs.

        * Output:

            :rtype: None or more instance of class lldp_profile on Success  or\
            a dictionary with error.

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_lldp import lldp_profile
from pyfos.utils import brcd_util
# End module imports


def _show_lldp_profile(session, lldp_profileObj):
    objlist = lldp_profile.get(session)
    lldp_profilelist = list()
    if isinstance(objlist, lldp_profile):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
#            if lldp_profileObj.peek_tx_interval() is not None and\
#               lldp_profileObj.peek_tx_interval() !=\
#               objlist[i].peek_tx_interval():
#                continue
            if lldp_profileObj.peek_name() is not None and\
               lldp_profileObj.peek_name() != objlist[i].peek_name():
                continue
#            if lldp_profileObj.peek_multiplier() is not None and\
#               lldp_profileObj.peek_multiplier() !=\
#               objlist[i].peek_multiplier():
#                continue
#            if lldp_profileObj.peek_enabled_tlvs_tlv() != "[]" and\
#               lldp_profileObj.peek_enabled_tlvs_tlv() !=\
#               objlist[i].peek_enabled_tlvs_tlv():
#                continue
            lldp_profilelist.append(objlist[i])
    else:
        print(objlist)
    return lldp_profilelist


def show_lldp_profile(session, tx_interval=None, name=None, multiplier=None,
                      enabled_tlvs_tlv=None):
    lldp_profileObj = lldp_profile()
    lldp_profileObj.set_tx_interval(tx_interval)
    lldp_profileObj.set_name(name)
    lldp_profileObj.set_multiplier(multiplier)
    lldp_profileObj.set_enabled_tlvs_tlv(enabled_tlvs_tlv)
    return _show_lldp_profile(session, lldp_profileObj)


def validate(lldp_profileObj):
    if lldp_profileObj.peek_tx_interval() is None or\
       lldp_profileObj.peek_name() is None or\
       lldp_profileObj.peek_multiplier() is None or\
       lldp_profileObj.peek_enabled_tlvs_tlv() == "[]":
        return 0
    return 0


def main(argv):
    filters = ["tx_interval", "name", "multiplier", "enabled_tlvs",
               "enabled_tlvs_tlv"]
    inputs = brcd_util.parse(argv, lldp_profile, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _show_lldp_profile(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
