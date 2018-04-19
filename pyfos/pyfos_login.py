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

import http.client as httplib
import base64
import ssl
import pyfos.pyfos_util as pyfos_util

LOGIN_RESTCONF = "/rest/login"
LOGOUT_RESTCONF = "/rest/logout"


def credential_to_user(credential):
    auth_str = credential.get("Authorization")
    encoded_str = auth_str.split(" ")[1]
    print("print encoded string", encoded_str)
    credential_in_char = base64.b64decode(encoded_str)

    return credential_in_char.split(":")[0]


def login(user, password, ip_addr, isHttps):
    if isHttps == "self":
        conn = httplib.HTTPSConnection(
                ip_addr, context=ssl._create_unverified_context())
    elif isHttps == "CA":
        conn = httplib.HTTPSConnection(ip_addr)
    else:
        conn = httplib.HTTPConnection(ip_addr)

    auth = user + ":" + password
    auth_encoded = base64.b64encode(auth.encode())

    credential = {"Authorization": "Basic " + auth_encoded.decode(),
                  "User-Agent": "Rest-Conf"}

#    print ("being sent", credential)

    conn.request("POST", LOGIN_RESTCONF, "", credential)

    resp = conn.getresponse()
#    print resp.reason
#    page = resp.read()
#    print page
    auth = resp.getheader('authorization')
    content = resp.getheader('content-type')

    if auth is None:
        if resp.status == 404 and content in 'text/html; charset=iso-8859-1':
            return {"login-error": "Rest unsupported FOS version"}
        else:
            errors = pyfos_util.set_response_parse(resp)

        if 'client-error-message' in errors:
            return {
                    "login-error":
                    errors['client-errors']['errors']['error']['error-message']
                    }
        elif 'server-error-message' in errors:
            return {"login-error": errors['server-error-message']}
        else:
            return {"login-error": "unknown login error"}
    else:
        return {"Authorization": auth}


def logout(credential, ip_addr, isHttps):
    if isHttps == "self":
        conn = httplib.HTTPSConnection(
                ip_addr, context=ssl._create_unverified_context())
    elif isHttps == "CA":
        conn = httplib.HTTPSConnection(ip_addr)
    else:
        conn = httplib.HTTPConnection(ip_addr)

#    print credential

    conn.request("POST", LOGOUT_RESTCONF, "", credential)

    resp = conn.getresponse()
#    print resp.status
#    print resp.reason
#    page = resp.read()
#    print resp.getheaders()

    content = resp.getheader('content-type')
    if resp.status == 404 and content in 'text/html; charset=iso-8859-1':
        return {"login-error": "Rest unsupported FOS version"}
    return pyfos_util.set_response_parse(resp)
