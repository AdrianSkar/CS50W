"""
Refs:
 https://cs50.harvard.edu/web/2020/notes/2/
 https://www.w3schools.com/python/python_classes.asp
"""


class Flight():
	# __init__ is the 'constructor' and its called every time the class is used
	# to create a new object
	def __init__(self, capacity):
		# `self` ≈ `this` in JS
		self.capacity = capacity
		self.passengers = []

	def open_seats(self):
		return self.capacity - len(self.passengers)

	def add_passenger(self, name):
		if not self.open_seats():
			return False
		self.passengers.append(name)
		return True
	test = 2


flight = Flight(3)
print(flight.capacity)

people = ['Dan', 'Harry', 'Kira', 'Jena']

for person in people:
	print(flight.open_seats())
	if flight.add_passenger(person):
		print(f"{person} has a seat on the flight.")
	else:
		print(f"No seats left, {person} is out.")

print(flight.test)
flight.test = 32
print(flight.test)
# Deletes the reference in the current context
del flight.test
print(flight.test)

print(Flight.test)
# Deletes the property
del Flight.test
# print(Flight.test) # Err: Flight has no attribute test
