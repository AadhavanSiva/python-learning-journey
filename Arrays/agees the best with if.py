# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 20:25:56 2018

@author: Sharmila
"""

userAge = int (input("please enter your age"))

if (userAge  <= 1 and userAge > 0):
    print ("You are a new born baby")
    
if ( userAge  > 2 and userAge < 2 ):
    print ("You are a baby")

if (userAge  > 2 and userAge  <= 3 ):
    print ("You are a toddler")
    
if (userAge  > 3  and userAge  <= 5 ):
    print ("You are a preschooler")    
    
if(userAge  > 6 and userAge  <= 12 ):
    print ("You are a gradeschoolers")
    
if (userAge  > 13 and userAge  <= 18 ):
    print ("You are a teenagers")
    
if (userAge  > 19 and userAge  <= 21  ):
    print ("You are a young adult")
    
if(userAge  > 22 and userAge <= 1000 ):
    print ("You are a adult")