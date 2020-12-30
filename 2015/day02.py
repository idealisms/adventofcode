import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

total = 0
for line in inp.splitlines():
  dims = [int(x) for x in re.findall(r'\d+', line)]
  sides = sorted([a * b for a, b in itertools.combinations(dims, 2)])
  total += sum(sides) * 2 + sides[0]

print('part1:', total)

total = 0
for line in inp.splitlines():
  dims = [int(x) for x in re.findall(r'\d+', line)]
  lengths = [2 * (a + b) for a, b in itertools.combinations(dims, 2)]
  total += min(lengths) + math.prod(dims)

print('part2:', total)
