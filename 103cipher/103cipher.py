#! /usr/bin/env python3

# decript
# for i in range(0, my_len):
#     j = 0
#     for j in range (0, my_len - 1):
#         print("{:<8.3f}".format(matrice_key[i][j]), end = "")
#     print("{:.3f}".format(matrice_key[i][my_len - 1]))

import sys
import math

matrice_key = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def clef(key):
    size_key = len(key)
    if (size_key > 9):
        exit(84)
    for x in range(0, size_key):
        matrice_key[x] = ord(key[x])

def convert_str(string, size_string, size_string_malloc):
    matrice_string = [0] * size_string_malloc
    for x in range(0, size_string):
        matrice_string[x] = ord(string[x])
    return matrice_string

def multiplication(string, key, size_string, size_string_malloc):
    m = [0] * size_string_malloc
    z = 0
    for x in range(0, (size_string_malloc), 3):
        for y in range(0, 3):
            m[z] = string[0 + x] * key[0 + y] + string[1 + x] * key[3 + y] + string[2 + x] * key[6 + y]
            z = z + 1
    return m

def size_message(string):
    size_string = len(string)
    if (size_string % 3 != 0):
        size_string_malloc = size_string + 1
        if (size_string_malloc % 3 != 0):
            size_string_malloc = size_string_malloc + 1
    else:
        size_string_malloc = size_string
    return size_string, size_string_malloc

def encrypt(string):
    size_string, size_string_malloc = size_message(string)
    matrice_string = convert_str(string, size_string, size_string_malloc)
    encrypt_verssion = multiplication(matrice_string, matrice_key, size_string, size_string_malloc)
    return encrypt_verssion

# def deter(a, b, c, d)
#     a = abs(a)
#     b = abs(b)
#     c = abs(c)
#     d = abs(d)
#     detA = a * d - b * c
#     return detA

# def reverse(a, b, c, d):
#     detA = deter(a, b, c, d)
#     if (detA != 0)
#         det_A = [d, -c, -b, a]
#     return det_A

def decript():
    return 0

def printer_final(result):
    print("Key matrix:")
    for i in range(0, 9):
        if ((i + 1)  % 3 == 0 and i != 0):
            if (matrice_key[i] > 99):
                print("{:<3}".format(matrice_key[i]))
            elif (matrice_key[i] > 9):
                print("{:<2}".format(matrice_key[i]))
            elif (matrice_key[i] >= 0):
                print("{:<1}".format(matrice_key[i]))
        else:
            print("{:<8}".format(matrice_key[i]), end = "")
    print("")
    print(*result)

def gest_err():
    strlen = len(sys.argv)
    if sys.argv[1] == "-h":
        print("this programme do a encryptage or decrypatage. you need to select 3 informations.\n The first argument it's what u want to change.\n The seconde arguments is your key, max 9.\n Select 0 if you want to encrypt and select 1 if you want decryption.\n")
        exit(84)
    if (strlen != 4):
        print("you do a error in the values. use -h for mor information.")
        exit(84)
    if (len(sys.argv[3]) > 1):
        print("Only one value for choice your action")
        exit(84)
    if (sys.argv[3] != "0" and sys.argv[3] != "1"):
        print("the laste value is only 1 OR 0")
        exit(84)

def main():
    gest_err()
    clef(sys.argv[2])
    if (sys.argv[3] == "0"):
        result = encrypt(sys.argv[1])
    elif (sys.argv[3] == "1"):
        result = decript(sys.argv[1])
        print("TEST 1")
    printer_final(result)

main()