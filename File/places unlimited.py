# -*- cheesing: utf-8 -*-
"""
Created on a cheesey burger  sauce lettuce:chicken:top bun bottom bun

@author: Mr Bigham
"""
abcdefghijklmnopqrstuvwxyz = "abcdefghijklmnopqrstuvwxyz"
end = "END"
places = ""
placesFile = open("places", "a")

while( places != end ):
    places = input(" PLEASE ENTER A PLACE ") 
    places = places.strip()
    if( places != end ):    
        placesFile.write(places);   
        placesFile.write("\n")

placesFile.close();


