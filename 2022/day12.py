import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
grid = inp.splitlines()
rows = len(grid)
cols = len(grid[0])
steps = [[-1 for _ in range(cols)] for _ in range(rows)]
er = ec = -1
for r, row in enumerate(grid):
    c = row.find('S')
    if c != -1:
        steps[r][c] = 0
    c = row.find('E')
    if c != -1:
        er = r
        ec = c

def can_step(r, c, tr, tc):
    if (tr < 0 or tr >= rows
        or tc < 0 or tc >= cols):
        return False
    if steps[tr][tc] != -1:
        return False
    target_height = ord('z' if grid[tr][tc] == 'E' else grid[tr][tc])
    return target_height <= ord('a' if grid[r][c] == 'S' else grid[r][c]) + 1

for step in range(rows * cols + 1):
    for r, row in enumerate(grid):
        for c, el in enumerate(row):
            if steps[r][c] == step:
                if can_step(r, c, r-1, c):
                    steps[r-1][c] = step + 1
                if can_step(r, c, r+1, c):
                    steps[r+1][c] = step + 1
                if can_step(r, c, r, c-1):
                    steps[r][c-1] = step + 1
                if can_step(r, c, r, c+1):
                    steps[r][c+1] = step + 1
    if steps[er][ec] != -1:
        break

print(steps[er][ec])

# part2
steps = [[-1 for _ in range(cols)] for _ in range(rows)]
for r, row in enumerate(grid):
    for c, el in enumerate(row):
        if el in 'Sa':
            steps[r][c] = 0

for step in range(rows * cols + 1):
    for r, row in enumerate(grid):
        for c, el in enumerate(row):
            if steps[r][c] == step:
                if can_step(r, c, r-1, c):
                    steps[r-1][c] = step + 1
                if can_step(r, c, r+1, c):
                    steps[r+1][c] = step + 1
                if can_step(r, c, r, c-1):
                    steps[r][c-1] = step + 1
                if can_step(r, c, r, c+1):
                    steps[r][c+1] = step + 1
    if steps[er][ec] != -1:
        break

print(steps[er][ec])
