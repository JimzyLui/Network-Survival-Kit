#!/usr/bin/python3

## **6. Data Collector** - This tool will automate transfering of data for all your findings.
#   - This tool will make use of the open() method.
#   - It will be able to save your findings to a standard .txt file when invoked with appropriate formatting in a report format.
#   - HINT: You will need to store results of other tools for this tool to work.


import argparse
import os
from datetime import datetime

class Report:
    pathRpt = os.path.dirname(os.path.realpath(__file__))
    fileNameRpt = 'rpt.txt'
    rptLocation = pathRpt + "//"+fileNameRpt
    pass  

rpt = ''

def setup():
    global rpt 
    rpt = Report()


def start():
    global rpt 
    setup()
    rpt.time_start = datetime.now()

def end():
    global rpt
    rpt.time_end = datetime.now()
    rpt.duration = rpt.time_end - rpt.time_start
    print(f"Time to process: {rpt.duration} seconds")

def collect(strRptRow):
    global rpt
    end()
    write_data(strRptRow)
    pass

def write_data(strRptRow):
    global rpt
    # write data to file
    rptFile = open(rpt.rptLocation, 'a')
    rptFile.write(strRptRow)
    stats = f"\nTime to run: {rpt.duration} ms\n\n"
    rptFile.write(stats)
    rptFile.close()

def read_data():
    global rpt
    # read all data from the report file
    rptFile = open(rpt.rptLocation,'r')
    # print rptFile.read()
    rptFile.close()



'''
if __name__ == "__main__":
    # create parser
    parser = argparse.ArgumentParser(
        prog="data_collector",
        description="stores data within a report"
    )

    parser.add_argument("strReportRow", default='', help="data to save")
    parser.add_argument("--save", nargs='?', default='', help="write data to report")

    args = parser.parse_args()
    print(args)

    data_collector(args.strRptRow)
'''