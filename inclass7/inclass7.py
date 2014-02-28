# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:36:45 2014

@author: SeongHyeok Im
"""

def factorial(n):
    """
    """
    if n <= 1:
        return 1
    return factorial(n - 1) * n

def fibonacci(n):
    """ Return n-th fibonacci number started from 0 and 1
    """
    if n <= 0:
        print "Below 0 is not allowed"
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    for i in range(30):
        print i, fibonacci(i)