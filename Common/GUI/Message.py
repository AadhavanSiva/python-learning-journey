# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 19:07:19 2019

@author: Aadhavan
"""

import tkinter as tk
master = tk.Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = tk.Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack()
tk.mainloop()