# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:09:32 2019

@author: Aadhavan
"""

firstList = [56,67,5,3,1,3,6,6,]
index = 0
values = len(firstList) - 1

lowest = 0
while(index <= values):
    print("withinloop")
    if(firstList[index] < firstList[values]):
      lowest = firstList[index]
      #print("work")
      index -= 1
    elif(firstList[index] > firstList[values]):
      lowest = firstList[values]
      #print("wrong")
      values += 1
    else:
     lowest = firstList[values]
     index -= 1
     #print("else")
    index += 1
    values -= 1
print(lowest)