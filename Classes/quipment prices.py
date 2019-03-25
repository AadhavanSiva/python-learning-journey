# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 12:09:05 2019

@author: Aadhavan
"""

class Equipment:
    def __init__(self, name1, price, brand, game):
        self.name = name1
        self.price = price
        self.brand = brand
        self.game = game
        
    def writeToConsole(self):
        print("THE product IS", self.name)
        print("THE PRICE OF the equipment IS", self.price)
        print("THE BRAND NAME IS", self.brand)
        print("THE GAME IT'S USED FOR IS", self.game)

#Java equivalent
#   Equipment bat = new Equipment("bat", "$300", "Tri-Valley sports", "baseball")
bat = Equipment("bat", "$300", "Tri-Valley sports", "baseball")
bat.writeToConsole()

helmet = Equipment("helmet","$50","Tri-Valley sports","baseball",)
helmet.writeToConsole()

gloves = Equipment("gloves","$15","Tri-Valley sports","baseball",)
gloves.writeToConsole()

ball = Equipment("ball","$5","Tri-Valley sports","baseball",)
ball.writeToConsole()
