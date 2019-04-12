from functools import reduce
from itertools import combinations

# inp = 'day2part1.in'
# inp = 'day2part2.in'
inp = 'day2.in'

""" Part 1 """
keys = 2, 3
nums = {_val: 0 for _val in keys}
boxes = list()
with open(inp, 'r') as f:
    for line in f:
        boxes.append(line.strip())
        values = set(filter(lambda _j: _j in nums,
                            map(lambda _i: line.count(_i), line)))
        for value in values:
            try:
                nums[value] += 1
            except KeyError:
                pass
print(reduce(lambda _x, _y: _x * _y, nums.values()))

""" Part 2 """


def diff(str0, str1):
    count = 0
    for m, n in zip(str0, str1):
        if m != n:
            count += 1
    return count


similar, num = None, 0
for i, j in combinations(range(len(boxes)), 2):
    i, j = boxes[i], boxes[j]
    if similar is None:
        similar = i, j
        num = diff(i, j)
    else:
        if diff(i, j) < num:
            similar = i, j
            num = diff(i, j)
i, j = similar
shared = str()
for x, y in zip(i, j):
    if x == y:
        shared += x
print(shared)
