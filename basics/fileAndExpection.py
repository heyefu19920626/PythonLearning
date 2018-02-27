
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
with open('write_path','a') as file:
	file.write(ts)
