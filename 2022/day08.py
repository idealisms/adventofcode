import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
grid = inp.splitlines()
rows = len(grid)
cols = len(grid[0])

def is_visible(row, col):
    if row in (0, rows - 1) or col in (0, cols - 1):
        return True
    if all(grid[r][col] < grid[row][col] for r in range(row)):
        return True
    if all(grid[r][col] < grid[row][col] for r in range(rows - 1, row, -1)):
        return True
    if all(grid[row][c] < grid[row][col] for c in range(col)):
        return True
    if all(grid[row][c] < grid[row][col] for c in range(cols - 1, col, -1)):
        return True
    return False

part1 = 0
for row in range(rows):
    for col in range(cols):
        if is_visible(row, col):
            part1 += 1
print(part1)

def scenic_score(row, col):
    up = down = left = right = 0
    for r in range(row - 1, -1, -1):
        up += 1
        if grid[r][col] >= grid[row][col]:
            break
    for r in range(row + 1, rows):
        down += 1
        if grid[r][col] >= grid[row][col]:
            break
    for c in range(col - 1, -1, -1):
        left += 1
        if grid[row][c] >= grid[row][col]:
            break
    for c in range(col + 1, cols):
        right += 1
        if grid[row][c] >= grid[row][col]:
            break
    return up * down * left * right

part2 = 0
for row in range(rows):
    for col in range(cols):
        part2 = max(part2, scenic_score(row, col))
print(part2)