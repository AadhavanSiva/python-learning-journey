# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:53:07 2020

@author: Aadhavan
"""

colors = ["Red", "Blue", "White", "Yellow"]
print(colors[0])
print(colors[2])

#print entire list
print("To print entire list", colors)

print("Number of colors", len(colors))
#print one by one by looping thru the list

number_of_values = len(colors)-1
#sum = 0
counter = 0
print("To print entire list one by one with while loop")
while (counter <= number_of_values): 
    print( colors[counter] )
    counter = counter + 1
    


print("Adding Orange color")
print("To print entire list one by one with for loop")
colors.append("Orange")
for color_name in colors:
    print(color_name)
    if( color_name == "White"):
        print("This is favourite color")

print("Removing Orange")
colors.remove("Orange")

print("To print entire list one by one with for loop, after removing orange")
for color_name in colors:
    print(color_name)
    
print("Clearing the list")
colors.clear()

print("To print entire list one by one with for loop, after clearing")
for color_name in colors:
    print(color_name)
print("end")