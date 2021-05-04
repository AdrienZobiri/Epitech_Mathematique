#! /usr/bin/env python3

from math import *
from sys import *

def main():
    if (len(argv) < 3 or len(argv) > 4):
        if (len(argv) == 2):
            if (argv[1] == "-h"):
                print ("USAGE\n    ./106bombyx n [k | i0 i1]\n\nDESCRIPTION\n    n      number of first generation individuals\n    k     growth rate from 1 to 4\n    i0    initial generation (included)\n    i1    final generation (included)")
                exit(0)
            else:
                exit(84)
        else:
            exit(84)
    if (argv[1].isdigit() == False):
        exit(84)
    n = int(argv[1])
    if n < 0:
        exit(84)
    if (len(argv) == 3):
        k = float(argv[2])
        if (k < 1 or k > 4):
            exit(84)
        for x in range (1, 101):
            print(x, "{:.2f}".format(round(n, 2)))
            n = (k * n) * ((1000 - n) / 1000)
    elif (len(argv) == 4):
        for z in range(1, len(argv)):
            if (argv[z].isdigit() == False):
                exit(84)
        sprint = int(argv[2])
        eprint = int(argv[3])
        if (sprint < 0 or eprint < 0):
            exit(84)
        k = 1.00
        for y in range (100, 401):
            n = int(argv[1])
            for x in range (1, sprint):
                n = (k * n) * ((1000 - n) / 1000)
                x = x + 1
            for x in range (sprint, eprint+1):
                print("{:.2f}".format(k), "{:.2f}".format(round(n, 2)))
                n = (k * n) * ((1000 - n) / 1000)
                x = x + 1
            k = k + 0.01

main()