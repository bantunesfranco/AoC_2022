blocked = set()
pnr = 0

with open("input.txt", "r") as f:
	for line in f:
		x = [list(map(int, point.split(','))) for point in line.strip().split(" -> ")]
		for (x1, y1), (x2, y2) in zip(x, x[1:]):
			x1, x2 = sorted([x1, x2])
			y1, y2 = sorted([y1, y2])
			for x in range(x1, x2 + 1):
				for y in range(y1, y2 + 1):
					blocked.add((x, y))
					pnr = max(pnr, y + 1)

p = 0;

while True:
	sx, sy = (500, 0)
	while True:
		if sy >= pnr:
			print(p)
			exit(0)
		if (sx, sy + 1) not in blocked:
			sy += 1
			continue
		if (sx - 1, sy + 1) not in blocked:
			sx -= 1
			sy += 1
			continue
		if (sx + 1, sy + 1) not in blocked:
			sx += 1
			sy += 1
			continue
		blocked.add((sx, sy))
		p += 1

# while (500, 0) not in blocked:
# 	sx, sy = (500, 0)
# 	while True:
# 		if sy >= pnr:
# 			break
# 		if (sx, sy + 1) not in blocked:
# 			sy += 1
# 			continue
# 		if (sx - 1, sy + 1) not in blocked:
# 			sx -= 1
# 			sy += 1
# 			continue
# 		if (sx + 1, sy + 1) not in blocked:
# 			sx += 1
# 			sy += 1
# 			continue
# 		break
# 	blocked.add((sx, sy))
# 	p += 1

# print(p)
