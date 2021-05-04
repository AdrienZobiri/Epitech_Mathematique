#! /usr/bin/env python3

from math import *
from sys import *

opt = int(argv[1])
xp = float(argv[2])
yp = float(argv[3])
zp = float(argv[4])
xv = float(argv[5])
yv = float(argv[6])
zv = float(argv[7])
p = float(argv[8])

if len(argv) < 9:
    print ("Too few arguments, 8 needed")
    exit (84)
if len(argv) > 9:
    print ("Too much arguments, 8 needed")
    exit (84)

def print_sphere_lines():
    print ("sphere of radius %0.f") % (p)
    print ("straight line going through the (%0.f, %0.f, %0.f) point and of direction vector (%0.f, %0.f, %0.f)") % (xp,yp,zp,xv,yv,zv)
    a = pow(xv, 2) + pow(yv, 2) + pow(zv, 2)
    b = 2 * ((xp * xv) + (yp * yv) + (zp * zv))
    c = pow(xp, 2) + pow(yp, 2) + pow(zp, 2) - pow(p, 2)
    delta = pow(b,2) - (4 * a * c)
    if (2*a == 0):
        print("There is an infinite number of intersection points.")
    elif (delta > 0):
        t1 = (-b+sqrt(delta)) / (2 * a)
        t2 = (-b-sqrt(delta)) / (2 * a)
        i1 = [xp + t1 * xv, yp + t1 * yv, zp + t1 * zv]
        i2 = [xp + t2 * xv, yp + t2 * yv, zp + t2 * zv]
        print("2 intersection points:")
        print("(%.3f, %.3f, %.3f)") % (i1[0],i1[1],i1[2])
        print("(%.3f, %.3f, %.3f)") % (i2[0],i2[1],i2[2])
    elif (delta == 0):
        t1 = -b / (2 * a)
        i1 = [xp + t1 * xv, yp + t1 * yv, zp + t1 * zv]
        print("1 intersection point:")
        print("(%.3f, %.3f, %.3f)") % (i1[0],i1[1],i1[2])
    elif (delta < 0):
        print ("No intersection point.")

def print_cylinder_lines():
    print ("cylinder of radius %0.f") % (p)
    print ("Line passing through the point (%0.f, %0.f, %0.f) and parallel to the vector (%0.f, %0.f, %0.f)") % (xp,yp,zp,xv,yv,zv)
    a = pow(xv, 2) + pow(yv, 2)
    b = 2 * ((xp * xv) + (yp * yv))
    c = pow(xp, 2) + pow(yp, 2) - pow(p, 2)
    delta = pow(b,2) - (4 * a * c)
    if (2*a == 0):
        print("There is an infinite number of intersection points.")
    elif (delta > 0):
        t1 = (-b+sqrt(delta)) / (2 * a)
        t2 = (-b-sqrt(delta)) / (2 * a)
        i1 = [xp + t1 * xv, yp + t1 * yv, zp + t1 * zv]
        i2 = [xp + t2 * xv, yp + t2 * yv, zp + t2 * zv]
        print("2 intersection points:")
        print("(%.3f, %.3f, %.3f)") % (i1[0],i1[1],i1[2])
        print("(%.3f, %.3f, %.3f)") % (i2[0],i2[1],i2[2])
    elif (delta == 0):
        t1 = -b / (2 * a)
        i1 = [xp + t1 * xv, yp + t1 * yv, zp + t1 * zv]
        print("1 intersection point:")
        print("(%.3f, %.3f, %.3f)") % (i1[0],i1[1],i1[2])
    elif (delta < 0):
        print ("No intersection point.")

def print_cone_lines():
    print ("Cone with a %0.f degree angle") % (p)
    print ("Line passing through the point (%0.f, %0.f, %0.f) and parallel to the vector (%0.f, %0.f, %0.f)") % (xp,yp,zp,xv,yv,zv)
    a = pow(xv, 2) + pow(yv, 2)
    b = 2 * ((xp * xv) + (yp * yv))
    c = pow(xp, 2) + pow(yp, 2) - (pow(zp, 2) * pow(tan(p), 2))
    delta = pow(b,2) - (4 * a * c)
    if (2*a == 0):
        print("There is an infinite number of intersection points.")
    elif (delta > 0):
        t1 = (-b+sqrt(delta)) / (2 * a)
        t2 = (-b-sqrt(delta)) / (2 * a)
        i1 = [xp + t1 * xv, yp + t1 * yv, zp + t1 * zv]
        i2 = [xp + t2 * xv, yp + t2 * yv, zp + t2 * zv]
        print("2 intersection points:")
        print("(%.3f, %.3f, %.3f)") % (i1[0],i1[1],i1[2])
        print("(%.3f, %.3f, %.3f)") % (i2[0],i2[1],i2[2])
    elif (delta == 0):
        t1 = -b / (2 * a)
        i1 = [xp + t1 * xv, yp + t1 * yv, zp + t1 * zv]
        print("1 intersection point:")
        print("(%.3f, %.3f, %.3f)") % (i1[0],i1[1],i1[2])
    elif (delta < 0):
        print ("No intersection point.")

def main():
    if (len(argv) != 2):
        exit (84)
    if (argv[1] == "-h"):
        print ("USAGE\n\t./104intersection opt xp yp zp xv yv zv p\n")
        print ("DESCRIPTION\n\topt\t\tsurface option: 1 for a sphere, 2 for a cylinder, 3 for a cone\n")
        print ("(xp, yp, zp)\tcoordinates of a point by which the light ray passes through\n")
        print ("(xv, yv, zv)\tcoordinates of a vector parallel to the light ray\n")
        print ("p\t\t parameter: radius of the sphere, radius of the cylinder, or angle formed by the cone and the Z-axis\n")
        exit(0)
    if (opt == 1):
        print_sphere_lines()
    elif (opt == 2):
        print_cylinder_lines()
    elif (opt == 3):
        print_cone_lines()

main()