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
:mod:`audit_show` - PyFOS util to show the audit configuration on a switch.
*******************************************************************************
The :mod:`audit_show` util provides the option to show the parameters of the \
audit on a switch.

This module is a stand-alone script that can be used to display the audit
configuration on a switch.

* Input:

| Infrastructure Options:

  | -i,--ipaddr=IPADDR     The IP address of the FOS switch.
  | -L,--login=LOGIN       The login name.
  | -P,--password=PASSWORD The password.
  | -f,--vfid=VFID         The VFID to which the request is \
                            directed [OPTIONAL].
  | -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           Verbose mode [OPTIONAL].


* Output:
    * Audit log configuration information

.. function:: show_audit(session)

        Example Usage of the Method::

                ret = audit_show.show_audit(session)
                print (ret)

        Details::

                result = audit_show.show_audit(session)

        * Input:
                :param session: The session returned by the login.

        * Output:
                :rtype: A dictionary of return status matching the\
                 REST response.

        *Use Cases*

           Retrieve the audit log configuration information.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_logging import audit
from pyfos.utils import brcd_util


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
