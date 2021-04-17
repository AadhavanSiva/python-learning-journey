# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 18:13:19 2021

@author: Aadhavan
"""
import tkinter as tk

def Print():
    index = 0
    results = 0
    one = first.get()
    two = second.get()
    while results + 1 <= one:
       print(two + index)
       results = two + index
       index += 1
main = tk.Tk()

tk.Label(main, text='First Number').grid(row=0)
tk.Label(main, text='Second Number').grid(row=1)

first =  tk.IntVar()
second = tk.IntVar()

firstNumber = tk.Entry(main,textvariable= first).grid(row=0, column=1)
secondNumber = tk.Entry(main,textvariable= second).grid(row=1, column=1)

tn = tk.Button(main, text="Calculate price", command= Print).grid(row=2, column=1)

main.mainloop()
