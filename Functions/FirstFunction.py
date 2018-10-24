# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:43:00 2018

@author: Sharmila
"""



def double(number):
    result = number * 2;
    return result;

def triple(number):
    result = number * 3;
    return result;
#    
def addTwoNumbers(number1, number2):
    result = number1 + number2;
    return result;

def Hello():
    print("Hello")
    return

def sayHello(language = "english"):
    if( language == "spanish"):
        print("Hola")
    elif( language=="french"):
        print("Bonjour")
    elif( language=="german"):
        print("Hallo")
    else:
        print("Hello")
    return;

#number=5
#xyz = double(number);
#print(xyz) 
#
#
#a, b = 5, 4
#addResult = addTwoNumbers(a,b);
#print(addResult)

Hello()
sayHello("german");
sayHello();

number1 = triple(2323442)
print(number1)
sum = addTwoNumbers(4, 8)
print(sum)