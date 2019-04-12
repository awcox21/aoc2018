from itertools import cycle

freq = 0
changes = list()
with open('day1.in', 'r') as f:
    for line in f:
        changes.append(int(line))
        freq += int(line)
print(freq)

changes = cycle(changes)
freq, count = 0, 0
values = {freq}
for value in changes:
    freq += value
    count += 1
    if freq in values:
        break
    else:
        values.add(freq)
print(freq, count)
