# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:19:36 2019

@author: Aadhavan
"""
limit = int(input("please enter a number"))
def  showNumber(limit):
    index =0
    while index <= limit:
        remainder = index  % 2
        if remainder == 1:
            print(index,"odd")
            index += 1
        else:
            print(index,"even")
            index += 1
    index += 1
    return index
print(showNumber(limit))

        