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

cols = list(zip(*points))
max_x = max(cols[0] + cols[2])
max_y = max(cols[1] + cols[3])
print(max_x, max_y)

board = [[0] * 1000 for _ in range(1000)]

for point_pair in points:
    if point_pair[0] == point_pair[2]:
        a = min(point_pair[1], point_pair[3])
        b = max(point_pair[1], point_pair[3])
        for n in range(a, b+1):
            board[point_pair[0]][n] += 1
    elif point_pair[1] == point_pair[3]:
        a = min(point_pair[0], point_pair[2])
        b = max(point_pair[0], point_pair[2])
        for n in range(a, b+1):
            board[n][point_pair[1]] += 1

part1 = 0
for row in board:
    for n in row:
        if n > 1:
            part1 += 1
print(part1)

board = [[0] * 1000 for _ in range(1000)]
# board = [[0] * 10 for _ in range(10)]

for point_pair in points:
    if point_pair[0] == point_pair[2]:
        a = min(point_pair[1], point_pair[3])
        b = max(point_pair[1], point_pair[3])
        for n in range(a, b+1):
            board[point_pair[0]][n] += 1
    elif point_pair[1] == point_pair[3]:
        a = min(point_pair[0], point_pair[2])
        b = max(point_pair[0], point_pair[2])
        for n in range(a, b+1):
            board[n][point_pair[1]] += 1
    else:
        x_range = y_range = None
        if point_pair[1] < point_pair[3]:
            x_range = range(point_pair[1], point_pair[3]+1)
        else:
            x_range = range(point_pair[1], point_pair[3]-1, -1)
        if point_pair[0] < point_pair[2]:
            y_range = range(point_pair[0], point_pair[2]+1)
        else:
            y_range = range(point_pair[0], point_pair[2]-1, -1)
        x_range = list(x_range)
        y_range = list(y_range)
        for x, y in zip(x_range, y_range):
            board[y][x] += 1

part2 = 0
for row in board:
    # print(row)
    for n in row:
        if n > 1:
            part2 += 1
print(part2)
