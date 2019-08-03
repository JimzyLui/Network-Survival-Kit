#!/usr/bin/python3

## **3. Port Scanner** - 
# This tool will scan for open ports on any domain or IP 
# and return a report when completed.
#  - This tool will make use of the socket and sys modules.
#  - It will be able to scan any range of ports.
#  - It will generate a report in the format of: "Port 80: OPEN"


import argparse
import socket
import sys


# create parser
parser = argparse.ArgumentParser(
    prog="Network Survival Kit",
    description="Command line networking tool kit"
)

parser.add_argument("url", nargs='?', default='', help="Get info from URL")

args = parser.parse_args()
print(args)

url = args.url or ''

def port_scanner(domain_or_ip):
    pass

def print_rpt_line(port, status):
    print("Port {}: {}".format(port, status))
