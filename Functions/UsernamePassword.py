# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:02:40 2021

@author: Aadhavan
"""
class Authenticator:
    usernamePassword = {
                        }
    userDetails = []
    def registerNewAccount(self, User):
        self.usernamePassword[User[0]] = User[1]
        self.userDetails.append(User)
        
    def CheckUsernameAndPassword(self, userName, password):
#        userName = input("Enter your username")
#        password = input("Enter your password")
        print(userName)
        u = self.usernamePassword.keys()

        if userName not in u:
            return print("Indvalid username or password !")
        if self.usernamePassword[userName] == password:
            print("login correct")
        else: 
            print("Indvalid username or password !")


User1 = ("user1", "password1","user1@example.com","01/01/2000")
User2 = ("user2", "password2","user2@example.com","01/01/2001")

L = Authenticator()
L.registerNewAccount(User1)
L.registerNewAccount(User2)
L.CheckUsernameAndPassword("user1","password3")







