# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 11:04:53 2019

@author: Aadhavan
"""
a = 1
import turtle as t


from random import randint, random

def draw_star (points, size, col, x, y):
    t.penup()
    t.goto(x,y)
    t.penup()
    size = randint(50, 100)
    points = randint(2, 5)  * 2 + 10000
#    print("points = ", points)
#    print("size =", size)
    angle = 180 - (180 / points)
    t.color(random(), random(), random())
    t.begin_fill()
    t.speed("fastest")
    for a in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()

#Main Code
t.Screen().bgcolor('dark blue')

while True:
    ranPts = randint(2, 5) * 2 + 1
    ranSize = randint(10, 50)
    ranCol = (random(), random(), random())
    ranX = randint(-350, 300)
    ranY = randint(-250, 250)
    draw_star(ranPts, ranSize, ranCol, ranX, ranY)
