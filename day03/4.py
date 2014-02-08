# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:34:39 2014

@author: sim
"""

"""
1) Write a function called hypotenuse that takes floats a and b and prints the length of the hypotenuse of a triangle with side lengths a and b.
"""
import math
def hypotenuse(a, b):
    print math.sqrt(a ** 2 + b ** 2)
    print (a**2 + b**2) ** 0.5  # nice

hypotenuse(3, 4)

"""
2) Do Exercise 3-3 (right justify) (Note: don't use loops!)
                                                                 allen
"""
def right_justify(s):
    print ' ' * (70 - len(s)) + s

right_justify("Steven");

"""
3) Do Exercise 3-4 (do_twice)
"""

def do_twice(f):
    f()
    f()

def print_spam():
    print 'spam'

do_twice(print_spam)