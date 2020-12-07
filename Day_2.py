# Day 2 problem
with open("textfiles/problem2.txt") as fp:
    limits = []
    letters = []
    strings = []
    for items in fp:
        temp = items.split()
        hyphen = 0
        int1 = ''
        int2 = ''
        for char in temp[0]:
            if char == '-':
                hyphen = 1
                continue
            if hyphen:
                int2 += char
            else:
                int1 += char
        limits.append((int(int1), int(int2)))
        letters.append(temp[1][0])
        strings.append(temp[2])
    
    valid = 0
    for i in range(len(strings)):
        pos1, pos2 = 0, 0
        if (strings[i][limits[i][0] - 1] == letters[i]):
            pos1 = 1
        if (strings[i][limits[i][1] - 1] == letters[i]):
            pos2 = 1
        if pos1 != pos2:
            valid += 1
        
    
    print(valid)
