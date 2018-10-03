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

:mod:`seccertmgmt_action` - PyFOS util to modify Certificates
***************************************************************************************
The :mod:`seccertmgmt_action` provides options to modify certificates.

This module is a standalone script that can be used to import or export csr,
ca-client, ca-server) and supported certificates.

* inputs:

| Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch.
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

| Util scripts options:

  |    --certificate-entity=ENTITY-NAME         Certificate entity name
  |    --certificate-type=CERT-TYPE             Certificate type name
  |    --certificate-name=CERTNAME              Certificate Name
  |    --ca-certificate-name=CACERTNAME         CA certificate Name
  |    --seccertmgmt-operation=OPERATION    	seccertmgmt operation
  |    --protocol=PROTOCOL		Connection protocol
  |    --remote-host-ip=IP              Remote host ip address
  |    --remote-host-directory=DIR      Remote host directory
  |    --remote-login-user=LOGINUSER    Remote Login User
  |    --remote-login-password=PASSWORD Remote Login base64 encrypted password

* outputs:

    * Status of the seccertmgmt modify operation

.. function:: seccertmgmt_modify.export_import_cert(session, action, \
certificate-entity, certificate-type, certificate-name, ca-certificate-name, \
protocol, remote_ip, remote_dir, login_name, login_password)

    * Import a specified certificate from remote server to switch

        Example usage of the method::

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

        * inputs:
            :param session: session returned by login.
            :param cert-entity: certificate entity.
            :param cert-type: certificate type.
            :param cert-name: certificate name.
            :param ca-cert-name: CA certificate name.
            :param protocol: connection protocol.
            :param remote-host-ip: remote host ip address.
            :param remote-host-directoy: location in remote host.
            :param remote-login-user: user name of the remote host
            :param remote-login-password: password of the remote host

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Imports a specified certificate from a remote server to the switch.
        2. Exports certificate from switch to a remote server.
"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_security import security_certificate_action
import pyfos.utils.brcd_util as brcd_util


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


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = ['certificate_entity', 'certificate_type', 'operation',
               'certificate_name', 'remote_host_ip', 'remote_directory',
               'protocol', 'remote_user_name', 'remote_user_password']

    inputs = brcd_util.parse(argv, security_certificate_action, filters)

    seccertmgmt_obj = inputs['utilobject']

    # using variables instead of calling functions as the
    # function names are lengthy and difficult to fit the
    # the line length less than 80 chars for flake8.

    if (seccertmgmt_obj.peek_certificate_entity() is None or
       seccertmgmt_obj.peek_certificate_type() is None):
        print("Missing input(s)")
        print(inputs['utilusage'])
        sys.exit()

    session = brcd_util.getsession(inputs)

    result = _export_import_cert(inputs['session'], inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
        main(sys.argv[1:])
