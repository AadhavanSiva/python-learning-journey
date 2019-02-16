# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 11:24:31 2019

@author: Aadhavan
"""

import tkinter as tk

def show_language_selection():
    print(languageVariable.get())

root = tk.Tk()



languageVariable = tk.IntVar()

tk.Label(root, 
        text="""Choose a ZX
programming language:""",
        justify = tk.LEFT,
        padx = 20).pack()
tk.Radiobutton(root, 
              text="Python",
              padx = 20, 
              variable=languageVariable, 
              value=1).pack(anchor=tk.W)
tk.Radiobutton(root, 
              text="Scratch",
              padx = 20, 
              variable=languageVariable, 
              value=2).pack(anchor=tk.W)
tk.Radiobutton(root, 
              text="Java",
              padx = 20, 
              variable=languageVariable, 
              value=3).pack(anchor=tk.W)

tk.Button(root, text='Show', command=show_language_selection).pack()

root.mainloop()