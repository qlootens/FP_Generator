#!/usr/bin/python

"""
Customizable FP-Generator + Calculator

Written by Quinten Lootens 2017
For more information, hit me on github (qlootens)!
"""

import sys, generate_fp

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("usage: python fp_cal.py <number of bits power> <number of bits mantisse> <floating point bits>")
        print("Example: python fp_cal.py 3 4 10011001")
        sys.exit(1)


    print(generate_fp.calculate_fp(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]))
    sys.exit()