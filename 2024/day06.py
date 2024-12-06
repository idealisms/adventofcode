# Run using pypy3. Takes about 11s on my laptop.

import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
grid = inp.splitlines()
DIRS = (
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
)
d = 0

walls = set()
startr = startc = 0
for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char == '^':
            startr, startc = r, c
        elif char == '#':
            walls.add((r, c))

gr, gc = startr, startc
visited = set()

while 0 <= gr < len(grid) and 0 <= gc < len(grid[0]):
    visited.add((gr, gc))
    newr = gr + DIRS[d % 4][0]
    newc = gc + DIRS[d % 4][1]
    if (newr, newc) in walls:
        d += 1
    else:
        gr, gc = newr, newc
print(len(visited))

def is_loop(walls):
    gr, gc = startr, startc
    d = 0
    visited = set()
    while 0 <= gr < len(grid) and 0 <= gc < len(grid[0]):
        if (gr, gc, d) in visited:
            return True
        visited.add((gr, gc, d))
        newr = gr + DIRS[d][0]
        newc = gc + DIRS[d][1]
        if (newr, newc) in walls:
            d += 1
            d %= 4
        else:
            gr, gc = newr, newc
    return False

part2 = 0
for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if grid[r][c] != '.':
            continue
        test_walls = walls.copy()
        test_walls.add((r, c))
        if is_loop(test_walls):
            part2 += 1
print(part2)
