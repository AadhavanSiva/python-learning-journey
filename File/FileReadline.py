# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 19:12:02 2018

@author: Aadhavan
"""

vacationFile = open("VacationPlaces", "r")
while( True ):
    vacationData = vacationFile.readline();
    if not vacationData:
        break;
    print(vacationData)
    

vacationFile.close();
