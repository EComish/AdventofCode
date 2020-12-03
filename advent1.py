import csv



with open('input1.csv', mode='r') as csv_file:
		csv_reader = csv.reader(csv_file)
		input = []
		for row in csv_reader:
			input.append(row[0])
		
max = len(input)
for i in range(0,max):
	num = 2020-int(input[i])
	#print(num)
	for n in range(1,max-i):
		for m in range(1,max-i-n):
			#print(input[i+n])
			#print(input[i+n+m])
			if int(input[i+n+m])+int(input[i+n]) == num:
				print(int(input[i])*int(input[i+n])*int(input[i+n+m]))
			else:
				pass