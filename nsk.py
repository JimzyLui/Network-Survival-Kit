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

    parser.add_argument("--collect", action='store_true', help="collect the data and print out a summary report")
    parser.add_argument("--ip_map", help="ip mapping")
    parser.add_argument("--mac_lookup", help="mac address lookup")
    parser.add_argument("--port_scan", nargs=3, help="port scanner")
    parser.add_argument("--sys_info", help="system info")
    parser.add_argument("--client_browser", help="client browser")
    parser.add_argument("--verbose", action='store_true', help="Show processing details")

    args = parser.parse_args()
    #print(args)

    collect_data = args.collect
    if args.ip_map:
        ipMapping.run(args.ip_map)
    if args.mac_lookup:
        macAddressLookup.run(args.mac_lookup)
    # if args.port_scan:
        # portScanner.run(args.port_scan)
    if args.sys_info:
        sysInfoTool.run(args.sys_info)
    if args.client_browser:
        clientBrowser.run(args.client_browser, args.verbose)

