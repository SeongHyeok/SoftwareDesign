# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:52:54 2014

@author: pruvolo
"""

import pdb

def factorial(n):
    """ Computes the factorial of the non-negative input integer n """
    return_val = 1
    for i in range(n):
        print i
        return_val *= i + 1
    return return_val

if __name__ == '__main__':
    v = factorial(5)
    print "factorial(5):", v
