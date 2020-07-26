# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 17:38:50 2020

@author: Aadhavan
"""

def multiplication(number):
    index = 1
    plus = number
    string = "";
    while index <= 10:
        string += str(number)
        string += (' ')
        number += plus
        index += 1
    return string
result2 = multiplication(9)
print(result2)