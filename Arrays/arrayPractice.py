# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 19:39:53 2018

@author: Sharmila
"""
#
#numbers = []
#numbers.append(3);
#numbers.append(4);
names = ["Sharmila", "Oviya"]


#print(names[1])

names.append("Sivakumar")
names.append("Aadhavan")
names.append("Llyod")

#print(names[2])


index = len(names)-1
while (index > -1):
    print (names[index])
    index -= 1


#index = 4
#   Lloyd
#   index = 3
#   Aadhavan
#   2
#   Sivaku
#    1
#    oviya
#    0
#    Sharmila
#    -1