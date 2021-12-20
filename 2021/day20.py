import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

lines = inp.splitlines()
mapping = lines[0]

lights = set()
for row, line in enumerate(lines[2:]):
    for col, c in enumerate(line):
        if c == '#':
            lights.add((row, col))

def isLit(lights, r, c, r_min, r_max, c_min, c_max, canvas):
    digits = ''
    for r1 in (r-1, r, r+1):
        for c1 in (c-1, c, c+1):
            if r1 < r_min or r1 > r_max or c1 < c_min or c1 > c_max:
                digits += str(canvas)
            else:
                digits += '1' if (r1, c1) in lights else '0'
    # print(digits, int(digits, 2))
    return mapping[int(digits, 2)] == '#'

def step(lights, canvas=0):
    rows, cols = zip(*list(lights))
    r_min = min(rows)
    r_max = max(rows)
    c_min = min(cols)
    c_max = max(cols)
    
    new_lights = set()
    for r in range(r_min - 3, r_max + 4):
        for c in range(c_min - 3, c_max + 4):
            if isLit(lights, r, c, r_min, r_max, c_min, c_max, canvas):
                new_lights.add((r, c))
    return new_lights

part1 = step(lights, 0)
part1 = step(part1, 1)
print(len(part1))

part2 = lights
for _ in range(25):
    part2 = step(part2, 0)
    part2 = step(part2, 1)
print(len(part2))
    