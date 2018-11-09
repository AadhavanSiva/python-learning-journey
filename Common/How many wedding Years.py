# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 19:52:54 2018

@author: Aadhavan
"""

import datetime
currentTime = datetime.datetime.now()
currentYear = currentTime.year

print("Current year = ", currentYear)
sivaWeddingDate = datetime.datetime(2004, 11, 17)
sivaWeddingYear = sivaWeddingDate.year
numberOfYears = currentYear - sivaWeddingYear
print(numberOfYears)