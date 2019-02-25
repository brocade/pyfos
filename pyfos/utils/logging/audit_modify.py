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
:mod:`audit_modify` - PyFOS util to modify the audit configuration on a switch.
*******************************************************************************
The :mod:`audit_modify` util provides option to modify the configuration \
parameters of the audit on a switch.

This module is a stand-alone script that can be used to modify the audit
configuration on a switch.

* Input:

| Infrastructure Option:

  | -i,--ipaddr=IPADDR     The IP address of the FOS switch.
  | -L,--login=LOGIN       The login name.
  | -P,--password=PASSWORD The password.
  | -f,--vfid=VFID         The VFID to which the request is \
                            directed [OPTIONAL].
  | -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           Verbose mode [OPTIONAL].

|  Util Script Options:

  | --enable <true/false>
  | --severity <critical | error | warning | info>
  | --filters <zone | security | configuration | firmware | fabric \
              | ls | cli | maps>

* Output:
    * Status of the modify operation.

.. function:: modify_audit(session, audit_enabled, severity, filter)

        Example Usage of the Method::

                ret = audit_modify.modify_audit(session, audit_enabled,
                                                severity, filter)
                print (ret)

        Details::

                val = {
                  "audit_enabled": true/false,
                  "severity": severity level,
                  "filter_class_list_filter_class": filter class list
                }
                audit_obj = audit(val)
                result = _modify_audit(session, audit_obj)
                return result

        * Input:
                :param session: The session returned by the login.
                :param audit_enabled: True to enable; false to disable.
                :param severity_level: Critical, error, warning, or info.

        * Output:
                :rtype: A dictionary of return status matching the\
                 REST response.

        *Use Cases*
           Modify the audit log configuration.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_logging import audit
from pyfos.utils import brcd_util


def _modify_audit(session, restobject):
    return restobject.patch(session)


def modify_audit(session, audit_enabled, severity, filter_class):
    val = {
           "audit_enabled": audit_enabled,
           "severity": severity,
           "filter_class_list_filter_class": filter_class
          }
    audit_obj = audit(val)
    rc = validate(audit_obj)
    if rc == 1:
        return None
    result = _modify_audit(session, audit_obj)
    return result


def validate(audit_obj):
    if ((audit_obj.peek_audit_enabled() is None) and
       (not audit_obj.peek_severity_level()) and
       (not audit_obj.peek_filter_class_list_filter_class())):
        return 1
    else:
        return 0


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['audit_enabled', 'severity_level',
               'filter_class_list_filter_class']

    inputs = brcd_util.parse(argv, audit, filters, validate)

    session = brcd_util.getsession(inputs)

    result = _modify_audit(inputs['session'],
                           inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
