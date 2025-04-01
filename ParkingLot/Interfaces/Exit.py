from zope.interface import Interface

class IExit(Interface):
    def unPark(self, ticketId, floor):
        pass