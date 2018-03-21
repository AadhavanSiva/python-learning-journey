# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 19:05:13 2018

@author: Sharmila
"""
#1 - 64
#1
#2
#4
# 8
#16
#32
#64

#  64
#  32
#  16
#   8
#   4
#   2
#   1
# startingNumber 64
# ending number 1
# count = 64
# print 64
# count 32
# print 32
# count 16

startingNumber=int(input("Please enter a starting number"))
endingNumber = int(input("Please enter a ending number"))
 
count = startingNumber

while (count >= endingNumber):
    print (count)
    count /= 2
    count = int(count)
    
