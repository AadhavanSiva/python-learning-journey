# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 19:26:39 2018

@author: Sharmila
"""
ages =[6,8,10, 36, 43]

index = 0
while (index<= 4):
   userAge = input("Enter your age ")
   ages[index] = userAge
   index += 1
   
index = 0
while (index<= 4):
    print (ages[index] )
    index += 1