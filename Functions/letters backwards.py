# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 20:39:18 2018

@author: Aadhavan
"""

word = input("PLEASE ENTER A WORD")
length = len(word) - 1
index = 0
while(  length>= index ):
    print (word[length])
    length-=1