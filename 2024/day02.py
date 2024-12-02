import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9'''

def is_safe(levels):
    asc = list(sorted(levels))
    if levels == asc or list(reversed(levels)) == asc:
        for i in range(1, len(levels)):
            if not (1 <= abs(levels[i] - levels[i-1]) <= 3):
                return False
        return True
    return False

part1 = 0
for line in inp.splitlines():
    levels = list(map(int, line.split()))
    if is_safe(levels):
        part1 += 1
print(part1)

part2 = 0
for line in inp.splitlines():
    levels = list(map(int, line.split()))
    if is_safe(levels):
        part2 += 1
    else:
        for rem in range(len(levels)):
            test_levels = levels[:rem] + levels[rem+1:]
            if is_safe(test_levels):
                part2 += 1
                break
print(part2)
            