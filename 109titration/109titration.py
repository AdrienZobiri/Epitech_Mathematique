#! /usr/bin/env python3

from sys import *
import os

def derivative_point(actual, prev, n):
    v_next, ph_next = n
    v, ph = actual
    v_prev, ph_prev = prev
    der_right = (ph_next - ph) / (v_next - v)
    coeff_right = (v - v_prev) / (v_next - v_prev)
    der_left = (ph - ph_prev) / (v - v_prev)
    coeff_left = (v_next - v) / (v_next - v_prev)
    return (der_left * coeff_left) + (der_right * coeff_right)

def interp(x, x_a, x_b, y_a, y_b):
    y = y_a + ((x - x_a) * (y_b - y_a) / (x_b - x_a))
    return y

def get_est_sec_der(bounds):
    first, second, third = bounds
    xa, ya = first
    xb, yb = second
    xc, yc = third
    x = xa
    d_list = []
    while x <= xc:
        if x <= xb:
            d_list.append([x, interp(x, xa, xb, ya, yb)])
        else:
            d_list.append([x, interp(x, xb, xc, yb, yc)])
        x += 0.1
        x = round(x, 2)
    mini = 1000
    ind = 0
    for i in d_list:
        if abs(i[1]) < mini:
            mini = abs(i[1])
            ind = i[0]
    return d_list, ind

def titration():
    try:
        file = open(argv[1], "r")
        values = []
        for line in file.read().split("\n")[:-1]:
            values.append(line.split(";"))
    except:
        exit(84)
    for line in values:
        if not valid_line(line):
            exit(84)
    tr_values = []
    for vol, ph in values:
        tr_values.append([float(vol), float(ph)])
    values = tr_values

    print("Derivative:")
    der = []
    for i in range(1, len(values) - 1):
        volume = values[i][0]
        d = derivative_point(values[i], values[i - 1], values[i + 1])
        der.append([volume, d])
    maxi = 0
    volume_equivalence = 0
    for i in der:
        if i[1] > maxi:
            maxi = i[1]
            volume_equivalence = i[0]
    for volume, k in der:
        print(f"{volume} ml -> {k:.2f}")

    print(f"\nEquivalence point at {volume_equivalence} ml\n\nSecond derivative:")
    sec_der = []
    bounds_index = []
    for i in range(1, len(der) - 1):
        volume = der[i][0]
        d = derivative_point(der[i], der[i - 1], der[i + 1])
        sec_der.append((volume, d))
        if volume == volume_equivalence:
            bounds_index = [len(sec_der) - 2, len(sec_der) - 1, len(sec_der)]
    bounds = []
    for i in bounds_index:
        bounds.append(sec_der[i])
    for volume, k in sec_der:
        print(f"{volume} ml -> {k:.2f}")
    sec_deriv_estimated, volume_equivalence = ((sec_der, sec_der[0][0]), get_est_sec_der(bounds))[len(bounds) > 0]
    if len(bounds) > 0:
        sec_deriv_estimated, volume_equivalence = get_est_sec_der(bounds)
    else:
        sec_deriv_estimated, volume_equivalence = (sec_der, sec_der[0][0])

    print("\nSecond derivative estimated:")
    for volume, k in sec_deriv_estimated:
        print(f"{volume} ml -> {k:.2f}")

    print(f"\nEquivalence point at {volume_equivalence} ml")

def valid_line(line):
    if len(line) != 2:
        return False
    try:
        if float(line[0]) < 0 or float(line[1]) < 0:
            return False
    except:
        return False
    return True

def main():
    if (len(argv) != 2):
        exit (84)
    if (argv[1] == "-h"):
        print ("USAGE\n\t./109titration file\n\nDESCRIPTION\n\tfile\ta csv file containing 'vol;ph' line\n")
        exit(0)
    exist = os.path.isfile(argv[1])
    if not exist:
        exit(84)
    titration()

main()