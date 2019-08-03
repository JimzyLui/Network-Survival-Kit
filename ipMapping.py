#!/usr/bin/python3

# **2. IP Mapping** - This tool will return the corresponding IP address of any domain entered.
#   - This tool will make use of the socket module.
#   - It will take stdin from the user and return the IP address in the format of: 
#       "The IP address of target is: 58.65.22.14"


import argparse
from socket import gethostbyname


# create parser
parser = argparse.ArgumentParser(
    prog="Network Survival Kit",
    description="Command line networking tool kit"
)

parser.add_argument("url", nargs='?', default='', help="Get ip from the domain")

args = parser.parse_args()
print(args)

url = args.url or ''

def ip_mapper(url):
    ip = gethostbyname(url)
    print_rpt_line(url, ip)
    return ip

def print_rpt_line(url, ip):
    print("The IP address of {} is: {}".format(url, ip))

ip_mapper(url)