# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 18:12:39 2018

@author: Aadhavan
"""
def square(n):
    return n * 2;
   
def evenOrOdd(n):
    if( n % 2 == 0):
        print("Even")
        return
    print("Odd")
    return
number = 3
evenOrOdd(number)
returnValue = evenOrOdd(number)
print(returnValue)

twoSquare = square(number)
print(twoSquare)
