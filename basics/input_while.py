

# input function recives input as a string
age = input('How old are you? ')
print('You age is ' + age)
age = int(age)
if age > 25:
	print('You are over 25 years old.')
else:
	print('You are under 25.')

# modulo %
if age % 2 == 0:
	print('Your age is even.')
else:
	print('Your age is odd.')

# while loop and smybol
prompt = '\nTell me something,and I will repeat it back to you:'
prompt += '\nEnter "quit" to end the program.\n'
active = True
while active:
	message = input(prompt)
	if message != 'quit':
		print(message)
		# break
	else:
		active = False

# continue and break
active = 0
while active < 15:
	active += 1
	if active % 2 == 0:
		continue
	elif active > 10:
		break
	print(active)
	
# while loop operate list
unconfirmed_users = ['tom','alice','brian']
confirmed_users = []
print(confirmed_users)
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print('Verifying user:' + current_user.title())
	confirmed_users.append(current_user)
	print(unconfirmed_users)
print(confirmed_users)