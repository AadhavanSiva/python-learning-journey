# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 19:53:58 2021

@author: Aadhavan
"""
import tkinter as tk
import requests


#http://api.openweathermap.org/data/2.5/weather?q=Medway,MA,USA&appid=b0caa4afebdccc4888b3829712d01495&units=imperial

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
#    print(distance)s

    for row in distance['rows']:
        for element in row['elements']:
            duration = element['duration']
            distance = element['distance']
            distance_var.set(distance['text'])
            duration_var.set(duration['text'])
            distanceWalking_var.set(distance['text']) 
            durationWalking_var.set(duration['text'])

    



main = tk.Tk()
main.geometry("500x200")

distance_var = tk.IntVar()

duration_var = tk.IntVar()

distanceWalking_var = tk.IntVar()

durationWalking_var = tk.IntVar()

from_address_var = tk.StringVar()

from_address_var.set("Medway, MA")
to_address_var = tk.StringVar()
to_address_var.set("Franklin, MA")

tk.Label(main, text='From address').grid(row=2)
tk.Label(main, text='To address').grid(row=3)
fromAddressEntry = tk.Entry(main,textvariable=from_address_var).grid(row=2, column=1)
toAddressEntry = tk.Entry(main,textvariable=to_address_var).grid(row=3, column=1)


btn = tk.Button(main, text="Get distance", command=getDistance).grid(row=5, column=1)


tk.Label(main, text='Distance by car').grid(row=7, column=0)
tk.Label(main, text='',textvariable=distance_var).grid(row=7, column=1)

tk.Label(main, text='Duration in car').grid(row=8, column=0)
tk.Label(main, text='',textvariable=duration_var).grid(row=8, column=1)

tk.Label(main, text='Distance by walking').grid(row=9, column=0)
tk.Label(main, text='',textvariable=distanceWalking_var).grid(row=9, column=1)

tk.Label(main, text='Duration to walk').grid(row=10, column=0)
tk.Label(main, text='',textvariable=durationWalking_var).grid(row=10, column=1)

main.mainloop()