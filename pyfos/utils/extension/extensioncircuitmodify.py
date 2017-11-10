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

:mod:`extensioncircuitmodify` - PyFOS util for modifying a circuit object.
********************************************************************************
The :mod:`extensioncircuitmodify` provides circuit modify functionality.

This module is a standalone script that can be used to modify an extension
circuit.

* inputs:
    * -L=<login>: Login ID. If not provided, interactive
        prompt will request one.
    * -P=<password>: Password. If not provided, interactive
        prompt will request one.
    * -i=<IP address>: IP address
    * -n=<name>: slot/port name of the tunnel object for which this
        circuit is created.
    * -c=<circuit-id>: circuit Id of the circuit
    * -S=<local-ip-address>: Local IP Address of the circuit.
    * -D=<remote-ip-address>: Remote IP Address of the circuit.
    * -b=<minimum-communication-rate>: min comm rate of the circuit.
    * -B=<maximum-communication-rate>: max comm rate of the circuit.
    * -f=<VFID>: VFID or -1 if VF is disabled. If unspecified,
        VFID of 128 is assumed.
    * -a=<admin-enabled>: If circuit is admin enabled
* outputs:
    * Python dictionary content with RESTCONF response data 


.. function:: extensioncircuitmodify.modify_extension_circuit(session, name, cid, local,\
remote, minB = 500000, maxB=50000)
    
    *Create extension circuit* 

        Example usage of the method::
        
                ret = extensioncircuitmodify.modify_extension_circuit(session, name, cid,\
                local, remote, minB, maxB)
                print (ret)
                
        Details::
        
            circuit = {
                            "name": name,
                            "circuit-id": circuit,
                            "local-ip-address": local,
                            "remote-ip-address" : remote,
                            "minimum-communication-rate": minB,
                            "maximum-communication-rate": maxB,
                      }
            result = extensioncircuitmodify._modify_extension_circuit(session, circuit)

        * inputs:
            :param session: session returned by login
            :param name: VE port name expressed as slot/port.
            :param cid: circuit ID .
            :param local: circuit local IP address.
            :param remote: circuit Remote IP Address.
            :param minB: Min comm rate for the circuit.
            :param maxB: Max comm rate for the circuit.

        * outputs:    
            :rtype: dictionary of return status matching rest response

        *use cases*

        1. modify a circuit to an existing tunnel

"""

import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_util as pyfos_util
from pyfos.pyfos_extension_circuit import extension_circuit
import getpass
import getopt
import sys
import pyfos.utils.brcd_util as brcd_util

isHttps = "0"

def parse_ciruit(user_command, inputs,  value_dict):
	try:
		opts, args = getopt.getopt(user_command,"i:f:n:a:c:S:D:b:B:",
                  ["switch=","vfid=","name=","admin-enabled=", "circuit-id=",
                   "local-ip-address=","remote-ip-address",
                   "minimum-communication-rate=","maximum-communication-rate"])
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	status = 1
	compressionprotocol=dict()
	for opt, arg in opts:
		if opt in ("-i", "--switch"):
			inputs.update({'switch': arg})
			status = 0
		elif opt in ("-f", "--vfid="):
			inputs.update({'fid': arg})
		if opt in ("-n", "--name"):
			value_dict.update({'name': arg})
		if opt in ("-c", "--circuit-id"):
			value_dict.update({'circuit-id': arg})
		elif opt in ("-a", "--admin-enabled="):
			value_dict.update({'admin-enabled': arg})
		elif opt in ("-p", "--ipsec-policy="):
			value_dict.update({'ipsec-policy': arg})
		elif opt in ("-S", "--local-ip-address="):
			value_dict.update({'local-ip-address': arg})
		elif opt in ("-D", "--remote-ip-address="):
			value_dict.update({'remote-ip-address': arg})
		elif opt in ("-b", "--minimum-communication-rate="):
			value_dict.update({'minimum-communication-rate': arg})
		elif opt in ("-B", "--maximum-communication-rate="):
			value_dict.update({'maximum-communication-rate': arg})
	if status == 0:	
		login = input("Login:")
		password = getpass.getpass()
		inputs.update({'login': login})
		inputs.update({'password': password})

	return status


def _modify_extension_circuit(session, value_dict):
	cirobject = extension_circuit()
	cirobject.load(value_dict, 1)
	result = cirobject.patch(session)
	return result

def modify_extension_circuit(session, name, cid, local, remote,
                             minB = 500000, maxB=50000):
        value_dict = {'name': name, 'circuit-id': cid,
                      'local-ip-address':local,
                      'remote-ip-address':remote,
                      'minimum-communication-rate':minB,
                      'maximum-communication-rate': maxB }
        result = _modify_extension_circuit(value_dict)
        return result
  

def usage():
	print ("usage:")
	print ('extensioncircuitmodify.py -i <ipaddr> -n <name> -a <admin-enabled> ' +\
               '-c <circuit-id> -S <local-ip-address> -D<remote-ip-address> ' +\
               '-b<minimum-communication-rate> -B<maximum-communication-rate>')



def main(argv):
	#myinput=str("-i 10.17.3.70  -n 4/19 -c 0 -S 134.10.10.1" +\
        #            "-D 154.10.10.1 -b 100000 -B 100000")
	#argv = myinput.split()
	value_dict = dict()
	inputs = dict()
	ret = parse_ciruit(argv, inputs, value_dict)
	if ret !=0:
		usage()
		sys.exit()

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

	result = _modify_extension_circuit(session, value_dict)
	pyfos_util.response_print(result)
	pyfos_auth.logout(session)
    

if __name__ == "__main__": main(sys.argv[1:])
