import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

ranges = []
for line in inp.splitlines():
  lo, hi = [int(n) for n in re.findall(r'\d+', line)]
  ranges.append((lo, hi))

ranges.sort()
part1 = 0
part2 = 0
port = 0
for lo, hi in ranges:
  if lo <= port:
    port = max(port, hi + 1)
  else:
    if part1 == 0:
      part1 = port
    part2 += lo - port
    port = hi + 1

print('part1:', part1)
if port <= 4294967295:
  part2 += 4294967296 - port
print('part2:', part2)
