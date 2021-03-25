# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 17:50:44 2021

@author: Aadhavan
"""
def addAllNumbers (listOfNumbers):
    allNumbers = len(listOfNumbers) - 1
    sumOfNumbers = 0
    index = 0
    while index <= allNumbers:
        sumOfNumbers += listOfNumbers[index]
        index += 1
    return sumOfNumbers

def greatestNumber (listOfNumbers):
    allNumbers = len(listOfNumbers) - 1
    index = 0
    greatestNumber = 0
    while index <= allNumbers:
        if greatestNumber < listOfNumbers[index]:
            print("a")
            greatestNumber = listOfNumbers[index]
        index += 1
    return  greatestNumber   
            
numbers = []
index = 0
while index <= 4:
    numberToAdd = int(input("Please enter a number"))
    numbers.append(numberToAdd)
    index += 1

sumOfAllNumbers  =  addAllNumbers(numbers)

print("This is the sum of all the numbers you entered",sumOfAllNumbers )
greatestOfAllValues = greatestNumber(numbers)

print("This is the highest number you entered", greatestOfAllValues)
