#What is the sum of the priorities of those item types?
def d3a():
    f = open("Day03.txt", "r")
    txt = f.readlines()
    total = 0
    for line in txt:
        firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
        for char in firstpart:
            if char in secondpart:
                letter = char
        if letter.isupper() == True:
            total += ord(letter) - 38 #64 - 26
        else:
            total += ord(letter) - 96
    return total

#What is the sum of the priorities of those item types?
def d3b():
    f = open("Day03.txt", "r")
    txt = f.readlines()
    i = 0
    total = 0
    while i < len(txt):
        for char in txt[i]:
            if char in txt[i+1] and char in txt[i+2] and char != "\n": 
                letter = char
        if letter.isupper() == True:
            total += ord(letter) - 38 #64 - 26
        else:
            total += ord(letter) - 96
        i+=3
    return total
        