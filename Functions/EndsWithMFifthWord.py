# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 20:32:40 2020

@author: Aadhavan
"""

fileName = open("paragragh","r")
fileRead = fileName.read()
fileName.close()

words = fileRead.split()
print(words)
position = len(words) 
index = 0
while index  < position:
    counter = index % 5

    word = words[index]
    #
    if counter == 4:
        print("delete")
    else:
        if word[len(word)-1] == "m":
            print("delete")
        else:
            print(word)
    index += 1
    