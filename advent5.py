f = open("input5.txt", "r").read().split("\n")

max1 = 127
min1 = 0
max2 = 7
min2 = 0
seatid = 0
maxseatid = 0
allseats = []
for i in f:
	for j in range(len(i)):
		if i[j] == 'F':
			max1 = (max1-1-min1)/2 + min1
		elif i[j] == 'B':
			min1 = max1 - (max1-1-min1)/2
		elif i[j] == 'L':
			max2 = (max2-1-min2)/2 + min2
		elif i[j] == 'R':
			min2 = max2 - (max2-1-min2)/2
	seatid = max1*8 + max2
	allseats.append(seatid)
	if seatid > maxseatid:
		maxseatid = seatid
	min1 = min2 = 0
	max1 = 127
	max2 = 7
print(maxseatid)		#part 1

x = sorted(allseats)

prev = x[0]-1
yours = 0
for i in x:
	if i == prev + 1:
		prev = i
	elif i != prev + 1:
		yours = i - 1
		break
print(yours)			#part2
