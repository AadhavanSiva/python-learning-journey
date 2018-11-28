# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 17:43:13 2018

@author: Aadhavan
"""
# True - Occupied, False - Free
parkingLots = [False,False,False,False, False, False,]

while(True):
    lotNumber = int(input("Enter the lot number (0 - exit/to know status)"))
    if ( lotNumber == 0 ):
        break
    else:
        lotStatus = bool(int(input("Enter (0 - free), (1 - Occupied)")))
        #print(lotStatus)
    
    parkingLots[lotNumber-1] = lotStatus


position = 0
numberOfLots = len(parkingLots);
occupied = 0;
free = 0;
while(position < numberOfLots):
    if(parkingLots[position] == True):
        occupied += 1;
#    if(parkingLots[position] == False):
#        free += 1
    position += 1

    
print("Number of parking lots", numberOfLots)

print("No. of free", numberOfLots - occupied)

print("No. of occupied", occupied)
