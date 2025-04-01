from Interfaces.Floor import IFloor
from zope.interface import implementer

@implementer(IFloor)
class Floor():
    def __init__(self, number, totalSlots, truckSlots,bikeSlots):
        self.totalSlots = totalSlots
        self.truckSlots = truckSlots
        self.bikeSlots = bikeSlots
        self.number = number
        self.slots = [0]*totalSlots

    def showEmptySlots(self, vehicleType):
      
        if vehicleType == 'Truck':
            if self.slots[0] == 0:
                print('Avaialble slots numbers are 1')
            else:
                print('No Slots avaiable for'+vehicleType+'in floor number'+str(self.number))
        elif vehicleType == 'Bike':
            available = []
            for s in range(1,3):
                if self.slots[s] == 0:
                    available.append(s+1)
            if available:
                print('Available slot numbers are ')
                for s in available:
                    print(s)
            else:
                print('No Slots avaiable for'+vehicleType+'in floor number'+str(self.number))
        else:
            available = []
            for s in range(3,self.totalSlots):
                if self.slots[s] == 0:
                    available.append(s+1)
            if available:
                print('Available slot numbers are ')
                for s in available:
                    print(s)
            else:
                print('No Slots avaiable for'+vehicleType+'in floor number'+str(self.number))

    def ShowOccupiedSlots(self, vehicleType):
        if vehicleType == 'Truck':
            if self.slots[0] == 1:
                print('Occupied slots numbers are 1')
            else:
                print('No Slots occupied by '+vehicleType+'in floor number'+str(self.number))
        elif vehicleType == 'Bike':
            occupied = []
            for s in range(1,3):
                if self.slots[s] == 1:
                    occupied.append(s+1)
            if occupied:
                print('Occupied slot numbers are ')
                for s in occupied:
                    print(s)
            else:
                print('No Slots occupied by'+vehicleType+'in floor number'+str(self.number))
        else:
            occupied = []
            for s in range(3,self.totalSlots):
                if self.slots[s] == 1:
                    occupied.append(s+1)
            if occupied:
                print('Occupied slot numbers are ')
                for s in occupied:
                    print(s)
            else:
                print('No Slots occupied by'+vehicleType+'in floor number'+str(self.number))

    def ShowEmptySlots(self):
        availableSlots = {}
        truckSlots = []
        for s in range(self.truckSlots):
            if self.slots[s] == 0:
                truckSlots.append(s+1)
        availableSlots['Truck'] = truckSlots
        bikeSlots = []
        for s in range(self.truckSlots,self.truckSlots+self.bikeSlots):
            if self.slots[s]==0:
                bikeSlots.append(s+1)
        availableSlots['Bike'] = bikeSlots
        carSlots = []
        for s in range(self.truckSlots+self.bikeSlots,self.totalSlots):
            if self.slots[s]==0:
                carSlots.append(s+1)
        availableSlots['Car'] = carSlots
        print('Available slots are', availableSlots)
        

            
       

    
    