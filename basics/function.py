


# formal parameter and actual parameter
# keyword actual parameter
# default argument must follows non-default argument
def describe_pet(pet_name, animal_type='dog'):
	print('\nYour have a ' + animal_type  +".\nIt name is " + pet_name +".")

describe_pet(pet_name = 'Tom', animal_type = 'dog')
describe_pet('dog', 'Bob')
describe_pet('Smith')

# pass any number of arguments
# * will convert to tuple
def make_pizza(size, *toppings):
	print('\nMake a ' + str(size) + '-inch pizza with the following toppings:')
	for topping in toppings:
		print('- ' + topping)

make_pizza(15, 'pepperoni')
make_pizza(15, 'pepperoni', 'mushrooms')

# ** will convert to dictionaries
def build_profile(first, last, **user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('albert', 'enistein', loction='prinction', field='physics')
print('**')
print(user_profile)
