# -*- coding: utf-8 -*-
"""
Created on Tue May  1 21:11:13 2018

@author: Sharmila
"""

movieName = input("Please enter your fauvorite movie")

movieYear = input ("Please enter the time the movie released")

moviesFile = open("movieNameAndYear.dat", "a")

moviesFile.write(movieName)
moviesFile.write(",")
moviesFile.write(movieYear)
moviesFile.write("\n")

moviesFile.close()
print ("Done")
    