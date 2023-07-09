with open("input.txt", "r") as f:
	monkeys = []
	blocks = f.read().strip().split("\n\n")
	for block in blocks:
		lines = block.splitlines()
		monkey = []
		monkey.append(list(map(int, lines[1].strip().split(": ")[1].split(", "))))
		monkey.append(eval("lambda old:" + lines[2].split('=')[1]))
		for line in lines[3:]:
			monkey.append(int(line.split(' ')[-1]))
		monkeys.append(monkey)

# for monkey in monkeys:
# 	print(monkey)

s = [0 for _ in range(len(monkeys))]

# part 
for _ in range(20):
	for index, monkey in enumerate(monkeys):
		if len(monkey[0]) == 0:
			pass
		for item in monkey[0]:
			item = monkey[1](item)//3
			if item % monkey[2] == 0:
				monkeys[monkey[3]][0].append(item)
			else:
				monkeys[monkey[4]][0].append(item)
			# monkey[0].pop(0)
		s[index] += len(monkey[0])
		monkey[0] = []

# # part 2
# div = 1
# for monkey in monkeys:
# 	div *= monkey[2]

# for _ in range(10000):
# 	for index, monkey in enumerate(monkeys):
# 		for item in monkey[0]:
# 			item = monkey[1](item)
# 			item %= div
# 			if item % monkey[2] == 0:
# 				monkeys[monkey[3]][0].append(item)
# 			else:
# 				monkeys[monkey[4]][0].append(item)
# 		s[index] += len(monkey[0])
# 		monkey[0] = []

s = sorted(s, reverse=True) 
res = s[0] * s[1]

print(s)
print(res)
