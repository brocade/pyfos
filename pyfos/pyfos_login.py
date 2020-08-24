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
from pyfos import pyfos_util

LOGIN_RESTCONF = "/rest/login"
LOGOUT_RESTCONF = "/rest/logout"
AUTHTOKEN = "/rest/auth-token"


def credential_to_user(credential):
    auth_str = credential.get("Authorization")
    encoded_str = auth_str.split(" ")[1]
    # print("print encoded string", encoded_str)
    credential_in_char = base64.b64decode(encoded_str)

    return credential_in_char.split(":")[0]


def login(user, password, ip_addr, isHttps, delay, authtoken=None,
          sessionless=False):
    request_uri = None
    request_auth = None

    if sessionless is True:
        request_auth = "Basic "
    else:
        if authtoken is not None:
            request_uri = LOGIN_RESTCONF
            request_auth = "Custom_Auth "
        else:
            request_uri = LOGIN_RESTCONF
            request_auth = "Custom_Basic "

        if isHttps == "self":
            conn = httplib.HTTPSConnection(
                    ip_addr, 443, context=ssl._create_unverified_context())
        elif isHttps == "CA":
            conn = httplib.HTTPSConnection(ip_addr, 443)
        else:
            conn = httplib.HTTPConnection(ip_addr, 80)

    if authtoken is not None:
        auth = user + ":" + authtoken.auth_token
    else:
        auth = user + ":" + password

    auth_encoded = base64.b64encode(auth.encode())

    credential = {"Authorization": request_auth + auth_encoded.decode(),
                  "User-Agent": "Rest-Conf"}
    # print(credential)

    # print ("being sent", credential)
    if sessionless is True:
        # Check the content dict returned here is default
        return credential, {"content-type": "application/yang-data+xml",
                            "content-version": None}
    resp = pyfos_util.bsn_request(conn, "POST", request_uri, "", credential, delay)

#    print resp.reason
#    page = resp.read()
#    print page
    auth = resp.getheader('authorization')
    content = resp.getheader('content-type')
    contentlist = content.split(";")
    if auth is None:
        if resp.status == 404 and content in 'text/html; charset=iso-8859-1':
            return {"login-error": "Rest unsupported FOS version"}, dict()
        else:
            errors = pyfos_util.set_response_parse(resp)

        if 'client-error-message' in errors:
            return {
                    "login-error":
                    errors['client-errors']['errors']['error']['error-message']
                    }, dict()
        elif 'server-error-message' in errors:
            return {"login-error": errors['server-error-message']}, dict()
        else:
            return {"login-error": "unknown login error"}, dict()
    else:
        if len(contentlist) == 2:
            content_type = contentlist[0]
            content_ver = contentlist[1]
        else:
            content_type = content
            content_ver = None
        return {"Authorization": auth}, {"content-type": content_type,
                                         "content-version": content_ver}


def logout(credential, ip_addr, isHttps, delay):
    if isHttps == "self":
        conn = httplib.HTTPSConnection(
                ip_addr, 443, context=ssl._create_unverified_context())
    elif isHttps == "CA":
        conn = httplib.HTTPSConnection(ip_addr, 443)
    else:
        conn = httplib.HTTPConnection(ip_addr, 80)

#    print credential

    resp = pyfos_util.bsn_request(conn, "POST", LOGOUT_RESTCONF, "", credential, delay)

#    print resp.status
#    print resp.reason
#    page = resp.read()
#    print resp.getheaders()

    content = resp.getheader('content-type')
    if resp.status == 404 and content in 'text/html; charset=iso-8859-1':
        return {"login-error": "Rest unsupported FOS version"}
    return pyfos_util.set_response_parse(resp)
