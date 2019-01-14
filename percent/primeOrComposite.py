# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 12:11:14 2019

@author: Aadhavan
"""

Number = 3

main = Number 
index = 2

while( main >= index):
    s = Number % index
    index += 1
    if(s == 0):
        print ("composite")
        break;
#        s == s
if(s != 0 ):    
    print ("prime")
    
    