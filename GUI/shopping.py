# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 10:07:41 2019

@author: Aadhavan
"""

import tkinter as tk

def show_entry_fields():
    #userName = e1.get() + ", " + e2.get()
    #statusLabel.text = userName;
    print("chicken", chicken.get())
    print("chickenQT", ChickenQT.get() );
    print(pay.get() );





food = tk.Tk()
tk.Label(food, 
         text="DIARY PRODUCT"
         ).grid(row=0, column = 0)
tk.Label(food, 
         text="MEAT PRODUCT"
         ).grid(row=4, column = 0)

good = tk.IntVar()
good1= tk.IntVar()
good2= tk.IntVar()
chicken = tk.IntVar()
goat= tk.IntVar()
lamb= tk.IntVar()
pig = tk.IntVar()
cow= tk.IntVar()
turkey= tk.IntVar()
n= tk.IntVar()
pay=tk.IntVar()
tk.Label(food, text="QT").grid(row=5, column=1)
ChickenQT = tk.Entry(food)
ChickenQT.grid(row=5, column=2)


tk.Checkbutton(food, text="CHEESE", variable=good).grid(row=1, sticky=tk.W)
tk.Checkbutton(food, text="MILK", variable=good1).grid(row=2, sticky=tk.W)
tk.Checkbutton(food, text="YOGURT", variable=good2).grid(row=3, sticky=tk.W)
tk.Checkbutton(food, text="CHICKEN", variable=chicken).grid(row=5, sticky=tk.W)
tk.Checkbutton(food, text="GOAT", variable=goat).grid(row=6, sticky=tk.W)
tk.Checkbutton(food, text="LAMB", variable=lamb).grid(row=7, sticky=tk.W)
tk.Checkbutton(food, text="PIG", variable=pig).grid(row=8, sticky=tk.W)
tk.Checkbutton(food, text="COW", variable=cow).grid(row=9, sticky=tk.W)
tk.Checkbutton(food, text="TURKEY", variable=turkey).grid(row=10, sticky=tk.W)

tk.Radiobutton(food, 
              text="CREDIT",
              padx = 20, 
              variable=pay, 
              value=0).grid(row=11, sticky=tk.W)
tk.Radiobutton(food, 
              text="DEBIT",
              padx = 20, 
              variable=pay, 
              value=1).grid(row=11, column=1, sticky=tk.W)
tk.Radiobutton(food, 
              text="CASH",
              padx = 20, 
              variable=pay, 
              value=2).grid(row=11, column=2, sticky=tk.W)


tk.Button(food, text='Quit', command=food.destroy).grid(row=12, column=0,  pady=4)
tk.Button(food, text='Show', command=show_entry_fields).grid(row=12, column=1,  pady=4)


food.mainloop();


