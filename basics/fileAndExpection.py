
import json


file_path = 'test.txt'

# read the entire file
with open('test.txt',encoding='utf8') as file:
	content = file.read()
	print(content)

# read the file by line
with open(file_path,encoding='utf8') as file:
	for lines in file:
		print(lines.rstrip())

print(lines)

# read the file by line and save in list
with open(file_path,encoding='utf8') as file:
	# readline() readlines()
	lines = file.readlines()

print(lines)

ts = ''
for line in lines:
	ts += line.strip()
print(ts)

write_path = 'write.text'

# wirtten to the file
# w write append
with open('write_path','a') as file:
	file.write(ts)

# try expect
try:
	print(5/0)
except Exception:
	print('You can not divide by zero.')

# try expect pass else
print('Give me two numbers,and i will divide them.\nEnter "q" to quit.')
while True:
	first_number = input('\nFirst number')
	if first_number == 'q':
		break
	secone_number = input('\nSecond number')
	try:
		answer = int(first_number)/int(secone_number)
	except Exception:
		pass
	else:
		print(answer)



# save data use json.dump()
numbers = [1,2,3,4,5,6,7,8,9,0]
with open('numbers.json','w') as file:
	json.dump(numbers,file)

# load data use json.load()
with open('numbers.json') as file:
	numbers_new  = json.load(file)
print(numbers_new)