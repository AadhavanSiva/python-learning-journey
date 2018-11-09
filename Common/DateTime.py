# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 19:14:32 2018

@author: Aadhavan
"""

import datetime

#To get current time
currentTime = datetime.datetime.now()
print("Current time =", currentTime)

#to create DateTime object/data type
aadhavaBirthDate = datetime.datetime(2007,10, 30)

oviyaBirthDate = datetime.datetime(2009, 8, 28 )

print("Aadhvana's Birtdate :", aadhavaBirthDate )

print("Aadhvana's Birtdate(shortformat) :", aadhavaBirthDate.strftime("%x") )
print("Oviya's Birtdate :" ,oviyaBirthDate.strftime("%m/%d/%Y"))

currentYear = currentTime.year
print("Current year = ", currentYear)
aadhavaBirthYear = aadhavaBirthDate.year
aadhavanAge = currentYear - aadhavaBirthYear
print("Age ", aadhavanAge)

print("Aadhavan's Birth weekday = ", aadhavaBirthDate.strftime("%A") )
print("Oviya's Birth weekday = ", oviyaBirthDate.strftime("%A") )

