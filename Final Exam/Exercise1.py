# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 19:41:29 2020

@author: Aadhavan
"""


def numberOfSameWord (File,word):
    file = open(File,"r")
    FileRead = file.read()
    x = FileRead.find("word")
    print(x)

numberOfSameWord("paragraph","word")


txt = "Hello, welcome to my world."

x = txt.find("to")

print(x)
