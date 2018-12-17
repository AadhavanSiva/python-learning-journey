# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 18:02:57 2018

@author: Sharmila
"""

placesFile = open("Places","w")

while (True):
    place = input("Enter a place:")
    if (place == "end"):
        break;
    else:
        placesFile.write(place)
        placesFile.write("\n")
        
    print(place)
placesFile.close();