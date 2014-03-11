# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 15:24:03 2014

@author: SeongHyeok Im (Steven)
"""

def exclusive_or_dict(d1, d2):
    for key in d1.keys():
        if d2.has_key(key):
            d1.pop(key)
            d2.pop(key)
    res = dict(d1.items() + d2.items())
    return res

print exclusive_or_dict({'a':5, 'b':3}, {'a':7, 'c':3})
print exclusive_or_dict({'test':5, 'b':7.0, 3:'q'}, {'b':'world', 3:'q'})
print exclusive_or_dict({'1':1, '2':2}, {'2':3})
print exclusive_or_dict({}, {})
print exclusive_or_dict({'1':1, '2':2, '3':3}, {'4':4})