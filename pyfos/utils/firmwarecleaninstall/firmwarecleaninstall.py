#!/usr/bin/env python3

# Copyright © 2018 Broadcom. All Rights Reserved. The term “Broadcom” refers to
# Broadcom Inc. and/or its subsidiaries.
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

:mod:`firmwarecleaninstall` - PyFOS util to trigger the firmwarecleaninstall operation.
*******************************************************************************\
****************************
The :mod:`firmwarecleaninstall` util is used to execute the firmwarecleaninstall operation.

This module is a stand-alone script and API that can be used to execute the \
firmwarecleaninstall operation.

* Input:

| Infrastructure Options:

  | -i,--ipaddr=IPADDR: The IP address of the FOS switch.
  | -L,--login=LOGIN: The login name.
  | -P,--password=PASSWORD: The password.
  | -f,--vfid=VFID: The VFID to which the request is directed [OPTIONAL].
  | -s,--secured=MODE: The HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose: Verbose mode [OPTIONAL].

| Util Script Options:

  |    --hostname=REMOTE-SERVER: Sets the remote server IP address or \
                             domain-name.
  |    --username=USER-NAME: Sets the user name of the remote server.
  |    --userpassword=PASSWORD: Sets the remote user password in base64 \
                                format. Use "" for empty password for \
                                anonymous ftp.
  |    --filename=PATH: Sets the remote directory path to firmware location.
  |    --protocol=PROTOCOL: Sets the protocol (ftp|scp|sftp) used for the \
  |    --acceptEULA: Indicates acceptance of BSN EULA.
  |    --displayEULA: Display BSN EULA.

* Output:

    * Status of the supportsave operation.

"""

import sys
import getpass
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_operation_show_status import show_status
from pyfos.pyfos_brocade_operation_firmwarecleaninstall import firmwarecleaninstall
from pyfos import pyfos_util
from pyfos.utils import brcd_util

def usage():
    print("  Util Script Options:")
    print()
    print("    --hostname=REMOTE-SERVER     Sets the remote server IP address or")
    print("                                 domain-name.")
    print("    --username=USER-NAME         Sets the user name of the remote server.")
    print("    --userpassword=PASSWORD      Sets the remote user password in base64 format.")
    print("                                 Use \"\" for empty password for anonymous ftp.")
    print("    --filename=PATH              Sets the remote directory path to firmware")
    print("                                 location.")
    print("    --protocol=PROTOCOL          Sets the protocol (ftp|scp|sftp) used for the")
    print("                                 remote server connection.")
    print("    --acceptEULA                 Indicates acceptance of BSN EULA")
    print("    --displayEULA                Display BSN EULA")
    print()


def main(argv):
    valid_options = ["hostname", "username", "userpassword", "filename", "protocol", "acceptEULA", "displayEULA"]
    inputs = brcd_util.generic_input(argv, usage, valid_options)

    session = pyfos_auth.login(inputs["login"], inputs["password"],
                               inputs["ipaddr"], inputs["secured"],
                               verbose=inputs["verbose"])
    if pyfos_auth.is_failed_login(session):
        print("login failed because",
              session.get(pyfos_auth.CREDENTIAL_KEY)[pyfos_auth.LOGIN_ERROR_KEY])
        brcd_util.full_usage(usage, valid_options)
        sys.exit()

    brcd_util.exit_register(session)

    fci = firmwarecleaninstall()

    if "protocol" not in inputs:
        print("Missing protocol")
        usage()
        pyfos_auth.logout(session)
        sys.exit()
    else:
        fci.set_protocol(inputs["protocol"])

    if "hostname" not in inputs:
        print("Missing hostname")
        usage()
        pyfos_auth.logout(session)
        sys.exit()
    else:
        fci.set_host(inputs["hostname"])

    if "username" not in inputs:
        print("Missing username")
        usage()
        pyfos_auth.logout(session)
        sys.exit()
    else:
        fci.set_user_name(inputs["username"])

    if "userpassword" not in inputs:
        password = getpass.getpass()
        fci.set_password(password)
    else:
        fci.set_password(inputs["userpassword"])

    if "filename" not in inputs:
        print("Missing filename")
        usage()
        pyfos_auth.logout(session)
        sys.exit()
    else:
        fci.set_remote_directory(inputs["filename"])

    if "acceptEULA" in inputs or "displayEULA" in inputs:
        if "acceptEULA" in inputs:
            fci.set_eula_action("accept-eula")
        else:
            fci.set_eula_action("display-eula")
    else:
        fci.set_eula_action("decline_eula")

    fci_rsp_obj = fci.post(session)
    if ("info-message" in fci_rsp_obj and
       fci_rsp_obj["info-message"] ==
       "Switch version is lower than the object"):
        pyfos_util.response_print(fci_rsp_obj)
        pyfos_auth.logout(session)
        sys.exit()
    if pyfos_util.is_failed_resp(fci_rsp_obj):
        print("Firmwarecleaninstall operation failed.\n")
        pyfos_util.response_print(fci_rsp_obj)
        pyfos_auth.logout(session)
    else:
        pyfos_util.response_print(fci_rsp_obj)
        # will not log out if success since the switch is rebooting


if __name__ == "__main__":
    main(sys.argv[1:])
