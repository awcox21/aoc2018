import re
from collections import namedtuple
import numpy as np

Claim = namedtuple('Claim', ['id', 'x', 'y', 'w', 'h'])

def plot_sheet(sheet):
    rows, cols = sheet.shape
    str_ = str()
    for i in range(rows):
        for j in range(cols):
            if not sheet[i, j]:
                str_ += '.  '
            elif sheet[i, j] == 1:
                str_ += '#  '
            else:
                str_ += 'X  '
        str_ += '\n'
    print(str_)

def add(sheet, claim):
    _, x, y, w, h = claim
    try:
        sheet[y + h - 1, x + w - 1]
    except IndexError:
        raise IndexError('Claim outside bounds: {}'.format(claim))
    sheet[y: y + h, x: x + w] += 1

inp = 'day3.in'
claims = list()
with open(inp, 'r') as f:
    for line in f:
        match = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
        claims.append(Claim(*map(int, match.groups())))

width, height = 1000, 1000
sheet = np.zeros((width, height))
# plot_sheet(sheet)
# claim = Claim(123, 3, 2, 5, 4)
# claims = [Claim(1, 1, 3, 4, 4), Claim(2, 3, 1, 4, 4), Claim(3, 5, 5, 2, 2)]
for claim in claims:
    add(sheet, claim)
plot_sheet(sheet)
rows, cols = sheet.shape

""" Part 1 """
count = 0
for i in range(rows):
    for j in range(cols):
        if sheet[i, j] > 1:
            count += 1
print(count)

""" Part 2 """
for claim in claims:
    _, x, y, w, h = claim
    if np.all(np.less(sheet[y: y + h, x: x + w], 2)):
        print(claim)
