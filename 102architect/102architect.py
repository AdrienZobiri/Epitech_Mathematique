#! /usr/bin/env python3

import string
import sys
from math import cos, sin, radians, pi

def test_numbers(fortry):
    string = fortry
    string = string.replace('.','',1)
    if string.strip('-').isnumeric() == True :
        return True
    else :
        return False

def gest_err(nb_action):
    try :
        if sys.argv[1] == "-h":
            print("select first value for the first position and selecte what action you want to do.\n \
            -t for translation and x & y coordonates\n \
            -z for scaling and x & y coordonates\n \
            -r for rotation and degrees\n \
            -s for reflexion and degrees\n \
            in order do you want to execute\n")
            exit(84)
        i = 3
        while i < nb_action - 1:
            if sys.argv[i] == "-t" or sys.argv[i] == "-z" and (nb_action - i) > 1:
                if test_numbers(sys.argv[i + 1]) == True :
                    if test_numbers(sys.argv[i + 2]) == True :
                        i += 3
                    else :
                        print("la deuxième valeur suivante n'est pas un nombre")
                        exit (84)
                else :
                    print("la première valeur suivante n'est pas un nombre")
                    exit(84)

            elif sys.argv[i] == "-r" or sys.argv[i] == "-s" and nb_action - i > 0:
                if test_numbers(sys.argv[i + 1]) == True :
                    i += 2
                else:
                    print("La valeur suivante n'est pas un nombre")
                    exit(84)
            else:
                print("pas de flags a teste")
                exit(84)
        if (i == nb_action):
            return 0
        else :
            print("ERROR arguments\n")
            print("please selecte correct entree. './102architect help' for more information")
            exit(84)
    except :
        print("Error in the values")
        exit(84)

def printer(x0, y0, point_xyz, point_final, matrice_identitee):
    for x in range(0, 3):
        for y in range(0, 3):
            if matrice_identitee[x][y] > -0.005 and matrice_identitee[x][y] < 0.005:
                matrice_identitee[x][y] = 0.00
    matrice_identitee[0][0] = "%.2f"%matrice_identitee[0][0]
    matrice_identitee[0][1] = "%.2f"%matrice_identitee[0][1]
    matrice_identitee[0][2] = "%.2f"%matrice_identitee[0][2]
    matrice_identitee[1][0] = "%.2f"%matrice_identitee[1][0]
    matrice_identitee[1][1] = "%.2f"%matrice_identitee[1][1]
    matrice_identitee[1][2] = "%.2f"%matrice_identitee[1][2]
    matrice_identitee[2][0] = "%.2f"%matrice_identitee[2][0]
    matrice_identitee[2][1] = "%.2f"%matrice_identitee[2][1]
    matrice_identitee[2][2] = "%.2f"%matrice_identitee[2][2]
    print(matrice_identitee[0][0], "  ", matrice_identitee[0][1], "  ", matrice_identitee[0][2])
    print(matrice_identitee[1][0], "  ", matrice_identitee[1][1], "  ", matrice_identitee[1][2])
    print(matrice_identitee[2][0], "  ", matrice_identitee[2][1], "  ", matrice_identitee[2][2])
    # form="{0:8}{1:8}{2:8}"
    # for val in matrice_identitee:
    #     print(form.format(*val))
    print("(", format(float(point_xyz[0]), ".2f"), ", ", format(float(point_xyz[1]), ".2f"), ")", " => ", "(", format(float(point_final[0]), ".2f"),  ", ", format(float(point_final[1]), ".2f"), ")", sep='')

def translation(xt, yt, matrice_identitee):
    matrice_calcul = [[1.00, 0.00, 0.00], [0.00, 1.00, 0.00], [0.00, 0.00, 1.00]]
    print("Translation along vector (", int(xt), ", ", int(yt), ")", sep='')
    matrice_calcul[0][2] = xt
    matrice_calcul[1][2] = yt
    return global_calcul(matrice_calcul, matrice_identitee)

def scaling(xz, yz, matrice_identitee):
    matrice_calcul = [[1.00, 0.00, 0.00], [0.00, 1.00, 0.00], [0.00, 0.00, 1.00]]
    print("Scaling by factors", int(xz), "and", int(yz))
    matrice_calcul[0][0] = xz
    matrice_calcul[1][1] = yz
    return global_calcul(matrice_calcul, matrice_identitee)

def rotation(zr, matrice_identitee):
    matrice_calcul = [[1.00, 0.00, 0.00], [0.00, 1.00, 0.00], [0.00, 0.00, 1.00]]
    print("Rotation by a", int(zr), "degree angle")
    zr = radians(zr)
    matrice_calcul[0][0] = cos(zr)
    matrice_calcul[0][1] = -sin(zr)
    matrice_calcul[1][0] = sin(zr)
    matrice_calcul[1][1] = cos(zr)
    return global_calcul(matrice_calcul, matrice_identitee)

def reflection(zs, matrice_identitee):
    matrice_calcul = [[1.00, 0.00, 0.00], [0.00, 1.00, 0.00], [0.00, 0.00, 1.00]]
    print("Reflection over an axis with an inclination angle of", int(zs), "degrees")
    zs = radians(zs)
    matrice_calcul[0][0] = cos(2 * zs)
    matrice_calcul[0][1] = sin(2 *zs)
    matrice_calcul[1][0] = sin(2 * zs)
    matrice_calcul[1][1] = -cos(2 * zs)
    return global_calcul(matrice_calcul, matrice_identitee)

def global_calcul(matrice_calcul, matrice_identitee):
    m = [[0.00, 0.00, 0.00], [0.00, 0.00, 0.00], [0.00, 0.00, 0.00]]
    for x in range(0, 3):
        for y in range(0, 3):
            m[x][y] = matrice_calcul[x][0] * matrice_identitee[0][y] + matrice_calcul[x][1] * matrice_identitee[1][y] + matrice_calcul[x][2] * matrice_identitee[2][y]
    return m

def calcul_xyz(point_start, matrice_identitee):
    p = [0.00, 0.00, 0.00]
    for x in range(0, 3):
        for y in range(0, 3):
            p[x] = p[x] + (point_start[y] * matrice_identitee[x][y])
    return p

def main():
    matrice_identitee = [[1.00, 0.00, 0.00], [0.00, 1.00, 0.00], [0.00, 0.00, 1.00]]
    nb_entree = len(sys.argv)
    r = gest_err(nb_entree)
    if r == 0 :
        point_xyz = [float(sys.argv[1]), float(sys.argv[2]), float(1)]
        i = 3
        while i < nb_entree:
            if (sys.argv[i] == "-t"):
                matrice_identitee = translation(float(sys.argv[i + 1]), float(sys.argv[i + 2]), matrice_identitee)
                i += 3
            elif (sys.argv[i] == "-z"):
                matrice_identitee = scaling(float(sys.argv[i + 1]), float(sys.argv[i + 2]), matrice_identitee)
                i += 3
            elif (sys.argv[i] == "-r"):
                matrice_identitee = rotation(float(sys.argv[i + 1]), matrice_identitee)
                i += 2
            elif (sys.argv[i] == "-s"):
                matrice_identitee = reflection(float(sys.argv[i + 1]), matrice_identitee)
                i += 2
        point_final = calcul_xyz(point_xyz, matrice_identitee)
        printer(sys.argv[1], sys.argv[2], point_xyz, point_final, matrice_identitee)
        return 0
    else :
        exit(84)

main()