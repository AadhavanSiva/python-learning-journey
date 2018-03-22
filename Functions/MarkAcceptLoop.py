# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 19:42:08 2018

@author: Sharmila
"""

marks = int(input("Please enter your marks"))
while ( marks != 0 ):
    if (marks >= 60):
        print ("pass")
        
    if (marks < 60):
        print ("fail")

    marks = int(input("Please enter your marks"))
    
