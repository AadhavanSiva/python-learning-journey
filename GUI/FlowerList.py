# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 18:49:18 2021

@author: Aadhavan
"""

import tkinter as tk

def add():
    flowersList.append(first.get())
    print(first.get())
    
def Print():
    print(flowersList)

main = tk.Tk()

tk.Label(main, text='Flower').grid(row=0)

first =  tk.StringVar()

flower = tk.Entry(main,textvariable= first).grid(row=0, column=1)

tn = tk.Button(main, text="Add List", command= add).grid(row=2, column=1)
tn = tk.Button(main, text="Print list", command= Print).grid(row=2, column=2)

flowersList = []

main.mainloop()
