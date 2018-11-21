# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 18:01:43 2018

@author: Aadhavan
"""

#   1, 2, 3, 5, 8, 13, 21
one = 1
two = 2
result = one + two 
#Number = int(input(" PLEASE ENTER A NUMBER "))
counter = 0

while( counter <= 5  ):
    print (one)
    print (two)
    one += two 
    two += one
    counter += 2


    