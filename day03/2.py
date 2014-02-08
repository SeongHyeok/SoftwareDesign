# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:03:12 2014

@author: sim
"""

"""
1.)  Write some python code that prints "hello" if the a variable x of type "int" is in the interval [0,100], prints "goodbye" if x is in the interval (100,500), and "ciao" if x is in the interval [600,1000] (note square brackets mean that the interval is inclusive at a particular endpoint while a parenthesis means exclusive at the endpoint).  You can assume that the variable x has already been defined.
"""

x = 100

if (0 <= x <= 100):
    print "hello"
    x = 200
if (100 < x < 500):
    print "goodbye"
if (600 <= x <= 1000):
    print "ciao"


"""
2.)  Write some python code that prints "yes" if the variable x of type "int" is in the interval [0,100] or if the variable y of type "str" is equal to "01052".  You can assume that someone has already defined x and y.
"""
x = 0
y = "01052"

if (0 <= x <= 100) or (y == "01052"):
    print "yes"