#!/usr/bin/python3

## **3. Port Scanner** - 
# This tool will scan for open ports on any domain or IP 
# and return a report when completed.
#  - This tool will make use of the socket and sys modules.
#  - It will be able to scan any range of ports.
#  - It will generate a report in the format of: "Port 80: OPEN"

# scan 1-65k? or 45K?

import argparse
import socket
# import sys
import ipMapping


def port_scanner(domain_or_ip, portfrom, portto, verbose_tf):
    ip = ipMapping.ip_mapping(domain_or_ip)

    if portto=='':
        portto = portfrom
        portfrom = 1
    for port in range(int(portfrom), int(portto)):
        # check the port
        scan_port(ip, port, verbose_tf)
    

def scan_port(ip, port, verbose_tf):
    if verbose_tf:
        print('...scanning port {}'.format(port))
        # info = socket.getaddrinfo(ip, port)

    # set the default timeout to 1 sec
    socket.setdefaulttimeout(1)

    # create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # get socket to connect
    response_code = s.connect_ex((ip,port))
    if response_code==0:
        print_rpt_line(port, 'Open')

    s.close()
    # print(info)


def print_rpt_line(port, status):
    print("Port {}: {}".format(port, status))


if __name__ == "__main__":
    # create parser
    parser = argparse.ArgumentParser(
        prog="portScanner",
        description="Scans ports on a host or ip address",
        add_help=True
    )

    parser.add_argument("domain_or_ip", help="Domain or IP address")
    parser.add_argument("--portfrom", default='5', help="Starting port or port range starting at 1")
    # parser.add_argument("-from", default='5', help="Starting port or port range starting at 1")
    parser.add_argument("--portto", default='', help="upper port in port range")
    # parser.add_argument("-to", default='', help="upper port in port range")
    parser.add_argument("--verbose", action='store_true', help="Show processing details")
    args = parser.parse_args()
    verbose = args.verbose
    if verbose:
        print('domain: {}'.format(args.domain_or_ip))
        print('portfrom: {}'.format(args.portfrom))
        print('portto: {}'.format(args.portto))
        # print(args)

    port_scanner(args.domain_or_ip, args.portfrom, args.portto, verbose)

