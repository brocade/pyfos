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

:mod:`firmwaredownload` - PyFOS util to trigger the firmwaredownload operation.
*******************************************************************************
The :mod:`firmwaredownload` util is used to execute the firmwaredownload \
operation.

This module is a stand-alone script and API that can be used to execute the \
firmwaredownload operation.

* Input:

| Infrastructure Options:

  | -i,--ipaddr=IPADDR: The IP address of the FOS switch.
  | -L,--login=LOGIN: The login name.
  | -P,--password=PASSWORD: The password.
  | -f,--vfid=VFID: The VFID to which the request is directed [OPTIONAL].
  | -s,--secured=MODE: The HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose: Verbose mode [OPTIONAL].
  | -a,--authtoken: AuthToken value string or AuthTokenManager config file \
                    [OPTIONAL].
  | -z,--nosession: Session less Authentication [OPTIONAL].
  |    --nocredential: No credential Authentication [OPTIONAL].

| Util Script Options:

  |    --hostname=REMOTE-SERVER: Sets the remote server IP address or \
                             domain-name.
  |    --username=USER-NAME: Sets the user name of the remote server.
  |    --userpassword=PASSWORD: Sets the remote user password in base64 \
                                format.
  |    --filename=PATH:  Sets the remote directory path to firmware location.
  |    --protocol=PROTOCOL: Sets the protocol (ftp|scp|sftp) used for the \
                            remote server connection.
  |    --stage: stage the firmare to secondary partition.
  |    --activate: activate firmware that has been staged.
  |    --acceptEULA: indicate acceptance of BSN EULA.
  |    --displayEULA: Display BSN EULA.

* Output:

    * Status of the firmwaredownload operation.

"""

import sys
import getpass
import errno
from socket import error as socket_error
from time import sleep
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_operation_show_status import show_status
from pyfos.pyfos_brocade_operation_firmwaredownload import firmwaredownload
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def usage():
    print("  Util Script Options:")
    print()
    print("    --hostname=REMOTE-SERVER     Sets the remote server IP address")
    print("                                 or domain-name.")
    print("    --username=USER-NAME         Sets the user name of the remote ")
    print("                                 server.")
    print("    --userpassword=PASSWORD      Sets the remote user password in ")
    print("                                 base64 format.")
    print("                                 Use \"\" for empty password for ")
    print("                                 anonymous ftp.")
    print("    --filename=PATH              Sets the remote directory path to")
    print("                                 firmware location.")
    print("    --protocol=PROTOCOL          Sets the protocol (ftp|scp|sftp) ")
    print("                                 used for the remote server ")
    print("                                 connection.")
    print("    --stage                      stage the firmare to secondary ")
    print("                                 partition.")
    print("    --activate                   activate firmware that has been ")
    print("                                 staged.")
    print("    --acceptEULA                 Indicates acceptance of BSN EULA.")
    print("    --displayEULA                Display BSN EULA.")
    print()


def _get_firmwaredownload_status(session, ss_req_obj, ss_rsp_obj):
    status = show_status(ss_rsp_obj)
    ss_state = status.peek_status()

    if ss_state == "error":
        pyfos_util.response_print(ss_rsp_obj)
        return

    sleep(10)
    print("\r\n")

    try:
        while ("in-progress" in ss_state or "queued" in ss_state or
                "done" in ss_state):
            resp = ss_req_obj.post(session)
            if pyfos_util.is_failed_resp(resp):
                ss_state = "error"
                print("\r\n")
                pyfos_util.response_print(resp)
                break
            else:
                status = show_status(resp)
                eula_text = status.peek_eula_text()

                if eula_text:
                    print("EULA: \n", eula_text)
                    break
                else:
                    pyfos_util.response_print(status)

            ss_state = status.peek_status()
            if ss_state == "done":
                # stage = true, reponse displayed above now return
                break
            sleep(10)

    except socket_error as serr:
        if serr.errno == errno.ECONNREFUSED:
            print("Switch is rebooting as part of firmwaredownload. Use showstatus \
script with message-id as 20000 to track the firmwaredownload \
status after switch reboots.\n")


def fd_show_status(session, fd_dict):
    print(fd_dict)
    status_obj = {"show-status": {"message-id": fd_dict["show-status"]
                  ["message-id"]}}
    ss_req_obj = show_status(status_obj)
    ss_rsp_obj = ss_req_obj.post(session)
    if pyfos_util.is_failed_resp(ss_rsp_obj):
        print("Firmwaredownload operation failed.\n")
        pyfos_util.response_print(ss_rsp_obj)
        return
    _get_firmwaredownload_status(session, ss_req_obj, ss_rsp_obj)
    return


def main(argv):
    valid_options = ["hostname", "username", "userpassword", "filename",
                     "protocol", "activate", "stage", "acceptEULA",
                     "displayEULA"]
    inputs = brcd_util.generic_input(argv, usage, valid_options)

    session = pyfos_auth.login(inputs["login"], inputs["password"],
                               inputs["ipaddr"], inputs["secured"],
                               verbose=inputs["verbose"])
    if pyfos_auth.is_failed_login(session):
        print("login failed because",
              session.get(pyfos_auth.CREDENTIAL_KEY)
              [pyfos_auth.LOGIN_ERROR_KEY])
        brcd_util.full_usage(usage, valid_options)
        sys.exit()

    brcd_util.exit_register(session)

    fd = firmwaredownload()

    if "protocol" not in inputs:
        print("Missing protocol")
        usage()
        pyfos_auth.logout(session)
        sys.exit()
    else:
        fd.set_protocol(inputs["protocol"])

    if "hostname" not in inputs:
        print("Missing hostname")
        usage()
        pyfos_auth.logout(session)
        sys.exit()
    else:
        fd.set_host(inputs["hostname"])

    if "username" not in inputs:
        print("Missing username")
        usage()
        pyfos_auth.logout(session)
        sys.exit()
    else:
        fd.set_user_name(inputs["username"])

    if "userpassword" not in inputs:
        password = getpass.getpass()
        fd.set_password(password)
    else:
        fd.set_password(inputs["userpassword"])

    if "filename" not in inputs:
        print("Missing filename")
        usage()
        pyfos_auth.logout(session)
        sys.exit()
    else:
        fd.set_remote_directory(inputs["filename"])

    if "activate" in inputs:
        fd.set_activate(inputs["activate"])

    if "stage" in inputs:
        fd.set_stage(inputs["stage"])

    if "acceptEULA" in inputs and "displayEULA" in inputs:
        print("Accept and Display are mutually exclusive\n")
        pyfos_auth.logout(session)
        sys.exit()
    elif "acceptEULA" in inputs or "displayEULA" in inputs:
        if "acceptEULA" in inputs:
            fd.set_eula_action(inputs["acceptEULA"])
        else:
            fd.set_eula_action(inputs["displayEULA"])
    else:
        fd.set_eula_action("decline-eula")

    fd_rsp_obj = fd.post(session)
    if ("info-message" in fd_rsp_obj and
       fd_rsp_obj["info-message"] ==
       "Switch version is lower than the object"):
        pyfos_util.response_print(fd_rsp_obj)
        pyfos_auth.logout(session)
        sys.exit()
    if pyfos_util.is_failed_resp(fd_rsp_obj):
        print("Firmwaredownload operation failed.\n")
        pyfos_util.response_print(fd_rsp_obj)
    else:
        fd_show_status(session, fd_rsp_obj)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
