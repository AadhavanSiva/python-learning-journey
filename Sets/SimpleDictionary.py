# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 21:12:30 2018

@author: Aadhavan
"""


BaseBallScores ={ 
            "Aadhavan":3,
            "Gayle":1
                 };
#print(BaseBallScores)

print( BaseBallScores["Aadhavan"] );

BaseBallScores["Aadhavan"] += 1

print( BaseBallScores["Aadhavan"] );

for BaseBallScore in BaseBallScores:
    print(BaseBallScore)
    print(BaseBallScores[BaseBallScore])
    
BaseBallScores["Oviya"] = 3
print(BaseBallScores);

BaseBallScores["Oviya"] = 4
print(BaseBallScores);

playerName = input("Enter players name")
if playerName in BaseBallScores:
    print(BaseBallScores[playerName])
else:
    print("Invalid player name")
#for Country in CountryList:
#    if Country in CountryDictionary:
#        print("not working")
#        CountryDictionary[Country] += 1
#    else:
#        print("working")
#        CountryDictionary[Country] = 1
    
#print(CountryDictionary)