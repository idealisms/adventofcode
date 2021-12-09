import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

grid = inp.splitlines()
rows = len(grid)
cols = len(grid[0])
grid = []
grid.append(['9'] * (cols+2))
for row in inp.splitlines():
    grid.append(list('9' + row + '9'))
grid.append(['9'] * (cols+2))

part1 = 0
for r in range(1, rows + 1):
    for c in range(1, cols + 1):
        if (grid[r][c] < grid[r-1][c] and grid[r][c] < grid[r][c-1]
            and grid[r][c] < grid[r+1][c] and grid[r][c] < grid[r][c+1]):
            part1 += int(grid[r][c]) + 1
print(part1)

def fill(grid, r, c):
    if grid[r][c] == '9':
        return 0
    grid[r][c] = '9'
    size = 1
    size += fill(grid, r-1, c)
    size += fill(grid, r+1, c)
    size += fill(grid, r, c-1)
    size += fill(grid, r, c+1)
    return size

sizes = []
for r in range(1, rows + 1):
    for c in range(1, cols + 1):
        if grid[r][c] != '9':
            sizes.append(fill(grid, r, c))
print(math.prod(sorted(sizes)[-3:]))
