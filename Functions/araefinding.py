# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 10:42:54 2018

@author: Aadhavan
"""


def rectangleArea(Length, Width):
    area = Length * Width;
    return area;

def squareArea(oneside):
    area = oneside*oneside;
    return area;
    

Length =  int(input("What is the length"))
Width  =  int(input("What is the width"))
oneside =  int(input("what is only onesides value"))
result= rectangleArea(Length, Width)
print ("The area of a rectangle is",result)
result= squareArea(oneside)
print ("The area of a square is", result)



