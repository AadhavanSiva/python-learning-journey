# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:13:57 2020

@author: Oviya
"""

names = ["1", "2"]
if "3" in names:
    print(names)
Tv_shows = {
        1: "Family Fued",
        2: "Bunkd",
        3: "Scooby Doo",
        4: "Everybody Loves Ramond",
        5: "Everybody Loves Siva"
        }
for tvShow_ranks in  Tv_shows:
    print("Number: ",  tvShow_ranks,"  Name of Show: ", Tv_shows[tvShow_ranks])
    
rankPicker = int(input("Pick a rank"))
#if (rankPicker > 4):
#    print("Rank not found")
#else:
#    print(Tv_shows[rankPicker])
    
if rankPicker in Tv_shows:
    print(Tv_shows[rankPicker])
else:
    print("Rank not found")
    