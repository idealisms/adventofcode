import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE'''


grid = inp.splitlines()
R = len(grid)
C = len(grid[0])

m = {}
for r in range(R):
    for c in range(C):
        m[(r, c)] = grid[r][c]

def build_region(r, c):
    region = set()
    t = grid[r][c]
    q = [(r, c)]
    while len(q):
        r, c = q.pop()
        if (r, c) in region:
            continue
        if m.get((r, c)) == t:
            region.add((r, c))
            q.append((r-1, c))
            q.append((r+1, c))
            q.append((r, c-1))
            q.append((r, c+1))
    return region

def price(region, t):
    per = 0
    for pt in region:
        r, c = pt
        per += 1 if m.get((r+1, c)) != t else 0
        per += 1 if m.get((r-1, c)) != t else 0
        per += 1 if m.get((r, c+1)) != t else 0
        per += 1 if m.get((r, c-1)) != t else 0
    return len(region) * per

def price2(region, t):
    sides = 0
    for pt in region:
        r, c = pt
        if m.get((r-1, c)) != t:
            if m.get((r, c-1)) != t:
                sides += 1
            elif m.get((r-1, c-1)) == t:
                sides += 1
        if m.get((r+1, c)) != t:
            if m.get((r, c-1)) != t:
                sides += 1
            elif m.get((r+1, c-1)) == t:
                sides += 1
        if m.get((r, c-1)) != t:
            if m.get((r-1, c)) != t:
                sides += 1
            elif m.get((r-1, c-1)) == t:
                sides += 1
        if m.get((r, c+1)) != t:
            if m.get((r-1, c)) != t:
                sides += 1
            elif m.get((r-1, c+1)) == t:
                sides += 1
    return len(region) * sides

part1 = part2 = 0
visited = set()
for r in range(R):
    for c in range(C):
        if (r, c) in visited:
            continue
        region = build_region(r, c)
        pr = price(region, grid[r][c])
        part1 += pr
        visited |= region
        # print(grid[r][c], len(region), pr)
        pr = price2(region, grid[r][c])
        part2 += pr
print(part1)
print(part2)