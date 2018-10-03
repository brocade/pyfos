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
:mod:`audit_modify` - PyFOS util to modify audit configuration on switch.
*******************************************************************************
The :mod:`audit_modify` provides option to modify the config parameters\
of audit on switch.

This module is a standalone script that can be used to modify the audit
configuration on switch.

* inputs:

| Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch.
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

|  Util scripts options:

  | --enable, <true/false>
  | --severity <critical | error | warning | info>
  | --filters <zone | security | configuration | firmware | fabric \
              | ls | cli | maps>

* outputs:
    * Status of modify operation

.. function:: modify_audit(session, audit_enabled, severity, filter)

        Example usage of the method::

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

        * inputs:
                :param session: session returned by login.
                :param audit_enabled: true to enable, false to disable
                :param severity_level: can be any of critical | error |
                                       warning | info

        * outputs:
                :rtype: dictionary of return status matching rest response

        *use cases*
           Modify audit log configuration

"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_logging import audit
import pyfos.utils.brcd_util as brcd_util


def _modify_audit(session, restobject):
    return restobject.patch(session)


def modify_audit(session, audit_enabled, severity, filter_class):
    audit_obj = audit()
    if audit_enabled is not None:
        audit_obj.set_audit_enabled(audit_enabled)
    if severity is not None:
        audit_obj.set_severity_level(severity)
    if filter_class is not None:
        audit_obj.set_filter_class_list_filter_class(filter_class)

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
