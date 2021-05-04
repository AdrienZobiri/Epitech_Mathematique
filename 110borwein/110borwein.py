#!/usr/bin/python3

from math import *
import sys
import os

def calcul(n, x):
    if x == 0: return 1
    result = (sin(x) / x)
    j = 3
    for i in range(n):
        result *= sin(x / j) / (x / j)
        j += 2
    return result

def frange(start, end=None, inc=None):
    if end == None:
        end = start + 0.0
        start = 0.0
    inc = (1.0 if inc == None else inc)
    L = []
    while True:
        next = start + len(L) * inc
        if inc > 0 and next >= end or inc < 0 and next <= end:
            break
        L.append(next)
    return L

def midpoint(n):
    result = 0.00
    for i in frange(0, 5000, 0.5):
        result += (calcul(n, (i + (i + 0.5)) / 2)) * 0.5
    print("Midpoint:\nI%d = %.10f\ndiff = %.10f" %(n, result, abs(result - pi/2)))

def trapezoids(n):
    result = 0.00
    for i in frange(0, 5000, 0.5):
        result += ((calcul(n, i) + calcul(n, i + 0.5)) / 2) * 0.5
    print("\nTrapezoidal:\nI%d = %.10f\ndiff = %.10f" %(n, result, abs(result - pi/2)))

def simpson(n):
    result = 0.00
    for i in frange(0, 5000, 0.5):
        result += (((calcul(n, i) + calcul(n, i + 0.5)) + (4 * calcul(n, (i + (i + 0.5)) / 2))) / 6) * 0.5
    print("\nSimpson:\nI%d = %.10f\ndiff = %.10f" %(n, result, abs(result - pi/2)))

def main():
    if (len(sys.argv) != 2):
        exit (84)
    if (sys.argv[1] == "-h"):
        print ("USAGE\n\t./110borwein n\n\nDESCRIPTION\n\t constant defining the integral to be computed\n")
        exit(0)
    try:
        n = int(sys.argv[1])
    except ValueError:
        exit(84)
    if n < 0:
        exit(84)
    midpoint(n)
    trapezoids(n)
    simpson(n)

main()