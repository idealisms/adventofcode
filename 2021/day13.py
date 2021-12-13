import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

points_lines, folds_lines = inp.split('\n\n')

points = set()
for line in points_lines.splitlines():
    x, y = line.split(',')
    x = int(x)
    y = int(y)
    points.add((x, y))

folds_lines = folds_lines.splitlines()

def fold(direction, value, points):
    new_points = set()
    for pt in points:
        if direction == 'x':
            new_points.add((pt[0] if pt[0] < value else value - (pt[0] - value), pt[1]))
        else:
            new_points.add((pt[0], pt[1] if pt[1] < value else value - (pt[1] - value)))

    return new_points

part1 = None
for fold_line in folds_lines:
    direction, value = fold_line.split('=')
    points = fold(direction[-1], int(value), points)
    if part1 is None:
        part1 = len(points)
        print('part1:', part1)

xs, ys = zip(*points)
for r in range(max(ys)+1):
    row = []
    for c in range(max(xs)+1):
        if (c, r) in points:
            row.append('█')
        else:
            row.append(' ')
    print(''.join(row))
