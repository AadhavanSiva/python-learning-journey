# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 18:08:17 2018

@author: Aadhavan
"""

#  1000, 3, 990, 6, 980, 9, 970, 12, 960,,
numberOne = 1000
numberTwo = 3
usersNumber = int(input("enter number of times"))
counter = 0;

while (counter < usersNumber):
    print(numberOne)
    print(numberTwo)
    numberOne -= 10
    numberTwo += 3
    counter += 2