# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:32:29 2020

@author: Aadhavan
"""

FileName = input("Please enter  name for your file.")


numberFile = open(FileName,"x")
numberFile.close()

index = 0

numbersList = []
while index < 5:   
    number = input("Please enter a number:")
    numberFile = open(FileName,"a")
    numberFile.write(number);
    numberFile.write("\n");
    index += 1
    numberFile.close()
    numbersList.append(number)
    

print("This is the lowest number u entered",min(numbersList))
print("This is the highest number u entered",max(numbersList))

sums = 0
numberFile = open(FileName,"r")
for numbers in numberFile:
    numbersList.append(int(numbers))
    sums += int(numbers)
    
print("This is the sum of all the numbers u entered",sums)


    