# -* coding: utf-8 -*-
"""
Created on Mon Nov 12 16:09:29 2018

@author: Aadhavan
"""

#text = "This is a string"

#print(text[0])
characterToCheck = 'X'
sentence = input("Please enter a random sentence")
letterToCheck = input("Please enter a random letter to check at the beginning")

if (sentence[0] == letterToCheck):
    print(" This sentence starts with '", letterToCheck, "'")
else:
    print(" This sentence doesn't starts with '", letterToCheck, "'" )

