# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 01:10:34 2014

@author: SeongHyeok (Steven) Im
"""

def print_four_times(s):
    print s
    print s
    print s
    print s

def draw_internal(l1, l2):
    print l1
    print_four_times(l2)

def draw_grid():
    n = 2
    line1 = ("+" + "-" * 4) * n + "+"
    line2 = ("|" + " " * 4) * n + "|"
    
    draw_internal(line1, line2)
    draw_internal(line1, line2)
    print line1
    
draw_grid()


def draw_grid_4x4():    
    n = 4
    line1 = ("+" + "-" * 4) * n + "+"
    line2 = ("|" + " " * 4) * n + "|"
    
    draw_internal(line1, line2)
    draw_internal(line1, line2)
    draw_internal(line1, line2)
    draw_internal(line1, line2)
    print line1

draw_grid_4x4()