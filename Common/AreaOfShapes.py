# -*- coding: utf-8 -*
"""
Created on Wed Nov 20 18:08:40 2019

@author: Oviya
"""

def square_area(side):
    areaSquare = rectangle_area(side, side)
    return areaSquare

def rectangle_area(length, width):
    areaRectangle = length * width
    return areaRectangle

def square_perimeter(side):
    perimeterSquare = rectangle_perimeter(side, side)
    #perimetersquare = number * 4
    return perimeterSquare

def rectangle_perimeter(lenght, width):
    perimeterRectangle = lenght*2 + width*2
    return perimeterRectangle

sq_area = square_area(5)
print("Area square", sq_area)
rec_area = rectangle_area(7, 4)
print("Area rectangle ", rec_area)
print( "Area rectangle",rectangle_area(7, 4))
print( "Square perimeter", square_perimeter(5))
print("Rectangle perimeter",rectangle_perimeter(6,2))

    