# -*- coding: utf-8 -*-
"""
Created on Sun May  6 13:21:55 2018

@author: Sharmila
"""
namesFile = open("moviesName.dat","a")

name = input("Please enter a movie name")
while( name != "done" ):
    namesFile.write(name)
    namesFile.write(",")
    namesFile.write("\n")
    name = input("Please enter a movie name")

namesFile.close()
