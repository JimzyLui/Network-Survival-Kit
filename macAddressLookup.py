#!/usr/bin/python3

# **5. Mac Address Lookup** - This tool will return information on mac addressses.
#   - This tool will use the urllib2, json, and codecs modules.
#   - This tool will make an api call with mac address to http://macvendors.co/api
#   - It will take stndin from user.
#   - It will return a report in format of: "Company Name, Address".


import argparse
import urllib.request
import json
import codecs
import dataCollector



def run(addr):
    dataCollector.start()
    api_url = 'http://macvendors.co/api'
    url_req = f"{api_url}/{addr}/json"
    with urllib.request.urlopen(url_req) as resp:
        results = json.load(resp)

    # print_rpt_line(url, ip)
    rpt_line = print_rpt_line(results['result']['company'], results['result']['address'])
    dataCollector.collect(rpt_line)
    return 



def print_rpt_line(name, address):
    str_rpt = f"{name}, {address}"
    print(str_rpt)
    return str_rpt


if __name__ == "__main__":
    # create parser
    parser = argparse.ArgumentParser(
        prog="macAddressLookup",
        description="Returns information on mac address"
    )
    parser.add_argument("mac_address", default='', help="the mac address in the format XX-XX-XX-XX-XX-XX")
    args = parser.parse_args()
    mac_address = args.mac_address
    # mac_address = 'FC-A1-3E-2A-1C-33'
    mac_address = mac_address.replace('-','').replace(':','').replace('.','').replace(' ','')
    print(f"Mac Address: {mac_address}")

    if len(mac_address) == 12:
        run(mac_address)
    else:
        print(f"Invalid mac address.  It should be in the following format: XX-XX-XX-XX-XX-XX")


    
    

