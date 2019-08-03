#!/usr/bin/python3

## Client Browser** - 
# This tool will act as your client browswer to pull html from any domain.
#   - This tool will make use of the urllib module.
#   - It will be able to print the url, 
#       status code of request, 
#       request header info, 
#       server info, and the html.

import argparse
import urllib


# create parser
parser = argparse.ArgumentParser(
    prog="Network Survival Kit",
    description="Command line networking tool kit"
)

parser.add_argument("url", nargs='?', default='', help="Get info from URL")
# parser.add_argument("--protocol", choices=['tcp','icmp'], help="Network Protocol")

args = parser.parse_args()
print(args)

url = args.url or ''

def client_browser(url):
    pass
