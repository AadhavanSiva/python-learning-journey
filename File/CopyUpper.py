# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 18:49:39 2018

@author: Aadhavan
"""
case = input("Please enter if your message wants to be in upper or lower")
readFile = open("File1.txt", "r")
writeFile = open("File2.txt", "w")

fileData = readFile.read();
if (case == "upper"):
    print (fileData.upper())
    writeFile.write(fileData.upper());
else:
    print (fileData.lower())
    writeFile.write(fileData.lower());


readFile.close();
writeFile.close();
