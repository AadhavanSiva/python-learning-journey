# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 12:10:19 2018

@author: Aadhavan
"""
word = input(" PLEASE ENTER A WORD ")
last = len(word) -1
one = word[0]
One = (one.upper())
print (last)
zero = word[last]
Last = (zero.upper())
if (one == One):
    print(" FIRST LETTER IS CAPITAL ")
else:
    print(" FIRST LETTER IS NOT IN CAPITAL ")
    
if (zero == Last):
    print(" LAST LETTER IS CAPITAL ")
else:
    print(" LAST LETTER IS NOT IN CAPITAL ")
