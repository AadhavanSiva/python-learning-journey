# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:12:17 2020

@author: Aadhavan
"""

def vowelSearcher(word):
    vowels =  "aeiou"
    position = len(word)
    index = 0
    number = 0
    while position != index:
#         print("hi")
         finder = vowels.find(word[index])
         if finder >= 0:
#             print("p")
             number += 1
#             print(number)
         finder = 0
         index += 1
    return number
            
             
             
             



word = "ooe"
result = vowelSearcher(word)
print(result,"vowels are in the word", word)