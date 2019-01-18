# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:48:55 2019

@author: Aadhavan
"""

import tkinter as tk


def show_selections():
    print(())
    print(())



index = tk.Tk()




destination = tk.IntVar()
Class = tk.IntVar()
orgin = tk.IntVar()



tk.Label(index,text="FIRSTNAME").grid(row = 0)
tk.Label(index,text="LASTNAME").grid(row = 1, column =0)  
tk.Label(index,text="Orgin").grid(row = 2) 
tk.Label(index,text="Destination").grid(row = 3) 
tk.Label(index,text="CLASS").grid(row = 8, column=0) 



tk.Label(index, 
        text="""  """,
        justify = tk.LEFT,
        padx = 20).grid(row = 3, column = 3)



tk.Radiobutton(index, 
              text="NEW YORK",
              padx = 20, 
              variable=orgin, 
              value=1).grid(row=2, column=1)




tk.Radiobutton(index, 
              text="Boston",
              padx = 20, 
              variable=orgin, 
              value=2).grid(row=2, column=2)




tk.Radiobutton(index, 
              text="First",
              padx = 20, 
              variable=Class, 
              value=4).grid(row=8, column=1)



tk.Radiobutton(index, 
              text="Bussiness",
              padx = 20, 
              variable=Class, 
              value=5).grid(row=8, column=2)  
            



tk.Radiobutton(index, 
              text="economical",
              padx = 20, 
              variable=Class, 
              value=6).grid(row=8, column=3)




tk.Radiobutton(index, 
              text="Chennai",
              padx = 20, 
              variable=destination, 
              value=1).grid(row=3, column=1)



tk.Radiobutton(index, 
              text="Singapore",
              padx = 20, 
              variable=destination, 
              value=2).grid(row=3, column=2) 



tk.Radiobutton(index, 
              text="Kolkatta",
              padx = 20, 
              variable=destination, 
              value=3).grid(row=3, column=3)             



senior = tk.IntVar()
#checkbutton for Above25
tk.Checkbutton(index, text="Senior", 
               variable=senior).grid(row=5, sticky=tk.W)

#variable for Senior
vegetarianFood = tk.IntVar()
#checkbutton for Senior
tk.Checkbutton(index, text="Vegetarian Food",
               variable=vegetarianFood).grid(row=7, sticky=tk.W)


nameEntry = tk.Entry(index)
originEntry = tk.Entry(index)
destinationEntry = tk.Entry(index)




nameEntry.grid(row=0, column=1)
originEntry.grid(row=1, column=1)
destinationEntry.grid(row=1, column=1)



tk.Button(index, text='Show', command=show_selections).grid(row=10, sticky=tk.W)
tk.Button(index, text='Quit', command=index.destroy).grid(row=10, column=3,  pady=4)
index.mainloop()
index.mainloop()
