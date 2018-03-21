# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 18:32:32 2018

@author: Sharmila
"""

# startingNumber
# endingNumber
# incrementNumber
# starting number 1 
# ending number 5
# increment number 2
# result, 
#  1
#  3
#  5

# starting number 2 
# ending number 10
# increment number 3
# result, 
#  2
#  5
#  8

# 
# starting number 9
# ending number 2
# decrement number 3
# index 1

# result, 
#  9
#  6
#  3


startingNumber = int(input("Please enter starting number"))
endingNumber = int (input("Please enter a ending  number"))
decrement = int (input("Please enter  decrement "))

index = startingNumber

while ( index >= endingNumber ):
        print (index)
        index  -= decrement 