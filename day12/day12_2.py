from heapq import heappop, heappush
with open("input.txt", "r") as f:
	lines = f.read().strip().split()

grid = [list(line) for line in lines]
r = len(grid)
c = len(grid[0])

for i in range(r):
	for j in range(c):
		if grid[i][j] == "S":
			start = i, j
		if grid[i][j] == "E":
			end = i, j

characters = list("abcdefghijklmnopqrstuvwxyz")

def get_height(c):
	if c in characters:
		return characters.index(c)
	if c == "S":
		return 0
	if c == "E":
		return 25

def is_valid_pos(x, y):
	for mx, my in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
		nx = x + mx
		ny = y + my

		if not (0 <= nx < r and 0 <= ny < c):
			continue
		if get_height(grid[nx][ny]) >= get_height(grid[x][y]) - 1:
			yield nx, ny

visited = [['.'] * c for _ in range(r)]
heap = [(0, end[0], end[1])]

while True:
	steps, x, y = heappop(heap)

	if visited[x][y] != '.':
		continue
	visited[x][y] = lines[x][y]

	if get_height(grid[x][y]) == 0:
		print(steps)
		break

	for nx, ny in is_valid_pos(x, y):
		heappush(heap, (steps + 1, nx, ny))

for list in visited:
	str = ""
	for pos in list:
		str += str.join(pos)
	print(str)
