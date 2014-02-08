# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:59:07 2014

@author: sim
"""

## Fruitful function: returns value

#from math import *
#from math import sqrt
#import math

## import * is a bad idea.

def double(n):
    return 4 * n;

def mysqrt(n):
    return math.sqr(n)

"""
Practice Problems:

    Create a function called get_complementary_base that takes as input a string containing a single letter which represents a nucleotide and returns the complementary nucleotide.  If the input is invalid, the function should print an error.
    Create a function called is_between(x,y,z) (ThinkPython exercise 6.3) that returns true if and only if y is in the interval [x,z]
    Write a function called random_float(start,stop) which generates a random number in the interval [start,stop).  You should build your function using Python's built-in function random.random 

C <==> G
A <==> T
"""

def get_complementary_base(c):
    """
    Takes a character and returns complementary base
    c: argument
    """
    if c == "A":
        return "T"
    if c == "T":
        return "A"
    if c == "G":
        return "C"
    if c == "C":
        return "G"
    return "ERROR!"

def is_between(x, y, z):
    if x <= y <= z:
        return True
    return False

import random
def random_float(start, stop):
    return start + random.random() * (float(stop) - float(start))

print get_complementary_base("A")
print get_complementary_base("T")
print get_complementary_base("G")
print get_complementary_base("C")
print get_complementary_base("H")

print is_between(3, 3, 5)
print is_between(3, 4, 5)
print is_between(3, 6, 5)

print random_float(1, 2)
print random_float(0, 10)

def sum_1_to_n(n):
    """ returns the sum of all integers from 1 to n """
    return 0

def factorial(n):
    if n == 0:
        return 1
    s = n
    for i in range(1, n):
        s = s * i
    return s

def factorial2(n):
    s = 1;
    for i in range(n):
        s = s * (i + 1)
    return s