# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 20:56:13 2021

@author: Aadhavan
"""

import random


words1 = ("Python", "Hours", "Author", "Spoon", "Source")

words2 = ("Wednesday", "View", "combine", "fork", "project")


def combineRandomStrings (listOfWord1, listofwords2):
    

    randomWords1 = random.choice(listOfWord1)
    randomWords2 = random.choice(listofwords2)
    combinedString = randomWords1 + randomWords2
    return combinedString

def hello_brownie():
    print("Hello bujju")

print(combineRandomStrings(words1, words2))
print(combineRandomStrings(words1, words2))

hello_brownie()
