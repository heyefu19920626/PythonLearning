# Assagn a value to a list
messages = [value for value in range(1, 10)]
print(messages)

# print list
for value in messages:
    if value < 3:
        print("lesser than 3")
    elif value < 5:
        print("lesser than 5 and greater than 2")
    else:
        print("others")

messages.sort(reverse=True)
print(messages)
messages.reverse()
print(messages)

# slice up
print(messages[:5])
print(messages[-5:])

# copy list
messages_copy = messages[:]
messages.append(10)
messages_copy.append(11)
print(messages)
print(messages_copy)

# tuple
messages = (1, 3, 4)
print(messages)


# dictionries
dictionries = {
	"x_point": 5,
	"z_point": 7,
	}
print(dictionries)

# add dictionries proterty
dictionries["y_point"] = 6
print(dictionries)

# delete dictionaries properties
del(dictionries["z_point"])
print(dictionries)

# visit dictionries property
print("This dictionry x_point is " + str(dictionries["x_point"]) + ".")

# traverse dictionaries by key-value
for key,value in dictionries.items():
	print("\n" + key)
	print(value)

# traverse dicrionaries by key
# 1
for key in dictionries:
	print("\n" + key)
# 2
for key in dictionries.keys():
	print("\n" + str(dictionries[key]))

# traversal
for key in sorted(dictionries.keys()):
	print(key)
for value in sorted(dictionries.values()):
	print(value)

# set is similar to list,but each element must be unique
dictionries["x"] = 5
print(dictionries)
for value in set(dictionries.values()):
	print(value)

# nest
dictionries_1 = {
	'm': 'Python',
	'n': 'Java',
	'o': 'JavaScript',
	}
nestList = [dictionries,dictionries_1]
print(nestList)

# nested loop
aliens = []
for alien in range(10):
	alien_new = {'color':'green','point':5,'speed':'low'}
	aliens.append(alien_new)
print("Total number if aliens:" + str(len(aliens)))
print(aliens[:5])
