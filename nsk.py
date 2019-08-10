#!/usr/bin/python3

# This is the main program


import argparse
import dataCollector
import ipMapping
import macAddressLookup
import portScanner
import sysInfoTool
import clientBrowser


if __name__ == "__main__":
    # create parser
    parser = argparse.ArgumentParser(
        prog="nsk",
        description="Command line networking tool kit"
    )

    parser.add_argument("-c", "--collect", action='store_true', help="collect the data and print out a summary report")
    parser.add_argument("-i", "--ip_map", dest='ip', help="ip mapping")
    parser.add_argument("-m", "--mac_lookup", dest='mac', help="mac address lookup")
    parser.add_argument("-p", "--port_scan", dest='p', nargs='+', help="port scanner")
    parser.add_argument("-s", "--sys_info", help="system info")
    parser.add_argument("-b", "--client_browser", dest='url', help="client browser")
    parser.add_argument("-v", "--verbose", action='store_true', help="Show processing details")

    args = parser.parse_args()
    print(args)

    collect_data = args.collect
    if args.ip:
        ipMapping.run(args.ip)
    if args.mac:
        macAddressLookup.run(args.mac)
    if args.p:
        portScanner.run(args.p[0], args.p[1],args.p[2], args.verbose)
    if args.sys_info:
        sysInfoTool.run(args.sys_info)
    if args.url:
        clientBrowser.run(args.url, args.verbose)
    # still have to read or cat 'rpt.txt'

