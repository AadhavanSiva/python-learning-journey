# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 16:31:04 2020

@author: Aadhavan
"""

f = open("xdcfvgbh","r")
fw = open("new_file", "w")
count = 0
for line in f:
    new_list = []
    index = 0
    words = line.split( )
    while(index < len(words)):
        word = words[index]
        count += 1
        last_letter = word[len(word)-1]
        reminder = count % 5
        if(reminder != 0 and last_letter != 'm'):
            fw.write(word)
            fw.write(" ")
        index += 1
    fw.write("\n")
        
        
fw.close()
f.close()







