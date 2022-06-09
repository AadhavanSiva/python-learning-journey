import VehicleClass as Vehicle

vehicle2= Vehicle.Car(5,100,4)
vehicle1= Vehicle.Aeroplane(60,63500 ,5)
vehicle1.printAeroplane()
vehicle2.printCar()

if (vehicle1.canFly()):
    print("vehicle1 can fly")
else:
    print("vehicle1 cant fly")


if (vehicle2.canFly()):
    print("vehicle2 can fly")
else:
    print("vehicle2 cant fly")
