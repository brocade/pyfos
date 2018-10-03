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

:mod:`seccertmgmt_show` - PyFOS util for displaying certificates in the switch
***********************************************************************************
The :mod:`seccertmgmt_show` provides option to display certificate

This module can be used to display certificate. If certificate entity and type
are not provided, all certificate list information will be displayed.

* inputs:

|  Infrastructure options:

  |   -i,--ipaddr=IPADDR     IP address of FOS switch
  |   -L,--login=LOGIN       login name.
  |   -P,--password=PASSWORD password.
  |   -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  |   -v,--verbose           verbose mode[OPTIONAL].

|  Util scripts options:

  |    --certificate-entity=ENTITY-NAME    Certificate entity name
  |    --certificate-type=CERT-TYPE        Certificate type name
  |    --is-hexdump-show                   Display raw hex data

* outputs:
    * Certificate information

.. function:: seccertmgmt_show.show_system_security_seccertmgmt(session)

    * Display the Certificate and its information in the switch.

        Example usage of the method:

            ret = seccertmgmt_show.show_system_security_seccertmgmt(session, \
cert_entity, cert_type)
            print (ret)

        Details::

            result = seccertmgmt_show.show_system_security_seccertmgmt(
              session, \'cert\', \'https\')

        * inputs:
            :param session: session returned by login.
            :param cert_entity: associated certificate entity
            :param cert_type: associated certificate type

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Retrieve the Certificate related information.
"""

import sys
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_brocade_security import security_certificate
import pyfos.utils.brcd_util as brcd_util


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
