# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 21:12:30 2018

@author: Aadhavan
"""

CountryList = []
for i in  range(3):
    Country = input("Please Enter Your country:")
    CountryList.append(Country)

#CountrySet = set (CountryList)
#
#print(CountryList)
#print(CountrySet)
#
#if "US"in (CountrySet):
#    print ("attended")
#    
CountryDictionary ={}
for Country in CountryList:
    if Country in CountryDictionary:
        print("not working")
        CountryDictionary[Country] += 1
    else:
        print("working")
        CountryDictionary[Country] = 1
    
print(CountryDictionary)