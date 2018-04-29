# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 12:28:58 2018

@author: Sharmila
"""

vacationFile = open("VacationPlaces", "r")

vacationData = vacationFile.read();

print(vacationData);

vacationFile.close

print("Done")