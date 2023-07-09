
def	rps(line):
	result = 0
	match line:
		case "AX":
			result = 1 + 3
		case "AY":
			result = 2 + 6
		case "AZ":
			result = 3 + 0
		case "BX":
			result = 1 + 0
		case "BY":
			result = 2 + 3
		case "BZ":
			result = 3 + 6
		case "CX":
			result = 1 + 6
		case "CY":
			result = 2 + 0
		case "CZ":
			result = 3 + 3
	return result

def	rps2(line):
	result2 = 0
	match line:
		case "AX":
			result2 = 3 + 0
		case "AY":
			result2 = 1 + 3
		case "AZ":
			result2 = 2 + 6
		case "BX":
			result2 = 1 + 0
		case "BY":
			result2 = 2 + 3
		case "BZ":
			result2 = 3 + 6
		case "CX":
			result2 = 2 + 0
		case "CY":
			result2 = 3 + 3
		case "CZ":
			result2 = 1 + 6
	return result2

with open("input.txt", 'r') as f:
	total = 0
	total2 = 0
	lines = f.readlines()
	for line in lines:
		line = line.strip('\n')
		line = line.replace(' ', '')
		# print(line)
		total += rps(line)
		total2 += rps2(line)

print(total)
print(total2)