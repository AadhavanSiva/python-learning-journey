# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 12:40:13 2018

@author: Aadhavan
"""

moviesFile = open("moviesName","r")
while ( True ):
    movieName = moviesFile.readline();
    if not movieName:
        break;
    movieName = movieName.strip();
    
    print(movieName[0],movieName[1])

moviesFile.close();
