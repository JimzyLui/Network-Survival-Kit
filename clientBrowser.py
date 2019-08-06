#!/usr/bin/python3

## Client Browser** - 
# This tool will act as your client browswer to pull html from any domain.
#   - This tool will make use of the urllib module.
#   - It will be able to print the url, 
#       status code of request, 
#       request header info, 
#       server info, and the html.

import argparse
import urllib.request


def client_browser(url, verbose_tf):
    url = check_url(url)
    req = urllib.request.Request(url)
    # print(req)
    with urllib.request.urlopen(req) as obj_response:
        # html = obj_response.read().decode("utf-8")
        #print(html)
        url_real = obj_response.geturl()
        info = obj_response.info()
        statuscode = obj_response.getcode()
        header = obj_response.getheaders()
        print('URL: {}'.format(url))
        print(f'Real URL: {url_real}')
        print('Request Status: {}'.format(statuscode))
        # print_header(header)
        # html = obj_response.read()
        print(f'Request Header Info: {header}')
        print(f'Server Info: {info}')
        html = obj_response.read(9000).decode('utf-8')
        print(f"HTML:\n{html}")


def check_url(url):
    if url[4] =='http':
        return url
    elif url[3]=='ftp':
        return url
    elif url[3]=='udp':
        return url
    else:
        url = 'http://' + url
        return url


def print_header(hdr):
    # print(hdr)
    print('Header: ')
    for h in hdr:
        print(" {h}".format(h))



def print_rpt_line(port, status):
    print("Port {}: {}".format(port, status))


if __name__ == "__main__":
    # create parser
    parser = argparse.ArgumentParser(
        prog="clientBrowser",
        description="Pulls html from any domain",
        add_help=True
    )

    parser.add_argument("url", help="Domain or IP address")
    parser.add_argument("--verbose", action='store_true', help="Show processing details")
    args = parser.parse_args()
    verbose = args.verbose
    if verbose:
        print('url: {}'.format(args.url))
                      
    client_browser(args.url, verbose)

