# Day 9 problem
def binary_search(array, size, item):
    if size == 1 and array[0] != item:
        return None
    mid = int(size/2)
    if array[mid] == item:
        return item
    diff = item - array[mid]
    if diff > 0:
        return binary_search(array[mid:], size - mid, item)
    else:
        return binary_search(array[0:mid + 1], size - mid, item)

# First part
numbers = []
with open("textfiles/problem9.txt") as fp:
    for num in fp:
        numbers.append(int(num))
    
queue = []
for i in range(25, len(numbers)):
    queue.append(numbers[i])

fail = 0
start = 25
while queue and not fail and start <= len(numbers):
    found = 0
    key_num = queue.pop(0)
    array = (numbers[start - 25:start])
    for item in array:
        if binary_search(sorted(array), len(array), key_num - item):
            found = 1
            break
    if not found:
        fail = 1
        print("Number that fails: {}".format(key_num))
        break
    start += 1

# Second part
found = 0
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if sum(numbers[i:j]) == key_num:
            found = 1
            print("Encryption Weakness is: {}".format(max(numbers[i:j]) + min(numbers[i:j])))
            break
    if found:
        break
