# Copyright © 2019 Broadcom. All rights reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.
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

:mod:`pyfos_auth_token` - PyFOS module to facilitate \
        Auth-Token based session to a FOS switch.
*******************************************************\
*******************************************************\
********************************************************
The :mod:`pyfos_auth_token` module provides functions to create,
delete Auth-Token and Management, including establishing session
with FOS switch using them.

"""
import json
import sys
import time
from pathlib import Path
from pyfos import pyfos_util


class json_encoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)


class auth_token():
    """ This class represents a REST-supported Auth-Token for a FOS switch.

    .. Attributes:
        ip: The FOS switch IP address.
        uri: The URI string to access the corresponding object via REST.
        user: The user associated with the FOS switch.
        auth_token: The AuthToken associated with the FOS switch.

    """

    def __init__(self, session=None, myarg=None):
        """ This constructor for the class representing an AuthToken.

            .. Attributes:
                session : The switch session associated with the AuthToken.
                myarg: The argument for AuthToken as a dictonary or another\
                    instance of the same class.
        """
        self.uri = "/rest/auth-token"
        self.ip = None
        self.user = None
        self.auth_token = None
        self.mgr = None

        if session is not None:
            self.ip = session.get("ip_addr")
            self.user = session.get("user")
            self.auth_token = None
        if myarg is not None:
            self.__set__(session, myarg)

    def __set__(self, session, myarg):
        """ Set the auth_token instance values from passed parameters."""
        if myarg is not None:
            if isinstance(myarg, dict):
                try:
                    self.auth_token = myarg.get('TOKEN')
                    self.ip = myarg.get('IP')
                    self.user = myarg.get('USER')

                except AttributeError as err:
                    print("Auth Token missing in the arguments : ", err)

            elif isinstance(myarg, self.__class__):
                self.ip = myarg.ip
                self.user = myarg.user
                self.auth_token = myarg.auth_token
            else:
                print("unknown argument passed")

    def debugenabled(self):
        if self.mgr is not None and self.mgr.debug is False:
            return False
        return True

    def setValue(self, ip, user, uauth_token):
        """ Set the auth_token instance with the values specified."""
        self.ip = ip
        self.user = user
        self.auth_token = uauth_token

    def reprJSON(self):
        """ Represent auth_token in JSON."""
        mydict = dict()
        if self.debugenabled() is True:
            mydict["IP"] = self.ip
            mydict["USER"] = self.user
        mydict["TOKEN"] = self.auth_token
        return mydict

    def create(self, session):
        """ Create the AuthToken for the FOS switch as in session."""
        errors = None
        credential = pyfos_util.getcredential(session)
        delay = pyfos_util.getthrottledelay(session)
        vfidstr = pyfos_util.vfidstr_get(session)
        self.ip = session.get("ip_addr")

        conn = pyfos_util.http_connection(session)

        pyfos_util.debug(session, "POST ", self.uri + vfidstr, "")

        response = pyfos_util.bsn_request(conn, "POST", self.uri + vfidstr, "", credential, delay)

        page = response.read()
        # print (page)
        auth = response.getheader('authorization')
        if response.status == 201:
            if auth is not None:
                self.auth_token = auth

        if len(page) != 0:
            errors = {"http-resp-code": response.status,
                      "client-error-code": response.status,
                      "client-error-message": response.reason,
                      "client-errors": pyfos_util.parse_page(page)}
        else:
            if response.status == 201:
                errors = {"http-resp-code": response.status,
                          "success-code": response.status,
                          "success-message": response.reason,
                          "success-type": "Success"}
            else:
                errors = {"http-resp-code": response.status,
                          "client-error-code": response.status,
                          "client-error-message": response.reason,
                          "client-errors": None}
        return errors

    def delete(self, session):
        """ Delete the AuthToken created for a FOS switch."""
        errors = None
        credential = pyfos_util.getcredential(session)
        delay = pyfos_util.getthrottledelay(session)
        vfidstr = pyfos_util.vfidstr_get(session)
        self.ip = session.get("ip_addr")

        conn = pyfos_util.http_connection(session)

        pyfos_util.debug(session, "DELETE ", self.uri + vfidstr, "")

        resp = pyfos_util.bsn_request(conn, "DELETE", self.uri + vfidstr, "", credential, delay)

        page = resp.read()
        if resp.status == 204:
            if self.auth_token is None:
                print("Auth Token Deleted : " + "Auth Token not present in " +
                      "the local token cache.")
            else:
                print("Auth Token Deleted : ", self.auth_token)

        if resp.status != 204:
            errors = {"http-resp-code": resp.status,
                      "client-error-code": resp.status,
                      "client-error-message": resp.reason,
                      "client-errors": pyfos_util.parse_page(page)}
        else:
            errors = {"http-resp-code": resp.status,
                      "success-code": resp.status,
                      "success-message": resp.reason,
                      "success-type": "Success"}
        return errors

    def __eq__(self, rhs):
        if self.ip == rhs.ip and self.user == rhs.user:
            return True
        return False


class auth_token_manager():
    """ The Manager for AuthToken[s] created for all FOS switches."""

    def __init__(self, configfile=None):
        """ The constructor for AuthToken Manager"""

        # Default Conf store
        self.defdirname = None
        self.defdirpath = None
        self.defconfigfilename = None
        self.defconfigpath = None
        self.deftokenfilename = None
        self.deftokenfilepath = None
        self.deftokenpath = None

        self.defconfdict = dict()
        self.loaddict = dict()
        self.tokendict = dict()

        # User Conf Store
        self.userdirname = None
        self.userdirpath = None
        self.userconfigfilename = None
        self.userconfigpath = None
        self.usertokenfilename = None
        self.usertokenpath = None
        self.userconfigdata = None

        self.userconfdict = dict()

        # Token Store
        self.tokenlist = list()
        self.tokendict = dict()
        self.tokendata = None
        self.debug = True

        # Load the conf Store
        self.readConfStore(configfile)

    def setdefaultStore(self):
        """ Set the Default Config/AutToken Store details."""
        # Module path
        # modulePath = Path(Path(sys.exec_prefix).resolve())
        modulePath = Path(Path.home())
        moduleparent = Path(modulePath.resolve())

        # Default Directory
        self.defdirname = str(moduleparent.joinpath("Auth_Token"))
        self.defdirpath = Path(self.defdirname)

        # Default config file Path
        self.defconfigfilename = str(self.defdirpath.joinpath("conf.json"))
        self.defconfigpath = Path(self.defconfigfilename)

        # Default Directory Path create
        if not self.defdirpath.exists():
            self.defdirpath.mkdir()

        # self
        self.deftokenfilename = str(self.defdirpath.joinpath("auth_tokens" +
                                                             ".json"))
        self.deftokenpath = Path(self.deftokenfilename)

        # Add default Config Details.
        if not self.defconfigpath.exists():
            self.defconfdict['token_file'] = str(self.deftokenfilename)
            self.writeDefaultConfStore()

        # Add default Config Details.
        if not self.deftokenpath.exists():
            self.loaddict = dict()
            self.tokendata = self.formatOutput(self.loaddict)
            self.tokendict = json.loads(self.tokendata)
            self.writeDefaultTokenStore()

    def readUserConfStore(self, userConfig):
        """ Read the Default Config/AutToken Store details."""
        # User Config path
        configPath = Path(Path(userConfig).resolve())
        configparent = Path(configPath.parent)

        # User Config Directory
        self.userdirname = configparent.resolve()
        self.userdirpath = Path(self.userdirname)

        # user config file Path
        self.userconfigfilename = str(self.userdirpath.joinpath("conf.json"))
        self.userconfigpath = Path(self.userconfigfilename)

        if self.userconfigpath.exists():
            userConfighandle = open(self.userconfigfilename, 'r')
            self.userconfigdata = userConfighandle.read()
            userConfighandle.close()
        else:
            self.userconfigdata = self.formatOutput(dict())

        try:
            self.userconfdict = json.loads(self.userconfigdata)

        except ValueError as err:
            print("Unable to load authToken Manager config : ", err)
            sys.exit(1)

        if "token_file" in self.userconfdict.keys():
            self.usertokenfilename = self.userconfdict['token_file']
            self.usertokenpath = Path(self.usertokenfilename)
        else:
            print("The user Token file is missing in the configuration")
            self.usertokenfilename =\
                str(self.userdirname.joinpath("auth_tokens.json"))

            self.usertokenpath = Path(self.usertokenfilename)
            print("Setting Auth Token file by default to :",
                  self.usertokenfilename)
            self.userconfdict['token_file'] = str(self.usertokenfilename)
            self.writeUserConfStore()

        if not self.usertokenpath.exists():
            # Default token  store
            self.loaddict = dict()
            self.tokendata = self.formatOutput(self.loaddict)
            self.tokendict = dict()
            self.writeUserTokenStore()

    def readTokenStore(self, tokenFile):
        """ Read the Default/User configured AutToken Store details."""
        tokenpath = Path(tokenFile)
        if tokenpath.exists():
            tokenhandle = open(str(tokenpath), 'r')
            self.tokendata = tokenhandle.read()
            tokenhandle.close()
        else:
            self.tokendata = self.formatOutput(dict())

        try:
            self.loaddict = json.loads(self.tokendata)

        except ValueError as err:
            print("Unable to load authTokens : ", err)
            sys.exit(1)

        if any(self.loaddict):
            for k, v in self.loaddict.items():
                switchdict = dict()
                for k1, v1 in v.items():
                    tmpauthtoken = auth_token(None, v1)
                    tmpauthtoken.mgr = self
                    switchdict.update(dict({k1: tmpauthtoken}))
                    self.tokenlist.append(tmpauthtoken)
                self.tokendict.update(dict({k: switchdict}))

    def readConfStore(self, userConfigFile=None):
        """ Read the Default/User configured Config Store details."""
        # set the Default for config/token store
        self.setdefaultStore()

        # Read the default config
        if self.defconfigpath.exists():
            defConfighandle = open(self.defconfigfilename, 'r')
            defconfigdata = defConfighandle.read()
            defConfighandle.close()
        else:
            defconfigdata = self.formatOutput(dict())

        try:
            self.defconfdict = json.loads(defconfigdata)

        except ValueError as err:
            print("Unable to load authToken Manager config : ", err)
            sys.exit(1)

        # Check user config in input or is set in default config.
        if userConfigFile is not None:
            self.readUserConfStore(userConfigFile)
        elif "user_config" in self.defconfdict.keys():
            self.readUserConfStore(self.defconfdict["user_config"])
        # else:
            # print("Using default configs")

        if self.usertokenfilename is not None:
            self.readTokenStore(self.usertokenfilename)
        else:
            self.readTokenStore(self.deftokenfilename)

    def findToken(self, ip, user):
        """ Find the AuthToken for the user for a FOS switch."""
        try:
            myauth = self.tokendict[ip][user]
        except KeyError:
            # print("No authToken found : ", err)
            return None
        return myauth

    def addToken(self, token):
        """ Add the AuthToken to the current AuthToken store."""
        if token.ip in self.tokendict.keys():
            switchdict = self.tokendict[token.ip]
            switchdict.update(dict({token.user: token}))
        else:
            switchdict = dict({token.user: token})

        self.tokendict.update(dict({token.ip: switchdict}))
        # map the manager to token
        token.mgr = self

        for itertoken in self.tokenlist:
            if itertoken == token:
                self.tokenlist.remove(itertoken)
                break
        self.tokenlist.append(token)
        self.writeTokenStore()
        return True

    def removeToken(self, token):
        """ Remove the AuthToken to the current AuthToken store."""
        if self.findToken(token.ip, token.user) is not None:
            del self.tokendict[token.ip][token.user]
            for itertoken in self.tokenlist:
                if itertoken == token:
                    itertoken.mgr = None
                    self.tokenlist.remove(itertoken)
                    break
            self.writeTokenStore()
        else:
            # print("No token found in the the token dict")
            return False
        return True

    def delete(self, session):
        authtoken = self.getToken(session)
        if authtoken is None:
            authtoken = auth_token(session)

        # Delete the authtoken from switch
        ret = authtoken.delete(session)

        # Remove from cache if its present as well
        if ret["http-resp-code"] == 204 or ret["http-resp-code"] == 400 and\
           ret["client-errors"]["errors"]["error"]["error-message"] ==\
           "Auth token not present":
            self.removeToken(authtoken)
        return ret

    def getToken(self, session):
        """ Get the AuthToken for the user for a FOS switch."""
        return self.findToken(session['ip_addr'], session['user'])

    def generateToken(self, session):
        """ Generate an AuthToken for the user for a FOS switch."""
        myauth = auth_token(session)
        ret = myauth.create(session)
        if ret['http-resp-code'] != 201:
            return ret
        newret = self.addToken(myauth)
        if newret is False:
            print("Failed to add the auth token to token store.")
            print("\nAuthToken:", self.formatOutput(myauth))
        return ret

    def formatOutput(self, buffer):
        return json.dumps(buffer, cls=json_encoder, sort_keys=True, indent=4)

    def writeFile(self, writefile, buffer):
        ret = True
        try:
            wb = open(writefile, 'w')
            wb.write(self.formatOutput(buffer))
            wb.flush()
        except IOError as errs:
            print("Error in file operation:", writefile,
                  "\nData:\n", self.formatOutput(buffer), errs)
            ret = False
        finally:
            wb.close()
        return ret

    def writeTokenStore(self):
        """ Write the AuthToken store."""
        if self.usertokenfilename is None:
            ret = self.writeDefaultTokenStore()
        else:
            ret = self.writeUserTokenStore()
        return ret

    def writeUserTokenStore(self):
        """ Write the User AuthToken store."""
        return self.writeFile(self.usertokenfilename, self.tokendict)

    def writeUserConfStore(self):
        """ Write the User Config store."""
        return self.writeFile(self.userconfigfilename, self.userconfdict)

    def writeDefaultConfStore(self):
        """ Write the Default Config store."""
        return self.writeFile(self.defconfigfilename, self.defconfdict)

    def writeDefaultTokenStore(self):
        """ Write the Default AuthToken store."""
        return self.writeFile(self.deftokenfilename, self.tokendict)

    def setUserStoreAsDefaultStore(self):
        """ Set the User store as Default store for AuthToken Manager."""
        response = dict()
        response['status'] = True
        response['message'] = "Success"
        # Add default Config Details.
        if self.userconfigfilename is not None:
            if "user_config" in self.defconfdict.keys():
                previoususerconfig = self.defconfdict['user_config']
                self.defconfdict['previous_user_config'] = previoususerconfig
                myoldconfigs = list([str(previoususerconfig)])
                if "all_user_config" not in self.defconfdict.keys():
                    self.defconfdict['all_user_config'] = myoldconfigs
                else:
                    self.defconfdict['all_user_config'] += myoldconfigs

            self.defconfdict['user_config'] = str(self.userconfigfilename)
            self.writeDefaultConfStore()
        else:
            # print("No user Tokenfile  found to set as default store")
            response['message'] = str("No user Token file found " +
                                      " cannot set any other default store.")
        return response

    def resetUserDefaultStore(self):
        """ Reset the Default store for AuthToken Manager."""
        response = dict()
        response['status'] = True
        response['message'] = "Success"
        if self.userconfigfilename is not None:
            self.defconfdict['previous_user_config'] = self.userconfigfilename
            myoldconfigs = list([str(self.userconfigfilename)])
            if "all_user_config" not in self.defconfdict.keys():
                self.defconfdict['all_user_config'] = myoldconfigs
            else:
                self.defconfdict['all_user_config'] += myoldconfigs
            del self.defconfdict['user_config']
            self.writeDefaultConfStore()
        else:
            # print("No user token file found nothing to reset")
            response['message'] = "No user token file found nothing to reset."
        return response

    def debugshow(self):
        """ Display AuthToken Manager configuration and AuthTokens."""
        print("Default Confg File    :", self.defconfigfilename)
        print("Default Token File    :", self.deftokenfilename)
        print("User Confg File       :", self.userconfigfilename)
        print("User Token File       :", self.usertokenfilename)

        print("Default Config Store  :", self.formatOutput(self.defconfdict))
        if self.userconfigfilename is not None:
            print("User Config Store     :",
                  self.formatOutput(self.userconfdict))
        print("Token Store           :", self.formatOutput(self.tokendict))
        return True

    def show(self):
        """ Display AuthToken Manager configuration and AuthTokens."""
        if self.userconfigfilename is not None:
            print("Confg File            :", self.userconfigfilename)
            print("Token File            :", self.usertokenfilename)
        else:
            print("Confg File            :", self.defconfigfilename)
            print("Token File            :", self.deftokenfilename)

        self.debug = False
        print("Token Store           :", self.formatOutput(self.tokendict))
        self.debug = True
        return True

    def migrate(self, tokenManager):
        """ Migrate AuthToken manager from another instance."""
        response = dict()
        response['status'] = True
        response['message'] = "Success"
        for itertoken in tokenManager.tokenlist:
            newauth = auth_token()
            newauth = itertoken
            ret = self.addToken(newauth)
            if ret is False:
                return ret
        return response

    @staticmethod
    def getAuthTokenInstance(ip, user, token):
        newAuth = auth_token()
        newAuth.setValue(ip, user, token)
        return newAuth

    @staticmethod
    def isvalidconfig(filename):
        if filename is None:
            return False
        tokenpath = Path(filename)
        if tokenpath.exists():
            return True
        return False
