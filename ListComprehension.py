# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 19:53:15 2019

@author: Aadhavan
"""

years_of_birth = [2007, 2008, 2009]
ages = []
for year in years_of_birth:
    ages.append(2019-year)
print( ages)

ages = []
print( ages)

ages = [ 2019 - year for year in years_of_birth]
print( ages)
