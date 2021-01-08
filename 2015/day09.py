import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

# Traveling salesman (8! = 40320 possible routes)
dist = {}
locs = set()
for line in inp.splitlines():
  loc1, loc2, d = re.split(r' to | = ', line)
  locs.add(loc1)
  locs.add(loc2)
  dist[(loc1, loc2)] = int(d)
  dist[(loc2, loc1)] = int(d)

shortest = 10**8
longest = 0
for perm in itertools.permutations(locs):
  d = sum(dist[(loc1, loc2)] for loc1, loc2 in zip(perm[:-1], perm[1:]))
  shortest = min(shortest, d)
  longest = max(longest, d)
print('part1:', shortest)
print('part2:', longest)
