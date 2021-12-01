import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

p = None
part1 = 0
for n in inp.split():
    n = int(n)
    if p is not None:
        if n > p:
            part1 += 1
    p = n
print(part1)

p = None
part2 = 0
nums = list(map(int, inp.split()))
for i in range(len(inp) - 2):
    n = sum(nums[i:i+3])
    if p is not None:
        if n > p:
            part2 += 1
    p = n
print(part2)
