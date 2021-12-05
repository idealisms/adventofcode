import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

# inp = '''0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2'''

points = []
for line in inp.splitlines():
    points.append([int(n) for n in line.replace('-> ', '').replace(',', ' ').split()])

board = collections.defaultdict(int)

Point = collections.namedtuple('Point', ['x', 'y'])

starts = [Point(p[0], p[1]) for p in points]
ends = [Point(p[2], p[3]) for p in points]

for start, end in zip(starts, ends):
    if start.x == end.x:
        a = min(start.y, end.y)
        b = max(start.y, end.y)
        for n in range(a, b+1):
            pt = (start.x, n)
            board[pt] += 1
    elif start.y == end.y:
        a = min(start.x, end.x)
        b = max(start.x, end.x)
        for n in range(a, b+1):
            pt = (n, start.y)
            board[pt] += 1

part1 = sum(1 if n > 1 else 0 for n in board.values())
print(part1)

board = collections.defaultdict(int)

for start, end in zip(starts, ends):
    if start.x == end.x:
        a = min(start.y, end.y)
        b = max(start.y, end.y)
        for n in range(a, b+1):
            pt = (start.x, n)
            board[pt] += 1
    elif start.y == end.y:
        a = min(start.x, end.x)
        b = max(start.x, end.x)
        for n in range(a, b+1):
            pt = (n, start.y)
            board[pt] += 1
    else:
        x_range = y_range = None
        if start.x < end.x:
            x_range = range(start.x, end.x+1)
        else:
            x_range = range(start.x, end.x-1, -1)
        if start.y < end.y:
            y_range = range(start.y, end.y+1)
        else:
            y_range = range(start.y, end.y-1, -1)
        for pt in zip(x_range, y_range):
            board[pt] += 1

part2 = sum(1 if n > 1 else 0 for n in board.values())
print(part2)
