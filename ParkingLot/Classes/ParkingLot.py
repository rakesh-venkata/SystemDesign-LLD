from Classes.Entry import Entry
from Classes.Exit import Exit
from Classes.Floor import Floor

class ParkingLot:
    def __init__(self, ID):
        self.floors = []
        self.entry = []
        self.exit = []
        self.id = ID
    
    def addFloor(self,totalSlots,truckSlots,bikeSlots):
        newFloor = Floor(len(self.floors)+1, totalSlots, truckSlots, bikeSlots)
        self.floors.append(newFloor)
        print('Floor '+str(len(self.floors))+' is added')

    def addSlot(self, floorNumber):
        self.floors[floorNumber-1].slots.append(0)
        print('New slot is added')

    def addEntry(self):
        newEntry = Entry()
        self.entry.append(newEntry)

    def addExit(self):
        self.exit.append(Exit())

    def parkVehicle(self,vehicle):
        return self.entry[0].generateTicket(vehicle, self.floors, self.id)

    def unParkVehicle(self, ticketId):
        self.exit[0].unPark(ticketId, self.floors)

