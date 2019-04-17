# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 14:30:08 2019

@author: Aadhavan
"""
firstList = [77, 77, 77]

index = 0
values = len(firstList) - 1

highest = 0
while(index <= values):
    if(firstList[index] > firstList[values]):
      highest = firstList[index]
      #print("work")
      index -= 1
    elif(firstList[index] < firstList[values]):
      highest = firstList[values]
      #print("wrong")
      values += 1
    else:
     highest = firstList[values]
     index -= 1
     #print("else")
    index += 1
    values -= 1
print(highest)

firstList[index] = 0
index = 0
highest = 0
values = len(firstList) - 1

while(index <= values):
    if(firstList[index] > firstList[values]):
      highest = firstList[index]
      #print("work")
      index -= 1
    elif(firstList[index] < firstList[values]):
      highest = firstList[values]
      #print("wrong")
      values += 1
    else:
     highest = firstList[values]
     index -= 1
     #print("else")
    index += 1
    values -= 1
    
print(highest)
