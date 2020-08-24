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


# lldp_global_show.py(pyGen v1.0.0)


"""

:mod:`lldp_global_show` - PyFOS util to show for lldp_global
*******************************************************************************
The :mod:`lldp_global_show` PyFOS util to show for lldp_global


The LLDP switch level configuration and operational parameters.

lldp_global_show : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --tlv=TLV The list of mandatory LLDP TLVs (chassis-id, port-id and\
      time-to-live) which cannot be modified.
    * --multiplier=MULTIPLIER The LLDP timeout multiplier value. Default value\
      is 4
    * --enabled-state=ENABLED-STATE The LLDP protocol state of the switch. The\
      possible values are:  true : LLDP is enabled on the switch  false :\
      LLDP is disabled on the switch Default value is true.
    * --tx-interval=TX-INTERVAL The LLDP Tx interval of the switch. Default\
      value is 30 seconds
    * --tlv=TLV The list of optional TLVs enabled on the switch. The dcbx,\
      fcoe-app, fcoe-lls, sys-name and port-desc TLVs are enabled by default\
      and user can disable them if required. The dcbx TLV should be enabled\
      beforehand to enable fcoe-app and fcoe-lls TLVs.
    * --system-description=SYSTEM-DESCRIPTION The LLDP system description of\
      the switch.
    * --system-name=SYSTEM-NAME The LLDP system name of the switch.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: lldp_global_show.show_lldp_global(session, mandatory_tlvs_tlv,\
multiplier, enabled_state, tx_interval, optional_tlvs_tlv,\
system_description, system_name)

    *Show lldp_global*

        Example Usage of the Method::

            ret = lldp_global_show.show_lldp_global(session,\
            mandatory_tlvs_tlv, multiplier, enabled_state, tx_interval,\
            optional_tlvs_tlv, system_description, system_name)
            print (ret)

        Details::

            lldp_globalObj = lldp_global()
            lldp_globalObj.set_mandatory_tlvs_tlv(mandatory_tlvs_tlv)
            lldp_globalObj.set_multiplier(multiplier)
            lldp_globalObj.set_enabled_state(enabled_state)
            lldp_globalObj.set_tx_interval(tx_interval)
            lldp_globalObj.set_optional_tlvs_tlv(optional_tlvs_tlv)
            lldp_globalObj.set_system_description(system_description)
            lldp_globalObj.set_system_name(system_name)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param mandatory_tlvs_tlv: The list of mandatory LLDP TLVs\
              (chassis-id, port-id and time-to-live) which cannot be\
              modified.
            :param multiplier: The LLDP timeout multiplier value. Default\
              value is 4
            :param enabled_state: The LLDP protocol state of the switch. The\
              possible values are:  true : LLDP is enabled on the switch \
              false : LLDP is disabled on the switch Default value is true.
            :param tx_interval: The LLDP Tx interval of the switch. Default\
              value is 30 seconds
            :param optional_tlvs_tlv: The list of optional TLVs enabled on the\
              switch. The dcbx, fcoe-app, fcoe-lls, sys-name and port-desc\
              TLVs are enabled by default and user can disable them if\
              required. The dcbx TLV should be enabled beforehand to enable\
              fcoe-app and fcoe-lls TLVs.
            :param system_description: The LLDP system description of the\
              switch.
            :param system_name: The LLDP system name of the switch.

        * Output:

            :rtype: None or more instance of class lldp_global on Success  or\
            a dictionary with error.

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_lldp import lldp_global
from pyfos.utils import brcd_util
# End module imports


def _show_lldp_global(session, lldp_globalObj):
    objlist = lldp_global.get(session)
    lldp_globallist = list()
    if isinstance(objlist, lldp_global):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if lldp_globalObj.peek_mandatory_tlvs_tlv() != [] and\
               lldp_globalObj.peek_mandatory_tlvs_tlv() !=\
               objlist[i].peek_mandatory_tlvs_tlv():
                continue
            if lldp_globalObj.peek_multiplier() is not None and\
               lldp_globalObj.peek_multiplier() !=\
               objlist[i].peek_multiplier():
                continue
            if lldp_globalObj.peek_enabled_state() is not None and\
               lldp_globalObj.peek_enabled_state() !=\
               objlist[i].peek_enabled_state():
                continue
            if lldp_globalObj.peek_tx_interval() is not None and\
               lldp_globalObj.peek_tx_interval() !=\
               objlist[i].peek_tx_interval():
                continue
            if lldp_globalObj.peek_optional_tlvs_tlv() != [] and\
               lldp_globalObj.peek_optional_tlvs_tlv() !=\
               objlist[i].peek_optional_tlvs_tlv():
                continue
            if lldp_globalObj.peek_system_description() is not None and\
               lldp_globalObj.peek_system_description() !=\
               objlist[i].peek_system_description():
                continue
            if lldp_globalObj.peek_system_name() is not None and\
               lldp_globalObj.peek_system_name() !=\
               objlist[i].peek_system_name():
                continue
            lldp_globallist.append(objlist[i])
    else:
        print(objlist)
    return lldp_globallist


def show_lldp_global(session, mandatory_tlvs_tlv=None, multiplier=None,
                     enabled_state=None, tx_interval=None,
                     optional_tlvs_tlv=None, system_description=None,
                     system_name=None):
    lldp_globalObj = lldp_global()
    lldp_globalObj.set_mandatory_tlvs_tlv(mandatory_tlvs_tlv)
    lldp_globalObj.set_multiplier(multiplier)
    lldp_globalObj.set_enabled_state(enabled_state)
    lldp_globalObj.set_tx_interval(tx_interval)
    lldp_globalObj.set_optional_tlvs_tlv(optional_tlvs_tlv)
    lldp_globalObj.set_system_description(system_description)
    lldp_globalObj.set_system_name(system_name)
    return _show_lldp_global(session, lldp_globalObj)


def validate(lldp_globalObj):
    if lldp_globalObj.peek_mandatory_tlvs_tlv() == "[]" or\
       lldp_globalObj.peek_multiplier() is None or\
       lldp_globalObj.peek_enabled_state() is None or\
       lldp_globalObj.peek_tx_interval() is None or\
       lldp_globalObj.peek_optional_tlvs_tlv() == "[]" or\
       lldp_globalObj.peek_system_description() is None or\
       lldp_globalObj.peek_system_name() is None:
        return 0
    return 0


def main(argv):
    filters = ["mandatory_tlvs_tlv", "mandatory_tlvs", "multiplier",
               "enabled_state", "tx_interval", "optional_tlvs_tlv",
               "optional_tlvs", "system_description", "system_name"]
    inputs = brcd_util.parse(argv, lldp_global, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _show_lldp_global(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
