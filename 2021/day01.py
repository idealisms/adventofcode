import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

nums = list(map(int, inp.split()))

part1 = 0
for i in range(len(nums) - 1):
    if nums[i+1] > nums[i]:
        part1 += 1
print(part1)

part2 = 0
for i in range(len(inp) - 2):
    if sum(nums[i+1:i+4]) > sum(nums[i:i+3]):
        part2 += 1
print(part2)
