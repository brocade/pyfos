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

:mod:`snmp_v1_trap_modify` - PyFOS util for updating snmp v1 trap entries
**************************************************************************
The :mod:`snmp_v1_trap_modify` provides option to modify snmp v1 trap entry
attributes

This module can be used to modify the attributes of host receipient like
ipaddress, port number and severity level.

* inputs:

|  Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

|  Util scripts options:

  | --index=INDEX                   Index of SNMPv1 host recipient
  | --host=HOST                     IP address of trap recipient
  | --port-number=PORT-NUMBER       The port number of trap recipient[OPTIONAL]
  | --severity-level=SEVERITY-LEVEL Severity level of trap recipient[OPTIONAL]

* outputs:

    * Status of the patch operation on v1 trap's attributes.

.. function:: v1_trap_obj.set_host(host_ip)

    * Configures host ip address

        Example usage of the method::

            ret =  v1_trap_obj.set_host(host_ip)
            print (ret)

        Details::

            v1_trap_obj = v1_trap()
            if host_ip is not None:
               v1_trap_obj.set_host(host_ip)

            result = _set_snmp_v1_trap(session, v1_trap_obj)

        * inputs:
            :param session: session returned by login.
            :param host-ip: IP address of a host.

        * outputs:
            :rtype: dictionary of return status matching rest response


.. function:: v1_trap_obj.set_trap_severity_level(sev_level)

    * Configures trap severity level

        Example usage of the method::

            ret =  v1_trap_obj.set_trap_severity_level(sev_level)
            print (ret)

        Details::

            v1_trap_obj = v1_trap()
            if sev_level is not None:
               v1_trap_obj.set_trap_severity_level(sev_level)

            result = _set_snmp_v1_trap(session, v1_trap_obj)

        * inputs:
            :param session: session returned by login.
            :param sev_level: severity level of swEVentTrap.

        * outputs:
            :rtype: dictionary of return status matching rest response


.. function:: v1_trap_obj.set_port_number(port_number)

    * Configures port number of the host

        Example usage of the method::

            ret =  v1_trap_obj.set_port_number(port_number)
            print (ret)

        Details::

            v1_trap_obj = v1_trap()
            if port_number is not None:
               v1_trap_obj.set_port_number(port_number)

            result = _set_snmp_v1_trap(session, v1_trap_obj)

        * inputs:
            :param session: session returned by login.
            :param host-ip: port number of the host.

        * outputs:
            :rtype: dictionary of return status matching rest response


"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_snmp import v1_trap


def _set_snmp_v1_trap(session, restobject):
    return restobject.patch(session)


def _set_host(session, host_ip):
    v1_trap_obj = v1_trap()
    if host_ip is not None:
        v1_trap_obj.set_host(host_ip)
    result = _set_snmp_v1_trap(session, v1_trap_obj)
    return result


def _set_trap_severity_level(session, sev_level):
    v1_trap_obj = v1_trap()
    if sev_level is not None:
        v1_trap_obj.set_trap_severity_level(sev_level)
    result = _set_snmp_v1_trap(session, v1_trap_obj)
    return result


def _set_port_number(session, port_number):
    v1_trap_obj = v1_trap()
    if port_number is not None:
        v1_trap_obj.set_port_number(port_number)
    result = _set_snmp_v1_trap(session, v1_trap_obj)
    return result


def validate(v1_trap_obj):
    if (v1_trap_obj.peek_index() is None and v1_trap_obj.peek_host() is None):
        return 1
    return 0


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['index', 'host', 'trap_severity_level', 'port_number']

    inputs = brcd_util.parse(argv, v1_trap, filters, validate)

    session = brcd_util.getsession(inputs)

    result = _set_snmp_v1_trap(inputs['session'], inputs['utilobject'])
    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
