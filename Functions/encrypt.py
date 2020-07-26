# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 15:46:28 2020

@author: Aadhavan
"""

#def PrintWord(word):
#    index = 0
#    position = len(word)
#    while(index <= position):
#        print(word[index])
#        index += 1
#        if (index >= position):
#            break
#    return word
#
#result = PrintWord("word")
#print(result)

def encrypt(word):
    normal =  "abcdefghijklmnopqrstuvwxyz"
    encrypt = "bcdefghijklmnopqrstuvwxyza"
    position = len(word)
    index = 0
    encryptedWord = ""
    while(index < position):  
        number = normal.find(word[index])
        if number == -1  :
            encryptedWord += str(word[index])
        else :
            number = normal.find(word[index])
            print("P")
            encryptedWord += str(encrypt[number])
            
        index += 1
    return encryptedWord

result = encrypt("hmm")
print(result)

result = encrypt("hi")
print(result)

result = encrypt("beats")
print(result)



