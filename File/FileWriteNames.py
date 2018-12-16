# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 12:22:39 2018

@author: Sharmila
"""
names = ["Aadhavan", "oviya", "Sanju" ]
#namesFile = open("KidsNames", "a")
position = len(names)-1

zero = 0
counter = 0
A = "A"
index = 0
n = 0

while (position >= counter):
    counter += 1
    store = names[n]
    xstore = store[0]
    if (xstore == A):
        index +=1
    n += 1
print(index)
#if(position <= counter):
    
    


