#!/usr/bin/python3

import argparse
from socket import getfqdn


# create parser
parser = argparse.ArgumentParser(
    prog="Network Survival Kit",
    description="Command line networking tool kit"
)

parser.add_argument("ip", nargs='?', default='', help="Number of execution threads")
# parser.add_argument("--protocol", choices=['tcp','icmp'], help="Network Protocol")

args = parser.parse_args()
print(args)

ip = args.ip or ''



def sys_info_tool(ip):
    host_name = getfqdn()
    print('The hostname is: {}'.format(host_name))
    return host_name

# def main():
    # sys_info_tool(ip)


sys_info_tool(ip)
