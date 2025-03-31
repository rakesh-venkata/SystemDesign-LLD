class Item:
    count = 0  # class attributes
    def __init__(self, name : str, price : float, quantity : int): # Add types for readability
        self.__name = name # object speciifc attributes #It is private attribute # provides Encapsulation
        self.price = price
        self.quantity = quantity
        Item.count+=1

    def calculateTotalPrice(self, price, quantity):
        return price*quantity
    
    @classmethod    # decarators used to convert to class function 
    def increaseCount(cls):   # can access via class and takes first argument as class
        Item.count += 5

    @staticmethod
    def decreaseCount(): # can access via class/object.It doesn't take any object or class parameter
        Item.count -= 5

    @property
    def name(self):   # getter method
        return self.__name
    
    @name.setter
    def name(self, value):  # setter method
        self.__name = value
    
class Phone(Item):
    def __init__(self, name, price, quantity, brokenPhones = 0):
        super().__init__(name,price, quantity)  # call parent constructor to initilize parent attributes
        self.brokenPhones = brokenPhones

    def getBrokenPhones(self):
        return self.brokenPhones

item1 = Item('Phone', 30000, 4)
print(item1.name) # calling getter
item1.name = 'Laptop' # Setting attribute
print(item1.name)
print(item1.calculateTotalPrice(item1.price,item1.quantity))
item2 = Item('Phone', 30000, 5)
print(Item.increaseCount())
print(Item.decreaseCount())
print(item1.decreaseCount())
print(Item.count)
phone1 = Phone('Iphone', 100000, 4,2)
print('Broken Phones count is '+ str(phone1.getBrokenPhones()))
print(phone1.calculateTotalPrice(phone1.price,phone1.quantity))
print(Item.calculateTotalPrice(30, 2)) # throws error beacause it is object function and takes first argument as object