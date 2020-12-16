f = open("input6.txt", "r").read().split("\n\n")
a = []
bob = []
count = 0
count2 = 0
counted = []

for i in f:
	a.append(i.split())

#part1
for i in a:
	for j in i:
		for char in j:
			if char in bob:
				pass
			else:
				bob.append(char)
	count += len(bob)
	bob = []

print(count)

#part2
for i in a:
	for j in i:
		for char in j:
			bob.append(char)

	for k in bob:
		if bob.count(k) == len(i) and k not in counted:
			counted.append(k)
			count2 += 1
	counted = []
	bob = []
print(count2)	