# Day 1 problem 
# Commented out code are 2nd challange
with open("textfiles/problem1.txt") as fp:
    all_int = []
    pairs = []
    # triples = [] 
    for num in fp:
        all_int.append(int(num))
        
    for int1 in all_int:
        for int2 in all_int:
            if (int1 + int2) == 2020:
                pairs.append((int1, int2))
            #for int3 in all_int:
             #   if (int1 + int2 + int3) == 2020:
              #      triples.append((int1, int2, int3))
    
    for int1, int2 in pairs:
        print(int1, int2, (int1*int2))

    #for int1, int2, int3 in triples:
     #   print(int1, int2, int3, (int1*int2*int3))
