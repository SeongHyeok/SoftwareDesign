# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:28:12 2014

@author: sim
"""

from unum.units import *
n = 100 * m * m
t = 5 * min
e = n / t
print e.asUnit((mile*mile) / h)

def hinge(n):
    if (n < 0):
        return 0
    if (n >= 0):
        return n

print hinge(-4)
print hinge(5)

def print_number_of_days(n):
    print "Input is " + str(n),
    if (n != 1):
        print "days"
    else:
        print "day"

print_number_of_days(1)
print_number_of_days(3)