# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:46:50 2020

@author: Aadhavan
"""
strings = {
        }

def Attribute(styles):
    style = styles.split(":")
    styles = styles.split(";")
    index = 0
    index2 = 1
    numberOfAttribute = len(styles) - 1
    while index2 <= numberOfAttribute:
        strings[styles[index]] = styles[index2] 
        index += 2
        index2 += 2
Attribute("background-color:powderblue;color:powderblue:")

print(strings)

