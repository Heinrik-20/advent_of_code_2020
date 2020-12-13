# Day 10 problem
from collections import defaultdict

# First part
joltages = []
with open("textfiles/problem10.txt") as fp:
    for jolt in fp:
        joltages.append(int(jolt))

one_diff = 0
three_diff = 0
joltages.sort()
for i in range(len(joltages) - 1):
    diff = abs(joltages[i] - joltages[i + 1])
    if diff == 1:
        one_diff += 1
    elif diff == 3:
        three_diff += 1
    else:
        print("chain broken")
        break

print("Number of 1-jolt differences multiplied by the number of 3-jolt differences: {}"
      .format((one_diff + 1) * (three_diff + 1)))

# Second part 
# Uses memoization to solve counts
# Had some help from https://hackernoon.com/google-interview-questions-deconstructed-the-knights-dialer-f780d516f029
joltages.append(0)
joltages.append(max(joltages) + 3)
joltages.sort()
graph = defaultdict(list)
for jolt1 in joltages:
    for jolt2 in joltages:
        diff = jolt2 - jolt1
        if diff > 0 and diff <= 3:
            graph[jolt1].append(jolt2)

counts = defaultdict(int)
def find_counts(graph, source, end):
    global counts
    if source == end:
        return 1
    else:
        for node in graph[source]:
            if (node, end) not in counts.keys():
                counts[(source, end)] += find_counts(graph, node, end)
            else:
                counts[(source, end)] += counts[(node, end)]
        return counts[(source, end)]

print("Number of distinct ways to arrange adapters: {}".format(find_counts(graph, 0, max(joltages))))
