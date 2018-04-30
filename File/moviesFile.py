# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 20:06:48 2018

@author: Sharmila
"""
movieName = input("please enter a movie")
movieYear = input("please enter a year")

moviesFile = open("moviesNameAndYear", "a")

moviesFile.write(movieName)
moviesFile.write(",")
moviesFile.write(movieYear)
moviesFile.write("\n")
moviesFile.close();