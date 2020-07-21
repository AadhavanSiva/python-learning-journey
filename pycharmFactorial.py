# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 20:45:57 2020

@author: Aadhavan
"""

def factorial(numberOfTimes):
    a = 1
    b = 2
    index =   0
    numberOfTimes -= 1
    while(index != numberOfTimes ):
        a *= b
        index += 1
        b += 1
    return a

numberOfTimes = 1

result = factorial(numberOfTimes)
print("The factorial of",numberOfTimes, "is", result )