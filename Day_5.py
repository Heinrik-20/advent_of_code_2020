# Day 5 problem

def boarding_pass_decoder(code):
    total_rows = 128
    row_range = [0, 127]
    for i in range(7):
        if code[i] == "F":
            row_range[1] -= (total_rows/2) 
        elif code[i] == "B":
            row_range[0] += (total_rows/2)
        total_rows /= 2
    
    total_cols = 8
    col_range = [0, 7]
    for i in range(7, len(code)):
        if code[i] == "L":
            col_range[1] -= (total_cols/2)
        elif code[i] == "R":
            col_range[0] += (total_cols/2)
        total_cols /= 2 
        
    return int((row_range[0] * 8) + col_range[0])

with open("textfiles/problem5.txt") as fp:
    # Challenge 1
    boarding_ID = []
    for code in fp:
        boarding_ID.append(boarding_pass_decoder(str(code)))
        
    print(max(boarding_ID))
    # Challenge 2
    ID = 31
    boarding_ID.sort()
    for i in range(len(boarding_ID)):
        ID += 1
        if boarding_ID[i] != ID:
            print(ID)
            break
