class Vehicle:
    def __init__(self, seatCount, maxFuel):
        self.seatCount = seatCount
        self.maxFuel = maxFuel

    def canFly(self):
        return False

class Car(Vehicle):
    def __init__(self,  seatCount, maxFuel, tires):
        super().__init__( seatCount, maxFuel)
        self.tires = tires

    def printCar(self):
        print("This car has ",self.seatCount, " seats, it's max fuel is", self.maxFuel,"gallons and has", self.tires,"tires")


class Aeroplane (Vehicle):
    def __init__(self, seatCount, maxFuel, wings):
        super().__init__( seatCount, maxFuel)
        self.wings = wings

    def canFly(self):
        return True

    def printAeroplane(self):
        print("This aeroplane has ",self.seatCount, " seats, it's max fuel is", self.maxFuel,"gallons and has", self.wings,"wings")

# vehicle1= Aeroplane(60,63500 ,5)
# vehicle2= Car(5,100,4)
# vehicle1.printAeroplane()
# vehicle2.printCar()
#
# if (vehicle1.canFly()):
#     print("vehicle1 can fly")
# else:
#     print("vehicle1 cant fly")
#
#
# if (vehicle2.canFly()):
#     print("vehicle2 can fly")
# else:
#     print("vehicle2 cant fly")






