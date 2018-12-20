# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 17:36:24 2018

@author: Aadhavan
"""

a = 5;
print("a =",id(a))
b=7
print("b =",id(b))
b=a
print("after b=a")
print("a =",id(a))

print(b)
print("b =",id(b))
a = 10
print(b)
