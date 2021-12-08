import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

nums = list(map(int, inp.split(',')))
print(max(nums), min(nums), len(nums))

def arithSum(n):
    return int(n * (n+1) / 2)

part1 = 9999999
part2 = 999999999
for target in range(max(nums)):
    dist = sum([abs(n - target) for n in nums])
    part1 = min(part1, dist)

    dist = sum([arithSum(abs(n-target)) for n in nums])
    part2 = min(part2, dist)
print(part1)
print(part2)