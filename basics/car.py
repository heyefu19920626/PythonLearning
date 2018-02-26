""" 一个可用于表示汽车的类"""

import battery

# set default values for properties
class Car():
	# each method must contain the parameter self 
	def __init__(self, make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def read_odometer(self):
		print('This car has ' + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		self.odometer_reading += mileage

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name

	def fill_gas_tank(self):
		print('The car has a gas tank!')


# inherit class
class Electriccar(Car):
	# invokes the parent class method initialization
	def __init__(self, make, model, year):
		super().__init__(make, model,year)
		# defined properties for subclasses
		self.battery = battery.Battery()

	# override the parent class method
	def fill_gas_tank(self):
		print('This car does not need a gas tank!')