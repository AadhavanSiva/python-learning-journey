# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 18:45:47 2019

@author: Aadhavan
"""
import tkinter as tk

index = tk.Tk()

tk.Label(index,text="WHAT IS YOUR NAME").grid(row = 0) 
tk.Label(index,text="WHAT IS YOUR orgin").grid(row = 1) 
tk.Label(index,text="WHAT IS YOUR destination").grid(row = 2) 

nameEntry = tk.Entry(index)
originEntry = tk.Entry(index)
destinationEntry = tk.Entry(index)

nameEntry.grid(row=0, column=1)
originEntry.grid(row=1, column=1)
destinationEntry.grid(row=1, column=1)

tk.Button(index, text='Quit', command=index.destroy).grid(row=3, column=0,  pady=4)

index.mainloop()

   