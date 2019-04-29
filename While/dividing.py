# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:52:08 2019
@author: Aadhavan
"""

divisor = 8
dividend = int(input("PLEASE ENTER A NUMDER TO BE DIVIDED BY 8"))
if(divisor  <= dividend):
    print("good")
    r = dividend % divisor
    if(r >= 1):
       print("The number is not diviseble by 8")
    else:
       print("The number is diviseble by 8")

else:
    print("The number was too low")