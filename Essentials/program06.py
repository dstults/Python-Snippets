from dUtilities import *
from dataclasses import FrozenInstanceError, dataclass

# -------------------------------------------------------------
title("Basic Objects")
# -------------------------------------------------------------

class Person1:
	# Basic constructor
	def __init__(self, name, age, address):
		self.name = name
		self.age = age
		self.address = address
	# toString override
	def __str__(self):
		return "[ Person1: " + self.name + " / " + str(self.age) + " / " + self.address + " ]"

p1 = Person1("Bob", 35, "111 Happy Way")
p2 = Person1("Sally", 42, "221st W Overdrive")
p3 = Person1("Bob", 35, "111 Happy Way")
print("\nHave a look at the code, too much going on here to show.")
typeInfo("p1", p1)
typeInfo("p2", p2)
typeInfo("p3", p3)

print("\nSample equality check for regular objects.")
typeInfo("p1 == p2", p1 == p2)
typeInfo("p1 == p3", p1 == p3)

# -------------------------------------------------------------
title("Basic Objects (cont'd)")
# -------------------------------------------------------------

class Person2:
	# Basic constructor
	def __init__(self, name, age, address):
		self.name = name
		self.age = age
		self.address = address
	# toString override
	def __str__(self):
		return "[ Person2: " + self.name + " / " + str(self.age) + " / " + self.address + " ]"
	# equality override
	def __eq__(self, obj):
		if type(obj) != Person2:
			print("Didn't even pass the type check!")
			return False
		return self.name == obj.name and self.age == obj.age and self.address == obj.address

p4 = Person2("Bob", 35, "111 Happy Way")
p5 = Person1("Sally", 42, "221st W Overdrive")
p6 = Person2("Bob", 35, "111 Happy Way")
print("\nEquality check for the same data type:")
typeInfo("p4", p4)
typeInfo("p5", p5)
typeInfo("p6", p6)
typeInfo("p4 == p5", p4 == p5)
typeInfo("p4 == p6", p4 == p6)

print("\nEquality check against different data type:")
typeInfo("p4 == p1", p4 == p1)

print("\nChange class variables and see if they still match:")
p4.name = "Hank"
print('p4.name = "Hank"')
typeInfo("p4", p4)
typeInfo("p4 == p6", p4 == p6)

print("\nPut it back and compare again:")
p4.name = "Bob"
print('p4.name = "Bob"')
typeInfo("p4 == p6", p4 == p6)

# -------------------------------------------------------------
title("Dataclass Objects")
# -------------------------------------------------------------

@dataclass
class Person3:
	name: str
	age: int
	address: str
	# toString override
	def __str__(self):
		return "[ Person3: " + self.name + " / " + str(self.age) + " / " + self.address + " ]"

p7 = Person3("Bob", 35, "111 Happy Way")
p8 = Person3("Sally", 42, "221st W Overdrive")
p9 = Person3("Bob", 35, "111 Happy Way")
print("\nNext up is dataclasses, works like objects but equality automatically compares data")
print("Top of the file >>> from dataclasses import dataclass !!!!")
print("Top of the class >>> @dataclass !!!!")
print("\nEquality check for the same data type:")
typeInfo("p7", p7)
typeInfo("p8", p8)
typeInfo("p9", p9)
typeInfo("p7 == p8", p7 == p8)
typeInfo("p7 == p9", p7 == p9)

print("\nEquality check against different data types:")
typeInfo("p7 == p1", p7 == p1)
typeInfo("p7 == p4", p7 == p4)

print("\nCan I still change dataclass records?")
p7.name = "Hank"
print('p7.name = "Hank"')
typeInfo("p7", p7)
p8.age = 21
print('p8.age = 21')
typeInfo("p8", p8)

print("\nEquality check post-changes:")
typeInfo("p7 == p8", p7 == p8)
typeInfo("p7 == p9", p7 == p9)

print("\nAnd...put it back and compare:")
p7.name = "Bob"
print('p7.name = "Bob"')
typeInfo("p7 == p9", p7 == p9)

print("\nNote: by passing frozen=True to the dataclass() decorator you can emulate immutability")

@dataclass(frozen=True)
class Person4:
	name: str
	age: int
	address: str
	# toString override
	def __str__(self):
		return "[ Person3: " + self.name + " / " + str(self.age) + " / " + self.address + " ]"

p10 = Person4("Bob", 35, "111 Happy Way")
print("\nHere's a sample of a dataclass that's frozen:")
typeInfo("p10", p10)

print('\nWhen we attempt to modify it with \'p10.name = "Hank"\'...')
try:
	p10.name = "Hank"
except FrozenInstanceError: # Custom error!
	printError("dataclasses.FrozenInstanceError: cannot assign to field 'name'")
print("\nData is unchanged:")
typeInfo("p10", p10)

programEnd()
