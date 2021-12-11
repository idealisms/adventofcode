import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

grid = {}
for r, line in enumerate(inp.splitlines()):
    for c, n in enumerate(line):
        grid[(r, c)] = int(n)

part1 = 0
for step in range(100000):
    to_flash = set()
    has_flashed = set()

    for pt in grid.keys():
        grid[pt] += 1
        if grid[pt] > 9:
            to_flash.add(pt)
            has_flashed.add(pt)

    while len(to_flash) > 0:
        new_to_flash = set()
        for pt in to_flash:
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    pt2 = (pt[0] + dr, pt[1] + dc)
                    if pt2 in grid:
                        grid[pt2] += 1
                        if grid[pt2] > 9 and pt2 not in has_flashed:
                            new_to_flash.add(pt2)
        to_flash = new_to_flash
        has_flashed = has_flashed.union(new_to_flash)

    if len(has_flashed) == len(grid):
        print('part2:', step+1)
        break
    for pt in grid.keys():
        if grid[pt] > 9:
            grid[pt] = 0

    part1 += len(has_flashed)
    if step == 99:
        print('part1:', part1)

