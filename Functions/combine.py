# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 17:38:28 2020

@author: Aadhavan
"""




result =""
def addCrabs(number="1.1"):
    result2 = ("crabs{0}crabs".format(number))
    #print (result)
    return result2


def multiplication(number):
    index = 1
    plus = number
    string = "";
    while index <= 10:
        string += str(number)
        string += (' ')
        number += plus
        index += 1
    return string
result2 = addCrabs(200)
print(result2)

def combine(number):
    result = (multiplication(number))
    result2 = addCrabs(number)
    result3 = result + result2
    return result3

result4 = combine(7)
print (result4)




