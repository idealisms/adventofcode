import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

part1 = part2 = 0
for line in inp.splitlines():
    a, b = line.split(',')
    a1, a2 = map(int, a.split('-'))
    b1, b2 = map(int, b.split('-'))
    if a1 >= b1 and a2 <= b2:
        part1 += 1
    elif b1 >= a1 and b2 <= a2:
        part1 += 1
    if len(set(range(a1, a2+1)).intersection(set(range(b1, b2+1)))):
        part2 += 1
print(part1)
print(part2)
