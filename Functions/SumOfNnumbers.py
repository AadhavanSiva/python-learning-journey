# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 21:34:44 2018

@author: Sharmila
"""

sum = 0
number = int(input("Enter a number"))
while ( number != 0 ):
    sum += number
    number = int(input("Enter a number"))
    
print("Sum is ", sum)