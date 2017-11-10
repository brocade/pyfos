# Copyright 2017 Brocade Communications Systems, Inc.  All rights reserved.
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

:mod:`pyfos_util` - PyFOS module to provide utility functions.
*********************************************************************************************************
The :mod:`pyfos_util` provides a utility functions.

"""

import http.client as httplib
import json
import xmltodict
from requests.utils import quote

VF_ID = "?vf-id="
HTTP = "http://"
HTTPS = "https://"
GET = "GET "
POST = "POST "
PATCH = "PATCH "
PUT = "PUT "
DELETE = "DELETE "

isErrorRequest = 0


class test():
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.overall_passed = True
        self.overall_result_description = None
        self.requests = []


class result():
    "Stores requests and responses"
    def __init__(self, passed, request, response):
        self.passed = passed
        self.request = request
        self.response = response


current_test = None
executed_tests = []
current_request = None


class json_encoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)


def parse_page(page):
    # print (page)
    ret_elements = xmltodict.parse(page)
    return ret_elements


def set_response_parse(response):

    page = response.read()

    test_parse_response(response, page)

    if response.status >= 100 and response.status < 200:
        ret_error = {"info-code": response.status,
                     "info-message": response.reason,
                     "info-type": "Informational"}
    elif response.status >= 200 and response.status < 300:
        ret_error = {"success-code": response.status,
                     "success-message": response.reason,
                     "success-type": "Success"}
    elif response.status >= 300 and response.status < 400:
        ret_error = {"redirection-code": response.status,
                     "redirection-message": response.reason,
                     "redirection-type": "Redirection"}
    elif response.status >= 400 and response.status < 500:
        # if response.status == 404:
        #     ret_error = {"server-error-code": response.status,
        #                  "server-error-message": response.reason,
        #                  "server-error-type": "Server error",
        #                  "error-message": "No such URI"}
        #     return ret_error
        # page = response.read()
        # print page
        ret_error = parse_page(page)
    else:
        ret_error = {"server-error-code": response.status,
                     "server-error-message": response.reason,
                     "server-error-type": "Server error"}

    return ret_error


def get_response_parse(response):

    page = response.read()

    # print page

    test_parse_response(response, page)

    if response.status >= 100 and response.status < 200:
        ret_error = {"info-code": response.status,
                     "info-message": response.reason,
                     "info-type": "Informational"}
        return ret_error
    elif response.status >= 200 and response.status < 300:
        # print page
        ret_elements = parse_page(page)
        return ret_elements["Response"]
    elif response.status >= 300 and response.status < 400:
        ret_error = {"redirection-code": response.status,
                     "redirection-message": response.reason,
                     "redirection-type": "Redirection"}
        return ret_error
    elif response.status >= 400 and response.status < 500:
        # page = response.read()
        # print page
        ret_error = parse_page(page)
    else:
        ret_error = {"server-error-code": response.status,
                     "server-error-message": response.reason,
                     "server-error-type": "Server error"}

    return ret_error


def test_title_set(title, description):
    global current_test

    if current_test is None:
        print("Starting test case", title, ":", description)
        current_test = test(title, description)
    else:
        executed_tests.append(current_test)
        print("Starting test case", title, ":", description)
        current_test = test(title, description)


def test_explicit_result_passed(description):
    global current_test
    if current_test is None:
        print("current_test is set to None")
    else:
        current_test.overall_passed = True
        current_test.overall_result_description = description


def test_explicit_result_failed(description):
    global current_test
    if current_test is None:
        print("current_test is set to None")
    else:
        current_test.overall_passed = False
        current_test.overall_result_description = description


def test_add_to_failed_requests(request, resp):
    global current_test

    # if any is failing, mark the overall to be false
    if current_test:
        current_test.overall_passed = False
        current_test.requests.append(result(False, request, resp))


def test_add_to_succeeded_requests(request, resp):
    global current_test

    # leave the overall mark as is
    if current_test:
        current_test.requests.append(result(True, request, resp))


def test_negative_test_set(isErrReq):
    global isErrorRequest
    isErrorRequest = isErrReq


def test_parse_response(response, page):
    # Print switch response as is if isDebug is set
    # and set the failed error if response has error
    resp = ("\nResponse:\n" + str(response.status) +
            " " + response.reason + "\n" + str(page))

    if isErrorRequest == 0 and response.status >= 400:
        test_add_to_failed_requests(current_request, resp)
    else:
        test_add_to_succeeded_requests(current_request, resp)


def response_print(response):
    """Print dictionary into JSON format

    :param response: dictionary of information to be printed
    """
    print(json.dumps(response, cls=json_encoder, sort_keys=True, indent=4))


def test_results_print():
    global current_test
    global executed_tests

    # make sure to pick up the last test
    if current_test is not None:
        executed_tests.append(current_test)

    total = len(executed_tests)
    failed = 0
    failed_requests = 0
    passed = 0
    passed_requests = 0
    for test in executed_tests:
        if test.overall_passed is False:
            failed += 1
        else:
            passed += 1
        for request in test.requests:
            if request.passed is True:
                passed_requests += 1
            else:
                failed_requests += 1

    print("\nTEST RESULTS SUMMARY:")
    print("=====================\n")
    print("Passed test cases:\t\t", passed)
    print("Failed test cases:\t\t", failed)
    print("Total test cases:\t\t", total)
    print("Successful requests:\t\t", passed_requests)
    print("Failed requests:\t\t", failed_requests)
    print("Total requests:\t\t\t", passed_requests + failed_requests)

    if failed == 0:
        print("\nTest cases completed successfully.\n")
    else:
        print("\nFailed tests:")
        print("=========================\n")

        count = 0
        for test in executed_tests:
            if test.overall_passed is False:
                print("Error #", count, ":", test.title)
                print("Test description:", test.description)
                if test.overall_result_description is not None:
                    print("Test result description:",
                          test.overall_result_description)
                if len(test.requests) > 0:
                    print("=========")
                    for request in test.requests:
                        print(request.request)
                        print(request.response)
                        print(" ")
                        count += 1


def http_connection(session):
    ip_addr = session.get("ip_addr")
    isHttps = session.get("ishttps")

    if isHttps == "1":
        conn = httplib.HTTPSConnection(ip_addr)
    else:
        conn = httplib.HTTPConnection(ip_addr)

    return conn


def vfidstr_get(session):
    vfid = session.get("vfid")
    if vfid == -1:
        return ""
    else:
        return VF_ID + str(vfid)


def debug(session, http_cmd, cmd, content):
    debug = session.get("debug")
    isHttps = session.get("ishttps")

    if isHttps == "1":
        http_cmd += HTTPS
    else:
        http_cmd += HTTP

    if content == "":
        request = http_cmd + session.get("ip_addr") + cmd
        if debug:
            print(request)
    else:
        request = (http_cmd + session.get("ip_addr") +
                   cmd + " - CONTENT -> " + content)
        if debug:
            print(request)

    # Track the responses
    global current_request
    current_request = request


def get_request(session, cmd, content):
    credential = session.get("credential")
    vfidstr = vfidstr_get(session)

    conn = http_connection(session)

    debug(session, GET, cmd + vfidstr, content)

    conn.request("GET", cmd + vfidstr, content, credential)

    resp = conn.getresponse()
    return get_response_parse(resp)


def put_request(session, cmd, content):
    return patch_request(session, cmd, content)


def put_request_orig(session, cmd, content):
    credential = session.get("credential")
    vfidstr = vfidstr_get(session)

    conn = http_connection(session)

    debug(session, PUT, cmd + vfidstr, content)

    conn.request("PUT", cmd + vfidstr, content, credential)

    resp = conn.getresponse()
    return set_response_parse(resp)


def patch_request(session, cmd, content):
    credential = session.get("credential")
    vfidstr = vfidstr_get(session)

    conn = http_connection(session)

    debug(session, PATCH, cmd + vfidstr, content)

    conn.request("PATCH", cmd + vfidstr, content, credential)

    resp = conn.getresponse()
    return set_response_parse(resp)


def post_request(session, cmd, content):
    credential = session.get("credential")
    vfidstr = vfidstr_get(session)

    conn = http_connection(session)

    debug(session, POST, cmd + vfidstr, content)

    conn.request("POST", cmd + vfidstr, content, credential)

    resp = conn.getresponse()
    return set_response_parse(resp)


def delete_request(session, cmd, content):
    credential = session.get("credential")
    vfidstr = vfidstr_get(session)

    conn = http_connection(session)

    debug(session, DELETE, cmd + vfidstr, content)

    conn.request("DELETE", cmd + vfidstr, content, credential)

    resp = conn.getresponse()
    return set_response_parse(resp)


def encode_slotport(name):
    return quote(name, safe='')


def get_from_list(resp, key, index):
    if isinstance(resp, dict):
        if key in resp:
            return resp[key][index]
        else:
            return None
    else:
        return None


def get_from_dict(resp, key):
    if isinstance(resp, dict):
        if key in resp:
            return resp[key]
        else:
            return None
    else:
        return None


def is_success_resp(resp):
    if (isinstance(resp, dict) and 'success-type' in resp and
            resp['success-type'] == 'Success'):
        return True
    else:
        return False


def is_failed_resp(resp):
    if isinstance(resp, dict) and 'errors' in resp:
        return True
    elif isinstance(resp, dict) and 'server-error-code' in resp:
        return True
    else:
        return False
