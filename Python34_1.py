Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> foo = 'abc'
>>> for c in foo:
	print c
	
SyntaxError: Missing parentheses in call to 'print'
>>> foo = 'abc'
>>> for c in foo:
	print(c)

	
a
b
c
>>> foo = 'abd'
>>> for i in range(len(foo)):
	print(foo[i],'(%d)'%i)

	
a (0)
b (1)
d (2)
>>> foo = 'abc'
>>> for i,ch in enumerate(foo):
	print(ch,'(%d)'%i)

	
a (0)
b (1)
c (2)
>>> def addMe2Me(x):
	return (x+x)

>>> addMe2Me(4.25)
8.5
>>> addMe2Me('Python')
'PythonPython'
>>> class FooClass(object):
"""my very first class: FooClass"""
version = 0.1 # class (data) attribute
def __init__(self, nm='John Doe'):
"""constructor"""
self.name = nm # class instance (data) attribute
print 'Created a class instance for', nm
def showname(self):
"""display instance attribute and class name"""
print 'Your name is', self.name
print 'My name is', self.__class__.__name__
def showver(self):
"""display class(static) attribute"""
print self.version # references FooClass.version
def addMe2Me(self, x): # does not use 'self'
"""apply + operation to argument"""
return x + x
SyntaxError: expected an indented block
>>> class FooClass(object):
	varsion = 0.1

	
>>> foo1 = FooClass()
>>> 
>>> 
>>> class FooClass(object):
	varsion = 0.1
	def _init_(self,nm='Joe'):
		self.name = nm
		print('Created a class instance for',nm)
		def showname(self):
			print('Your name is ',self.name)
			print('My name is',self._class_._name_)

			
>>> foo1 = FooClass()
>>> 
>>> 
>>> class FooClass(object):
	varsion = 0.1
	def _init_(self,nm='Joe'):
		self.name = nm
		print('Created a class instance for',nm)

		
>>> foo1 = FooClass();
>>> class FooClass(object):
	varsion = 0.1
	def _init_(self,nm='Joe'):
		self.name = nm
		print('Created a class instance for')

		
>>> foo1 = FooClass()
>>> 
>>> class FooClass(object):
version = 0.1 
def __init__(self, nm='John Doe'):
self.name = nm 
print 'Created a class instance for', nm
def showname(self):
print 'Your name is', self.name
print 'My name is', self.__class__.__name__
def showver(self):
print self.version
def addMe2Me(self, x):
return x + x
SyntaxError: expected an indented block
>>> class FooClass(object):
	version = 0.1 
	def __init__(self, nm='John Doe'):
		self.name = nm 
		print 'Created a class instance for', nm
	def showname(self):
		print 'Your name is', self.name
		print 'My name is', self.__class__.__name__
	def showver(self):
		print self.version
	def addMe2Me(self, x):
		return x + x
	
SyntaxError: Missing parentheses in call to 'print'
>>> class FooClass(object):
	version = 0.1 
	def __init__(self, nm='John Doe'):
		self.name = nm 
		print ('Created a class instance for', nm)
	def showname(self):
		print ('Your name is', self.name)
		print ('My name is', self.__class__.__name__)
	def showver(self):
		print (self.version)
	def addMe2Me(self, x):
		return x + x

	
>>> foo1=FooClass()
Created a class instance for John Doe
>>> foo1.showname()
Your name is John Doe
My name is FooClass
>>> foo1.showver
<bound method FooClass.showver of <__main__.FooClass object at 0x035AAC70>>
>>> foo1.showver()
0.1
>>> foo1.add
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    foo1.add
AttributeError: 'FooClass' object has no attribute 'add'
>>> foo1.addMe2Me(5)
10
>>> class FooClass(object):
	version = 0.1 
	def __init__(self, nm='John Doe'):
		self.name = nm 
		print ('Created a class instance for', nm)
	def showname(self):
		print ('Your name is', self.name)
		print ('My name is', self.__class__.__name__)
	def showver(self):
		print (self.version)
	def addMe2Me(self, x):
		return x + x

>>> import sys
>>> sys.stdout.write('hello world!\n')
hello world!
13
>>> sys.platform
'win32'
>>> sys.version
'3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)]'
>>>
