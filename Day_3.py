# Day 3 problem
with open("textfiles/problem3.txt") as fp:
    area_map = []
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for items in fp:
        area_map.append(items.split())
        
    trees = 0
    max_length = len(area_map)
    item_length = 0
    for char in area_map[0][0]:
        item_length += 1
        
    # Challenge 1 solution    
    #c_index, r_index = 0, 0
    #while (c_index < max_length):
        #if (area_map[c_index][0][r_index % item_length] == "#"):
         #   trees += 1
        #r_index += 3
        #c_index += 1
    #print(trees)    
        
    # Challenge 2 solution
    total_trees = 1
    for r_incre, c_incre in slopes:
        c_index, r_index = 0, 0
        trees = 0
        while (c_index < max_length):
            if (area_map[c_index][0][r_index % item_length] == "#"):
                trees += 1
            r_index += r_incre
            c_index += c_incre
        total_trees *= trees
    print(total_trees)
