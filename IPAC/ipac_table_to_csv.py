"""
    A very  simple script to read an IPAC table and output
    a comma delimited file for easier import into a spreadsheet.

    Author: Jimmy Newland
            https://jimmynewland.com
            newton@jayfox.net
    Last updated: 2019/02/23

    Usage: Invoke the script from the command line.
           python -f ngc3372.tbl -o ngc3372.csv
           or
           python -f ngc3372.tbl -o ngc3372.data -d \t
"""
import argparse
from astropy.io import ascii

# Setup the command line argument parser.
parser = argparse.ArgumentParser(description='Convert an IPAC table file into a comma or tab delimited file')
parser.add_argument('-f', metavar='filename', type=str, help='IPAC table filename', required=True)
parser.add_argument('-o', metavar='output', type=str, help='output filename', required=True)
parser.add_argument('-d', metavar='delimiter', type=str, help='data delimiter (default is comma)', default=',', required=False)
args = parser.parse_args()

with open(args.f) as file:
  data = ascii.read(args.f)
  ascii.write(data, output=args.o, delimiter=args.d)

