import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

part1 = 0
part2 = 0
for line in inp.splitlines():
  nums = [int(n) for n in line.split()]
  part1 += max(nums) - min(nums)

  for a, b in itertools.combinations(nums, 2):
    a, b = max(a, b), min(a, b)
    if a % b == 0:
      part2 += a // b
      break
print('part1:', part1)
print('part2:', part2)