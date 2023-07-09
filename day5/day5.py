l1 = ["S", "L", "F", "Z", "D", "B", "R", "H"]
l2 = ["R", "Z", "M", "B", "T"]
l3 = ["S", "N", "H", "C", "L", "Z"]
l4 = ["J", "F", "C", "S"]
l5 = ["B", "Z", "R", "W", "H", "G", "P"]
l6 = ["T", "M", "N", "D", "G", "Z", "J", "V"]
l7 = ["Q", "P", "S", "F", "W", "N", "L", "G"]
l8 = ["R", "Z", "M"]
l9 = ["T", "R", "V", "G", "L", "C", "M"]

lst = [l1, l2, l3, l4, l5, l6, l7, l8, l9]

def	move(line, lst):
	match line[1]:
		case 1:
			item1 = lst[0]
		case 2:
			item1 = lst[1]
		case 3:
			item1 = lst[2]
		case 4:
			item1 = lst[3]
		case 5:
			item1 = lst[4]
		case 6:
			item1 = lst[5]
		case 7:
			item1 = lst[6]
		case 8:
			item1 = lst[7]
		case 9:
			item1 = lst[8]

	match line[2]:
		case 1:
			item2 = lst[0]
		case 2:
			item2 = lst[1]
		case 3:
			item2 = lst[2]
		case 4:
			item2 = lst[3]
		case 5:
			item2 = lst[4]
		case 6:
			item2 = lst[5]
		case 7:
			item2 = lst[6]
		case 8:
			item2 = lst[7]
		case 9:
			item2 = lst[8]

	number = line[0]
	nb = 0

	#for part 1s
	while nb < number:
		crate = item1[0]
		item2.insert(0, crate)
		item1.pop(0)
		nb += 1
	
	# #for part 2
	# while nb < number:
	# 	popped = number - 1 - nb
	# 	crate = item1[popped]
	# 	item2.insert(0, crate)
	# 	item1.pop(popped)
	# 	nb += 1

def print_out(lst):
	output = ""
	for pos in lst[:]:
		output += str(pos[0])
		# print(pos[0])

	print(f"\n{output}\n")

with open("input.txt", "r") as f:
	lines = f.readlines()[10:]
	for line in lines:
		line = line.strip('\n')
		line = line.split(" ")
		line.pop(0)
		line.pop(1)
		line.pop(2)
		for pos, item in enumerate(line):
			line[pos] = int(item)
		move(line, lst)
	print_out(lst)
