import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
towels_str, patterns_str = inp.split('\n\n')
TOWELS = towels_str.split(', ')

mem = {}
def solve(pattern):
    if pattern == '':
        return 1
    if pattern in mem:
        return mem[pattern]
    total = 0
    for towel in TOWELS:
        if pattern.startswith(towel):
            total += solve(pattern[len(towel):])
    mem[pattern] = total
    return total

part1 = 0
part2 = 0
for pattern in patterns_str.splitlines():
    if solve(pattern) > 0:
        part1 += 1
    part2 += solve(pattern)
print(part1)
print(part2)

