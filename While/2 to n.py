# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 18:59:53 2018

@author: Aadhavan
"""

odd = 3
number = int(input(" PLEASE ENTER AN EVEN NUMBER "))
result = 0
index = 0                     
while (index < number):
    #print(even)
    result += odd
    odd += 3
    index += 1 
       
print(result)