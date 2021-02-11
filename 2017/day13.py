import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''0: 3
# 1: 2
# 4: 4
# 6: 4'''

firewall = {}
for line in inp.splitlines():
  depth, range_ = [int(n) for n in re.findall(r'\d+', line)]
  firewall[depth] = range_

part1 = 0
print('part1:', sum(depth * range_ for depth, range_ in firewall.items()
                    if depth % (2 * (range_ - 1)) == 0))

for delay in itertools.count(0):
  if any((depth + delay) % (2 * (range_ - 1)) == 0
         for depth, range_ in firewall.items()):
    continue
  print('part2:', delay)
  break
