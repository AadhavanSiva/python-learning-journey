# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 21:29:43 2020

@author: Aadhavan
"""

#Ask the user for 5 names (keyboard input), and map the first names 
#to last names in a dictionary. Then print all the last names whose
# corresponding first names end with letters ‘a’ through ‘m’, in alphabetical order.



index = 0
fullNames = {}
Names = []
while index != 2:
    letters = "abcdefghijklm"
    firstNames = input("Please enter your first name:")
    position = len(firstNames) -1
    lastNames = input("Please enter your last name:")
    fullNames[firstNames] = lastNames
    index += 1
#    find = letters.find(firstNames[position])
#    if find != -1 :
    if firstNames[position] in letters:
        Names.append(lastNames)
    
print(fullNames)
print(Names)
Names.sort()

position = len(Names)
index = 0
while index != position:
    print(Names[index])
    index += 1