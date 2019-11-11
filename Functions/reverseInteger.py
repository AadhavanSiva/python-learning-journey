# -*- codisng: utf-8 -*-
"""
Created on Mon Nov 11 16:55:00 2019

@author: Aadhavan
"""
    


def pair(number):
    index = 0
    reword = "";
    position = len(number) - 1
    while index <= position:
        reword += (number[position])
        position -= 1
    check = True
    secretnumber = 6
    
    if(number == secretnumber):
        print(number,secretnumber)
        check = True
    elif(number != secretnumber):
        check = False
    else:
        print("not working")
    return check

number = input(" Please enter number")
check = True
secretnumber = 21
print(pair(check))
























def pair(secretnumber):
    check = True
    secretnumber = 6
    if(number == secretnumber):
        print(number,secretnumber)
        check = True
    elif(number != secretnumber):
        check = False
    else:
        print("not working")
    return check

