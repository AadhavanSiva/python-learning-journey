# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:53:00 2020

@author: Aadhavan
"""

index = 1
file = open("text.txt","r")
read = file.readlines()

file = open("text.txt","r")

lines = []

while (index <= len(read)):
    fileRead = file.readline()
    lines.append(fileRead)
    index += 1

numberOfLines = len(read) - 1

line = []

while numberOfLines != -1:
#    print(lines[numberOfLines])
    line.append(lines[numberOfLines])
    numberOfLines -= 1
    
print(line)
numberOfLines = len(read) 
file.close()

File = open("reverse.txt","w")

index = 0 

while index != numberOfLines:
    File.writelines(line[index])
    index += 1
    
file.close()
File.close()

