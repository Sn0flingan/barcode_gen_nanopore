# barcode_gen.py
#
# Runs on Python3
#
# Created by Alice (Sn0flingan) on 2018-07-13
#

import argparse
from random import choice
from Levenshtein import distance
from progress.counter import Counter

def main():
    args = get_arguments()
    if args.verbosity >= 1:
        print("\n--- Generating barcodes ---")
    barcodes =[]
    for i in range(args.numOfBc):
        barcode = generate_barcode(args.length, "")
        if not len(barcodes) == 0:
            if args.verbosity >=2:
                c = Counter("    Barcode candidate no: ")
            while min(distance(barcode,previous_bc) for previous_bc in barcodes)<=args.distance:
                barcode = generate_barcode(args.length, "")
                if args.verbosity >=2:
                    c.next()
            if args.verbosity >=2:
                c.finish()
                print("")
        barcodes.append(barcode)
        if args.verbosity >= 1:
            print('Barcode {}: {}'.format(i+1, barcode))
    write_2_file(barcodes, args.output, args.verbosity)
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
    parser.add_argument("-v", "--verbosity", help="adjust level of console output",
                        default=0, type=int)
    args = parser.parse_args()
    if args.verbosity >= 1:
        print("\n--- Input arguments parsed ---")
        print("Length: {}".format(args.length))
        print("Number of barcodes: {}".format(args.numOfBc))
        print("Minimum distance: {}".format(args.distance))
        print("Output file: {}".format(args.output))
        print("Verbosity: {}".format(args.verbosity))
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

def write_2_file(barcodes, file, verbosity):
    filehandle = open(file, 'w')
    formated_barcodes = ['bc_{}\t{}\n'.format(idx+1, barcode) for idx, barcode in enumerate(barcodes)]
    filehandle.writelines(formated_barcodes)
    filehandle.close()
    if verbosity >= 1:
        print("\n--- Saved results ---")
        print("Saved barcodes to: {}".format(file))

main()
