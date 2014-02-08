# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:53:19 2014

@author: sim
"""

def do_twice(f, n):
    f(n)
    f(n)

def print_spam():
    print 'spam'

def print_twice(s):
    print s
    print s

do_twice(print_spam)