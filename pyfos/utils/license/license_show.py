#!/usr/bin/env python3


# Copyright © 2019-2020 Broadcom. All rights reserved.
# The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries.
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


# license_show.py(pyGen v1.0.0)


"""

:mod:`license_show` - PyFOS util to show for license
*******************************************************************************
The :mod:`license_show` PyFOS util to show for license


A list of licenses installed on the switch.

license_show : usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].
    * -a,--authtoken: AuthToken value or AuthTokenManager config\
    file[OPTIONAL].
    * -z,--nosession: Sessionless authentication based login[OPTIONAL].
    * --nocredential: No credential to be sent in the request[OPTIONAL].

* Util Script Options:
    * --name=NAME: The representation of the license would be either license\
      key or serial number. The license key is a string with alpha numeric\
      characters and the License serial number is a string with the format\
      of 'FOS-XX-X-XX-XXXXXXXX'. Example of a license key and serial number\
      mentioned below. License key: 'HP9ttZNSgmB4MCD3NmNWgQDWtAKBFtXtBSFJF'\
      Serial number: 'FOS-00-0-02-11201234'
* Output:
    * Python dictionary content with RESTCONF response data.


.. function:: license_show.show_license(session, name)

    *Show license*

    Example Usage of the Method::

            ret = license_show.show_license(session, name)
            print (ret)

    Details::

        licenseObj = license()
        licenseObj.set_name(name)
        ret = _show_license(session, licenseObj)
        print (ret)

    **Inputs**

    :param session: The session returned by the login.
    :param name: The representation of the license would be either license key\
      or serial number. The license key is a string with alpha numeric\
      characters and the License serial number is a string with the format\
      of 'FOS-XX-X-XX-XXXXXXXX'. Example of a license key and serial number\
      mentioned below. License key: 'HP9ttZNSgmB4MCD3NmNWgQDWtAKBFtXtBSFJF'\
      Serial number: 'FOS-00-0-02-11201234'

    **Output**

    :rtype: None or one/more instance of class license on Success  or a\
    dictionary with error.

"""


# Start utils imports
import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_license import license

from pyfos.utils import brcd_util
# End module imports


def _show_license(session, licenseObj):
    objlist = license.get(session)
    licenselist = list()
    if isinstance(objlist, license):
        objlist = [objlist]
    if isinstance(objlist, list):
        for i in range(len(objlist)):
            if licenseObj.peek_name() is not None and licenseObj.peek_name()\
               != objlist[i].peek_name():
                continue
            licenselist.append(objlist[i])
    else:
        print(objlist)
    return licenselist


def show_license(session, name=None):
    licenseObj = license()
    licenseObj.set_name(name)
    return _show_license(session, licenseObj)


def validate(licenseObj):
    if licenseObj.peek_name() is None:
        return 0
    return 0


def main(argv):
    filters = ["name"]
    inputs = brcd_util.parse(argv, license, filters, validate)
    session = brcd_util.getsession(inputs)
    result = _show_license(session, inputs['utilobject'])
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
