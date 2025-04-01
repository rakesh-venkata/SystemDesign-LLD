from zope.interface import implementer
from Interfaces.Exit import IExit
import time
from datetime import datetime

@implementer(IExit)
class Exit():
    def unPark(self,ticketId, floors):
        _,floorNo,slotNo = ticketId.split('_')
        for floor in floors:
            if floor.number == int(floorNo):
                floor.slots[int(slotNo)-1] = 0
                print(floorNo+'with'+slotNo+'is un parked ')
        
        