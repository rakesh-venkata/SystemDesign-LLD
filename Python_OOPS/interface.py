from zope.interface import Interface,implementer
	
	
class MyInterface(Interface): 
	def method1(self, x): 
		pass
	def method2(self): 
		pass
	
@implementer(MyInterface) 
class MyClass: 
	def method1(self, x): 
		return x**2
	def method2(self): 
		return "foo"

obj1 = MyClass() 

print(obj1.method1(5)) 
print(obj1.method2())


