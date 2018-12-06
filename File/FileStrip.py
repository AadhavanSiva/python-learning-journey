# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 19:37:59 2018

@author: Aadhavan
"""

with open("VacationPlaces", "r") as fd:
    for line in fd:
        print(line)
        line = line.strip()