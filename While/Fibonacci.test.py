# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 19:50:17 2020

@author: Aadhavan
"""

def fibanacci(number):
    first = 0
    second = 1
    result = first + second
    index = 1
    #print(one)
    if ( number == 0 ):
        return 0
    while index < number:
        result = first + second
        first = second
        second = result
        index += 1
        #print(result)
        #print(one)
    return result
#    index = 0
#    index = number % 2
#    if index == 1:
#        result += one
#        one += second
#        second += result
#        print(result)
#    else:
#        result += one
#        one -= result
#        second += one
#        print(one,"4")
#    number -= 2
#    one = 1
#    second = 1
#    result = 0
#    index = 0
#    index = 0
#    fibanacciNumbers = []
#    while index <= 18:
#        result += one
#        one += second
#        second += one
##        print(result)
##        print(one)
#        index += 2
#        if index >= 12:
#            fibanacciNumbers.append(result)
#            fibanacciNumbers.append(one)
#    print(fibanacciNumbers)
#        
nthFibNumber = fibanacci(3)
print(nthFibNumber)

for x in range(10, 21):
    nthFibNumber = fibanacci(x)
    print(nthFibNumber)