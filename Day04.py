#In how many assignment pairs does one range fully contain the other?
def d4a():
	f = open("Day04.txt", "r")
	txt = f.readlines()
	total = 0
	for line in txt:
		splitted = line.split(",")
		first = splitted[0].split("-")
		second = splitted[1].split("-")
		if int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]):
			total += 1
		elif int(second[0]) >= int(first[0]) and int(second[1]) <= int(first[1]):
			total += 1
	return total

#In how many assignment pairs do the ranges overlap?
def d4b():
	f = open("Day04.txt", "r")
	txt = f.readlines()
	total = 0
	for line in txt:
		splitted = line.split(",")
		first = splitted[0].split("-")
		second = splitted[1].split("-")
		if int(first[0]) >= int(second[0]) and int(first[0]) <= int(second[1]):
			total += 1
		elif int(second[0]) >= int(first[0]) and int(second[0]) <= int(first[1]):
			total += 1
	return total