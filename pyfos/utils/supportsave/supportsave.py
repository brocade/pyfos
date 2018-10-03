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

:mod:`supportsave` - PyFOS util to trigger supportsave operation
*******************************************************************************
The :mod:`supportsave` provides options to execute supportsave operation.

This module is a standalone script and API that can be used to execute
supportsave operation. Supportsave collects all the log files from the switch
and copies into the remote server.

* Inputs:

| Infrastructure options:

  | -i,--ipaddr=IPADDR: IP address of FOS switch
  | -L,--login=LOGIN: Login name
  | -P,--password=PASSWORD: Password
  | -f,--vfid=VFID: VFID to which the request is directed to [OPTIONAL]
  | -s,--secured=MODE: HTTPS mode "self" or "CA" [OPTIONAL]
  | -v,--verbose: Verbose mode[OPTIONAL]

| Util scripts options:

  |    --host=REMOTE-SERVER: Remote server ipaddress/domain-name
  |    --user=USER-NAME: User name of the remote server
  |    --passwd=PASSWORD: Remote user password
  |    --path=PATH:	Remote directory path to copy supportsave files
  |    --protocol=PROTOCOL: Protocol used for remote server connection

* Outputs:

    * Status of the supportsave operation

.. function:: _post_supportsave(session, ssObj)

    *Supportsave operation*

        Example usage of the method::

            status = supportsave(session, ssObj)

        Details::

            ss_dict = {
                "host": host,
                "user-name": user,
                "password": password,
                "remote-directory": path,
                "protocol" : protocol,
            }
            ss_obj = supportsave()
            ss_obj.load(ss_dict, 1)
            result = ss_obj.post(session)

        * Inputs:
            :param session: Session returned by login
            :param remote-directory: Remote server directory
            :param host: Remote server
            :param user: Remote server user
            :param password: Remote server password
            :param protocol: Remote server connection.

        * Outputs:
            :rtype: Dictionary of return status matching rest response

        *Use cases*

         Trigger supportsave and get the status

"""

import pyfos.pyfos_auth as pyfos_auth
from pyfos.pyfos_brocade_operation_show_status import show_status
from pyfos.pyfos_brocade_operation_supportsave import supportsave
from time import sleep
import pyfos.pyfos_util as pyfos_util
import pyfos.utils.brcd_util as brcd_util
import sys


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
    if ss_state is "failed":
        pyfos_util.response_print(resp)

    return


def ss_show_status(session, ssObj):

    ss_obj = show_status(ssObj)
    id = ss_obj.peek_message_id()
    status_obj = {"show-status": {"message-id": id}}
    ss_req_obj = show_status(status_obj)
    ss_rsp_obj = _post_supportsave(session, ss_req_obj)
    if pyfos_util.is_failed_resp(ss_rsp_obj):
        print("Supportsave operation failed.\n")
        pyfos_util.response_print(ss_rsp_obj)
        return
    _get_supportsave_status(session, ss_req_obj, ss_rsp_obj)
    return


def ss_validate(ss_obj):
    if ss_obj.peek_user_name() is None or \
       ss_obj.peek_remote_directory() is None or \
       ss_obj.peek_password() is None or \
       ss_obj.peek_protocol() is None or \
       ss_obj.peek_host() is None:
        return 1
    return 0


def main(argv):
    filters = ['host', 'user_name',
               'password', 'remote_directory',
               'protocol']
    inputs = brcd_util.parse(argv, supportsave, filters, ss_validate)
    ss_obj = inputs['utilobject']

    session = brcd_util.getsession(inputs)
    ss_rsp_obj = _post_supportsave(session, ss_obj)
    if pyfos_util.is_failed_resp(ss_rsp_obj):
        print("Supportsave operation failed.\n")
        pyfos_util.response_print(ss_rsp_obj)
    else:
        ss_show_status(session, ss_rsp_obj)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
