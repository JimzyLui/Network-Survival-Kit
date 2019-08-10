#!/usr/bin/python3

## **1. System Info Tool** - This tool will grab the hostname of the target machine.
#   - This tool will need to use the socket module.
#   - It will print the hostname to stdout in the format of: "The hostname is: NoSoupForYou"

import argparse
from socket import getfqdn


def run(ip):
    host_name = getfqdn()
    print('The hostname is: {}'.format(host_name))
    return host_name

if __name__ == "__main__":
    # create parser
    parser = argparse.ArgumentParser(
        prog="sysInfoTool",
        description="Get the hostname of an ip address"
    )

    parser.add_argument("ip", nargs='?', default='', help="Number of execution threads")

    args = parser.parse_args()
    print(args)

    run(args.ip)
