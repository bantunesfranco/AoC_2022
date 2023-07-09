import string

lists = []
lists2 = []

with open("input.txt", 'r') as f:
	lines = f.readlines()
	for line in lines:
		list = []
		line = line.strip('\n')
		lists2.append(line)
		list.append(line[:len(line)//2])
		list.append( line[int(len(line))//2:])
		lists.append(list)

keys = dict(zip(string.ascii_letters, (i for i in range(1,53))))

total = 0
for list in lists:
	keylist = []
	min_val = 54
	for	key, value in keys.items():
		if key in list[0] and key in list[1]:
			if value < min_val:
				keylist.append(key)
				min_val = value
	print(f"{list} {keylist} {min_val}")
	total += min_val

print(f"\nTotal of part 1 is {total}\n\n")


total = 0
i = 0
j = 0

while i < len(lists2):
	keylist = []
	list = []
	j = 0
	min_val = 54
	while j < 3:
		list.append(lists2[i + j])
		j += 1
	for	key, value in keys.items():
		if (key in list[0] and key in list[1]) and key in list[2]:
			if value < min_val:
				keylist.append(key)
				min_val = value
	print(f"{list} {keylist} {min_val}")
	total += min_val
	i += j

print(f"\nTotal of part 2 is {total}\n")