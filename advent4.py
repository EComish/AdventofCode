d = {"byr":"", "iyr": "","eyr":"", "hgt": "","hcl":"", "ecl": "","pid":"", "cid": "" }
a = []
f = open("input4.txt", "r").read().split("\n\n")

for i in f:
	a.append(i.split())
count = 0

for j in a:
	for k in j:
		b = k.split(':')
		d.update({b[0]:b[1]})
	
	for i in d:
		if d[i] == "" and i != 'cid':
			print('invalid')
			count += 1
			break
		elif i == "byr" and (int(d[i]) < 1920 or int(d[i]) > 2002):
			print('invalid')
			count += 1
			break
		elif i == "iyr" and (int(d[i]) < 2010 or int(d[i]) > 2020):
			print('invalid')
			count += 1
			break
		elif i == "eyr" and (int(d[i]) < 2020 or int(d[i]) > 2030):
			print('invalid')
			count += 1
			break
		elif i == 'hgt' and d[i][-2:] == 'cm':
			if int(d[i][:-2]) < 150 or int(d[i][:-2]) > 193:
				print('invalid')
				count += 1
				break
		elif i == 'hgt' and d[i][-2:] == 'in':
			if int(d[i][:-2]) < 59 or int(d[i][:-2]) > 76:
				print('invalid')
				count += 1
				break
		elif i == 'hcl' and (d[i][0] != '#' or len(d[i]) != 7):
				print('invalid')
				count += 1
				break
		elif i == 'ecl' and d[i] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
				print('invalid')
				count += 1
				break
		elif i == 'pid' and len(d[i]) != 9:
				print('invalid')
				count += 1
				break
		elif i == 'cid':
				break
	for i in d:
		d[i] = ""

print("No. invalid: ", count)
print("No. valid: ", len(a)-count-1)


