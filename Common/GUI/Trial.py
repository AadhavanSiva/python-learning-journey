# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:08:15 2019

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
#tk.mainloop()

def show_language_selection():
    print(languageVariable.get())

root1 = tk.Tk()


age = 11;

languageVariable = tk.IntVar()

tk.Label(root1, 
        text="""Choose a 
programming language:""",
        justify = tk.LEFT,
        padx = 20).pack()
tk.Radiobutton(root1, 
              text="Python",
              padx = 20, 
              variable=languageVariable, 
              value=1).pack(anchor=tk.W)
tk.Radiobutton(root1, 
              text="Scratch",
              padx = 20, 
              variable=languageVariable, 
              value=2).pack(anchor=tk.W)
tk.Radiobutton(root1, 
              text="Java",
              padx = 20, 
              variable=languageVariable, 
              value=3).pack(anchor=tk.W)

tk.Button(root1, text='Show', command=show_language_selection).pack()

root1.mainloop()