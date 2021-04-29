# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 19:53:58 2021

@author: Aadhavan
"""
import tkinter as tk
import requests

def getDistance():
    from_address = from_address_var.get()
    to_address = to_address_var.get()
    print(from_address)

    response = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=" + from_address + "&destinations=" + to_address + "&key=REDACTED_GOOGLE_API_KEY")


    # print response
    print(response)

    # print json content
    # print(response.json())
    distance = response.json()
    print(distance)
    for mins in distance:
        #print(f"time = {mins['duration']}")
        break





main = tk.Tk()
main.geometry("500x200")
from_address_var = tk.StringVar()
to_address_var = tk.StringVar()

tk.Label(main, text='From address').grid(row=2)
tk.Label(main, text='To address').grid(row=3)
fromAddressEntry = tk.Entry(main,textvariable=from_address_var).grid(row=2, column=1)
toAddressEntry = tk.Entry(main,textvariable=to_address_var).grid(row=3, column=1)






btn = tk.Button(main, text="Get distance", command=getDistance).grid(row=7, column=1)
main.mainloop()