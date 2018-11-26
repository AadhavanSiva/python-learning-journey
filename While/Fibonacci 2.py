# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 19:35:44 2018

@author: Aadhavan
"""

# 1, 2, 3, 5, 8, 13, 
one = 1
two = 2
number = int(input(" PLEASE ENTER A NUMBER "))
counter = 2
while ( counter <= number ):
    print (one)
    print (two)
    one += two
    two += one
    counter += 2