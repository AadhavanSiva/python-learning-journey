# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 12:48:04 2020

@author: Aadhavan
"""

FileName = input("Please enter a file name:")


numberFile = open(FileName,"x")
numberFile.close()

index = 0

numberList = []
while index < 3:
    number = input("Please enter a number:")
    print (number)
    numberFile = open(FileName,"a")
    numberFile.write(number);
    numberFile.write("\n");
    index += 1
    numberFile.close()

sumOfx = 0
numberFile = open(FileName,"r")
for x in numberFile:
    numberList.append(int(x))
    sumOfx += int(x)
numberFile.close()
    
numberFile = open(FileName,"a");
numberFileMin = min(numberList)
print("{0} is the minimum number in your file.".format(int(numberFileMin)))
numberFile.write(str(numberFileMin));
numberFile.write("\n");
numberFile.close()

numberFile = open(FileName,"a");
numberFileMax = max(numberList)
print("{0} is the maximum number in your file.".format(int(numberFileMax)))
numberFile.write(str(numberFileMax));
numberFile.write("\n");
numberFile.close()
     
numberFile = open(FileName,"a");
print("{0} is the sum of all the numbers in your file.".format(int(sumOfx)))
numberFile.write(str(sumOfx));
numberFile.write("\n");
numberFile.close()



import os
os.remove(FileName)






