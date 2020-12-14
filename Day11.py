# Day 11 problem
from copy import deepcopy
seating = []
with open("textfiles/problem11.txt") as fp:
    for line in fp:
        seating.append(list(line.strip()))

def check_adjacent(seating, r_index, c_index):
    adjacents =[(-1, 0), (0, -1), (0, 1), (1, 0), 
                (-1, -1), (-1, 1), (1, -1), (1, 1)]
    ignored = set()
    if r_index == 0:
        ignored.add(adjacents[0])
        ignored.add(adjacents[4])
        ignored.add(adjacents[5])
    elif r_index == (len(seating) - 1):
        ignored.add(adjacents[3])
        ignored.add(adjacents[6])
        ignored.add(adjacents[7])
    if c_index == 0:
        ignored.add(adjacents[1])
        ignored.add(adjacents[4])
        ignored.add(adjacents[6])
    elif c_index == (len(seating[r_index]) - 1):
        ignored.add(adjacents[2])
        ignored.add(adjacents[5])
        ignored.add(adjacents[7])
    
    occupied_seats = 0
    # First part
    '''
    for changes in adjacents:
        if changes not in ignored:
            row, col = r_index + changes[0], c_index + changes[1]
            if seating[row][col] == "#":
                occupied_seats += 1
    '''            
        
    # Second part 
    for changes in adjacents:
        row, col = r_index, c_index
        if changes not in ignored:
            row, col = row + changes[0], col + changes[1]
            while (row < len(seating)) and (col < len(seating[0])) and (row >= 0) and (col >= 0):
                if seating[row][col] == "#":
                    occupied_seats += 1
                    break
                elif seating[row][col] == ".":
                    row += changes[0]
                    col += changes[1]
                elif seating[row][col] == "L":
                    break
    
    return occupied_seats
    
def apply_rules(seating):
    change = 0
    orig_seating = deepcopy(seating)
    for r_index in range(len(seating)):
        for c_index in range(len(seating[r_index])):
            if orig_seating[r_index][c_index] == "L":
                occupied_seats = check_adjacent(orig_seating, r_index, c_index)
                if occupied_seats == 0:
                    seating[r_index][c_index] = "#"
                    change = 1
            elif orig_seating[r_index][c_index] == "#":
                occupied_seats = check_adjacent(orig_seating, r_index, c_index)
                #if occupied_seats >= 4: # For part 1
                if occupied_seats >= 5:
                    seating[r_index][c_index] = "L"
                    change = 1
                    
    return seating, change

change = 1
while change:
    seating, change = apply_rules(seating)

occupied = 0
for r_index in range(len(seating)):
    for c_index in range(len(seating[r_index])):
        if seating[r_index][c_index] == "#":
            occupied += 1

print(occupied)
