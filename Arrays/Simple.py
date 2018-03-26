# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 19:08:06 2018

@author: Sharmila
"""

ages = [ 10, 8, 36, 43 ]

fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange", "Strawberry"]

fruit1 = "Apple"
fruit2 = "Banana"

#print(ages[0])
#
#print(ages[1])
#
#print(ages[3])

ages[0] = 11

#print(ages[0])

#print(fruit1)
#print(fruit2)

print( len(ages) )
print( len(fruits) )
#
#index = 0
#while( index <= 4):
#    favoriteFruit = input( "Enter your favorite fruit")
#    fruits[index] = favoriteFruit
#    index += 1
#
#
index = 0
while( index < len(fruits) ):
    print( fruits[index] )
    index += 1
    