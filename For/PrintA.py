# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 20:39:21 2018

@author: Sharmila
"""
#print( "A" * 1)
#print( "A" * 2)
#print( "A" * 3)
#
#print( "A" * 3)
#print( "A" * 2)
#print( "A" * 1)

# Learned range function is to generate list of numbers with 2 & 3 parameters
Length = 5
toPrint = "8"
numbers = range( 1, Length +1)

for number in numbers :
    print(toPrint * number ) 
    
numbers = range(Length, 0, -1)
for number in numbers :
    #print(pos)
    print(toPrint * number ) 


#numbers = 10
#toPrint = "o"
#for pos in range(1,numbers +1):
#    print(toPrint*pos)
#numbers = [1,2,3]
#for number in numbers:
#    print("O"*number)
#    
    
    