#! /usr/bin/env python3

from math import *
from sys import *

## error handless
def transform_to_float():
    try:
        for i in range(2, len(argv)):
            argv[i] = float(argv[i])
    except ValueError:
        print("Argument isn't a number")
        exit(84)

def try_size_of_matrix():
    szmat = trunc(sqrt(len(argv) - 2))
    if trunc(sqrt(len(argv) - 2)) ** 2 != (len(argv) - 2):
        print("Missing arguments.\nUsage: ./108trigo fun a0 a1 a2 ...")
        exit(84)
    return szmat

##tools mathematical
def identity_mat(n):
    tmp = []
    for x in range(n):
        ident = []
        for y in range(n):
            ident.append(1 if y == x else 0)
        tmp.append(ident)
    return tmp

def init_mat(n, z):
    tmp = []
    for x in range(n):
        ident = []
        for y in range(n):
            ident.append(z)
        tmp.append(ident)
    return tmp

def multi_mat(mat1, mat2):
    tmp = []
    for x in range(len(mat1)):
        mult = []
        for y in range(len(mat2[0])):
            a = 0
            for z in range(len(mat1[0])):
                a += mat1[x][z] * mat2[z][y]
            mult.append(a)
        tmp.append(mult)
    return tmp

def pow_mat(mat, n):
    tmp = mat
    for x in range(n - 1):
        tmp = multi_mat(tmp, mat)
    return tmp

def div_mat(mat, z):
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            mat[x][y] /= z
    return mat

def add_mat(mat1, mat2):
    tmp = []
    for x in range(len(mat1)):
        c = []
        for y in range(len(mat1[0])):
            c.append(mat1[x][y] + mat2[x][y])
        tmp.append(c)
    return tmp

def sub_mat(mat1, mat2):
    tmp = []
    for x in range(len(mat1)):
        c = []
        for y in range(len(mat1[0])):
            c.append(mat1[x][y] - mat2[x][y])
        tmp.append(c)
    return tmp

## function mathematic
def func_exp(tab):
    tmp = identity_mat(len(tab))
    for x in range(1, 50):
        tmp = add_mat(tmp, div_mat(pow_mat(tab, x), factorial(x)))
    return tmp

def func_cos(tab):
    tmp = identity_mat(len(tab))
    for x in range(1, 40):
        if x % 2 == 0:
            tmp = add_mat(tmp, div_mat(pow_mat(tab, 2 * x), factorial(2 * x)))
        else:
            tmp = sub_mat(tmp, div_mat(pow_mat(tab, 2 * x), factorial(2 * x)))
    return tmp

def func_sin(tab):
    tmp = tab
    for x in range(1, 40):
        if x % 2 == 0:
            tmp = add_mat(tmp, div_mat(pow_mat(tab, 2 * x + 1), factorial(2 * x + 1)))
        else:
            tmp = sub_mat(tmp, div_mat(pow_mat(tab, 2 * x + 1), factorial(2 * x + 1)))
    return tmp

def func_cosh(tab):
    tmp = identity_mat(len(tab))
    for x in range(1, 40):
        tmp = add_mat(tmp, div_mat(pow_mat(tab, 2 * x), factorial(2 * x)))
    return tmp

def func_sinh(tab):
    tmp = tab
    for x in range(1, 40):
        tmp = add_mat(tmp, div_mat(pow_mat(tab, 2 * x + 1), factorial(2 * x + 1)))
    return tmp

## what function use
def process(tab):
    action = ["COS", "COSH", "EXP", "SIN", "SINH"]
    func_math = [func_cos, func_cosh, func_exp, func_sin, func_sinh]
    for i in range(len(func_math)):
        if argv[1] == action[i]:
            tab = func_math[i](tab)
    return tab

def main():
    if (len(argv) <= 2):
        exit (84)
    if (argv[1] not in ["EXP", "COS", "SIN", "COSH", "SINH"]):
        exit (84)
    if (len(argv) == 2):
        if (argv[1] == "-h"):
            print ("USAGE\n\t./108trigo fun a0 a1 a2*\n\nDESCRIPTION\n\tfun\tfunction to be applied, among at least “EXP”, “COS”, “SIN”, “COSH” and “SINH”\n\tai\tcoeficients of the matrix\n")
            exit(0)
    transform_to_float()
    szmat = try_size_of_matrix()
    tab = []
    for i in range(int(szmat)):
        tab.append([])
        for j in range(int(szmat)):
            tab[i].append(argv[i * int(szmat) + j + 2])
    tab = process(tab)
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            print("%.2f%c" % (tab[i][j], '\t' if (j != len(tab[i]) - 1) else '\n'), end="")

main()