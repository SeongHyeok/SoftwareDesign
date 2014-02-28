# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:23:51 2014

@author: SeongHyeok Im
"""

def sum_of_squares(n):
    s = 0
    for i in range(1, n + 1):
        s += i * i
    return s

print sum_of_squares(1)
print sum_of_squares(2)
print sum_of_squares(3)
print sum_of_squares(4)

def filter_out_negative_numbers(l):
    r = []
    for item in l:
        if item >= 0:
            r.append(item)
    return r

print filter_out_negative_numbers([-2, 5, 10, -100, 5])
print filter_out_negative_numbers([-1, -1, 0, 0])
print filter_out_negative_numbers([0, 0, 0, 0])