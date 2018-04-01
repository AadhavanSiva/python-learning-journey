# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 20:31:17 2018

@author: Sharmila
"""

movies = ["Moana","Bee","Balto", "Frozen", "Finding Nemo"]

print("Movie names")
index = 0
while (index < len(movies)):
    print (movies[index])
    index += 1
    
movie = input("Please enter a movie")
print (movie)

#if ( movie == movies[0] or movie == movies[1] or movie == movies[2]):
#    print("Movie found")
    
index = 0
while (index < len(movies)):
    if (movies[index] == movie):
        print("Movie found")
        print("at index", index)
    index += 1