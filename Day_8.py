# Day 8 problem
import copy
instructions = []
with open("textfiles/problem8.txt") as fp:
    for item in fp:
        step = item.split()
        step[1] = int(step[1])
        instructions.append(list(step))

def count_steps_taken(instructions):
    index_tracker = set()
    accumulator = 0
    queue = []
    queue.append(0)
    found = 0
    
    while queue:
        index = queue.pop(0)
        if index < len(instructions):
            ins = instructions[index][0]
            step = instructions[index][1]
            if ins == "nop":
                index += 1
            elif ins == "acc":
                accumulator += step
                index += 1
            elif ins == "jmp":
                index += step

            if index not in index_tracker:
                index_tracker.add(index)
                queue.append(index)
        else:
            found = 1
            break
            
    return(found, accumulator)

print("Value of accumulator before instructions being executed second time: {}".format(count_steps_taken(instructions)[1]))

queue = []
for i in range(total_ins):
    if (instructions[i][0] == "nop") or (instructions[i][0] == "jmp"):
        queue.append(i)
    
accumulator = 0
for index in queue:
    found = 0
    cpy = copy.deepcopy(instructions)
    if instructions[index][0] == "jmp":
        cpy[index][0] = "nop"
        found, accumulator = count_steps_taken(cpy)
    elif instructions[index][0] == "nop":
        cpy[index][0] == "jmp"
        found, accumulator = count_steps_taken(cpy)
    
    if found:
        print("Value of accumulator in the corrected code: {}".format(accumulator))
        break
