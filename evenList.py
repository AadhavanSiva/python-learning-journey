# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 18:33:00 2019

@author: Aadhavan
"""
list1 = [3,4,6,9,10,14,19,23,36]
list2 =[]
numbers = len(list1) -  1
a = 0
while (a <= numbers):
    r = list1[a] % 2
    if (r == 0):
        list2.append(list1[a])
    a +=    1
print(list2)


