#How many characters need to be processed before the first start-of-packet marker is detected?
def d6a():
    f = open("Day06.txt", "r")
    txt = f.readline()
    index = 3
    while index < len(txt):
        actual = txt[index-3:index+1]
        i=0
        while i < len(actual):
            modedArr = list(actual)
            modedArr = modedArr[i + 1::]
            if actual[i] in modedArr:
                index += 1
                break              
            i+=1    
            if i==4:
                return index + 1
     
            

#How many characters need to be processed before the first start-of-message marker is detected?
def d6b():
    f = open("Day06.txt", "r")
    txt = f.readline()
    index = 13
    while index < len(txt):
        actual = txt[index-13:index+1]
        i=0
        while i < len(actual):
            modedArr = list(actual)
            modedArr = modedArr[i + 1::]
            if actual[i] in modedArr:
                index += 1
                break              
            i+=1    
            if i==14:
                return index + 1
        