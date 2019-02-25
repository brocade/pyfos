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

:mod:`seccertmgmt_show` - PyFOS util for displaying certificates in the switch.
***********************************************************************************
The :mod:`seccertmgmt_show` util provides the option to display a certificate.

This module can be used to display a certificate. If the certificate entity \
and type are not provided, information for all certificates is displayed.

* Input:

| Infrastructure Options:

|   -i,--ipaddr=IPADDR     The IP address of the FOS switch.
|   -L,--login=LOGIN       The login name.
|   -P,--password=PASSWORD The password.
|   -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           Verbose mode [OPTIONAL].

* Util Script Options:

  |    --certificate-entity=ENTITY-NAME    Sets the certificate entity name.
  |    --certificate-type=CERT-TYPE        Sets the certificate type.
  |    --is-hexdump-show                   Displays the raw hex data.

* Output:
    * The certificate information.

.. function:: seccertmgmt_show.show_system_security_seccertmgmt(session)

    * Displays the certificate and its information in the switch.

        Example Usage of the Method:

            ret = seccertmgmt_show.show_system_security_seccertmgmt(session, \
cert_entity, cert_type)
            print (ret)

        Details::

            result = seccertmgmt_show.show_system_security_seccertmgmt(
              session, \'cert\', \'https\')

        * Input:
            :param session: The session returned by the login.
            :param cert_entity: The associated certificate entity.
            :param cert_type: The associated certificate type.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Retrieve the certificate-related information.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_security import security_certificate
from pyfos.utils import brcd_util


def _show_cert(session, restobject):
    return restobject.get(session)


def show_security_certificate(session, cert_entity, cert_type):
    seccertmgmt_obj = security_certificate()
    seccertmgmt_obj.set_certificate_entity(cert_entity)
    seccertmgmt_obj.set_certificate_entity(cert_type)

    result = _show_cert(session, seccertmgmt_obj)
    return result


def main(argv):
    # Print arguments
    # print(sys.argv[1:])

    filters = ['certificate_entity', 'certificate_type']

    inputs = brcd_util.parse(argv, security_certificate, filters)

    session = brcd_util.getsession(inputs)

    result = _show_cert(inputs['session'], inputs['utilobject'])

    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
