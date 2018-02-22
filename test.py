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
dictionries = {"x_point":5}
print(dictionries)

# add dictionries proterty
dictionries["y_point"] = 6
print(dictionries)

#visit dictionries property
print("This dictionry x_point is " + str(dictionries["x_point"]) + ".")
