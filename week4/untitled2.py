# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 18:47:56 2020

@author: Aadhavan
"""

def recursive_function(number):
    if number == 10:
        return (number)
    return recursive_function(number + 1)
print(recursive_function(1))