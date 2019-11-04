# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 18:39:33 2019

@author: Aadhavan
"""
#

quotient  = number % 3
quotient2 = number % 5
quotient3 = number % 15

def fizz_buzz(number):
    quotient  = number % 3
    quotient2 = number % 5
    quotient3 = number % 15
    if(quotient3 <= 0):
        answer = "fizz_buzz"
    elif(quotient <= 0):
        answer = "fizz"
    elif(quotient2 <= 0):
        answer = "buzz"
    else:
        answer = number
    
    return answer
    

three = 3
five = 5
number = int(input("PLEASE ENTER A NUMBER"))
print( fizz_buzz(number ))