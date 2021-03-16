# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:25:48 2021

@author: Aadhavan
"""

usernamePassword = {
        "user1" : "password1",
        "user2" : "password2",
        "Sharmila1654" : "Jasmine123",
        "user3" : "password3",
                        }
def CheckUsernameAndPassword(usernamePassword):
    userName = input("Enter your username")
    password = input("Enter your password")
    if password == usernamePassword[userName]:
        print("login correct")
        
CheckUsernameAndPassword(usernamePassword)