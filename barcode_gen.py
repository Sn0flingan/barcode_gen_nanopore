# barcode_gen.py
#
# Runs on Python3
#
# Created by Alice (Sn0flingan) on 2018-07-13
#

import argparse
import random

def main():
    args = get_arguments()
    barcode = generate_barcode(args.length, [])
    print(barcode)
    return

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

def generate_barcode(bc_len, bc):
    if bc_len == 0:
        return bc
    bc.append(random.choice("atgc"))
    return generate_barcode(bc_len-1, bc)

main()
