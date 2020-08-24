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

:mod:`seccertmgmt_extension_show` - PyFOS util to show Extension certificates.
***********************************************************************************
The :mod:`seccertmgmt_extension_show` util to display Extension certificates.

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

  |    --certificate-entity=ENTITY-NAME   Sets the certificate entity name.
  |    --local-certificate=[true|false]   Get local or remote certificate.
  |    --certificate-name=[CERTIFICATE-NAME] Get certificate by name.
  |    --keypair-tag=[KEYPAIR-TAG]  Get certificate by keypair-tag.

* Output:
    * The certificate information.

.. function:: seccertmgmt_show.show_system_security_seccertmgmt(session)

    * Displays the certificate and its information in the switch.

        Example Usage of the Method:

            ret = seccertmgmt_show.show_extension_security_certificate(\
session, cert_entity, cert_type)
            print (ret)

        Details::

            result = seccertmgmt_extension_show.extension_security_certificate(
              session, \'cert\')

        * Input:
            :param session: The session returned by the login..
            :param cert_name: The associated certificate name.
            :param keypair-tag: The associated keypair-tag.
            :param cert_entity: The associated certificate entity.
            :param local-certificate: The local/remote certificate.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Retrieve the certificate-related information.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_security import security_certificate_extension
from pyfos.utils import brcd_util


def _show_cert(session, restobject):
    objlist = security_certificate_extension.get(session)
    certificatelist = []
    if isinstance(objlist, security_certificate_extension):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if not isinstance(objlist[i], security_certificate_extension):
                continue
            if restobject.peek_certificate_entity() is not None\
               and restobject.peek_certificate_entity() !=\
               objlist[i].peek_certificate_entity():
                continue
            if restobject.peek_local_certificate() is not None\
               and restobject.peek_local_certificate() !=\
               objlist[i].peek_local_certificate():
                continue
            if restobject.peek_keypair_tag() is not None\
               and restobject.peek_keypair_tag() !=\
               objlist[i].peek_keypair_tag():
                continue
            if restobject.peek_certificate_name() is not None\
               and restobject.peek_certificate_name() !=\
               objlist[i].peek_certificate_name():
                continue
            certificatelist.append(objlist[i])
    else:
        print(objlist)
    return certificatelist


def extension_security_certificate(session, certname=None, keypair=None,
                                   cert_entity=None, local=None):
    seccertmgmt_obj = security_certificate_extension()
    seccertmgmt_obj.set_certificate_entity(cert_entity)
    seccertmgmt_obj.set_certificate_name(certname)
    seccertmgmt_obj.set_keypair_tag(keypair)
    seccertmgmt_obj.set_local(local)

    result = _show_cert(session, seccertmgmt_obj)
    return result


def main(argv):
    # Print arguments
    # print(sys.argv[1:])

    filters = ['certificate_entity', 'local_certificate', 'keypair_tag',
               'certificate_name']

    inputs = brcd_util.parse(argv, security_certificate_extension, filters)

    session = brcd_util.getsession(inputs)

    result = _show_cert(inputs['session'], inputs['utilobject'])

    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
