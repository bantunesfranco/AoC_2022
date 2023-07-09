from functools import cmp_to_key

with open("input.txt", "r") as f:
	blocks = f.read().strip().split("\n\n")

def check(l1, l2):
	if type(l1) == int and type(l2) == list:
		l1 = [l1]

	if type(l1) == list and type(l2) == int:
		l2 = [l2]

	if type(l1) == int and type(l2) == int:
		if l1 < l2:
			return 1
		if l1 == l2:
			return 0
		if l1 > l2:
			return -1

	if type(l1) == list and type(l2) == list:
		i = 0
		while i < len(l1) and i < len(l2):
			n = check(l1[i], l2[i])
			if n == 1:
				return 1
			if n == -1:
				return -1
			i += 1

		if i == len(l1):
			if i == len(l2):
				return 0
			if i < len(l2):
				return 1

		if i == len(l2):
			return -1

res = 0
for i, block in enumerate(blocks):
	x, y = map(eval, block.split('\n'))
	if check(x, y) == 1:
		res += (i + 1)

print(res)

with open("input.txt", "r") as f:
	lines = list(map(eval, f.read().split()))

i2 = 1
i6 = 2

for line in lines:
	if check(line, [[2]]) < 0:
		i2 += 1
		i6 += 1
	if check(line, [[6]]) < 0:
		i6 += 1

res = i2 * i6
print(i2, i6, res)