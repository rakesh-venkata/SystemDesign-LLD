from zope.interface import Interface

class IEntry(Interface):
    def generateTicket(vehicle,floors):
        pass
