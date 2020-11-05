# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 19:56:33 2020

@author: Aadhavan
"""

FileName = input("Please enter a file name:")

    
numberFile = open(FileName,"r")
numberFile.close()


index = 1

while index <= 3:
    numberFile = open(FileName,"a")
    number = input("Please enter a number")
    numberFile.write(number)
    numberFile.write("\n")
    index += 1
    numberFile.close()
    print(number)
    
numberFile = open(FileName,"r")
Min = min(numberFile)
print( f"{Min} is the lowest number in the file")
numberFile.close()


numberFile = open(FileName,"r")
Max = max(numberFile)
print(Max,"is the highest number in the file")
numberFile.close()


