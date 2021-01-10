import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

all_names = set()
scores = collections.defaultdict(int)
for line in inp.splitlines():
  # Alice would lose 57 happiness units by sitting next to Bob.
  mo = re.match(r'(\w+) would (lose|gain) (\d+) happiness units by sitting next to (\w+)[.]', line)
  delta = int(mo.group(3))
  if mo.group(2) == 'lose':
    delta = -delta
  names = tuple(sorted(mo.group(1, 4)))
  scores[names] += delta
  all_names.update(names)

def score(order):
  total = 0
  for i, name in enumerate(order):
    neighbor_name = order[(i + 1) % len(order)]
    names = tuple(sorted([name, neighbor_name]))
    total += scores[names]
  return total

best = 0
for order in itertools.permutations(all_names):
  best = max(best, score(order))

print('part1:', best)

my_name = 'AA'
for name in all_names:
  scores[(my_name, name)] = 0
all_names.update([my_name])

best = 0
for order in itertools.permutations(all_names):
  best = max(best, score(order))

print('part2:', best)
