import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
banks = [int(n) for n in inp.split()]

seen = {}
part1 = None
size = len(banks)
for steps in itertools.count():
  key = tuple(banks)
  if key in seen:
    part1 = steps
    part2 = steps - seen[key]
    break
  seen[key] = steps

  idx = banks.index(max(banks))
  count = banks[idx]
  banks[idx] = 0
  for i in range(count):
    banks[(idx + 1 + i) % size] += 1

print('part1:', part1)
print('part2:', part2)
