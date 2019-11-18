# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 19:32:19 2019

@author: Oviya
"""



def difference(number1, number2):
    print(number1, number2)
    if(number1 <= number2):
        subtract = number2 - number1
    else:
        subtract = number1 - number2
    return subtract


number1 = -2
number2 = 4
result = difference(number1, number2)
print(result)
    
print()