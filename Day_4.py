# Day 4 problem
with open("textfiles/problem4.txt") as fp:
    compulsory = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl","pid"]
    compulsory.sort()
    passports = []
    one_passport = []
    for items in fp:
        if len(items.split()) == 0:
            passports.append(one_passport)
            one_passport = []
            continue
        else:
            for string in items.split():
                one_passport.append(string)
    passports.append(one_passport)
    valid = 0
    for passport in passports.copy():
        if len(passport) < 7:
            passports.remove(passport)
            continue
        elif len(passport) == 8:
            valid += 1
            continue
        else:
            invalid = 0
            passport.sort()
            for i in range(len(passport)):
                if (compulsory[i] not in passport[i]):
                    invalid = 1
                    passports.remove(passport)
                    break
            if not invalid:
                #print(passport)
                valid += 1
    print("Stage 1 valid: {}".format(valid))
    rules = {"byr": (1920, 2002), "iyr": (2010, 2020), "eyr": (2020, 2030), "hgt": {"cm": (150, 193), "in": (59, 76)}, 
            "ecl": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]}
    valid_nums = "0123456789"
    valid_char = "abcdef"
    valid = 0
    for passport in passports:
        invalid = 0
        for item in passport:
            if ("cid" in item):
                continue
            else:
                item_list = item.split(":")
                field = item_list[0]
                if field in ["byr", "iyr", "eyr"]:
                    if int(item_list[1]) < rules[field][0] or int(item_list[1]) > rules[field][1]:
                        invalid = 1
                if field == "ecl":
                    if item_list[1] not in rules[field]:
                        invalid = 1
                if field == "hgt":
                    if "cm" in item_list[1]:
                        item_list[1] = item_list[1].replace("cm", "")
                        if (int(item_list[1]) < rules[field]["cm"][0] or int(item_list[1]) > rules[field]["cm"][1]):
                            invalid = 1
                    elif "in" in item_list[1]:
                        item_list[1] = item_list[1].replace("in", "")
                        if (int(item_list[1]) < rules[field]["in"][0] or int(item_list[1]) > rules[field]["in"][1]):
                            invalid = 1
                    elif "in" not in item_list[1] and "cm" not in item_list[1]:
                        invalid = 1
                if field == "pid":
                    if len(item_list[1]) != 9:
                        invalid = 1
                    else:
                        for char in item_list[1]:
                            if not char.isdigit():
                                invalid = 1
                                break
                    
                if field == "hcl":
                    if len(item_list[1]) != 7:
                        invalid = 1
                        break
                    if item_list[1][0] != "#":
                        invalid = 1
                        break
                    for i in range(1, len(item_list[1])):
                        invalid = 0
                        if item_list[1][i] not in valid_nums and item_list[1][i] not in valid_char:
                            invalid = 1
                            break           
            if invalid:
                break
        if invalid == 0:
            valid += 1
                    
    print("Stage 2 valid: {}".format(valid))
