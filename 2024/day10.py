import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732'''

grid = inp.splitlines()
R = len(grid)
C = len(grid[0])

def score(r, c):
    ps = []
    ps.append((r, c))
    summits = set()
    while len(ps) > 0:
        r, c = ps.pop(0)
        h = grid[r][c]
        if h == '9':
            summits.add((r, c))
            continue
        if r > 0 and grid[r-1][c] == str(int(h) + 1):
            ps.append((r-1, c))
        if r < R - 1 and grid[r+1][c] == str(int(h) + 1):
            ps.append((r+1, c))
        if c > 0 and grid[r][c-1] == str(int(h) + 1):
            ps.append((r, c - 1))
        if c < C - 1 and grid[r][c+1] == str(int(h) + 1):
            ps.append((r, c+1))
    return len(summits)

def rating(r, c):
    ps = []
    ps.append((r, c))
    summits = 0
    while len(ps) > 0:
        r, c = ps.pop(0)
        h = grid[r][c]
        if h == '9':
            summits += 1
            continue
        if r > 0 and grid[r-1][c] == str(int(h) + 1):
            ps.append((r-1, c))
        if r < R - 1 and grid[r+1][c] == str(int(h) + 1):
            ps.append((r+1, c))
        if c > 0 and grid[r][c-1] == str(int(h) + 1):
            ps.append((r, c - 1))
        if c < C - 1 and grid[r][c+1] == str(int(h) + 1):
            ps.append((r, c+1))
    return summits

part1 = part2 = 0
for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char == '0':
            part1 += score(r, c)
            part2 += rating(r, c)
print(part1)
print(part2)
