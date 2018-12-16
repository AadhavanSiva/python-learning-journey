# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 13:16:30 2018

@author: Aadhavan
"""

movieNames = []

moviesFile = open("moviesName","r")
count = 0
startWith = input("Enter the character to search the movie");
while( True ):
    movieName = moviesFile.readline();
    if not movieName:
        break;
    movieName = movieName.strip()
    if(movieName[0] == startWith):
        #print(movieName)
        count += 1
        movieNames.append(movieName)
    #print(movieName)
print("Movie name starts with ", startWith, " = ", count)

position = len(movieNames) - 1
count = 0
while(count <= position):
    print(movieNames[count])
    count += 1
moviesFile.close();
