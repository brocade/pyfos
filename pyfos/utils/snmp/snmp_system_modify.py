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

:mod:`snmp_system_modify` - PyFOS util for updating snmp system attributes
**************************************************************************
The :mod:`snmp_system_modify` provides option to modify snmp system
attributes

This module can be used to modify system description, location, contact,
informs enabled, encryption enabled, audit interval, default config,
security level for get & set operations and snmpv1 enabled.

* inputs:

|  Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

|  Util scripts options:

  | --sys-description=SYS-DESCRIPTION System description[OPTIONAL]
  | --sys-location=SYS-LOCATION       System location[OPTIONAL]
  | --sys-contact=SYS-CONTACT         System contact[OPTIONAL]
  | --informs-enabled=INFORMS-ENABLED Informs enabled <true|false>[OPTIONAL]
  | --audit-interval=AUDIT-INTERVAL   Audit interval[OPTIONAL]
  | --sec-get-level=SEC-GET-LEVEL     SNMP GET security level[OPTIONAL]
  | --sec-set-level=SEC-SET-LEVEL     SNMP SET security level[OPTIONAL]
  | --default-config=DEFAULT-CONFIG   Defaulting SNMP configurations[OPTIONAL]
  | --snmpv1-enabled=SNMPV1-ENABLED   SNMPv1 is enabled <true|false>[OPTIONAL]
  | --encryption-enabled=ENCRYPTION-ENABLED Encryption enabled <true|false>

* outputs:

    * Status of the modified system description

.. function:: system_obj.set_description(description)

    * Configures system description

        Example usage of the method::

            ret = system_obj.set_description(description)
            print (ret)

        Details::

            system_obj = system()
            system_obj.set_description(description)
            if description is not None:
                system_obj.set_description(description)

            result = _set_snmp_system(session, system_obj)

        * inputs:
            :param session: session returned by login.
            :param description: system description.

        * outputs:
            :rtype: dictionary of return status matching rest response

    * Status of the modified system location

.. function:: system_obj.set_location(location)

    * Configures system location

        Example usage of the method::

            ret = system_obj.set_location(location)
            print (ret)

        Details::

            system_obj = system()
            system_obj.set_location(location)
            if location is not None:
                system_obj.set_location(location)

            result = _set_snmp_system(session, system_obj)

        * inputs:
            :param session: session returned by login.
            :param location: system location.

        * outputs:
            :rtype: dictionary of return status matching rest response

    * Status of the modified system contact

.. function:: system_obj.set_contact(contact)

    * Configures system contact

        Example usage of the method::

            ret = system_obj.set_contact(contact)
            print (ret)

        Details::

            system_obj = system()
            system_obj.set_contact(contact)
            if contact is not None:
                system_obj.set_contact(contact)

            result = _set_snmp_system(session, system_obj)

        * inputs:
            :param session: session returned by login.
            :param contact: system contact.

        * outputs:
            :rtype: dictionary of return status matching rest response

    * Status of the modified snmpv3 informs_enabled

.. function:: system_obj.set_informs_enabled(informs_enabled)

    * Configures snmpv3 informs enabled

        Example usage of the method::

            ret = system_obj.set_informs_enabled(informs_enabled)
            print (ret)

        Details::

            system_obj = system()
            system_obj.set_informs_enabled(informs_enabled)
            if informs_enabled is not None:
                system_obj.set_informs_enabled(informs_enabled)

            result = _set_snmp_informs_enabled(session, system_obj)

        * inputs:
            :param session: session returned by login.
            :param informs_enabled: snmpv3 informs enabled.

        * outputs:
            :rtype: dictionary of return status matching rest response

    * Status of the modified snmpv3 passwords encryption flag enabled

.. function:: system_obj.set_encryption_enabled(encrypt_enabled)

    * Configures snmpv3 passwords encryption flag enabled

        Example usage of the method::

            ret = system_obj.set_encryption_enabled(encrypt_enabled)
            print (ret)

        Details::

            system_obj = system()
            system_obj.set_encryption_enabled(encrypt_enabled)
            if encrypt_enabled is not None:
                system_obj.set_encryption_enabled(encrypt_enabled)

            result = _set_snmp_system(session, system_obj)

        * inputs:
            :param session: session returned by login.
            :param encryption enabled flag: snmpv3 passwords
                                             encryption flag enabled.

        * outputs:
            :rtype: dictionary of return status matching rest response

    * Status of the modified system audit interval

.. function:: system_obj.set_audit_interval(audit_interval)

    * Configures system audit interval

        Example usage of the method::

            ret = system_obj.set_audit_interval(audit_interval)
            print (ret)

        Details::

            system_obj = system()
            system_obj.set_audit_interval(audit_interval)
            if audit_interval is not None:
                system_obj.set_audit_interval(audit_interval)

            result = _set_snmp_audit_interval(session, system_obj)

        * inputs:
            :param session: session returned by login.
            :param audit_interval: system audit interval.

        * outputs:
            :rtype: dictionary of return status matching rest response

    * Status of the modified snmp default configurations

