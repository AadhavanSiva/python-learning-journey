# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 19:11:13 2021

@author: Aadhavan
"""
import pickle


class unoCard:
    def _init_ (self, color, value, name):
        self.color = color
        self.value = value
        self.name = name
    def Print (self):
        print("The card color is ", self.color)
        print("The card's value is " + self.value)
        print("The card is called " + self.name)

Card1 = unoCard("red","Skip","Red Skip")

storage = open("Storage","wb")
#
pickle.dump(Card1,storage)
#
storage.close()
#    
        