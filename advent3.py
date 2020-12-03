import csv

with open('input3.csv', mode='r') as csv_file:
		csv_reader = csv.reader(csv_file)
		input = []
		for row in csv_reader:
			input.append(row[0])
print(len(input[0]))
count = 0
pos = 0
for i in range(len(input)):		#right 3 down 1
	point = input[i][pos]
	pos += 3
	if pos > 30:
		pos = pos - 31
	if point == '#':
		count += 1
	else:
		pass
print('ans: ', count)

count1 = 0
pos = 0
for i in range(len(input)):		#right 1 down 1
	point = input[i][pos]
	pos += 1
	if pos > 30:
		pos = pos - 31
	if point == '#':
		count1 += 1
	else:
		pass
print('ans: ', count1)

count2 = 0
pos = 0
for i in range(len(input)):		#right 5 down 1
	point = input[i][pos]
	pos += 5
	if pos > 30:
		pos = pos - 31
	if point == '#':
		count2 += 1
	else:
		pass
print('ans: ', count2)

count3 = 0
pos = 0
for i in range(len(input)):		#right 7 down 1
	point = input[i][pos]
	pos += 7
	if pos > 30:
		pos = pos - 31
	if point == '#':
		count3 += 1
	else:
		pass
print('ans: ', count3)

count4 = 0
pos = 0
for i in range(len(input)):		#right 1 down 2
	if i % 2 == 0:
		point = input[i][pos]
		pos += 1
		if pos > 30:
			pos = pos - 31
		if point == '#':
			count4 += 1
		else:
			pass
	else:
		pass
print('ans: ', count4)

final = count*count1*count2*count3*count4
print(final)