# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 17:46:24 2019

@author: Aadhavan
"""
def reverse_string(word):
    index = 0
    reword = "";
    position = len(word) - 1
    while index <= position:
        reword += (word[position])
        position -= 1
        print (reword)
    return reword

def is_palindrome_number(number):
    number_string = str(number)
    print("Number =", number)
    print("Number string = ", number_string)
    reverse_string1 = reverse_string(number_string)
    print("reverse string1 = ", reverse_string1)
    if( number_string == reverse_string1):
        return True
    else:
        return False
    
number = input(" Please enter a number")
print("Reversed string=", reverse_string(str(number)) )

print(is_palindrome_number(number))
