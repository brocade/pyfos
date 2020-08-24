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

:mod:`showstatus` - PyFOS util to trigger the showstatus operation.
*******************************************************************************
The :mod:`showstatus` util is used to execute the showstatus operation.

This module is a stand-alone script and API that can be used to execute the \
showstatus operation.

* Input:

| Infrastructure Options:

  | -i,--ipaddr=IPADDR: The IP address of the FOS switch.
  | -L,--login=LOGIN: The login name.
  | -P,--password=PASSWORD: The password.
  | -f,--vfid=VFID: The VFID to which the request is directed [OPTIONAL].
  | -s,--secured=MODE: The HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose: Verbose mode [OPTIONAL].

| Util Script Options:

  |    --messageid=MESSAGEID: Input messageid of the asynchronous operation

* Output:

    * Status of the asynchronous operation.

"""

import sys
import errno
from socket import error as socket_error
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_operation_show_status import show_status
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def usage():
    print("  Util Script Options:")
    print()
    print("  --messageid=MESSAGEID: Input messageid of the asynchronous \
          operation")
    print()


def fd_show_status(session, status_obj):
    try:
        ss_req_obj = show_status(status_obj)
        ss_rsp_obj = ss_req_obj.post(session)
        if pyfos_util.is_failed_resp(ss_rsp_obj):
            print("Show-status operation failed.\n")
            pyfos_util.response_print(ss_rsp_obj)
            return
        pyfos_util.response_print(ss_rsp_obj)
        return

    except socket_error as serr:
        if serr.errno != errno.ECONNREFUSED:
            print("Switch rebooting please try later.\n")


def main(argv):
    valid_options = ["messageid"]
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

    messageid = None
    if 'messageid' in inputs:
        messageid = inputs['messageid']

    status_obj = {"show-status": {"message-id": messageid}}
    fd_show_status(session, status_obj)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
