# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:46:03 2014

@author: sim
"""

def get_cumul_sum(l):
    """Exercise 10-3 (from Think Python)
    """
    s = 0
    r= []
    for i in l:
        s += i
        r.append(s)
    return r

print get_cumul_sum([1, 2, 3])
print get_cumul_sum([1, 2, 3, 4, 5, -15, 3])

def has_duplicates(l):
    """Check list whether it has duplicate one or not
    """
    for i in range(len(l)):
        for j in range(len(l)):
            if i == j:
                continue
            if l[i] == l[j]:
                return True
    return False

print has_duplicates([0, 1, 2])
print has_duplicates([0, 1, 1])
print has_duplicates([0, 1, 3, 4, 43563465, 3345])
print has_duplicates(['A', 3, 4, 5, 6, 'B', 'C', 7, 8, 9, 'C', 10, 11])
print has_duplicates(['asdf', 'asdf'])

import random

max_days = [
    31, 28, 31, 30, 31,
    30, 31, 31, 30, 31,
    30, 31]

def generate_birthdays(n):
    """Generates n birthdays
    """
    l = []
    for i in range(n):
        m = random.randint(1, 12)   # January(1) to December(12)
        d = random.randint(1, max_days[m - 1])
        l.append([m, d])
    return l

print generate_birthdays(3)

trials = 100
persons = 23
n = 0
for i in range(trials):
    if has_duplicates(generate_birthdays(persons)):
        n += 1
print float(n) / float(trials)
