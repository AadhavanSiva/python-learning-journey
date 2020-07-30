# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 20:21:04 2020

@author: Aadhavan
"""
def prefectNumber(number):
    counter = number - 1
    index = 1
    dupe = 0
    while index < counter:
        result = 0
        result = number % index

        if result <= 0:

            dupe += index
        index += 1
        
    if dupe == number:
        value = True
    else:
        value = False
    return value

number = int(input("PLEASE ENTER A NUMBER"))

result = prefectNumber(number)
print (result)