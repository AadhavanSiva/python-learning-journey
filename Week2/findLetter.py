# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 21:02:01 2020

@author: Aadhavan
"""

#Write a function that takes a string and a character, uses a dictionary
#that contains the frequencies of each character, and returns the frequ
#ency of a given character. For example, count_freq(“Hello World”, “o”)
#should return 2, because the string “Hello World” contains 2 “o”s.

#thisdict = {
#  "brand": "Ford",
#  "model": "Mustang",
#  "year": 1964
#}
#thisdict["color"] = "red"
#print(thisdict)

def findLetter(word,letter):
    index = 0
    position = len(word) -1
    letters = {}

    while index <= position :   


        if (word[index] in letters):
            x = letters[word[index]]
            letters[word[index]] += 1
            print(x)
        else:
            letters[word[index]] = 1

        index += 1
    
    print(letters)
    if letter in letters:
        return letters[letter]
    else:
        return print(letters)


findLetter("hi u dog","u")
