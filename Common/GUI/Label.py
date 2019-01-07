# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 18:41:35 2019

@author: Aadhavan
"""

# To import tkinter module
import tkinter as tk


# To create main window
window1 = tk.Tk()

#To create the first label
tk.Label(window1, 
		 text="Red Text in Times Font",
		 fg = "red",
		 font = "Times").pack()
tk.Label(window1, 
		 text="Green Text in Helvetica Font",
		 fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic").pack()
tk.Label(window1, 
		 text="Blue Text in Verdana bold",
		 fg = "blue",
		 bg = "yellow",
		 font = "Verdana 10 bold").pack()

window1.mainloop()