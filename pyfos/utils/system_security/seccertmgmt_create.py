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

:mod:`seccertmgmt_create` - PyFOS util for generating certificates on a switch
***********************************************************************************
The :mod:`seccertmgmt_create` provides option to generate certificate

This module can be used to create/generate certificate for a specified entity
and type

* Input:

| Infrastructure Options:

|   -i,--ipaddr=IPADDR     The IP address of the FOS switch.
|   -L,--login=LOGIN       The login name.
|   -P,--password=PASSWORD The password.
|   -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           Verbose mode [OPTIONAL].

* Util Script Options:

   |   --certificate-entity=ENTITY-NAME    Sets the certificate entity name.
   |   --certificate-type=CERT-TYPE        Sets the certificate type name.
   |   --key-size=VALUE                    Sets the key size.
   |   --country-name=VALUE                Sets the country name.
   |   --state-name=VALUE                  Sets the state name.
   |   --unit-name=VALUE                   Sets the unit name.
   |   --hash-type=VALUE                   Sets the hash type.
   |   --algorithm-type=VALUE              Sets the algorithm type.
   |   --organization-name=VALUE           Sets the organization name.
   |   --years=VALUE                       Sets the certificate validity.
   |   --domain-name=VALUE                 Sets the domain name.
   |   --locality-name=VALUE               Sets the locality name.

* Output:
    * The certificate created.

.. function:: seccertmgmt_create.create_security_certificate(session)

    * Generate a certificate in the switch.

        Example Usage of the Method:

            ret = seccertmgmt_create.create_security_certificate(session, \
cert_entity, cert_type)
            print (ret)

        Details::

            result = seccertmgmt_create.create_system_security_seccertmgmt(
              session, \'cert\', \'https\')

        * Input:
            :param session: THe session returned by the login.
            :param cert_entity: The associated certificate entity \
                                (ca-client/ca-server/cert/csr).
            :param cert_type: The associated certificate type \
                              (commoncert/https/syslog/ldap/radius).

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        * Use Cases*

        1. Generate the specified certificate.


"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_security import security_certificate_generate
from pyfos.utils import brcd_util


def _create_cert(session, restobject):
    return restobject.post(session)


def create_security_certificate(session, cert_entity, cert_type, algo_type,
                                key_size, hash_type, years, country_name,
                                state_name, locality_name, organization_name,
                                unit_name, domain_name):
    seccertmgmt_obj = security_certificate_generate()
    seccertmgmt_obj.set_certificate_entity(cert_entity)
    seccertmgmt_obj.set_certificate_type(cert_type)
    seccertmgmt_obj.set_algorithm_type(algo_type)
    seccertmgmt_obj.set_key_size(key_size)
    seccertmgmt_obj.set_hash_type(hash_type)
    seccertmgmt_obj.set_years(years)
    seccertmgmt_obj.set_country_name(country_name)
    seccertmgmt_obj.set_state_name(state_name)
    seccertmgmt_obj.set_locality_name(locality_name)
    seccertmgmt_obj.set_organization_name(organization_name)
    seccertmgmt_obj.set_unit_name(unit_name)
    seccertmgmt_obj.set_domain_name(domain_name)

    result = _create_cert(session, seccertmgmt_obj)
    return result


def main(argv):
    # Print arguments
    # print(sys.argv[1:])

    filters = ['certificate_entity', 'certificate_type', 'algorithm_type',
               'key_size', 'hash_type', 'years', 'country_name', 'state_name',
               'locality_name', 'organization_name', 'unit_name',
               'domain_name']

    inputs = brcd_util.parse(argv, security_certificate_generate, filters)

    seccertmgmt_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    if (seccertmgmt_obj.peek_certificate_entity() is None or
            seccertmgmt_obj.peek_certificate_type() is None):
        print("Missing input(s)")
        print(inputs['utilusage'])
        sys.exit()

    if seccertmgmt_obj.peek_certificate_entity() == "csr":
        if (seccertmgmt_obj.peek_country_name() is None or
                seccertmgmt_obj.peek_state_name() is None or
                seccertmgmt_obj.peek_locality_name() is None or
                seccertmgmt_obj.peek_organization_name() is None or
                seccertmgmt_obj.peek_unit_name() is None):
            print("Missing input(s)")
            print(inputs['utilusage'])
            sys.exit()

    result = _create_cert(inputs['session'], inputs['utilobject'])

    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
