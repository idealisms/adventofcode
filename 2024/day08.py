import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............'''


grid = inp.splitlines()
R = len(grid)
C = len(grid[0])
m = collections.defaultdict(list)
for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char != '.':
            m[char].append((r, c))

antinodes = set()
for k in m.keys():
    towers = m[k]
    for t, p1 in enumerate(towers):
        for p2 in towers[t+1:]:
            # print(p1, p2)
            dr, dc = abs(p1[0] - p2[0]), abs(p1[1] - p2[1])
            r = p1[0] - dr if p1[0] < p2[0] else p1[0] + dr
            c = p1[1] - dc if p1[1] < p2[1] else p1[1] + dc
            if 0 <= r < R and 0 <= c < C:
                antinodes.add((r, c))
            r = p2[0] - dr if p2[0] < p1[0] else p2[0] + dr
            c = p2[1] - dc if p2[1] < p1[1] else p2[1] + dc
            if 0 <= r < R and 0 <= c < C:
                antinodes.add((r, c))
print(len(antinodes))

antinodes = set()
for r in range(R):
    for c in range(C):
        for k in m.keys():
            towers = m[k]
            for t, p1 in enumerate(towers):
                for p2 in towers[t+1:]:
                    if (r, c) in [p1, p2]:
                        antinodes.add((r, c))
                        continue
                    pts = sorted([p1, p2, (r, c)])
                    if p1[0] == p2[0] and p1[0] == r:
                        antinodes.add((r, c))
                        continue
                    if p2[0] - p1[0] == 0 or r - p1[0] == 0:
                        continue
                    if (float(p2[1] - p1[1]) / (p2[0] - p1[0]) ==
                        float(c - p1[1]) / (r - p1[0])):
                        antinodes.add((r, c))
print(len(antinodes))
