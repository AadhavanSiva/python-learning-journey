# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 18:49:19 2019

@author: Aadhavan
"""


import tkinter as tk

def show_entry_fields():
    #userName = e1.get() + ", " + e2.get()
    #statusLabel.text = userName;
    print("First Name: ", e1.get() );
    print("Last Name: ", e2.get() );

#   msg = tk.Message(master, text ="First Name: %s\nLast Name: %s" ); 
#   msg.config(bg='lightgreen', font=('times', 24, 'italic'))
#   msg.pack()
   #% (e1dsdqweq.get(), e2.get()))

#main window
master = tk.Tk()

msg = tk.Message(master, text = "")
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
#msg.pack()
 
tk.Label(master, 
         text="First Name"
         ).grid(row=0)
tk.Label(master, text="Last Name").grid(row=1)


e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master, text='Quit', command=master.destroy).grid(row=3, column=0,  pady=4)
tk.Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1,  pady=4)

master.mainloop( )