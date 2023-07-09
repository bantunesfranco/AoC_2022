
lst = []

with open("input.txt", "r") as f:
	line = f.read().strip()

i = 0
while True:
	# print(line[i])
	data = line[i:(i+4)]
	if len(set(list(data))) == 4:
		print(i + 4)
		break
	i += 1

i = 0
while True:
	# print(line[i])
	data = line[i:(i+14)]
	if len(set(list(data))) == 14:
		print(i + 14)
		break
	i += 1