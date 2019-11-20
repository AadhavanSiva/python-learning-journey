# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 18:27:07 2019

@author: Oviya
"""

def square(number):
    result = number * number
    return result

def is_even(number):
    remainder = number % 2
    print(remainder)
    if( remainder > 0):
        return False
    else:
        return True

def multiples_of_n(number, n):
    remainder = number % n
    print(remainder)
    if( remainder > 0):
        return False
    else:
        return True
    
def multiples_of_8(number):
    remainder = number % 8
    print(remainder)
    if( remainder > 0):
        return False
    else:
        return True
    
def multiples_of_5(number):
    remainder = number % 5
    print(remainder)
    if( remainder > 0):
        return False
    else:
        return True

print( square(5) )
print( square(4) )
print(is_even(7))

print(is_even(78))

number = 12354
if( multiples_of_8(number) ):
    print(number, " is a multiples of eight")
else:
    print(number, " is not a multiples of eight")
    
n = 3
if( multiples_of_n(number, n) ):
    print(number, " is a multiples of ", n)
else:
    print(number, " is not a multiples of ", n)
    
print( multiples_of_n(3080, 22))