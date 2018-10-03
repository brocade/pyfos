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
:mod:`audit_show` - PyFOS util to show audit configuration on switch.
*******************************************************************************
The :mod:`audit_show` provides option to show the parameters of audit on a
switch.

This module is a standalone script that can be used to display the audit
configuration on a switch.

* inputs:

| Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch.
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].


* outputs:
    * audit log configuration information

.. function:: show_audit(session)

        Example usage of the method::

                ret = audit_show.show_audit(session)
                print (ret)

        Details::

                result = audit_show.show_audit(session)

        * inputs:
                :param session: session returned by login.

        * outputs:
                :rtype: dictionary of return status matching rest response

        *Use cases*

           Retrieve the Audit log configuration information.

"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_logging import audit
import pyfos.utils.brcd_util as brcd_util


def show_audit(session):
    audit_obj = audit()
    result = audit_obj.get(session)
    return result


def main(argv):
    filters = []
    inputs = brcd_util.parse(argv, audit, filters)

    session = brcd_util.getsession(inputs)

    result = show_audit(inputs['session'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
            main(sys.argv[1:])
