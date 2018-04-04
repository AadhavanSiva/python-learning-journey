# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 20:30:39 2018

@author: Sharmila
"""

coins = []
usercoins = int(input("please enter the amount of coins you have"))

if (usercoins != 0):
    coins.append(usercoins)

while(usercoins != 0):
    usercoins = int(input("please enter the amount of coins you have"))
    if (usercoins != 0):    
        coins.append(usercoins)

if ( len(coins) != 0) :
    print("Printing coins array")
else:
    print (" You have zero coins ")
    
index = 0
while (index < len(coins)):
    print (coins[index] )
    index += 1  
#print (coins)
    
