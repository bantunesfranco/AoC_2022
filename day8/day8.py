with open("input.txt", "r") as f:
	lines = f.read().splitlines()

grid = []
for line in lines:
	grid.append(list(map(int, line)))

res = 0

for row in range(len(grid)):
	for collumn in range(len(grid[row])):
		tree = grid[row][collumn]
		if all(grid[row][x] < tree for x in range(collumn)) or all(grid[row][x] < tree for x in range(collumn + 1, len(grid[row])))\
			or all(grid[x][collumn] < tree for x in range(row)) or all(grid[x][collumn] < tree for x in range(row + 1, len(grid))):
			res += 1

print(res)

res = 0

for row in range(len(grid)):
	for collumn in range(len(grid[row])):
		tree = grid[row][collumn]
		n = s = w = e = 0
		for x in range(collumn - 1, -1 , -1):
			w += 1
			if grid[row][x] >= tree:
				break
		for x in range(collumn + 1, len(grid[row])):
			e += 1
			if grid[row][x] >= tree:
				break
		for x in range(row - 1, -1 , -1):
			n += 1
			if grid[x][collumn] >= tree:
				break
		for x in range(row + 1, len(grid)):
			s += 1
			if grid[x][collumn] >= tree:
				break
		res = max(res, n * s * w * e)

print(res)
