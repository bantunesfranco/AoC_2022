with open("input.txt", "r") as f:
	lines = f.readlines()

cycles = 0
x = 1
total = []
grid = [list(' ' for _ in range(40)) for _ in range(6)]

def check(cycles, x, total):

	target = [20,60,100,140,180,220]
	power = 0
	if cycles in target:
		power = x * cycles
		total.append(power)
		print(f"cycles: {cycles} and x: {x} and power: {power}")

def draw(x):
	for r in range(6):
		for c in range(40):
			if x == c or (x - 1) == c or (x + 1) == c:
				grid[r][c] = '#'

for line in lines:
	line = line.strip('\n')
	line = line.split(" ")

	# print(line)
	if line[0] == "noop":
		cycles += 1
		check(cycles, x, total)
		draw(x)
	elif line[0] == "addx":
		cycles += 1
		check(cycles, x, total)
		draw(x)
		cycles += 1
		check(cycles, x, total)
		draw(x)
		x += int(line[1])
	# print(f"cycles: {cycles} and x: {x}")

res = sum(total)
print(f"total is {res}\n")

for list in grid:
	str = ""
	for pos in list:
		str += str.join(pos)
	print(str)


# with open("input.txt") as fin:
#     lines = fin.read().strip().split("\n")

# cur_X = 1
# op = 0
# ans = 0

# row = 0
# col = 0

# X = [1] * 241

# for line in lines:
#     parts = line.split(" ")

#     if parts[0] == "noop":
#         op += 1
#         X[op] = cur_X

#     elif parts[0] == "addx":
#         V = int(parts[1])

#         X[op + 1] = cur_X
#         cur_X += V

#         op += 2
#         X[op] = cur_X


# # Ranges from [1, 39]
# ans = [[None] * 40 for _ in range(6)]

# for row in range(6):
#     for col in range(40):
#         counter = row * 40 + col + 1
#         if abs(X[counter - 1] - (col)) <= 1:
#             ans[row][col] = "##"
#         else:
#             ans[row][col] = "  "


# for row in ans:
#     print("".join(row))