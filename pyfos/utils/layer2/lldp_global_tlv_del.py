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


# lldp_global_tlv_del.py(pyGen v1.0.0)


"""

:mod:`lldp_global_tlv_del` - PyFOS util to delete for lldp_global
*******************************************************************************
The :mod:`lldp_global_tlv_del` PyFOS util to delete for lldp_global


The LLDP switch level configuration and operational parameters.

lldp_global_tlv_del : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * --tlv=TLV The list of optional TLVs enabled on the switch. The dcbx,\
      fcoe-app, fcoe-lls, sys-name and port-desc TLVs are enabled by default\
      and user can disable them if required. The dcbx TLV should be enabled\
      beforehand to enable fcoe-app and fcoe-lls TLVs.
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: lldp_global_tlv_del.delete_lldp_global(session,\
optional_tlvs_tlv)

    *Delete lldp_global*

        Example Usage of the Method::

            ret = lldp_global_tlv_del.delete_lldp_global(session,\
            optional_tlvs_tlv)
            print (ret)

        Details::

            lldp_globalObj = lldp_global()
            lldp_globalObj.set_optional_tlvs_tlv(optional_tlvs_tlv)
            print (ret)

        * Input::

            :param session: The session returned by the login.
            :param optional_tlvs_tlv: The list of optional TLVs enabled on the\
              switch. The dcbx, fcoe-app, fcoe-lls, sys-name and port-desc\
              TLVs are enabled by default and user can disable them if\
              required. The dcbx TLV should be enabled beforehand to enable\
              fcoe-app and fcoe-lls TLVs.

        * Output:

            :rtype: Dictionary of response

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_lldp import lldp_global
from pyfos.utils import brcd_util
# End module imports


def _delete_lldp_global(session, lldp_globalObj):
    return lldp_globalObj.delete(session)


def delete_lldp_global(session, optional_tlvs_tlv=None):
    lldp_globalObj = lldp_global()
    lldp_globalObj.set_optional_tlvs_tlv(optional_tlvs_tlv)
    return _delete_lldp_global(session, lldp_globalObj)


def validate(lldp_globalObj):
    if lldp_globalObj.peek_optional_tlvs_tlv() == "[]":
        return 1
    return 0


def main(argv):
    filters = ["optional_tlvs_tlv"]
    inputs = brcd_util.parse(argv, lldp_global, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _delete_lldp_global(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
