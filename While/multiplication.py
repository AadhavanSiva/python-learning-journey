d# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 11:33:27 2019

@author: Aadhavan
"""

number = int(input("PLEASE ENTER A NUMBER THAT YOU WOULD LIKE TO KNOW THE MULTIPLICATION TABLES OF:"))

index = 0
m = int(input("PLEASE ENTER A NUMBER FOR HOW MUCH MULTIPLICATION TABLES WOULD YOU LIKE TO KNOW"))
n = 1
while(m >= n):
    index += number
    print(n,"*",number,"=",index)
    n += 1