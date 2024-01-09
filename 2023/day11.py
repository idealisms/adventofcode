import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....'''

grid = inp.splitlines()
xs = []
ys = []
for r, row in enumerate(grid):
    for c, value in enumerate(row):
        if value == '#':
            xs.append(r)
            ys.append(c)
ys.sort()

def expand(lst, factor=1):
    new_lst = [lst[0]]
    blanks = 0
    for i in range(len(lst) - 1):
        blanks += factor * max(0, lst[i+1] - lst[i] - 1)
        new_lst.append(lst[i+1] + blanks)
    return new_lst

def dist(lst):
    total = 0
    for i, a in enumerate(lst):
        for b in lst[i+1:]:
            total += b - a
    return total

part1 = dist(expand(xs)) + dist(expand(ys))
print(part1)
part2 = dist(expand(xs, 999999)) + dist(expand(ys, 999999))
print(part2)
