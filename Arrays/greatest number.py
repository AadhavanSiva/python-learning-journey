# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 19:20:38 2018

Compare number with greatest, if greater store number to greatest

@author: Sharmila
"""
greatest = 0




number =int(input("please enter a number "))


while (number != 0):
    if (greatest < number):
        greatest = number
    number = int(input("please enter a number "))
    
print (greatest)