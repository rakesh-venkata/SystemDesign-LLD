from Classes.Vehicle import Vehicle
from Classes.ParkingLot import ParkingLot
import time

Parking = ParkingLot('PARK01')
Parking.addFloor(10,1,2)
Parking.addFloor(12,1,2)
Parking.addEntry()
Parking.addExit()

vehicle1 = Vehicle('Truck', 'Truck001', 'Orange')
vehicle2 = Vehicle('Truck', 'Truck002', 'Orange')
vehicle3 = Vehicle('Truck', 'Truck003', 'Orange')
vehicle4 = Vehicle('Bike', 'Bike001', 'Black')
vehicle5 = Vehicle('Bike', 'Bike002', 'Black')
vehicle6 = Vehicle('Bike', 'Bike003', 'Black')

ticketId1 = Parking.parkVehicle(vehicle1)
print(Parking.parkVehicle(vehicle2))
print(Parking.parkVehicle(vehicle3))

print(Parking.parkVehicle(vehicle4))
print(Parking.parkVehicle(vehicle5))
print(Parking.parkVehicle(vehicle6))

for floor in Parking.floors:
    print('floor slots are')
    print(floor.slots)

print(Parking.unParkVehicle(ticketId1))

for floor in Parking.floors:
    print('floor slots are')
    print(floor.slots)
print(Parking.parkVehicle(vehicle3))



for floor in Parking.floors:
    print('floor slots are')
    print(floor.slots)

