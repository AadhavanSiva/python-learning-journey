# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 20:36:28 2020

@author: Aadhavan
"""
def fibonacci(number):
    number1 = 1
    number2 = 1
    counter = 2
    numbers = [1,1]
    while( counter < number ):
        result = number1 + number2
#        print(result)
        number1 = number2
        number2 = result
        counter += 1
        numbers.append(result)
    return result
result = fibonacci(10000)
print (result)