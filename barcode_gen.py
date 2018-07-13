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
    barcodes =[]
    for i in range(args.numOfBc):
        barcode = generate_barcode(args.length, [])
        barcodes.append(barcode)
    print(barcodes)
    return

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", help="length of barcodes",
                        default=12, type=int)
    parser.add_argument("-n", "--numOfBc", help="number of barcodes to generate",
                        default=2, type=int)
    parser.add_argument("-o", "--output", help="name of output file",
                        default="barcodes.txt")
    args = parser.parse_args()
    return args

def generate_barcode(bc_len, bc):
    if bc_len == 0:
        return bc
    next_base = random.choice("atgc")
    if not len(bc) == 0:
        while next_base == bc[-1]:
            next_base = random.choice("atgc")
    bc.append(next_base)
    return generate_barcode(bc_len-1, bc)

main()
