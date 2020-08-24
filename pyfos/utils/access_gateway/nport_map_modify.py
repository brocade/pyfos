#!/usr/bin/env python3

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

"""

:mod:`nport_map_modify` - PyFOS util for updating F-port to N-port mappings
***********************************************************************************
The :mod:`nport_map_modify` provides option to modify N-port mappings,
Failover and Failback modes

This module can be used to modify N-port mappings, Failover and Failback modes.

* inputs:

|  Infrastructure options:

  | -i,--ipaddr=IPADDR     IP address of FOS switch
  | -L,--login=LOGIN       login name.
  | -P,--password=PASSWORD password.
  | -f,--vfid=VFID         VFID to which the request is directed to [OPTIONAL].
  | -s,--secured=MODE      HTTPS mode "self" or "CA" [OPTIONAL].
  | -v,--verbose           verbose mode[OPTIONAL].

|  Util scripts options:

  | --static-f-ports=STATIC-F-PORTS           List of statically mapped F-ports
  | --config-f-ports=CONFIG-F-PORTS           List of mapped F-ports
  | --n-port=N-PORT                           N-Port Name
  | --failback=FAILBACK                       Failback mode of N-port <0|1>
  | --failover=FAILOVER                       Failover mode of N-port <0|1>
  | --preferred-f-ports=CONFIG-F-PORTS        List of preferred mapped F-ports

* outputs:

    * Status of the mappings delete operation

.. function:: nport_map_modify.set_mapped_fports(session, nport, mfports)

    * Configures a specified list of F_Ports to be mapped to a given N_Port

        Example usage of the method::

            ret = nport_map_modify.set_mapped_fports(session, nport, mfports)
            print (ret)

        Details::

            nport_obj = n_port_map()
            nport_obj.set_n_port(nport)
            if mfports is not None:
                nport_obj.set_configured_f_port_list_f_port(mfports)

            result = _set_access_gateway_nportmap(session, nport_obj)

        * inputs:
            :param session: session returned by login.
            :param N-port: N-port identifier in slot/port format.
            :param mfports: F-ports to be mapped to N-port.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

1. Configures a specified list of F_Ports to be mapped to a given N_Port.
This new map configuration will overwrite any existing map configuration
for the specified N_Port.

.. function:: nport_map_modify.set_static_fports(session, nport, sfports)

     * Statically maps the specified list of F-Ports to a given N-port.

        Example usage of the method::

            ret = nport_map_modify.set_static_fports(session, nport, sfports)
            print (ret)

        Details::

            nport_obj = n_port_map()
            nport_obj.set_n_port(nport)
            if sfports is not None:
                nport_obj.set_configured_f_port_list_f_port(sfports)

            result = _set_access_gateway_nportmap(session, nport_obj)

        * inputs:
            :param session: session returned by login.
            :param N-port: N-port identifier in slot/port format.
            :param sfports: F-ports to be statically mapped to N-port.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

1. Configures a specified list of F_Ports to be statically mapped to a given
N_Port. This new map configuration will overwrite any existing static map
configuration for the specified N_Port.

.. function:: nport_map_modify.set_failback_mode(session, nport, failbackmode)

    * Configures Failback mode for N-Ports

     Example usage of the method::

            ret = nportmapmodify.set_failback_mode(
                     session, nport, failbackmode)
            print (ret)

        Details::

            nport_obj = n_port_map()
            nport_obj.set_n_port(nport)
            nport_obj.set_failback_mode(failbackmode)
            result = _set_access_gateway_nportmap(session, nport_obj)

        * inputs:
            :param session: session returned by login.
            :param N-port: N-port identifier in slot/port format.
            :param failback: Failback mode for a given N-port.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*
         1. Configures Failback mode for N-port

.. function:: nport_map_modify.set_failover_mode(session, nport, failovermode)

    * Configures Failover mode for given N_Port

        Example usage of the method::

            ret = nportmapmodify.set_failover_mode(
                   session, nport, failovermode)
            print (ret)

        Details::

            nport_obj = n_port_map()
            nport_obj.set_n_port(nport)
            nport_obj.set_failover_mode(failovermode)
            result = _set_access_gateway_nportmap(session, nport_obj)

        * inputs:
            :param session: session returned by login.
            :param N-port: N-port identifier in slot/port format.
            :param failover: Failover mode for a given N-port.

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

       1. Configures Failover mode for N-port

.. function:: nport_map_modify.set_preferred_fports(session, nport, preffports)

     * The specified list of F-ports sets as preferred N_Port.

        Example usage of the method::

            ret = nport_map_modify.set_preferred_fports\
(session, nport, preffports)
            print (ret)

        Details::

            nport_obj = n_port_map()
            nport_obj.set_n_port(nport)
            if preffports is not None:
                nport_obj.set_preferred_f_ports_preferred_f_port(preffports)

            result = _set_access_gateway_nportmap(session, nport_obj)

        * inputs:
            :param session: session returned by login.
            :param N-port: N-port identifier in slot/port format.
            :param preffports: Sets the preferred N_Port for the F_Ports

        * outputs:
            :rtype: dictionary of return status matching rest response

        *use cases*

          1. Configures a specified list of F_Ports to be preferred mapped
             to a given N_Port. This new map configuration will overwrite
             any existing preferred mapping configuration for the specified
             N_Port.
"""

