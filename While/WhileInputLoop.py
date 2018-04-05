# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 19:20:38 2018

Compare number with greatest, if greater store number to greatest

@author: Sharmila
"""
# 7 3 2 9 12 0


numberone = 0
numbertwo = 0


number =int(input("please enter a number "))
#if (number > 5):
#    numberone += 1
#     
    

while (number != 0):
    #print(number);
    if (number >= 5):
        numberone += 1
        print ("Greater than or equal to 5 ")
    else:
        numbertwo += 1
        print("Lesser than 5")
        
        
    number = int(input("please enter a number "))
    
        
print ("Greater than 5 count = ", numberone)
print ("Lesser than or equal 5 count = ", numbertwo)
    
print("***  Done   ***")













number =int(input("please enter a number "))

while (number != 0):
    #print(number);
    if (number >= 5):
        print ("Greater than or equal to 5 ")
    else:
        print("Lesser than 5")
    number = int(input("please enter a number "))
    
print("***  Done   ***")