# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 18:43:41 2019

@author: Aadhavan
"""
g = 0
number = int(input("PLEASE ENTER A NUMBER"))
q = number
index = 2
while (q >= index):
    if(q == index):
        break;
    w = q % index 
    g = w
    index += 1
    if(g == 0): 
        print("composite")
        break;
if(g >= 1):
        print("prime")
        