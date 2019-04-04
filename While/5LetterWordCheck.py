# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:19:17 2019

@author: Aadhavan
"""
word1 = input("Please enter a word")
word2 = input("Please enter a 5 letter word to check")

last1 = len(word1) - 1
index = 0
while(index >= last1):
    if(word2[0] == word1[index]):
        index += 1
        if(word2[1] == word1[index]):
            index += 1
            if(word2[2] == word1[index]):
                index += 1
                if(word2[3] == word1[index]):
                    index += 1
                    if(word2[4] == word1[index]):
                        print("Word is there")
    
    index += 1
