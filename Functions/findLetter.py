# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 16:40:46 2020

@author: Aadhavan
"""

def findLetters(word,letter):
    index = 0
    counter = len(word) -1
    numberOfLetters = {}
    while index <= counter :   
        if (word[index] in numberOfLetters):
            numberOfLetters[word[index]] += 1
        else:
            numberOfLetters[word[index]] = 1
        index += 1    
    if letter in numberOfLetters:
        return numberOfLetters[letter]
    else:
        return 0

result = findLetters("serupuu","u")
print(result)