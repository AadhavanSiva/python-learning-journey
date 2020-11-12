# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 17:49:59 2020
@author: Aadhavan
"""

FileName =("cities.txt")
americanFile = open("americanCities.txt","w")
CitiesFile = open("normalCities.txt","w")

File = open(FileName,"r")
index = 0
for x in File:
    words = x.split()
    words[0] = x.split(",")   
    words = x.split()
    print(words[0])
    print(words[1])
    print("    ")
    if words[1] == "USA":
        print("ye")
        americanFile.write(words[0])
        americanFile.write(words[1])
        americanFile.write("\n")
    else:
        CitiesFile.write(words[0])
        CitiesFile.write(words[1])
        CitiesFile.write("\n")
File.close()