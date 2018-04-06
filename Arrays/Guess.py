# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 15:32:22 2018

 print (" author: Sharmila")
"""


numbers = [5, 4, 6, 5, 2]

index = 0
while( index < 650):
    numbers.append(1)
    index += 1
numbers.append(2)

acceptNumber = int(input("There is a secret number. Can you guess what it is. Hint: inside 10 over -1:")) 

index = 0
found = False
while ( index < len(numbers)):
    
    if ( numbers[index] == acceptNumber ):
         found = True
         break
         
    index += 1

if ( found == False):
    print("You failed, please try")
else:
    print ("CONGRATULATIONS !!! You have found the secret number")