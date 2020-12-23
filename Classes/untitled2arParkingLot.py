# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 18:45:13 2020

@author: Aadhavan
"""


class CarParkingLot:
  def __init__(self,Occupied, length, width):
    self.Occupied = Occupied
    self.length = length
    self.width = width

  def print(self):
    print("The parkingLot is " + self.Occupied)
    print("The parkingLot is " + self.length + "long")
    print("The parkingLot is " + self.width + " wide")
    
  def Occupy(self):
      self.Occupied = "occupied"
  
  def Free(self):
      self.Occupied = "free"

p1 = CarParkingLot("free", "36 ","7" )
p1.print()
p1.Occupy()
p1.print()
p1.Free()
p1.print()