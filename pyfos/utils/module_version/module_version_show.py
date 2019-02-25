#!/usr/bin/env python3

# Copyright 2019 Brocade Communications Systems LLC.  All rights reserved.
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

:mod:`module_version_show` - PyFOS util to show the module version details
**************************************************************************
The :mod:`module_version_show` provides option to display supported module
versions.

This module is a standalone script that can be used to display all the
supported module versions.

* Inputs:

| Infrastructure options:

  | -i,--ipaddr=IPADDR     The IP address of FOS switch.
  | -L,--login=LOGIN       The login name.
  | -P,--password=PASSWORD The password.
  | -f,--vfid=VFID         The VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           Verbose mode[OPTIONAL].

* Outputs:
    * Returns version details for all the supported modules from the switch.

"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_module_version import module_version
from pyfos.utils import brcd_util


def get_module_version_info(session):
    module_version_obj = module_version()
    result = module_version_obj.get(session)
    return result


def main(argv):

    filters = []
    inputs = brcd_util.parse(argv, module_version, filters)

    session = brcd_util.getsession(inputs)

    result = get_module_version_info(inputs['session'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
