# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 18:08:13 2020

@author: Aadhavan
"""




file = open("cities", "r")
lines = 0
cities = {}
countries = {}
for line in file:
    line = line.strip("\n")
    words = line.split(",")
    country = words[1].lstrip().rstrip()
    city = words[0].rstrip().lstrip()
    countries[country] = city
    cities[city] = country
   
numberOfcities = (len(cities))
print("The file cities has {0} unique cities and {1} unique countries".format(numberOfcities,len(countries)))