import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.utils import brcd_util
from pyfos.pyfos_brocade_access_gateway import n_port_map


def _set_access_gateway_nportmap(session, restobject):
    return restobject.patch(session)


def set_mapped_fports(session, nport, mfports):
    nport_obj = n_port_map()
    nport_obj.set_n_port(nport)
    if mfports is not None:
        nport_obj.set_configured_f_port_list_f_port(mfports)
    result = _set_access_gateway_nportmap(session, nport_obj)
    return result


def set_static_fports(session, nport, sfports):
    nport_obj = n_port_map()
    nport_obj.set_n_port(nport)
    if sfports is not None:
        nport_obj.set_static_f_port_list_f_port(sfports)
    result = _set_access_gateway_nportmap(session, nport_obj)
    return result


def set_preferred_fports(session, nport, preffports):
    nport_obj = n_port_map()
    nport_obj.set_n_port(nport)
    if preffports is not None:
        nport_obj.set_preferred_f_ports_preferred_f_port(preffports)
    result = _set_access_gateway_nportmap(session, nport_obj)
    return result


def set_failback_mode(session, nport, failbackmode):
    nport_obj = n_port_map()
    nport_obj.set_n_port(nport)
    nport_obj.set_failback_mode(failbackmode)
    result = _set_access_gateway_nportmap(session, nport_obj)
    return result


def set_failover_mode(session, nport, failovermode):
    nport_obj = n_port_map()
    nport_obj.set_n_port(nport)
    nport_obj.set_failover_mode(failovermode)
    result = _set_access_gateway_nportmap(session, nport_obj)
    return result


def validate(nportmap_obj):
    if (nportmap_obj.peek_n_port() is None or
            (not nportmap_obj.peek_configured_f_port_list_f_port() and
             not nportmap_obj.peek_static_f_port_list_f_port() and
             not nportmap_obj.peek_preferred_f_ports_preferred_f_port() and
             nportmap_obj.peek_failover_enabled() is None and
             nportmap_obj.peek_failback_enabled() is None)):
        return 1
    return 0


def main(argv):

    # Print arguments
    # print(sys.argv[1:])

    filters = [
        'n_port', 'configured_f_port_list_f_port', 'static_f_port_list_f_port',
        'preferred_f_ports_preferred_f_port', 'failback_enabled',
        'failover_enabled']
    inputs = brcd_util.parse(argv, n_port_map, filters, validate)

    session = brcd_util.getsession(inputs)

    result = _set_access_gateway_nportmap(
        inputs['session'], inputs['utilobject'])
    pyfos_util.response_print(result)

    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
