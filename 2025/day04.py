import collections
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.'''

grid = inp.splitlines()
R, C = len(grid), len(grid[0])
rolls = set()
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == '@':
            rolls.add((r, c))

part1 = 0
before_count = len(rolls)
has_removed = True
while has_removed:
    has_removed = False
    to_remove = set()
    for r, c in rolls:
        adj_count = 0
        for dr, dc in ((-1, -1), (-1, 0), (-1, 1),
                    (0, -1), (0, 1),
                    (1, -1), (1, 0), (1, 1)):
            nr, nc = r + dr, c + dc
            if (nr, nc) in rolls:
                adj_count += 1
        if adj_count < 4:
            to_remove.add((r, c))
            has_removed = True
    if part1 == 0:
        part1 = len(to_remove)
    rolls -= to_remove
print(part1)
print(before_count - len(rolls))
