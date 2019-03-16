# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 13:35:40 2019

@author: Sharmila
"""

height = int(input("The height of your choosen shape"))
base = int(input("The base of your choosen shape"))

if (height > 0 and base > 0):
    print("Your shape is", height, "tall")
    print("Your shape is", base, "base")
    n = input("Are you sure. Say 'yes' or 'no' ")
    s = n.rstrip()
    if(s == "yes"):
        True;
    elif(s == "no"):
        False;
    else:
        print("your choice is invalid.  Try again")
else:
    print("input has to be greater")