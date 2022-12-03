#What would your total score be if everything goes exactly according to your strategy guide?

def d2a():
    f = open("Day02.txt", "r")
    txt = f.readlines()
    total = 0
    for line in txt:
        if line[0] == 'A' and line[2] == 'X':
            total += 4
        elif line[0] == 'A' and line[2] == 'Y':
            total += 8
        elif line[0] == 'A' and line[2] == 'Z':
            total += 3
        elif line[0] == 'B' and line[2] == 'X':
            total += 1
        elif line[0] == 'B' and line[2] == 'Y':
            total += 5
        elif line[0] == 'B' and line[2] == 'Z':
            total += 9
        elif line[0] == 'C' and line[2] == 'X':
            total += 7
        elif line[0] == 'C' and line[2] == 'Y':
            total += 2
        elif line[0] == 'C' and line[2] == 'Z':
            total += 6
        else:
            continue

    return total

#Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
def d2b():
    f = open("Day02.txt", "r")
    txt = f.readlines()
    total = 0
    for line in txt:
        if line[0] == 'A' and line[2] == 'X':
            total += 3
        elif line[0] == 'A' and line[2] == 'Y':
            total += 4
        elif line[0] == 'A' and line[2] == 'Z':
            total += 8
        elif line[0] == 'B' and line[2] == 'X':
            total += 1
        elif line[0] == 'B' and line[2] == 'Y':
            total += 5
        elif line[0] == 'B' and line[2] == 'Z':
            total += 9
        elif line[0] == 'C' and line[2] == 'X':
            total += 2
        elif line[0] == 'C' and line[2] == 'Y':
            total += 6
        elif line[0] == 'C' and line[2] == 'Z':
            total += 7
        else:
            continue

    return total