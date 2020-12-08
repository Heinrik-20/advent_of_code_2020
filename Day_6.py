# Day 6 problem
with open("textfiles/problem6.txt") as fp:
    # Solution to first challenge
    '''
    questions_found = []
    question = set()
    for item in fp:
        item_list = item.split()
        if len(item_list) == 0:
            questions_found.append(question)
            question = set()
        else:
            for char in item_list[0]:
                question.add(char)
    questions_found.append(question)
    
    questions_count = 0
    for i in range(len(questions_found)):
        questions_count += len(questions_found[i])
    
    print("Number of questions which anyone answered yes: {}".format(questions_count))
    '''
    # Solution to first challenge
    questions_found = []
    question = {}
    passengers = 0
    for item in fp:
        item_list = item.split()
        if len(item_list) == 0:
            question["passengers"] = passengers
            passengers = 0
            questions_found.append(question)
            question = {}
            continue
        else:
            for char in item_list[0]:
                if char not in question.keys():
                    question[char] = 1
                else:
                    question[char] += 1
        passengers += 1
    question["passengers"] = passengers
    questions_found.append(question)
    
    question_count = 0
    for question_sets in questions_found:
        for keys in question_sets.keys():
            if keys == "passengers":
                continue
            elif question_sets[keys] == question_sets["passengers"]:
                question_count += 1
    print("Number of questions everyone answered yes: {}".format(question_count))
