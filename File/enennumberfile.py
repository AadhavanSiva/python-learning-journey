# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 16:00:59 2018

@author: Aadhavan
"""
evens = 0
evenNumberFile = open( "number", "w" )
number = int(input("Enter how much times"))
index = 0

while(index <= number):
    #print(evens)
    evenNumberFile.write(str(evens));
    evenNumberFile.write("\n")
    evens += 2
    index += 1

evenNumberFile.close();