import csv

with open('input2.csv', mode='r') as csv_file:
		csv_reader = csv.reader(csv_file)
		input = []
		for row in csv_reader:
			input.append(row[0])




count = 0

for i in input:
	breakd = i.split()
	bounds = breakd[0].split('-')
	letter = breakd[1][:1]
	password = breakd[2]
	num = password.count(letter)
	if num >= int(bounds[0]) and num <= int(bounds[1]):
		count += 1
	else:
		pass

print(count)
count2 = 0
for i in input:
	breakd = i.split()
	bounds = breakd[0].split('-')
	letter = breakd[1][:1]
	password = breakd[2]
	if password[int(bounds[0])-1] == letter and password[int(bounds[1])-1] != letter:
		count2 += 1
	elif password[int(bounds[1])-1] == letter and password[int(bounds[0])-1] != letter:
		count2 += 1
	else:
		pass
print(count2)

