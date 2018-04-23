# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 10:49:08 2018

@author: Sharmila
"""

numbers = []

userNumber = int (input("please enter a number"))
numbers.append(userNumber)
while (userNumber != 0):
    userNumber = int(input("please enter a number"))
    if(userNumber == 100 ):
        break;
    numbers.append(userNumber)

    
print("printing numbers array")
for number in numbers:
    print (number)