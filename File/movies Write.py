# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 12:39:50 2018

@author: Sharmila
"""

movies = ["Emoji", "Moana", "ninjago"]

moviesFile = open("moviesName", ("w"))
p = len(movies) - 1
for movie in movies:
    moviesFile.write(movie);
    moviesFile.write("\n")

moviesFile.close();
print("Done")

m = 0 
while (p >= m):
    m += 1
    print (m)
#moviesFile = open("moviesname","r")
#
#movieData = moviesFile.read();
#
#print(movieData);
#m = 0
#
#    
#moviesFile.close();
