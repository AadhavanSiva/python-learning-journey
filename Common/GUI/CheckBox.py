# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 19:00:07 2019

@author: Aadhavan
"""

import tkinter  as tk

def show_selections():
    print(above25.get())
    print(married.get())
    
root = tk.Tk()
#variable for Above 25
above25 = tk.IntVar()
#checkbutton for Above25
tk.Checkbutton(root, text="Above 25", 
               variable=above25).grid(row=0, sticky=tk.W)

#variable for married
married = tk.IntVar()
#checkbutton for Married
tk.Checkbutton(root, text="Married", variable=married).grid(row=1, sticky=tk.W)

tk.Button(root, text='Show', command=show_selections).grid(row=2, sticky=tk.W)
tk.mainloop()