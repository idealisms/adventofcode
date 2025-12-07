import collections
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''.......S.......
# ...............
# .......^.......
# ...............
# ......^.^......
# ...............
# .....^.^.^.....
# ...............
# ....^.^...^....
# ...............
# ...^.^...^.^...
# ...............
# ..^...^.....^..
# ...............
# .^.^.^.^.^...^.
# ...............'''
grid = inp.splitlines()
R, C = len(grid), len(grid[0])
beams = set([grid[0].find('S')])
part1 = 0
for r in range(1, R):
    row = grid[r]
    next_beams = set()
    splitters = set()
    for c in range(C):
        if grid[r][c] == '^':
            splitters.add(c)
    next_beams = beams - splitters
    for c in beams & splitters:
        part1 += 1
        next_beams.add(c - 1)
        next_beams.add(c + 1)
    beams = next_beams
print(part1)

beams = collections.defaultdict(int)
beams[grid[0].find('S')] += 1
for r in range(1, R):
    row = grid[r]
    next_beams = collections.defaultdict(int)
    splitters = set()
    for c in range(C):
        if grid[r][c] == '^':
            splitters.add(c)
    for c, cnt in beams.items():
        if c not in splitters:
            next_beams[c] += cnt
        else:
            next_beams[c-1] += cnt
            next_beams[c+1] += cnt
    beams = next_beams
print(sum(beams.values()))
