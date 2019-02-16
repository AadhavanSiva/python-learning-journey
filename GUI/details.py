# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 13:28:39 2019

@author: Aadhavan
"""

import tkinter as tk
def show_entry_fields():
    print("animal", animal.get())
    print("pet", pet.get() )
    print("Type", Type.get() )
    print("Habitat", habitat.get() )
    print(e1.get() );


details = tk.Tk()
animal = tk.IntVar()
e1 = tk.Entry(details)
e1.grid(row=0, column=1)
pet = tk.IntVar()
Type = tk.IntVar()
habitat = tk.IntVar()


tk.Label(details, 
         text="Name of the animal"
         ).grid(row=0)
tk.Radiobutton(details, 
              text="CARNIVORE",
              padx = 20, 
              variable=animal, 
              value=0).grid(row=1, column=0)
tk.Radiobutton(details, 
              text="HERBIVORE",
              padx = 20, 
              variable=animal, 
              value=1).grid(row=1, column=1)
tk.Radiobutton(details, 
              text="OMNIVORE",
              padx = 20, 
              variable=animal, 
              value=2).grid(row=1, column=2)

tk.Checkbutton(details, text="pet", 
               variable=pet).grid(row=2, column=0)


tk.Radiobutton(details, 
              text="mammal",
              padx = 20, 
              variable=Type, 
              value=0).grid(row=3, column=0)
tk.Radiobutton(details, 
              text="reptile",
              padx = 20, 
              variable=Type, 
              value=1).grid(row=3, column=1)
tk.Radiobutton(details, 
              text="flyer",
              padx = 20, 
              variable=Type, 
              value=2).grid(row=3, column=2)

tk.Radiobutton(details, 
              text="desert",
              padx = 20, 
              variable=habitat, 
              value=0).grid(row=4, column=0)
tk.Radiobutton(details, 
              text="tropical",
              padx = 20, 
              variable=habitat, 
              value=1).grid(row=4, column=1)
tk.Radiobutton(details, 
              text="cold",
              padx = 20, 
              variable=habitat, 
              value=2).grid(row=4, column=2)
tk.Radiobutton(details, 
              text="rainforests",
              padx = 20, 
              variable=habitat, 
              value=3).grid(row=4, column=3)
tk.Radiobutton(details, 
              text="ocean",
              padx = 20, 
              variable=habitat, 
              value=4).grid(row=4, column=4)
tk.Radiobutton(details, 
              text="pond, lakes, rivers",
              padx = 20, 
              variable=habitat, 
              value=5).grid(row=4, column=5)
tk.Radiobutton(details, 
              text="warmForests",
              padx = 20, 
              variable=habitat, 
              value=6).grid(row=4, column=6)

tk.Button(details, text='Quit', command=details.destroy).grid(row=5, column=0,  pady=4)
tk.Button(details, text='Show', command=show_entry_fields).grid(row=12, column=1,  pady=4)





details.mainloop()


