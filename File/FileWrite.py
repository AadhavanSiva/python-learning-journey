# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 12:22:39 2018

@author: Sharmila
"""

vacationSpots = ["New York", "Boston", "California", "Chennai", "Miami"]
#vacationSpots = ["Mysore", "Orlando"]

vacationFile = open("VacationPlaces", "a")

for vacationSpot in vacationSpots:
    vacationFile.write(vacationSpot);
    #vacationFile.writelines();
    vacationFile.write("\n")

 
vacationFile.close();
print("Done")