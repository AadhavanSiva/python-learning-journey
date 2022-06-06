# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 18:39:48 2020

@author: Aadhavan
"""

import random
rnumber = random.randint(0,5)
movies =[ "harry potter", "Zootopia", "ratatouille", "Nemo", "Moana", "Ice Age"]
print("Using randint, you will watch",movies[rnumber])


print("Using choice, you will watch",random.choice(movies))

desserts = ["ice cream", "cake","pancake","brownies","candy"]

random.shuffle(desserts)
print(desserts)

