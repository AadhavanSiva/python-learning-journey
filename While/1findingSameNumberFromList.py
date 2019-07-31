# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 14:54:10 2019

@author: Aadhavan
"""

list1 = [3,7,9]

list2 = [3,5,7,18]

list3 = []
index = 0

index2 = 0
one = list1[index]
two = list2 [index2]
position =  len(list1)-1
position2 =  len(list2)-1
a = 0
w = 0
while index <= position:
    while index2 <= position2:
        one = list1[index]
        two = list2 [index2]
        if  one == two:
            w +=1
            print("w")
            list3.append(two)
        #else:
        #    w += 0
        index2 += 1

        # if a != len(list1):
        #    break;
    index += 1
    index2 = 0
    a += 1
print ("there are", w, "that are the same")
print(list3)