# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 19:01:31 2018

@author: Sharmila
"""

readFile = open("File1.txt", "r")
writeFile = open("File2.txt", "w")

fileData = readFile.read();
print (fileData.lower())

writeFile.write(fileData);

readFile.close();
writeFile.close();




