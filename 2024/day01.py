import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
lines = [list(map(int, line.split())) for line in inp.splitlines()]
cols = list(map(sorted, zip(*lines)))
part1 = 0
for lhs, rhs in zip(*cols):
    part1 += abs(lhs - rhs)
print(part1)
part2 = 0
for lhs, rhs in zip(*cols):
    part2 += lhs * cols[1].count(lhs)
print(part2)
