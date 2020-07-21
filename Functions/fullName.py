# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 23:05:21 2020

@author: Aadhavan
"""
fullName = ""
def fullname(firstname='Aadhavan',lastname = 'Sivakumar'):
    result = ('{0} {1}'.format(firstname,lastname))
    return result

result = (fullname("oviya", "sivakumar")) 
print(result)