# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 19:54:30 2018

@author: Sharmila
"""

numbers = [8, 5, 4, 9]
abovefive = 0
belowfive = 0
equalfive = 0
    
    
for number in numbers:
    if (number > 5):
        abovefive += 1
    if (number < 5):
        belowfive += 1
    if (number == 5):
        equalfive += 1
        
print ("There are/is" ,abovefive ,"numbers that are/is greater than five" )
print ("There are/is" ,belowfive ,"numbers that are/is lesser than five" )
print ("There are/is" ,equalfive ,"numbers that are/is equal to five" )