.. function:: system_obj.set_default_config_default_control(default_contrl)

    * Configures snmp default values

        Example usage of the method::

            ret = system_obj.set_default_config_default_control(default_contrl)
            print (ret)

        Details::

            system_obj = system()
            system_obj.set_audit_interval(default_contrl)
            if default_contrl is not None:
                system_obj.set_default_config_default_control(default_contrl)

            result = _set_default_control(session, system_obj)

        * inputs:
            :param session: session returned by login.
            :param default_contrl: snmp default configuration value

        * outputs:
            :rtype: dictionary of return status matching rest response

    * Status of the modified snmp GET security level

.. function:: system_obj.set_security_get_level(sec_get_level)

    * Configures snmp GET security level

        Example usage of the method::

            ret = system_obj.set_security_get_level()
            print (ret)

        Details::

            system_obj = system()
            system_obj.set_security_get_level(sec_get_level)
            if sec_get_level is not None:
                system_obj.set_security_get_level(sec_get_level)

            result = _set_security_get_level(session, system_obj)

        * inputs:
            :param session: session returned by login.
            :param sec_get_level: snmp GET security level

        * outputs:
            :rtype: dictionary of return status matching rest response

    * Status of the modified snmp SET security level

.. function:: system_obj.set_security_set_level(sec_set_level)

    * Configures snmp SET security level

        Example usage of the method::

            ret = system_obj.set_security_set_level()
            print (ret)

        Details::

            system_obj = system()
            system_obj.set_security_set_level(sec_set_level)
            if sec_set_level is not None:
                system_obj.set_security_set_level(sec_set_level)

            result = _set_security_set_level(session, system_obj)

        * inputs:
            :param session: session returned by login.
            :param sec_get_level: snmp SET security level

        * outputs:
            :rtype: dictionary of return status matching rest response

    * Status of the modified snmpv1 flag enabled

.. function:: system_obj.set_snmpv1_enabled(snmpv1_enabled)

    * Configures snmpv1 flag enabled

        Example usage of the method::

            ret = system_obj.set_snmpv1_enabled()
            print (ret)

        Details::

            system_obj = system()
            system_obj.set_snmpv1_enabled(snmpv1_enabled)
            if snmpv1_enabled is not None:
                system_obj.set_snmpv1_enabled(snmpv1_enabled)

            result = _set_snmpv1_enabled(session, system_obj)

        * inputs:
            :param session: session returned by login.
            :param snmpv1_enabled: snmpv1 flag enabled.

        * outputs:
            :rtype: dictionary of return status matching rest response

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_snmp import system


def _set_snmp_system(session, restobject):
    return restobject.patch(session)


def _set_system_description(session, description):
    system_obj = system()
    if description is not None:
        system_obj.set_description(description)
    result = _set_snmp_system(session, system_obj)
    return result


def _set_system_location(session, location):
    system_obj = system()
    if location is not None:
        system_obj.set_location(location)
    result = _set_snmp_system(session, system_obj)
    return result


def _set_system_contact(session, contact):
    system_obj = system()
    if contact is not None:
        system_obj.set_contact(contact)
    result = _set_snmp_system(session, system_obj)
    return result


def _set_informs_enabled(session, informs_enabled):
    system_obj = system()
    if informs_enabled is not None:
        system_obj.set_informs_enabled(informs_enabled)
    result = _set_snmp_system(session, system_obj)
    return result


def _set_encrypt_enabled(session, encrypt_enabled):
    system_obj = system()
    if encrypt_enabled is not None:
        system_obj.set_encryption_enabled(encrypt_enabled)
    result = _set_snmp_system(session, system_obj)
    return result


def _set_audit_interval(session, audit_interval):
    system_obj = system()
    if audit_interval is not None:
        system_obj.set_audit_interval(audit_interval)
    result = _set_snmp_system(session, system_obj)
    return result


def _set_default_control(session, default_contrl):
    system_obj = system()
    if default_contrl is not None:
        system_obj.set_default_config_default_control(default_contrl)
    result = _set_snmp_system(session, system_obj)
    return result


def _set_security_get_level(session, sec_get_level):
    system_obj = system()
    if sec_get_level is not None:
        system_obj.set_security_get_level(sec_get_level)
    result = _set_snmp_system(session, system_obj)
    return result


def _set_security_set_level(session, sec_set_level):
    system_obj = system()
    if sec_set_level is not None:
        system_obj.set_security_set_level(sec_set_level)
    result = _set_snmp_system(session, system_obj)
    return result


def _set_snmpv1_enabled(session, snmpv1_enabled):
    system_obj = system()
    if snmpv1_enabled is not None:
        system_obj.set_snmpv1_enabled(snmpv1_enabled)
    result = _set_snmp_system(session, system_obj)
    return result


def validate(system_obj):
    if (system_obj.peek_description() is None and
            system_obj.peek_location() is None and
            system_obj.peek_contact() is None and
            system_obj.peek_informs_enabled() is None and
            system_obj.peek_encryption_enabled() is None and
            system_obj.peek_audit_interval() is None and
            system_obj.peek_security_get_level() is None and
            system_obj.peek_security_set_level() is None and
            system_obj.peek_snmpv1_enabled() is None):
        return 1
    return 0


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['description', 'location', 'contact', 'informs_enabled',
               'encryption_enabled', 'audit_interval',
               'default_config_default_control', 'security_get_level',
               'security_set_level', 'snmpv1_enabled']

    inputs = brcd_util.parse(argv, system, filters, validate)

    session = brcd_util.getsession(inputs)

    result = _set_snmp_system(inputs['session'], inputs['utilobject'])
    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
