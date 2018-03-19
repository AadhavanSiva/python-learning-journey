# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 21:22:02 2018

@author: Sharmila
"""

startingNumber = int(input("Please enter starting number"))
endingNumber = int(input("Please enter ending number"))

count = startingNumber

if( startingNumber < endingNumber):
    while (count <= endingNumber):
        print (count)
        count += 1 

if( startingNumber > endingNumber):
    while (count >= endingNumber):
        print (count)
        count -= 1 
        
