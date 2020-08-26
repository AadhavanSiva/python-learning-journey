# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 11:29:46 2020

@author: Aadhavan
"""

FileName = input("Please enter a name for the file u will be creating")
data = "1\n2\n3\n1\n2\n3\n"

#textFile = open(FileName,"x")
#textFile.close();


textFile = open(FileName,("a"))
textFile.write(data);
textFile.close();


textFile = open(FileName,("r"))
textData = textFile.read();
textFile.close();


textFile = open(FileName,("r"))
for x in textFile:
    number = data.count("\n")
print("Your file has {0} lines".format(number))
textFile.close();
