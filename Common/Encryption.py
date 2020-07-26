# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 11:48:02 2019

@author: Aadhavan
"""

index = 0
l = []
normalText = input ("ENTER A WORD")
m = len(normalText) - 1

while (index <= m):
    unicode = ord(normalText[index])
    print(unicode)
    encryptedText = chr(  unicode + 1 );
    index += 1
    l.append(encryptedText)

l = ''.join(l)

print (l)
