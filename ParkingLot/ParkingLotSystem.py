from Vehicle import Vehicle
from ParkingLot import ParkingLot

vehicle1 = Vehicle('Car', 'ABCDEF')
vehicle2 = Vehicle('Car', 'DEFGRH')
vehicle3 = Vehicle('Car', 'QWERTY')
vehicle4 = Vehicle('Car', 'ABCDEj')
vehicle5 = Vehicle('Car', 'DEFGRe')
vehicle6 = Vehicle('Car', 'QWERTp')

parkingSystem = ParkingLot(['Car'],1,4)
parkingSystem.parkVehicle(vehicle1)
parkingSystem.parkVehicle(vehicle4)
parkingSystem.parkVehicle(vehicle3)
parkingSystem.parkVehicle(vehicle2)
parkingSystem.parkVehicle(vehicle6)
parkingSystem.unParkVehicle(vehicle1)
parkingSystem.parkVehicle(vehicle6)
print(parkingSystem.slots)
