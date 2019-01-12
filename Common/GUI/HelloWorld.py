# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 19:08:13 2019

@author: Aadhavan
"""

import tkinter as tk

#to create main windows
root = tk.Tk()

#create static text and attach to pack
tk.Label(root, 
		 text="Hello World").pack()

root.mainloop()