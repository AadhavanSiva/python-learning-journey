# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 17:18:42 2021

@author: Aadhavan
"""

import tkinter as tk

def calculate_price():
    fishName = name_var.get()
    total_price = quantity_var.get() * price_var.get()
    print( f"Total price for {fishName} is {total_price}")


main = tk.Tk()

name_var = tk.StringVar()
quantity_var = tk.IntVar()
price_var = tk.IntVar()

tk.Label(main, text='Fish name').grid(row=0)
tk.Label(main, text='Quantity').grid(row=1)
tk.Label(main, text='Price').grid(row=2)

nameEntry = tk.Entry(main,textvariable=name_var).grid(row=0, column=1)
quantityEntry = tk.Entry(main, textvariable=quantity_var).grid(row=1, column=1)
priceEntry = tk.Entry(main,textvariable=price_var).grid(row=2, column=1)

btn = tk.Button(main, text="Calculate price", command=calculate_price).grid(row=4, column=2)
main.mainloop()
