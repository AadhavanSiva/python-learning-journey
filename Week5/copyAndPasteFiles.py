# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 17:59:54 2020

@author: Aadhavan
"""

fileName = open("read_n_words.py","r")
data = fileName.read();
print(data)
fileName.close()

fileName2 = open("read_n_words_1.py","w")
fileName2.write(data);
print(fileName2)
fileName.close()