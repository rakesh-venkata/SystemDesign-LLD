from zope.interface import implementer
from Interfaces.Entry import IEntry
from datetime import datetime

@implementer(IEntry)
class Entry():
    def generateTicket(self,vehicle,floors, ParkingLotId):
        vehicleType = vehicle.type
        slot = -1
        floor = -1
        if vehicleType=='Truck':
            for f in range(len(floors)):
                for s in range(floors[f].truckSlots):
                  if floors[f].slots[s] == 0:
                     slot = s+1
                     floor = f+1
                     break
                if slot!=-1:
                    break
        elif vehicleType == 'Bike':
            for f in range(len(floors)):
                for s in range(floors[f].truckSlots, floors[f].truckSlots + floors[f].bikeSlots):
                   if floors[f].slots[s] == 0:
                       slot = s+1
                       floor = f+1
                       break
                if slot!=-1:break
        else:
            for f in range(len(floors)):
                for s in range(floors[f].truckSlots + floors[f].bikeSlots, floors[f].totalSlots):
                   if floors[f].slots[s] == 0:
                       slot = s+1
                       floor = f+1
                       break
                if slot!=-1:break
        if slot == -1 or floor == -1:return 'No Slots'
        floors[floor-1].slots[slot-1] = 1
        return ParkingLotId+'_'+str(floor)+'_'+str(slot)

                

        
        
