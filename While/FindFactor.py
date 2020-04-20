# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 21:06:47 2020

@author: Aadhavan
"""

number = int(input("Enter a number"))

factor = int(input("Enter a factor of the number you entered"))
index = 0
if (True):
    remainder = number % factor
    if (remainder >=1):
        print (number, " is not divisible by ", factor)
    else:
        print (number, " is divisible by ", factor)
