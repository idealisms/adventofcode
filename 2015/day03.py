import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

def deliver(inp):
  gifts = set()
  pt = 0j
  gifts.add(pt)
  move = {
    '<': -1,
    '>': 1,
    '^': 1j,
    'v': -1j,
  }
  for c in inp:
    pt += move[c]
    gifts.add(pt)
  return gifts

print('part1:', len(deliver(inp)))

santa = ''.join(c for i, c in enumerate(inp) if i % 2 == 0)
robo_santa = ''.join(c for i, c in enumerate(inp) if i % 2 == 1)
print('part2:', len(deliver(santa).union(deliver(robo_santa))))
