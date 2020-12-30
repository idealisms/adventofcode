import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

def deliver(inp):
  gifts = set()
  x, y = 0, 0
  gifts.add((x, y))
  move = {
    '<': (-1, 0),
    '>': (1, 0),
    '^': (0, 1),
    'v': (0, -1),
  }
  for c in inp:
    dx, dy = move[c]
    x += dx
    y += dy
    gifts.add((x, y))
  return gifts

print('part1:', len(deliver(inp)))

santa = ''.join(c for i, c in enumerate(inp) if i % 2 == 0)
robo_santa = ''.join(c for i, c in enumerate(inp) if i % 2 == 1)
print('part2:', len(deliver(santa).union(deliver(robo_santa))))
