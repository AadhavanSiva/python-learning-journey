# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:29:29 2019

@author: Aadhavan
"""

numbers = [3,1,2,3,3,3]
compare = int(input("PLEASE ENTER A NUMBER"))
last = len(numbers) - 1
index = 0
answer = 0
numberOfTimesPrinted = 0
while(last >= index):
    if(compare == numbers[index]):
        answer += 1 
        numberOfTimesPrinted += 1
    index += 1
if(answer >= 1):
    print("The numbers", compare,"is in the list")
    print("The numbers", compare,"is in the list", numberOfTimesPrinted)
else:
    print("The numbers", compare,"is not the list")

