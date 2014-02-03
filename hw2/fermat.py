# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 01:48:07 2014

@author: SeongHyeok (Steven) Im
"""

import math

def check_fermat(a, b, c, n):
    if n > 2 and (math.pow(a, n) + math.pow(b, n) == math.pow(c, n)):
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work."
        
print "Program for checking Fermat's Last Theorem"
print "Input four numbers"
a = int(raw_input("a: "))
b = int(raw_input("b: "))
c = int(raw_input("c: "))
n = int(raw_input("n: "))
check_fermat(a, b, c, n)