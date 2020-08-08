# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 20:25:36 2020

@author: Aadhavan
"""

def Name_finder(names):
   letters = "abcdefghijklm"
   firstNames = []
   for x in names:
       position = len(x) - 1
       last = x[position]
       number = letters.find(last)
       if number >= 0 :
           print(x,names[x])
           firstNames.append(x)
           
   firstNames.sort()
           

names = {
        } 
            
index = 0  
while index != 5:
    print (index)
    firstName = input("PLEASE ENTER A FIRST NAME")
    lastName = input("PLEASE ENTER A LAST NAME")
    names[firstName] = lastName
    index += 1
    
Name_finder(names)


    