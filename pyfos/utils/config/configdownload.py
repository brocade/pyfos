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

:mod:`configdownload` - PyFOS util to trigger the configdownload operation.
*******************************************************************************\
****************************
The :mod:`configdownload` util is used to execute the configdownload operation.

This module is a stand-alone script and API that can be used to execute the \
configdownload operation.

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
  |    --userpassword=PASSWORD: Sets the remote user password in base64 format.
  |    --filename=PATH: Sets the remote directory path to configdownload location.
  |    --protocol=PROTOCOL: Sets the protocol (ftp|scp|sftp) used for the \
                            remote server connection.
  |    --type=TYPE: Sets the download type to all, vf, fid or map.

* Output:

    * Status of the supportsave operation.

"""

import sys
import getpass
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_operation_show_status import show_status
from pyfos.pyfos_brocade_operation_config import config
from pyfos import pyfos_util
from pyfos.utils import brcd_util

def usage():
    print("  Util Script Options:")
    print()
    print("    --hostname=REMOTE-SERVER     Sets the remote server IP address or")
    print("                                 domain-name.")
    print("    --username=USER-NAME         Sets the user name of the remote server.")
    print("    --userpassword=PASSWORD      Sets the remote user password in base64 format.")
    print("    --filename=PATH              Sets the remote directory path to config")
    print("                                 location.")
    print("    --protocol=PROTOCOL          Sets the protocol (ftp|scp|sftp) used for the")
    print("                                 remote server connection.")
    print("    --type=TYPE                  Sets the download type to all, vf, fid, or map.")
    print("                                 map/fid option requires logical switch number in")
    print("                                 the form of fid=<logical switch number>")
    print("                                 or map=<logical switch number>")
    print()


def main(argv):
    valid_options = ["hostname", "username", "userpassword", "filename", "protocol", "type"]
    inputs = brcd_util.generic_input(argv, usage, valid_options, sessionless=False)

    if 'vfid' in inputs:
        print("-f/--vfid is a no-op for config operations. Please remove.")
        usage()
        sys.exit()

    session = pyfos_auth.login(inputs["login"], inputs["password"],
                               inputs["ipaddr"], inputs["secured"],
                               verbose=inputs["verbose"])
    if pyfos_auth.is_failed_login(session):
        print("login failed because",
              session.get(pyfos_auth.CREDENTIAL_KEY)[pyfos_auth.LOGIN_ERROR_KEY])
        brcd_util.full_usage(usage, valid_options, sessionless=False)
        sys.exit()

    brcd_util.exit_register(session)

    cobj = config()

    if "protocol" not in inputs:
        print("Missing protocol")
        usage()
        pyfos_auth.logout(session)
        sys.exit()
    else:
        cobj.set_protocol(inputs["protocol"])

    if "hostname" not in inputs:
        print("Missing hostname")
        usage()
        pyfos_auth.logout(session)
        sys.exit()
    else:
        cobj.set_host(inputs["hostname"])

    if "username" not in inputs:
        print("Missing username")
        usage()
        pyfos_auth.logout(session)
        sys.exit()
    else:
        cobj.set_user_name(inputs["username"])

    if "userpassword" not in inputs:
        password = getpass.getpass()
        cobj.set_password(password)
    else:
        cobj.set_password(inputs["userpassword"])

    if "filename" not in inputs:
        print("Missing filename")
        usage()
        pyfos_auth.logout(session)
        sys.exit()
    else:
        cobj.set_path(inputs["filename"])

    if "type" not in inputs or ("type" in inputs and inputs["type"] != "all" and inputs["type"] != "vf" and "fid" not in inputs["type"] and "map" not in inputs["type"]):
        print("Missing type")
        usage()
        pyfos_auth.logout(session)
        sys.exit()
    else:
        cobj.set_type(inputs["type"])


    cobj.set_upload(False)
    
    config_rsp_obj = cobj.post(session)
    if ("info-message" in config_rsp_obj and
       config_rsp_obj["info-message"] ==
       "Switch version is lower than the object"):
        pyfos_util.response_print(config_rsp_obj)
        pyfos_auth.logout(session)
        sys.exit()
    if pyfos_util.is_failed_resp(config_rsp_obj):
        print("configdownload operation failed.\n")
        pyfos_util.response_print(config_rsp_obj)
        pyfos_auth.logout(session)
    else:
        pyfos_util.response_print(config_rsp_obj)
        # will not log out if success since the switch is rebooting


if __name__ == "__main__":
    main(sys.argv[1:])
