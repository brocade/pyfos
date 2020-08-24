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

:mod:`seccertmgmt_delete` - PyFOS util for deleting certificates on a switch.
***********************************************************************************
The :mod:`seccertmgmt_delete` provides the option to delete a certificate.

This module can be used to delete a certificate.

* Input:

| Infrastructure Options:

|   -i,--ipaddr=IPADDR     The IP address of the FOS switch.
|   -L,--login=LOGIN       The login name.
|   -P,--password=PASSWORD The password.
|   -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           The Verbose mode [OPTIONAL].

* Util Script Options:

   |    --certificate-entity=ENTITY-NAME     Sets the certificate entity name.
   |    --certificate-type=CERT-TYPE         Sets the certificate type.
   |    --keypair-tag=KEYPAIR-TAG            Sets the  keypair-tag.

* Output:
    * The certificate.

.. function:: seccertmgmt_delete.delete_security_certificate(session)

    * Deletes a certificate in the switch.

        Example Usage of the Method:

            ret = seccertmgmt_delete.delete_security_certificate( \
session, cert_entity, cert_type)
            print (ret)

        Details::

            result = seccertmgmt_delete.delete_security_certificate(
              session, \'cert\', \'https\')

        * Input:
            :param session: The session returned by the login.
            :param cert_entity: The associated certificate entity \
                                (commoncert/https/syslog/ldap/radius).
            :param cert_type: The associated certificate type \
                                (ca-client/ca-server/csr/cert).

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Delete a specified certificate.


"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_security import security_certificate_action
from pyfos.utils import brcd_util


def _delete_cert(session, restobject):
    return restobject.delete(session)


def delete_security_certificate(session, cert_entity, cert_type):
    seccertmgmt_obj = security_certificate_action()
    seccertmgmt_obj.set_certificate_entity(cert_entity)
    seccertmgmt_obj.set_certificate_type(cert_type)

    result = _delete_cert(session, seccertmgmt_obj)
    return result


def main(argv):
    # Print arguments
    # print(sys.argv[1:])

    filters = ['certificate_entity', 'certificate_type', 'keypair_tag',
               'certificate_name']

    inputs = brcd_util.parse(argv, security_certificate_action, filters)

    seccertmgmt_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    if (seccertmgmt_obj.peek_certificate_entity() is None or
            seccertmgmt_obj.peek_certificate_type() is None):
        print("Missing input(s)")
        print(inputs['utilusage'])
        sys.exit()

    result = _delete_cert(inputs['session'], inputs['utilobject'])

    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
