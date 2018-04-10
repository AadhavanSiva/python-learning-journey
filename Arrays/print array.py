# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 19:51:27 2018

@author: Sharmila
"""

dinosaurNames = ["tyranasaurus", "Tapejera", "Yudon"]

print("Check using while")
index = 0
while (index < len(dinosaurNames)):
    print(index)
    print (dinosaurNames[index])
    if(dinosaurNames[index][0] == 't'):
        print("Starts with 't'");
    index += 1
    
print("Print using while")
index = 0
while (index < len(dinosaurNames)):
    print (dinosaurNames[index])
    index += 1
    
print("Print using for")
for dinosaurName in  dinosaurNames :
    print(dinosaurName)
    
print("Check using for")
for dinosaurName in  dinosaurNames :
    if(dinosaurName.startswith("t") or dinosaurName.startswith("T")):
        print(dinosaurName, "Starts with 't'");