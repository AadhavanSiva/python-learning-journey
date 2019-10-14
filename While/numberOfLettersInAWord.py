# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 10:23:26 2019

@author: Aadhavan
"""

word = input("PLEASE ENTER A WORD.")#word
#letter = input("Please enter a letter")
index = 0
position = len(word) - 1
uniqueLetters = []
a = 0
nol = 0
b = 0
print("index =", index)
foundIt = False
while (index <= position):
    print("work1") 
    
    index2 = 0
    position2 = len(uniqueLetters) - 1
    
    found = False
    print("Unique letters", uniqueLetters)
    print("Letter to check", word[index])
    while(index2 <= position2 ):
        if(word[index] == uniqueLetters[index2]):
            found = True
            break
        index2 += 1
            
    if( found == False):
        uniqueLetters.append( word[index])
    index += 1

print(uniqueLetters)
#    if( word[index] == letter[0]):
#        foundIt = True
#        
#    
#    index += 1
#if( foundIt == True):
#    print("Found it")
#else:
#    print("Not found it")
##    while (word[index] != uniqueLetters[index2]):
#        print("work2")
#        nol = 0
#        if(word[index] ==)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#        if (word[index] == word[a]):
#            print("work3")
#            nol +=1
#            print (word[index], "=", nol)
#            word[index].append.uniqueleter
#        a += 1
#        index += 1
#    
#    