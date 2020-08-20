# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 18:46:24 2020

@author: Aadhavan
"""
def HailStone(number):
    even = number % 2
    if even == 0:
        print(int(number))
        HailStone(number / 2) 
    elif number == 1:
        print("1")
        return number
    else:
        print(int(number))
        HailStone(number*3+1)
    
        
HailStone(7)
#print(result)