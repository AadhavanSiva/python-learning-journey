# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 20:54:19 2020

@author: Aadhavan
"""

def fibonacci(number):
    number1 = 1
    number2 = 1
    counter = 1
    numbers = [number1, number2]
    sum = 0
    while( counter < 30 ):
        result = number1 + number2
#        print(result)
        number1 = number2
        number2 = result
        
        numbers.append(result)
       
        counter += 1
    print(numbers)
    counter = 9
    while( counter < 20 ):
        sum += numbers[counter]
        counter += 1

    print( "Sum of 10th through 20 fibonacci number is {0}".format(sum))
    return numbers[number-1]

result = fibonacci(20)
print (result)