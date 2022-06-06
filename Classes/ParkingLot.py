# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 18:45:13 2020

@author: Aadhavan
"""
Lot = 0

class CarParkingLot:
  def __init__(self, lot_id, Occupied, length, width):
    self.Occupied = Occupied
    self.length = length
    self.width = width
    self.lot_id = lot_id

  def print(self):
    print("The lot_id is ", self.lot_id)
    print("The parkingLot is " + self.Occupied)
    print("The parkingLot is " + self.length + " length")
    print("The parkingLot is " + self.width + " wide")
    
  def Occupy(self):
      self.Occupied = "occupied"
  
  def Free(self):
      self.Occupied = "free"
      
class ParkingLotManager:
    lot_list = []
    
    def Add(self,Lot):
        self.lot_list.append(Lot)
        pass;
    
    def Remove(self,Lot_id):
        index = 0
        while len(self.lot_list)-1 >= index:
            print("r")
            p = self.lot_list[index]
            print("p.lot_id",p.lot_id)
            print("Lot_id",Lot_id)
            if (p.lot_id == Lot_id):
                print("r2")
                self.lot_list.remove(p)
                return
            index += 1
        pass;
    
    def Print(self):
        for p in self.lot_list:
            p.print()
        pass;


p1 = CarParkingLot(101,"free", "36 ","7" )

p2 = CarParkingLot(102, "free", "54 ","9" )
#p1.print()
#p2.print()

manager =ParkingLotManager()
manager.Add(p1)
manager.Add(p2)
manager.Print()

manager.Remove(101)
print("After remove")
manager.Print()

#p1.print()
#p1.Occupy()
#p1.print()
#p1.Free()
#p1.print()