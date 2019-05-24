# -*- coding: utf-8 -*-
"""
Created on Fri May 24 16:27:29 2019

@author: Aadhavan
"""
#  1 * 2 * 3 * 4

factorial = int(input("PLEASE ENTER A NUMBER"))
result = 1

counter = 1
while(factorial >= counter):
    result = result * counter
    counter += 1
print("The factorial of ",factorial, " is ",result) 