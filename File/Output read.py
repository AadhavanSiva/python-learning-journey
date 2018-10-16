# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 20:14:59 2018

@author: Aadhavan
"""

file = open("C:\\FileTest\\FirstPythonIO.txt", "r")
for line in file:
    print(line)

file.close();
    
    

#print(file.readline())