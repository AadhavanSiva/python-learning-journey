# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 18:55:49 2018

@author: Sharmila
"""
# 12, 3, 15, 7, 8, 0
# Above 10 = 2
# Below 10 = 3

aboveTen = 0
belowTen = 0

coins = int(input("Please enter the number of coins you have"))
if (coins > 10):
    aboveTen += 1
    
else:
    belowTen += 1



while (coins != 0):
    coins = int(input("Please enter the number of coins you have"))
    if (coins > 10):
        aboveTen += 1
        
    else:
        belowTen += 1
    
print("aboveTen = ", aboveTen)
print("belowTen = ", belowTen)

#print()