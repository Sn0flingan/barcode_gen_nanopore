# Barcode Generator - Nanopore
Barcode generator tailored for nanopore sequencing.

Features:
- No homopolymers
- Distance threshold in [Levenshtein](https://en.wikipedia.org/wiki/Levenshtein_distance)

## Getting Started
### Installation of prerequisites

- Python3
- Levenshtein package for python (pip for install)

Installing Levenshtein-package:
```
pip install python-levenshtein
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
- Alice Anlind 

## Acknowledgments
- Vidilab's slack channel for RnD for suggestions of improvements 
