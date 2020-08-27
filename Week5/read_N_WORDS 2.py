# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 12:32:13 2020

@author: Aadhavan
"""

from read_n_words import read_n_word

#read_n_word("cities",1)

index = 1
while index != 6:
    result = read_n_word("read_n_words.py",index)
    if len(result) <= 3:
        print(result)
    index += 1
    


    
