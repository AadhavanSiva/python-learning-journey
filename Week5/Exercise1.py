# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 20:54:17 2020

@author: Aadhavan
"""
numbersList = range(1,100)
position = len(numbersList) - 1
index = 0

number = numbersList[position]
number2 = number - 1
result = slice(6,100,7)
result2 = (numbersList[result])


position = len(result2) - 1
while index <= position:
    
    print(result2[position])
    position -= 1

