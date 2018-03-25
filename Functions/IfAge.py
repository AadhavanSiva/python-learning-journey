# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 18:22:15 2018

@author: Sharmila       
"""

#Write a program to accept age
#   display adult if age >= 18 else display "not adult" 


userage = int (input ("Please enter your age"))

if (userage >= 18):
    print ("You are an adult")

if(userage < 18):
    print ("You are not an adult")