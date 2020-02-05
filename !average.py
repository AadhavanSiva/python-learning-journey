# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 18:27:34 2020

@author: Aadhavan
"""

values = [3, 2, 1, 0,0,0,0,0,0,4]
number_of_values = len(values)-1
sum = 0
counter = 0

while (number_of_values >= counter): 
    index = values[counter]
    sum += index
    counter += 1 

average = sum / counter 
print (average)    