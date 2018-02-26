
from car import Car,Electriccar

# define class
class Dog():
	"""一次模拟小狗的简单尝试"""

	def __init__(self, name, age):
		"""初始化属性name和age"""
		self.name = name
		self.age = age

	def sit(self):
		"""simulate when the dog was ordered to squat"""
		print(self.name.title() + ' is now sitting')

# super().__init__()
class Newdog(Dog):
	def __init__(self, name, age):
		super().__init__(name, age)

# use calss
my_dog = Dog('willie',6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years.")

my_dog.sit()

my_car = Car('China', 'A4', '2018')
my_car.read_odometer()
my_car.update_odometer(190)
my_car.read_odometer()

my_tesla = Electriccar('tesla', 'modex s',2018)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()

newdog = Newdog('111',5)