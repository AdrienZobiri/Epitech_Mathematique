#! /usr/bin/env python3

from math import *
from sys import *

def main():
    if (len(argv) >= 2 and (len(argv) - 1) % 2 == 0):
        if (len(argv) == 2):
            if (argv[1] == "-h"):
                print ("USAGE\n\t./107transfer [num den]*\n\nDESCRIPTION\n\tnum\tpolynomial numerator defined by its coefficients\n\tden\tpolynomial denominator defined by its coefficients\n")
                exit(0)
    else:
        exit (84)
    y = 1
    x = 0.000
    while (x <= 1.001):
        result = 1.0
        for y in range(1, len(argv), 2):
            try:
                num = [int(n) for n in argv[y].split('*')]
                dem = [int(n) for n in argv[y + 1].split('*')]
            except:
                exit(84)
            a = 0
            b = 0
            for i in range(len(num)):
                a += num[i] * x ** i
            for i in range(len(dem)):
                b += dem[i] * x ** i
            if (b == 0):
                exit (84)
            result *= (a / b)
        print("{:.3f} -> {:.5f}".format(x, result))
        x += 0.001

main()