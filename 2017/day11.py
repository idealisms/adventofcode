import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

#     n  ne
# nw     se
# sw  s
pos = 0+0j
steps = {
  'n': 1j,
  'ne': 1+1j,
  'se': 1,
  's': -1j,
  'sw': -1-1j,
  'nw': -1,
}

def dist(point):
  x, y = int(point.real), int(point.imag)
  if (x > 0 and y < 0) or (x < 0 and y > 0):
    return abs(x) + abs(y)
  return max(abs(x), abs(y))

part2 = 0
for d in inp.split(','):
  pos += steps[d]
  part2 = max(part2, dist(pos))

print('part1:', dist(pos))
print('part2:', part2)
