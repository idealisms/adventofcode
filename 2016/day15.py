import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
discs = []
for line in inp.splitlines():
  disc, positions, _, initial_pos = [int(n) for n in re.findall(r'\d+', line)]
  discs.append((disc, positions, initial_pos))

def is_valid(t):
  for disc, positions, initial_pos in discs:
    if (initial_pos + disc + t) % positions != 0:
      return False
  return True

for t in itertools.count():
  if is_valid(t):
    print('part1:', t)
    break

discs.append((7, 11, 0))
for t in itertools.count():
  if is_valid(t):
    print('part2:', t)
    break
