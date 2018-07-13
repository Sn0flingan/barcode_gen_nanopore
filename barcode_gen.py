# barcode_gen.py
#
# Runs on Python3
#
# Created by Alice (Sn0flingan) on 2018-07-13
#

import argparse
from random import choice
from Levenshtein import distance

def main():
    args = get_arguments()
    barcodes =[]
    for i in range(args.numOfBc):
        barcode = generate_barcode(args.length, "")
        if len(barcodes) == 0:
            barcodes.append(barcode)
            continue
        while min(distance(barcode,previous_bc) for previous_bc in barcodes)<=args.distance:
            barcode = generate_barcode(args.length, "")
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
    parser.add_argument("-d", "--distance", help="minimum Levenshtein distance between barcodes",
                        default=2, type=int)
    args = parser.parse_args()
    return args

def generate_barcode(bc_len, bc):
    if bc_len == 0:
        return bc
    next_base = choice("atgc")
    if not len(bc) == 0:
        while next_base == bc[-1]:
            next_base = choice("atgc")
    bc += next_base
    return generate_barcode(bc_len-1, bc)

main()
