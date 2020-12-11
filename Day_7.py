# Day 7 problem
# Solution to challenge 1
# Uses a Breadth First Search approach with FIFO (Queue)
main_bag = "shiny gold"
queue = []
queue.append(main_bag)
found = set()
while queue:
    pattern = queue.pop(0)
    if pattern != main_bag:
        found.add(pattern)
    with open("textfiles/problem7.txt") as fp:
        for string in fp:
            bag = " ".join(string.split()[0:2])
            if (pattern in string) and (pattern != bag):
                queue.append(bag)
                
print("Bags that can contain at least one {0}: {1}".format(main_bag,len(found)))

# Solution to challenge 2
# Uses Breadth First Search approach with LIFO (Stack)
bags = -1
queue = []
queue.append(main_bag)
no_other = set()
while queue:
    pattern = queue.pop(len(queue) - 1)
    key_bag = pattern
    bags += 1
    with open("textfiles/problem7.txt") as fp:
        for string in fp:
            if key_bag == (" ".join(string.split()[0:2])):
                if "no other" in string:
                    #print(key_bag)
                    no_other.add(key_bag)
                else:
                    index = 0
                    for word in string.split():
                        if word.isdigit():
                            for i in range(int(word)):
                                queue.append(" ".join(string.split()[index + 1:index + 3]))
                        index += 1

print("Individual bags in one {0} bag: {1}".format(main_bag, bags))
