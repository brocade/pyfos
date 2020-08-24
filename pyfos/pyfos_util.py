# Copyright © 2018 Broadcom.  All rights reserved.
# The term "Broadcom" refers to Broadcom Inc. and /or its subsidiaries.
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
The :mod:`pyfos_util` provides utility functions.

"""
import http.client as httplib
import json
import ssl
import time
from requests.utils import quote
from colorconsole import terminal
import xmltodict

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
        self.logs = None
        self.myobject = None


class result():
    "Stores requests and responses"
    def __init__(self, passed, request, response):
        self.passed = passed
        self.request = request
        self.response = response


current_test = None
executed_tests = []
current_request = None
screen = None


class json_encoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)


def parse_page(page):
    ret_elements = xmltodict.parse(page)
    return ret_elements


def set_response_parse(response):

    page = response.read()

    test_parse_response(response, page)

    if response.status >= 100 and response.status < 200:
        ret_error = {"http-resp-code": response.status,
                     "info-code": response.status,
                     "info-message": response.reason,
                     "info-type": "Informational"}
    elif response.status >= 200 and response.status < 300:
        ret_error = {"http-resp-code": response.status,
                     "success-code": response.status,
                     "success-message": response.reason,
                     "success-type": "Success"}
    elif response.status >= 300 and response.status < 400:
        ret_error = {"http-resp-code": response.status,
                     "redirection-code": response.status,
                     "redirection-message": response.reason,
                     "redirection-type": "Redirection"}
    elif response.status >= 400 and response.status < 500:
        ret_error = {"http-resp-code": response.status,
                     "client-error-code": response.status,
                     "client-error-message": response.reason,
                     "client-errors": parse_page(page)}
    else:
        ret_error = {"http-resp-code": response.status,
                     "server-error-code": response.status,
                     "server-error-message": response.reason,
                     "server-error-type": "Server error"}

    return ret_error


def get_response_parse(response, is_options=False):

    page = response.read()

    # print(page)

    test_parse_response(response, page)

    if response.status >= 100 and response.status < 200:
        ret_error = {"info-code": response.status,
                     "info-message": response.reason,
                     "info-type": "Informational"}
        return ret_error
    elif response.status >= 200 and response.status < 300:
        # print page
        if is_options:
            return response.getheader("Allow").split(", ")
        else:
            ret_elements = parse_page(page)
            return ret_elements["Response"]
    elif response.status >= 300 and response.status < 400:
        ret_error = {"redirection-code": response.status,
                     "redirection-message": response.reason,
                     "redirection-type": "Redirection"}
        return ret_error
    elif response.status >= 400 and response.status < 500:
        ret_error = {"client-error-code": response.status,
                     "client-error-message": response.reason,
                     "client-errors": parse_page(page)}
    else:
        ret_error = {"server-error-code": response.status,
                     "server-error-message": response.reason,
                     "server-error-type": "Server error"}

    return ret_error


def rpc_response_parse(response):

    page = response.read()

    # print(page)

    test_parse_response(response, page)

    if response.status >= 100 and response.status < 200:
        ret_error = {"info-code": response.status,
                     "info-message": response.reason,
                     "info-type": "Informational"}
        return ret_error
    elif response.status >= 200 and response.status < 300:
        if response.status == 204:
            ret_elements = {"http-resp-code": response.status,
                            "success-code": response.status,
                            "success-message": response.reason,
                            "success-type": "Success"}
            return ret_elements
        else:
            # print page
            ret_elements = parse_page(page)
            return ret_elements["Response"]
    elif response.status >= 300 and response.status < 400:
        ret_error = {"redirection-code": response.status,
                     "redirection-message": response.reason,
                     "redirection-type": "Redirection"}
        return ret_error
    elif response.status >= 400 and response.status < 500:
        ret_error = {"client-error-code": response.status,
                     "client-error-message": response.reason,
                     "client-errors": parse_page(page)}
    else:
        ret_error = {"server-error-code": response.status,
                     "server-error-message": response.reason,
                     "server-error-type": "Server error"}

    return ret_error


def initscreen():
    # pylint: disable=W0603
    global screen
    if screen is None:
        screen = terminal.get_terminal(conEmu=False)


def test_title_set(title, description):
    # pylint: disable=W0603
    global current_test
    global screen
    if screen is None:
        screen = terminal.get_terminal(conEmu=False)
    if current_test is None:
        print('\nStarting test case:', title, "::", description, "::", end="")
        current_test = test(title, description)
    else:
        print_current_test()
        executed_tests.append(current_test)
        print('Starting test case:', title, "::", description, "::", end="")
        current_test = test(title, description)


def print_test_red(arg):
    # pylint: disable=W0603
    global screen
    if screen is not None:
        screen.cprint(terminal.colors["RED"], None, arg + "\n")
        screen.reset_colors()
    else:
        print(arg)


def print_test_green(arg):
    # pylint: disable=W0603
    global screen
    if screen is not None:
        screen.cprint(terminal.colors["GREEN"], None, arg + "\n")
        screen.reset_colors()
    else:
        print(arg)


def print_test_yellow(arg):
    # pylint: disable=W0603
    global screen
    if screen is not None:
        screen.cprint(terminal.colors["YELLOW"], None, arg + "\n")
        screen.reset_colors()
    else:
        print(arg)


def print_test_blue(arg):
    # pylint: disable=W0603
    global screen
    if screen is not None:
        screen.cprint(terminal.colors["BLUE"], None, arg + "\n")
        screen.reset_colors()
    else:
        print(arg)


def print_test_lblue(arg):
    # pylint: disable=W0603
    global screen
    if screen is not None:
        screen.cprint(terminal.colors["LBLUE"], None, arg + "\n")
        screen.reset_colors()
    else:
        print(arg)


def print_test_lgreen(arg):
    # pylint: disable=W0603
    global screen
    if screen is not None:
        screen.cprint(terminal.colors["LGREEN"], None, arg + "\n")
        screen.reset_colors()
    else:
        print(arg)


def print_test_lred(arg):
    # pylint: disable=W0603
    global screen
    if screen is not None:
        screen.cprint(terminal.colors["LRED"], None, arg + "\n")
        screen.reset_colors()
    else:
        print(arg)


def test_explicit_result_passed(description):
    # pylint: disable=W0603
    global current_test
    if current_test is None:
        print("current_test is set to None")
    else:
        current_test.overall_passed = True
        current_test.overall_result_description = description


def test_explicit_result_failed(description):
    # pylint: disable=W0603
    global current_test
    if current_test is None:
        print("current_test is set to None")
    else:
        current_test.overall_passed = False
        current_test.overall_result_description = description


def test_add_to_failed_requests(request, resp):
    # pylint: disable=W0603
    global current_test

    # if any is failing, mark the overall to be false
    if current_test:
        current_test.overall_passed = False
        current_test.requests.append(result(False, request, resp))


def test_add_to_succeeded_requests(request, resp):
    # pylint: disable=W0603
    global current_test

    # leave the overall mark as is
    if current_test:
        current_test.requests.append(result(True, request, resp))


def test_negative_test_set(isErrReq):
    # pylint: disable=W0603
    global isErrorRequest
    isErrorRequest = isErrReq


def print_current_test():
    # pylint: disable=W0603
    global current_test
    if current_test:
        if current_test.overall_passed is True:
            if isErrorRequest == 0:
                print_test_green("Pass")
            else:
                print_test_yellow("Pass")
        if current_test.overall_passed is False:
            print_test_red("Fail")


def test_add_logs(isVerbose, log, myobject=None):
    # pylint: disable=W0603
    global current_test
    if current_test:
        current_test.logs = log
        if myobject is not None:
            current_test.myobject = str(myobject)
    if isVerbose == 1:
        test_print_verbose_logs()


def test_print_verbose_logs():
    # pylint: disable=W0603
    global current_test
    if current_test:
        if current_test.logs is not None:
            print_test_yellow("\nDebug Logs for testcase::")
            print_test_lblue(current_test.logs)
        if current_test.myobject is not None:
            print_test_yellow("Object details::")
            print_test_lgreen(current_test.myobject)
        print_test_yellow("Request/Response details::")
        if len(current_test.requests) > 0:
            print("===============================")
            for request in current_test.requests:
                print_test_lblue(request.request)
                print_test_lgreen(request.response)
                print(" ")


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
    """Prints dictionary into JSON format.

    :param response: Dictionary of information to be printed.
    """
    print(json.dumps(response, cls=json_encoder, sort_keys=True, indent=4))


def strjson(response):
    """returns dictionary into JSON format.

    :param response: Dictionary of information to be converted to JSON.
    """
    return str(json.dumps(response, cls=json_encoder,
                          sort_keys=True, indent=4))


def test_results_print():
    # pylint: disable=W0603
    global current_test
    global executed_tests

    # make sure to pick up the last test
    if current_test is not None:
        executed_tests.append(current_test)
        print_current_test()

    total = len(executed_tests)
    failed = 0
    failed_requests = 0
    passed = 0
    passed_requests = 0
    for executed_test in executed_tests:
        if executed_test.overall_passed is False:
            failed += 1
        else:
            passed += 1
        for request in executed_test.requests:
            if request.passed is True:
                passed_requests += 1
            else:
                failed_requests += 1

    print_test_yellow("\nTEST RESULTS SUMMARY:")
    print("=================================\n")
    print_test_lgreen('{0:50}:{1:4}'.format("Passed test cases:", passed))
    print_test_lred('{0:50}:{1:4}'.format("Failed test cases:", failed))
    print_test_lblue('{0:50}:{1:4}'.format("Total test cases:", total))
    print_test_green('{0:50}:{1:4}'.format("Successful requests:",
                                           passed_requests))
    print_test_red('{0:50}:{1:4}'.format("Failed requests:", failed_requests))
    print_test_lblue('{0:50}:{1:4}'.format("Total requests:",
                                           passed_requests + failed_requests))

    if failed == 0:
        print_test_lgreen("\nTest cases completed successfully.")
    else:
        print_test_lred("\nFailed tests:")
        print("=========================\n")

        count = 0
        for executed_test in executed_tests:
            if executed_test.overall_passed is False:
                print_test_yellow("Error #" + str(count) + ":" +
                                  executed_test.title)
                print_test_lred("Test description:" +
                                executed_test.description + "\n")
                if executed_test.overall_result_description is not None:
                    print_test_red("Test result description:" +
                                   str(executed_test.
                                       overall_result_description))
                if len(executed_test.requests) > 0:
                    print("=================")
                    for request in executed_test.requests:
                        print_test_lblue(request.request)
                        print_test_lred(request.response)
                        print(" ")
                        count += 1


def http_connection(session):
    ip_addr = session.get("ip_addr")
    isHttps = session.get("ishttps")

    if isHttps == "self":
        conn = httplib.HTTPSConnection(
                ip_addr, 443, context=ssl._create_unverified_context())
    elif isHttps == "CA":
        conn = httplib.HTTPSConnection(ip_addr, 443)
    else:
        conn = httplib.HTTPConnection(ip_addr, 80)

    return conn


def vfidstr_get(session):
    vfid = session.get("vfid")
    if vfid == -1:
        return ""
    else:
        return VF_ID + str(vfid)


def getcredential(session):
    nocred = session.get("nocredential")
    if nocred:
        credential = dict({})
    else:
        credential = session.get("credential")
    return credential


def getthrottledelay(session):
    delay = session.get("throttle_delay")
    return delay


def debug(session, http_cmd, cmd, content):
    debug_attrib = session.get("debug")
    isHttps = session.get("ishttps")

    if isHttps == "self":
        http_cmd += HTTPS
    elif isHttps == "CA":
        http_cmd += HTTPS
    else:
        http_cmd += HTTP

    if content == "":
        request = http_cmd + session.get("ip_addr") + cmd
        if debug_attrib:
            print(request)
    else:
        request = (http_cmd + session.get("ip_addr") +
                   cmd + " - CONTENT -> " + content)
        if debug_attrib:
            print(request)

    # Track the responses
    # pylint: disable=W0603
    global current_request
    current_request = request


def bsn_request(conn, command, uri, body, credential, delay):

    conn.request(command, uri, body, credential)

    resp = conn.getresponse()
    if resp.status == 503:
        if delay > 0:
            time.sleep(delay)

        conn.request(command, uri, body, credential)

        resp = conn.getresponse()

        return resp
    else:
        return resp


def options_request(session, cmd, content):
    credential = getcredential(session)
    delay = getthrottledelay(session)
    vfidstr = vfidstr_get(session)

    conn = http_connection(session)

    debug(session, GET, cmd + vfidstr, content)

    resp = bsn_request(conn, "OPTIONS", cmd + vfidstr, content, credential, delay)

    return get_response_parse(resp, True)


def get_request(session, cmd, content):
    credential = getcredential(session)
    delay = getthrottledelay(session)
    vfidstr = vfidstr_get(session)

    conn = http_connection(session)

    debug(session, GET, cmd + vfidstr, content)

    resp = bsn_request(conn, "GET", cmd + vfidstr, content, credential, delay)

    return get_response_parse(resp)


def put_request(session, cmd, content):
    return patch_request(session, cmd, content)


def put_request_orig(session, cmd, content):
    credential = getcredential(session)
    delay = getthrottledelay(session)
    vfidstr = vfidstr_get(session)

    conn = http_connection(session)

    debug(session, PUT, cmd + vfidstr, content)

    resp = bsn_request(conn, "PUT", cmd + vfidstr, content, credential, delay)

    return set_response_parse(resp)


def patch_request(session, cmd, content):
    credential = getcredential(session)
    delay = getthrottledelay(session)
    vfidstr = vfidstr_get(session)

    conn = http_connection(session)

    debug(session, PATCH, cmd + vfidstr, content)

    resp = bsn_request(conn, "PATCH", cmd + vfidstr, content, credential, delay)

    return set_response_parse(resp)


def post_request(session, cmd, content):
    credential = getcredential(session)
    delay = getthrottledelay(session)
    vfidstr = vfidstr_get(session)

    conn = http_connection(session)

    debug(session, POST, cmd + vfidstr, content)

    resp = bsn_request(conn, "POST", cmd + vfidstr, content, credential, delay)

    return set_response_parse(resp)


def delete_request(session, cmd, content):
    credential = getcredential(session)
    delay = getthrottledelay(session)
    vfidstr = vfidstr_get(session)

    conn = http_connection(session)

    debug(session, DELETE, cmd + vfidstr, content)

    resp = bsn_request(conn, "DELETE", cmd + vfidstr, content, credential, delay)

    return set_response_parse(resp)


def rpc_request(session, cmd, content):
    credential = getcredential(session)
    delay = getthrottledelay(session)
    vfidstr = vfidstr_get(session)

    conn = http_connection(session)

    debug(session, POST, cmd + vfidstr, content)

    resp = bsn_request(conn, "POST", cmd + vfidstr, content, credential, delay)

    return rpc_response_parse(resp)


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
    return bool(isinstance(resp, dict) and 'success-type' in resp
                and resp['success-type'] == 'Success')


def is_failed_resp(resp):
    if isinstance(resp, dict) and 'client-error-code' in resp:
        return True
    elif isinstance(resp, dict) and 'server-error-code' in resp:
        return True
    else:
        return False


def isWWN(inputstring):
    if inputstring.count(":") != 7:
        return False
    for i in inputstring.split(":"):
        try:
            int(i, 16)
        except ValueError:
            return False

    return True


def isIPAddr(inputstring):
    # check for IPv4
    if inputstring.count(".") == 3:
        for i in inputstring.split("."):
            try:
                int(i, 10)
            except ValueError:
                return False

        return True
    # check for IPv6
    elif inputstring.count(":") > 2:
        for i in inputstring.split(":"):
            try:
                int(i, 16)
            except ValueError:
                return False

            if len(i) > 4:
                return False

        return True
    else:
        return False


def isInt(inputstring):
    try:
        int(inputstring, 10)
    except ValueError:
        return False

    return True


def isSlotPort(inputstring):
    if inputstring.count("/") != 1:
        return False
    for i in inputstring.split("/"):
        try:
            int(i, 10)
        except ValueError:
            return False

    return True


def isDCommaI(inputstring):
    if inputstring.count(",") != 1:
        return False
    for i in inputstring.split(","):
        try:
            int(i, 10)
        except ValueError:
            return False

    return True
