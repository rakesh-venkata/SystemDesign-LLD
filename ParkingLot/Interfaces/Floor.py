from zope.interface import Interface

class IFloor(Interface):
  def showEmptySlots(self, vehicleType, floorNumber):
     pass
  
  def showEmptySlots(self,floorNumber):
     pass
  
  def showOccupiedSlots(self, vehicleType, floorNumber):
     pass


