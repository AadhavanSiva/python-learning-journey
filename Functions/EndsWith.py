# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 18:37:36 2018

@author: Aadhavan
"""

def endsWith(sentence, letterToCheck):
    position = len(sentence) - 1;
    if ( sentence[position] == letterToCheck):
         return True;
    else:
         return False; 
     
        
text = input("Enter a sentence")
letterToCheck =input("Enter a character/letter to check for")

    
found = endsWith(text, letterToCheck)
if( found):
    print("Ends with ", letterToCheck)
else:
    print("Doesn't end with ", letterToCheck)
#print(len("Hello"))