# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 18:52:55 2021

@author: Aadhavan
"""

def hoursToSeconds(hours):
    second = 0
    second = hours * 3600
    return second

hours = int(input("Please enter the number of hours you would like to change into seconds"))

print(hoursToSeconds(hours))