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

:mod:`snmp_access_control_modify` - PyFOS util to update snmp acl attributes
****************************************************************************
The :mod:`snmp_access_control` provides option to modify snmp access control
attributes

This module can be used to modify snmp access control attributes.

* inputs:

|  Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

|  Util scripts options:

  | --index=VALUE        Index of snmp access control list
  | --host=VALUE         The subnet area of the access host
  | --access-level=VALUE The access level of the access control entry[OPTIONAL]

* outputs:

    * Status of the patch operation on snmp access control's attributes

.. function:: access_control_obj.set_host(host_ip)

    * Configures host ip address for snmp access control list

        Example usage of the method::

            ret =  access_control_obj.set_host(host_ip)
            print (ret)

        Details::

            access_control_obj = access_control()
            if host_ip is not None:
               access_control_obj.set_host(host_ip)

            result = _set_access_control_obj(session, access_control_obj)

        * inputs:
            :param session: session returned by login.
            :param host-ip: IP address of a host.

        * outputs:
            :rtype: dictionary of return status matching rest response


.. function:: access_control_obj.set_access_level(access_level)

    * Configures snmp access control list.

        Example usage of the method::

            ret = access_control_obj.set_access_level(access_level)
            print (ret)

        Details::

            access_control_obj = access_control()
            if access_level is not None:
                v3_acc_obj.set_user_name(username)

            result = _set_snmp_access_control (session, v1_acc_obj)

        * inputs:
            :param session: session returned by login.
            :param access_level: access lelvel for each snmp get/set operations
                                 in access contol list

        * outputs:
            :rtype: dictionary of return status matching rest response

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_snmp import access_control


def _set_snmp_access_control(session, restobject):
    return restobject.patch(session)


def _set_host(session, host_ip):
    access_control_obj = access_control()
    if host_ip is not None:
        access_control_obj.set_host(host_ip)
    result = _set_snmp_access_control(session, access_control_obj)
    return result


def _set_access_level(session, access_level):
    access_control_obj = access_control()
    if access_level is not None:
        access_control_obj.set_access_level(access_level)
    result = _set_snmp_access_control(session, access_control_obj)
    return result


def validate(access_control_obj):
    if (access_control_obj.peek_index() is None and
            access_control_obj.peek_host() is None):
        return 1
    return 0


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['index', 'host', 'access_level']

    inputs = brcd_util.parse(argv, access_control, filters, validate)

    session = brcd_util.getsession(inputs)

    result = _set_snmp_access_control(inputs['session'], inputs['utilobject'])
    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
