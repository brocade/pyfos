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

:mod:`license_install` - PyFOS util to trigger the license_install operation.
*******************************************************************************
The :mod:`license_install` util is used to execute the license_install \
operation.

This module is a stand-alone script and API that can be used to execute the \
license_install operation.

* Input:

| Infrastructure Options:

  | -i,--ipaddr=IPADDR: The IP address of the FOS switch.
  | -L,--login=LOGIN: The login name.
  | -P,--password=PASSWORD: The password.
  | -f,--vfid=VFID: The VFID to which the request is directed [OPTIONAL].
  | -s,--secured=MODE: The HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose: Verbose mode [OPTIONAL].

| Util Script Options:

  |    --name=LICENSE-KEY: license key.

* Output:

    * Status of the lisencse install operation.

"""

import sys
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_operation_license import license_parameters
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def usage():
    print("  Util Script Options:")
    print()
    print("    --name=LICENSE-KEY           License key string.")
    print()


def main(argv):
    valid_options = ["name"]
    inputs = brcd_util.generic_input(argv, usage, valid_options)

    session = pyfos_auth.login(inputs["login"], inputs["password"],
                               inputs["ipaddr"], inputs["secured"],
                               verbose=inputs["verbose"])
    if pyfos_auth.is_failed_login(session):
        print("login failed because", session.get(
              pyfos_auth.CREDENTIAL_KEY)[pyfos_auth.LOGIN_ERROR_KEY])
        brcd_util.full_usage(usage, valid_options)
        sys.exit()

    brcd_util.exit_register(session)

    if "name" not in inputs:
        print("License key is required")
        brcd_util.full_usage(usage, valid_options)
        sys.exit()

    l_obj = license_parameters()
    l_obj.set_action("install")
    l_obj.set_name(inputs["name"])
    l_rsp_obj = l_obj.post(session)
    if ("info-message" in l_rsp_obj and
       l_rsp_obj["info-message"] ==
       "Switch version is lower than the object"):
        pyfos_util.response_print(l_rsp_obj)
        pyfos_auth.logout(session)
        sys.exit()
    else:
        pyfos_util.response_print(l_rsp_obj)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
