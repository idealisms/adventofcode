import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

possible = 0
for line in inp.splitlines():
  nums = [int(n) for n in re.findall(r'\d+', line)]
  nums.sort()
  if nums[0] + nums[1] > nums[2]:
    possible += 1
print('part1:', possible)

array = []
for line in inp.splitlines():
  array.append([int(n) for n in re.findall(r'\d+', line)])

transposed = list(zip(*array))
all_nums = []
for row in transposed:
  all_nums.extend(row)

possible = 0
while len(all_nums) > 0:
  nums = all_nums[:3]
  nums.sort()
  if nums[0] + nums[1] > nums[2]:
    possible += 1
  all_nums = all_nums[3:]
print('part2:', possible)
