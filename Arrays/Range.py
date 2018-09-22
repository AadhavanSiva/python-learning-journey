# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 12:00:33 2018

@author: Aadhavan
"""

size = int(input(" Please enter a random number "))
index ="1"

#print(index*2)


for po in range (1, size+1, +1):
    print(index * po )
    
SecondIndex ="2"
for po in range (size,0,-1):
    print(SecondIndex*po)
    