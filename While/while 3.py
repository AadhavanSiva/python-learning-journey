# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 21:29:33 2018

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


startingNumber = int(input("Please enter starting number"))
endingNumber = int (input("Please enter a ending  number"))

index = startingNumber
if( startingNumber < endingNumber ):
    while ( index <= endingNumber ):
        print (index)
        index += 1

if( startingNumber > endingNumber ):  
    while (index >= endingNumber):
         print (index)
         index -= 1

if( startingNumber == endingNumber ):
    print (index)