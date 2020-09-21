# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 20:35:27 2020

@author: Aadhavan
"""
file = open("numbers","w")

Numbers = ["1","1","2"]
index = 0
first = 1
second = 2

while index != 100:
    file.write(Numbers[index])
    file.write("\n")
    result = first + second
    first = second
    second = result
    index += 1
    Numbers.append(str(result))
    print(Numbers[index])

file.close()
