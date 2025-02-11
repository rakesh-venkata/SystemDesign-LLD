class ParkingLot:
    #Types of vehicles
    #no of floors
    # slots per floor
    slots = {}
    def __init__(self,vehicleTypes, noOfFloors, slotsPerFloor):
        self.vehicleTypes = vehicleTypes
        self.noOfFloors = noOfFloors
        self.slotsPerFloor = slotsPerFloor
        for each in self.vehicleTypes:
            self.slots[each] = ['' for i in range(self.noOfFloors*self.slotsPerFloor)]


    def parkVehicle(self,vehicle):
        for slot in range(len(self.slots[vehicle.type])):
            if self.slots[vehicle.type][slot] == '':
                self.slots[vehicle.type][slot] = vehicle.number
                print('Vehicle number:' +  vehicle.number + 'is parked in slot number :'+ str(slot+1))
                break
        else:
            print('No parking slots left for this vehicle type')
    
    def unParkVehicle(self,vehicle):
          for slot in range(len(self.slots[vehicle.type])):
             if self.slots[vehicle.type][slot] == vehicle.number:
                self.slots[vehicle.type][slot] = ''
                print('Vehicle number:' +  vehicle.number + 'is un parked from slot number :'+ str(slot+1))
                break
          else:
            print('This vehicle is not in our parking area')

