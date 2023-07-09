from collections import defaultdict

with open("input.txt" ,"r") as f:
	data = ("\n" + f.read().strip()).split("\n$ ")[1:]

path = []
dir_sizes = defaultdict(int)
subdirs = defaultdict(list)

def parse(data):
	lines = data.split('\n')
	command = lines[0]
	output = lines[1:]
	parts = command.split(" ")
	if parts[0] == "cd":
		if parts[1] == "..":
			path.pop()
		else:
			path.append(parts[1])
		return
	
	abspath = "/".join(path)

	sizes = []
	for line in output:
		if not line.startswith("dir"):
			sizes.append(int(line.split(" ")[0]))
		else:
			dir_name = line.split(" ")[1]
			subdirs[abspath].append(f"{abspath}/{dir_name}")
	dir_sizes[abspath] = sum(sizes)

for line in data:
	parse(line)

def get_size(abspath):
	size = dir_sizes[abspath]
	for subdir in subdirs[abspath]:
		size += get_size(subdir)
	return size

res = 0
for path in dir_sizes:
	if get_size(path) <= 100000:
		res += get_size(path)
print(f"size for part 1 is {res}")

unsed_size = 70000000 - get_size("/")
required_size = 30000000 - unsed_size
res = 999999999

for path in dir_sizes:
	size = get_size(path)
	if size >= required_size:
		res = min(res, size)
print(f"\nsize for part 2 is {res}")