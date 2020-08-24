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

:mod:`supportsave` - PyFOS util to trigger the supportsave operation.
*******************************************************************************
The :mod:`supportsave` util is used to execute the supportsave operation.

This module is a stand-alone script and API that can be used to execute the \
supportsave operation. Supportsave collects all log files from the switch
and copies them to the remote server.

* Input:

| Infrastructure Options:

  | -i,--ipaddr=IPADDR: The IP address of the FOS switch.
  | -L,--login=LOGIN: The login name.
  | -P,--password=PASSWORD: The password.
  | -f,--vfid=VFID: The VFID to which the request is directed [OPTIONAL].
  | -s,--secured=MODE: The HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose: Verbose mode [OPTIONAL].

| Util Script Options:

  |    --host=REMOTE-SERVER: Sets the remote server IP address or \
                             domain-name.
  |    --user=USER-NAME: Sets the user name of the remote server.
  |    --passwd=PASSWORD: Sets the remote user password in base64 format.
  |    --path=PATH:  Sets the remote directory path to copy the \
                     supportsave files.
  |    --protocol=PROTOCOL: Sets the protocol (ftp|scp|sftp) used for the \
                            remote server connection.
  |    --port=PORT: User defined port number can be configured for scp/sftp\
                   protocol
  |    --serial-mode=SERIAL-MODE: Legacy serial-mode module supportsave\
      collection. true  : Supportsave process will be done serialize module\
      by module. false : Supportsave process will be done in parallel for\
      multiple modules.

* Output:

    * Status of the supportsave operation.

.. function:: _post_supportsave(session, ssObj)

    *Supportsave Operation*

        Example Usage of the Method::

            status = supportsave(session, ssObj)

        Details::

            ss_dict = {
                "host": host,
                "user-name": user,
                "password": password,
                "remote-directory": path,
                "protocol": protocol,
            }
            ss_obj = supportsave()
            ss_obj.load(ss_dict, 1)
            result = ss_obj.post(session)

        * Input:
            :param session: The session returned by the login.
            :param remote-directory: The remote server directory.
            :param host: The remote server.
            :param user: The remote server user.
            :param password: The remote server password.
            :param protocol: The remote server connection.
            :param port: User defined port number can be configured only for\
              scp/sftp protocol
            :param serial_mode: Legacy serial-mode module supportsave\
              collection. true  : Supportsave process will be done serialize\
              module by module. false : Supportsave process will be done in\
              parallel for multiple modules.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

         Trigger supportsave and retrieve the status.

"""

import sys
from time import sleep
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_operation_show_status import show_status
from pyfos.pyfos_brocade_operation_supportsave import supportsave
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def _post_supportsave(session, ss):
    return ss.post(session)


def _get_supportsave_status(session, ss_req_obj, ss_rsp_obj):
    status = show_status(ss_rsp_obj)
    ss_state = status.peek_status()

    sleep(5)
    print("\r\n")

    while ("in-progress" in ss_state or "queued" in ss_state or
            "done" in ss_state):
        resp = _post_supportsave(session, ss_req_obj)
        if pyfos_util.is_failed_resp(resp):
            ss_state = "failed"
        else:
            status = show_status(resp)
            ss_state = status.peek_status()
            percentage = status.peek_percentage_complete()

        print("Supportsave status: " + ss_state +
              " Completion percentage: " +
              str(percentage) + "       ", end='\r', flush=True)

        sleep(5)

    print("\r\n")
    if ss_state == "failed":
        pyfos_util.response_print(resp)


def ss_show_status(session, ssObj):

    ss_obj = show_status(ssObj)
    ss_id = ss_obj.peek_message_id()
    status_obj = {"show-status": {"message-id": ss_id}}
    ss_req_obj = show_status(status_obj)
    ss_rsp_obj = _post_supportsave(session, ss_req_obj)
    if pyfos_util.is_failed_resp(ss_rsp_obj):
        print("Supportsave operation failed.\n")
        pyfos_util.response_print(ss_rsp_obj)
        return
    _get_supportsave_status(session, ss_req_obj, ss_rsp_obj)
    return


def ss_validate(ss_obj):
    if (ss_obj.peek_user_name() is None or
            ss_obj.peek_remote_directory() is None or
            ss_obj.peek_password() is None or ss_obj.peek_protocol() is None or
            ss_obj.peek_host() is None):
        return 1
    return 0


def main(argv):
    filters = ['host', 'user_name',
               'password', 'remote_directory', 'port', 'serial_mode',
               'protocol']
    inputs = brcd_util.parse(argv, supportsave, filters, ss_validate)
    ss_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)
    ss_rsp_obj = _post_supportsave(session, ss_obj)
    if ("info-message" in ss_rsp_obj and
       ss_rsp_obj["info-message"] ==
       "Switch version is lower than the object"):
        pyfos_util.response_print(ss_rsp_obj)
        pyfos_auth.logout(session)
        sys.exit()
    if pyfos_util.is_failed_resp(ss_rsp_obj):
        print("Supportsave operation failed.\n")
        pyfos_util.response_print(ss_rsp_obj)
    else:
        ss_show_status(session, ss_rsp_obj)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
