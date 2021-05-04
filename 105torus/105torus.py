#! /usr/bin/env python3

import sys
import math

def division(a, b):
    c = (a+b)/2
    return c

def equation(a, b, c, d, f, g, h, j):
    fa = (j*pow(a, 4))+(h*pow(a, 3))+(g*pow(a, 2))+(f*a)+d
    fb = (j*pow(b, 4))+(h*pow(b, 3))+(g*pow(b, 2))+(f*b)+d
    fc = (j*pow(c, 4))+(h*pow(c, 3))+(g*pow(c, 2))+(f*c)+d
    if (fa*fc < 0):
        return a, c, fc
    else:
        return b, c, fc


def gest_err():
    strlen = len(sys.argv)
    if sys.argv[1] == "-h":
        print("")
        exit(105)
    if (strlen != 8):
        print("you do a error in the values. use -h for mor information.")
        exit(84)

def main():
    gest_err()
    a = 1
    b = 0
    c = 0.5
    option = float(sys.argv[1])
    d = float(sys.argv[2])
    f = float(sys.argv[3])
    g = float(sys.argv[4])
    h = float(sys.argv[5])
    j = float(sys.argv[6])
    n = int(sys.argv[7])
    result = 0.5
    while (result >= pow(10, -n) or result <= -pow(10, -n)):
        c = division(a, b)
        a, b, result = equation(a, b, c, d, f, g, h, j)
        z = float("{:.{pre}f}".format(b, pre=n))
        if (z == b):
            print("x = {:.{pre}g}".format(b, pre=n))
        else:
            print("x = {:.{pre}f}".format(b, pre=n))
        if (b < 0 or b > 1):
            return 84
main()