#!/usr/bin/env python3

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

:mod:`extensiontunneldelete` - PyFOS util for deleting a tunnel.
********************************************************************************
The :mod:`extensiontunneldelete` provides tunnel deletion functionality.

This module is a standalone script that can be used to delete an extension
tunnel.

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * -n=<name>: slot/port name of the tunnel to be deleted.
 
* outputs:
    * Python dictionary content with RESTCONF response data
    
.. function:: extensiontunneldelete.delete_extension_tunnel(session, name)
    
    *Delete extension tunnel* 

        Example usage of the method::
        
            ret = extensiontunneldelete.delete_extension_tunnel(session, name)
            print (ret)
                
        Details::
        
            tunnel = {
                            "name": name,
 
                      }
            result = extensiontunneldelete._delete_extension_tunnel(session, tunnel)

        * inputs:
            :param session: session returned by login
            :param name: VE port name expressed as slot/port.

        * outputs:    
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. Delete an extension tunnel
"""


import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_extension_tunnel import extension_tunnel
import getpass
import getopt
import sys
import pyfos.utils.brcd_util as brcd_util

isHttps = "0"

def parse_tunnel(user_command, inputs,  value_dict):
	try:
		opts, args = getopt.getopt(user_command,"i:f:n:a:p:x:l:c:F:I:",
                ["switch=","vfid=","name=","admin-enabled=", "ipsec-policy=",
                 "ip-extension=","load-level=", "compression-tunnel=",
                 "fc-compression=", "ip-compression=" ])
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	status = 0
	compressionprotocol=dict()
	for opt, arg in opts:
		if opt in ("-i", "--switch"):
			inputs.update({'switch': arg})
		elif opt in ("-f", "--vfid="):
			inputs.update({'fid': arg})
		if opt in ("-n", "--name"):
			value_dict.update({'name': arg})
		elif opt in ("-a", "--admin-enabled="):
			value_dict.update({'admin-enabled': arg})	
		elif opt in ("-p", "--ipsec-policy="):
			value_dict.update({'ipsec-policy': arg})
		elif opt in ("-x", "--ip-extension="):
			value_dict.update({'ip-extension': arg})
		elif opt in ("-l", "--load-level="):
			value_dict.update({'load-level': arg})
		elif opt in ("-c", "--compression-tunnel="):
			value_dict.update({'compression-tunnel': arg})
		elif opt in ("-F", "--fc-compression="):
			compressionprotocol.update({'fc-compression': arg})
			if 'compression-protocol' in value_dict.keys():
				value_dict['compression-protocol'] = compressionprotocol
			else:
				value_dict.update({'compression-protocol':compressionprotocol})
		elif opt in ("-I", "--ip-compression"):
			compressionprotocol.update({'ip-compression': arg})
			if 'compression-protocol' in value_dict.keys():
				value_dict['compression-protocol'] = compressionprotocol
			else:
				value_dict.update({'compression-protocol':compressionprotocol})	
			
	login = input("Login:")
	password = getpass.getpass()
	inputs.update({'login': login})
	inputs.update({'password': password})
	status = 0
	return status


def _delete_extension_tunnel(session, value_dict):
    tnlobject = extension_tunnel(value_dict)
    result = tnlobject.delete(session)
    return result

def delete_extension_tunnel(session, name):
        value_dict = {'name': name}
        result = _delete_extension_tunnel(value_dict)
        return result
  

def usage():
    print ("usage:")
    print ('extensiontunneldelete.py -i <ipaddr> -n <name>')



def main(argv):
    #myinput=str("-i 10.17.3.70  -n 4/19 ")
    #argv = myinput.split()
    value_dict = dict()
    inputs = dict()
    ret = parse_tunnel(argv, inputs, value_dict)

    session = pyfos_auth.login(inputs["login"], inputs["password"],
                               inputs["switch"], isHttps)
    if pyfos_auth.is_failed_login(session):
        print ("login failed because",
            session.get(pyfos_auth.CREDENTIAL_KEY)[pyfos_auth.LOGIN_ERROR_KEY])
        usage()
        sys.exit()

    brcd_util.exit_register(session)

    vfid = None
    if 'vfid' in inputs:
        vfid = inputs['vfid']
        
    if vfid is not None:
        pyfos_auth.vfid_set(session, vfid)

    if "name" not in value_dict:
        pyfos_auth.logout(session)
        usage()
        sys.exit()
      
    result = _delete_extension_tunnel(session, value_dict)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)
    

if __name__ == "__main__": main(sys.argv[1:])
