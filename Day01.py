#Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

def d1a():
    f = open("Day01.txt", "r")
    i = 0
    lineSum = 0
    highest = 0
    txt = f.readlines()
    for line in txt:
        if line == '\n':
            if highest < lineSum:
                highest = lineSum
            lineSum = 0
        else:
            lineSum += int(txt[i])
        i += 1
    return highest

#Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
def d1b():
    f = open("Day01.txt", "r")
    i = 0
    lineSum = 0
    elves = []
    txt = f.readlines()
    for line in txt:
        if line == '\n':
            elves.append(lineSum)
            lineSum = 0
        else:
            lineSum += int(txt[i])
        i += 1
    elves.sort(reverse = True)
    total = elves[0] + elves[1] + elves[2]
    return total