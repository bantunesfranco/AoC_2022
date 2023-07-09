with open("input.txt", "r") as f:
	lines = f.read().strip().split()

res = 0
res2 = 0

for line in lines:
	areas = line.split(',')
	ranges = [list(map(int, area.split('-'))) for area in areas]
	a, b = ranges[0]
	c, d = ranges[1]

	if (a <= c and b >= d) or (c <= a and d >= b):
		res += 1
		print(a, b, c, d)

print(f"\nresult for part 1 is {res}\n")

for line in lines:
	areas = line.split(',')
	ranges = [list(map(int, area.split('-'))) for area in areas]
	a, b = ranges[0]
	c, d = ranges[1]

	# if (c <= b <= d) or (a <= d <= b) or (a <= c and b >= d) or (c <= a and d >= b):
	# 	res2 += 1
	# 	print(a, b, c, d)
	
	if not (b < c or a > d):
		res2 += 1
		print(a, b, c, d)

print(f"\nresult for part 2 is {res2}\n")
