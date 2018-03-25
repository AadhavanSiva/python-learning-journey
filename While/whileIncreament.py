# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 19:03:16 2018

@author: Sharmila
"""

#  Write a program to accept endingNumber and increment number
#       display numbers from 0 to endingNumber by increment number
#     Ex:  endingNumber 10
#            Increment Number 3
#            0
#            3
#            6
#            9
count = 0
increamentNumber = int(input("please enter a increament number"))  
endingNumber = int(input("please enter a ending number"))
while (count < endingNumber):
    print (count)
    count += increamentNumber         