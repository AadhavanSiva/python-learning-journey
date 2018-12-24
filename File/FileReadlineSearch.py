# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 19:12:02 2018

@author: Aadhavan
"""

inputPlace = input (" ENTER A PLACE WHERE A SPECIAL PROGRAM IS RUNNING ")
fileName = "VacationPlaces"
vacationFile = open(fileName, "r")
found = False;
while( True):
    vacationData = vacationFile.readline();
    vacationData = vacationData.strip()
    if not vacationData:
        break;
    #print(vacationData);
    if (inputPlace == vacationData):
        found = True;
        break;

    #    #print ("Sorry, special program is not available ")
    #else:
    #    found = True;
    #    #print (" Special program is available ")
    
if(found == True):
    print (" Special program is available ")
else:
    print ("Sorry, special program is not available ")
vacationFile.close();

#print("Done")