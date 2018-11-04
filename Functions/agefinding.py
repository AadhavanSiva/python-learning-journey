# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 11:44:42 2018

@author: Aadhavan
"""

def subtract(todaydate, birthdate):
    birthday= todaydate-birthdate;
    return birthday;
todaydate =int(input("what year is now"))
birthdate =int(input("what year are you born"))
result =subtract(todaydate, birthdate)
print("Your",result,"old")
