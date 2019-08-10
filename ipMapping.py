#!/usr/bin/python3

# **2. IP Mapping** - This tool will return the corresponding IP address of any domain entered.
#   - This tool will make use of the socket module.
#   - It will take stdin from the user and return the IP address in the format of: 
#       "The IP address of target is: 58.65.22.14"


import argparse
from socket import gethostbyname
import dataCollector


def run(url):
    dataCollector.start()
    ip = gethostbyname(url)
    rpt_line = print_rpt_line(url, ip)
    dataCollector.collect(rpt_line)
    return ip

def print_rpt_line(url, ip):
    rpt_line = f"The IP address of {url} is: {ip}"
    print(rpt_line)
    return rpt_line


if __name__ == "__main__":
    # create parser
    parser = argparse.ArgumentParser(
        prog="ipMapping",
        description="Command line networking tool kit"
    )

    parser.add_argument("url", nargs='?', default='', help="Get ip from the domain")

    args = parser.parse_args()

    run(args.url)

