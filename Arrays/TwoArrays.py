# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 19:53:47 2018

@author: Sharmila
"""

aboveTen = []
belowTen = []

coins = int(input("Please enter the number of coins you have"))
if (coins > 10):
    aboveTen.append(coins)

else:
    belowTen.append(coins) 



while (coins != 0):
    coins = int(input("Please enter the number of coins you have"))
    if (coins > 10):
        aboveTen.append(coins)
        
    else:
        belowTen.append(coins)

print("Above ten values are : ")
index = 0
while (index < len(aboveTen) ):
    print (aboveTen[index] )
    index += 1

print("below below values are :")
index = 0
while (index < len(belowTen) ):
    print (belowTen[index] )
    index += 1

