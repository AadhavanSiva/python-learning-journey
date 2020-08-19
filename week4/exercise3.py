# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 19:02:21 2020

@author: Aadhavan
"""

def checkPalindrome(word,index,list1,list2):
    position = len(word) - 1
    position -= index
    print(index)
    list1.append(word[index])
    print ("Position =>",position)
    list2.append(word[position])
    if index == position or index > position:
        print(list1)
        print(list2)
        if list1 == list2:
            return True
        else:
            return False
    else:
        index += 1
        
        return checkPalindrome(word, index,list1,list2) 
        
result = checkPalindrome("mom",0,[],[])
print(result)

        