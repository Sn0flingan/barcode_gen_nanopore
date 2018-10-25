# Barcode Generator - Nanopore
Barcode generator tailored for nanopore sequencing.

**Features:**
- No homopolymers
- GC-content between 40-60% (can be changed manually in the code)
- Distance threshold in [Levenshtein](https://en.wikipedia.org/wiki/Levenshtein_distance)
- Custom barcode length
- Custom number of barcodes

**Work in progress**
- Custom GC-content setting

**Known issues:**
- When the distance threshold is approximatly half of the barcode length or longer, generating more than 10 barcodes will be costly, in some cases impossible.

## Getting Started
### Installation of prerequisites

- Python3
- Levenshtein package for python (pip for install)
- Progress package - used for verbose output 

Installing Levenshtein-package:
```
pip3 install python-levenshtein
```

Installing progress package:
```
pip3 install progress
```

## Running the script

```
python3 barcode_gen.py
```

Several options are available, check them using the -h och --help flag:
```
python3 barcode_gen.py -h
```

## Authors
- **Alice Anlind** 

## Acknowledgments
- Vidilab's slack channel for RnD for suggestions of improvements 
