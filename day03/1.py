# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:40:00 2014

@author: sim
"""

"""
1.)  Write a python script that generates the following output (bonus: what is the shortest Python program that you can come up with that generates the correct output?)

aaaaaaaaaabaaaaaaaaaabaaaaaaaaaabaaaaaaaaaabaaaaaaaaaab
daaaaaaaaaacdaaaaaaaaaacdaaaaaaaaaacdaaaaaaaaaacdaaaaaaaaaac
"""

print ('a'*10+'b')*5
print ('d'+'a'*10+'c')*5

x='a'*10
print (x+'b')*5
print ('d'+x+'c')*5