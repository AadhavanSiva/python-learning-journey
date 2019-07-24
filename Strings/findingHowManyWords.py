# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 14:32:34 2019

@author: Aadhavan
"""

sentence = input("Enter a sentence")

space = " "
last = len(sentence) - 1
index = 0
nos = 0
while last >= index :
    if sentence[index] == space:
        nos += 1        
    index += 1
print(nos)
word = nos + 1
print("The number of words is", word)
    
