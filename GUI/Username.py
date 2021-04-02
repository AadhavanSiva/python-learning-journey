# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 17:04:28 2021

@author: Aadhavan
"""

import tkinter as tk

index = tk.Tk()

def printUser():
    username = name_var.get()
    print("work{username}")
    
    

tk.Label(index,text="What is your user name").grid(row = 0) 
tk.Label(index,text="What is your password").grid(row = 1) 
UsernameEntry = tk.Entry(index,textvariable=name_var).grid(row=0, column=1)
PasswordEntry = tk.Entry(index)

PasswordEntry.grid(row=1,column=1)

btn = tk.Button(index, text='Print', command=index).grid(row=3, column=0,  pady=4)
index.mainloop()
