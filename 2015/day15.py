import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
props = []
for line in inp.splitlines():
  matches = re.findall(r'(\w+) ([-]?\d+)', line)
  d = {}
  for prop, value in matches:
    d[prop] = int(value)
  props.append(d)

def permutations():
  TEASPOONS = 100
  for w in range(TEASPOONS + 1):
    for x in range(TEASPOONS - w + 1):
      for y in range(TEASPOONS - w - x + 1):
        z = TEASPOONS - w - x - y
        yield (w, x, y, z)

prop_names = set(props[0].keys())
prop_names.remove('calories')
best = 0
for w, x, y, z in permutations():
  total = 1
  for prop in prop_names:
    v = max(0, sum(teaspoons * props[i][prop] for i, teaspoons in enumerate((w, x, y, z))))
    total *= v
  best = max(best, total)
print('part1:', best)

best = 0
for w, x, y, z in permutations():
  calories = sum(teaspoons * props[i]['calories'] for i, teaspoons in enumerate((w, x, y, z)))
  if calories != 500:
    continue

  total = 1
  for prop in prop_names:
    v = max(0, sum(teaspoons * props[i][prop] for i, teaspoons in enumerate((w, x, y, z))))
    total *= v
  best = max(best, total)
print('part2:', best)
