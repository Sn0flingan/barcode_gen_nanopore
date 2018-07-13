# barcode_gen.py
#
# Runs on Python3
#
# Created by Alice (Sn0flingan) on 2018-07-13
#

import argparse

def main():
    args = get_arguments()

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", help="length of barcodes",
                        default=12, type=int)
    parser.add_argument("-n", help="number of barcodes to generate",
                        default=2, type=int)
    parser.add_argument("-o", "--output", help="name of output file",
                        default="barcodes.txt")
    args = parser.parse_args()
    return args

main()
