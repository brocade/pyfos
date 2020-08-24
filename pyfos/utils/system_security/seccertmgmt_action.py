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

:mod:`seccertmgmt_action` - PyFOS util to modify certificates.
***************************************************************************************
The :mod:`seccertmgmt_action` util provides options to modify certificates.

This module is a stand-alone script that can be used to import or export CSR,
CA-Client, CA-Server, and supported certificates.

* Input:

| Infrastructure Options:

|   -i,--ipaddr=IPADDR     The IP address of the FOS switch.
|   -L,--login=LOGIN       The login name.
|   -P,--password=PASSWORD The password.
|   -f,--vfid=VFID         The VFID to which the request \
                            is directed [OPTIONAL].
|   -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           Verbose mode [OPTIONAL].

* Util Script Options:

  |    --certificate-entity=ENTITY-NAME    Sets the certificate entity name.
  |    --certificate-type=CERT-TYPE        Sets the certificate type name.
  |    --ca-certificate=CACERT             Sets the CA certificate for import.
  |    --certificate-name=CERTNAME         Sets the certificate name.
  |    --ca-certificate-name=CACERTNAME    Sets the CA certificate name.
  |    --seccertmgmt-operation=OPERATION   Sets the seccertmgmt operation.
  |    --protocol=PROTOCOL		   Sets the connection protocol.
  |    --remote-host-ip=IP                 Sets the remote host IP address.
  |    --remote-host-directory=DIR         Sets the remote host directory.
  |    --remote-login-user=LOGINUSER       Sets the remote login user.
  |    --remote-login-password=PASSWORD    Sets the remote login base64 \
                                           encrypted password.
  |    --keypair-tag=KEYPAIR               Sets the keypair-tag for associated\
                                           certificate.

* Output:

    * The status of the seccertmgmt modify operation.

.. function:: seccertmgmt_modify.export_import_cert(session, action, \
certificate-entity, certificate-type, certificate-name, ca-certificate-name, \
protocol, remote_ip, remote_dir, login_name, login_password, keypiar-tag, \
ca-certificate)

    * Imports a specified certificate from a remote server to a switch.

        Example Usage of the Method::

            ret = seccertmgmt_modify.export_import_cert(session, OPERATION,\
ENTITY-NAME, CERT-TYPE, CERTNAME, CACERTNAME, PROTOCOL, IP, DIR, LOGINUSER,\
PASSWORD)
            print (ret)

        Details::

            class SECCERTMGMT:
                CERTNAME = cert.pem
                IP = 10.70.4.109
                DIR = /root/ca
                LOGINUSER = root
                PASSWORD = pray4green

            seccertmgmt_obj = seccertmgmt()
            seccertmgmt_obj.export_import_cert(session, action, cert_entity,\
cert_type, cert_name, ca_cert_name, protocol, remote_ip, remote_dir,\
login_name, login_password)
            result = seccertmgmt_obj.patch(session)

        * Input:
            :param session: The session returned by the login.
            :param cert-entity: The certificate entity.
            :param cert-type: The certificate type.
            :param cert-name: The certificate name.
            :param ca-cert-name: The CA certificate name.
            :param protocol: The connection protocol.
            :param remote-host-ip: The remote host IP address.
            :param remote-host-directoy: The location in the remote host.
            :param remote-login-user: The user name of the remote host.
            :param remote-login-password: The password of the remote host.
            :param ca-certificate: The CA who signed the Extension certificate.
            :param keypair-tag: The keypair-tag associated with certificate.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

        1. Import a specified certificate from a remote server to the switch.
        2. Export a certificate from a switch to a remote server.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_security import security_certificate_action
from pyfos.utils import brcd_util


def _export_import_cert(session, restobject):
    return restobject.patch(session)


def export_import_cert(session, action, cert_entity, cert_type, cert_name,
                       ca_cert_name, protocol, remote_ip, remote_dir,
                       login_name, login_password):
    seccertmgmt_obj = security_certificate_action()
    seccertmgmt_obj.set_seccertmgmt_action(action)
    seccertmgmt_obj.set_certificate_entity(cert_entity)
    seccertmgmt_obj.set_certificate_type(cert_type)
    seccertmgmt_obj.set_certificate_name(cert_name)
    seccertmgmt_obj.set_ca_certificate_name(ca_cert_name)
    seccertmgmt_obj.set_protocol(protocol)
    seccertmgmt_obj.set_remote_host_ip(remote_ip)
    seccertmgmt_obj.set_remote_dir(remote_dir)
    seccertmgmt_obj.set_remote_user_name(login_name)
    seccertmgmt_obj.set_remote_user_password(login_password)

    result = _export_import_cert(session, seccertmgmt_obj)
    return result


def validate(seccertmgmt_obj):
    if (seccertmgmt_obj.peek_certificate_entity() is None or
            seccertmgmt_obj.peek_certificate_type() is None):
        print("Missing input(s)")
        return 1
    if (seccertmgmt_obj.peek_certificate_type() != "extension" and
            seccertmgmt_obj.peek_ca_certificate() is not None):
        print("Additional input(s): \"CA certificate\" is provided for" +
              "non Extension certificate.")
        return 1
    return 0


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['certificate_entity', 'certificate_type', 'operation',
               'certificate_name', 'remote_host_ip', 'remote_directory',
               'protocol', 'remote_user_name', 'remote_user_password',
               'ca_certificate', 'keypair_tag']

    inputs = brcd_util.parse(argv, security_certificate_action, filters,
                             validate)

    seccertmgmt_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)

    result = _export_import_cert(inputs['session'], seccertmgmt_obj)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
