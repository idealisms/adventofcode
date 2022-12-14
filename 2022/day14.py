import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
_inp = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''

y_max = 0
cave = {}
for line in inp.splitlines():
    nums = list(map(int, re.findall('\d+', line)))
    while len(nums) > 2:
        x1, y1, x2, y2 = nums[:4]
        nums = nums[2:]
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                cave[(x1, y)] = '#'
        else:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                cave[(x, y1)] = '#'
        y_max = max(y1, y2, y_max)

def step(x, y):
    if y == y_max + 1:
        raise
    if (x, y+1) not in cave:
        return x, y+1
    elif (x-1, y+1) not in cave:
        return x-1, y+1
    elif (x+1, y+1) not in cave:
        return x+1, y+1
    raise

part1 = 0
while True:
    x = 500
    y = 0
    try:
        while y < y_max + 1:
            x, y = step(x, y)
        break
    except:
        # print(x, y)
        cave[(x, y)] = 'o'
        part1 += 1
print(part1)

part2 = part1
while True:
    x = 500
    y = 0
    try:
        while True:
            x, y = step(x, y)
    except:
        # print(x, y)
        cave[(x, y)] = 'o'
        part2 += 1
        if (x, y) == (500, 0):
            break
print(part2)
