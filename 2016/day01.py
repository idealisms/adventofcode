import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

N, E, S, W = range(4)
offset = [
  1j,
  1,
  -1j,
  -1,
]

direction = N
pos = 0+0j
seen = set()
twice = None
for instruction in inp.split(', '):
  direction += 1 if instruction[0] == 'R' else -1
  for _ in range(int(instruction[1:])):
    pos += offset[direction % 4]
    if twice is None and pos in seen:
      twice = pos
    seen.add(pos)

print('part1:', int(abs(pos.real) + abs(pos.imag)))
print('part2:', int(abs(twice.real) + abs(twice.imag)))
