import collections
import hashlib
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

part1 = ''
part2 = [None] * 8
for i in itertools.count(0):
  h = hashlib.md5(f'{inp}{i}'.encode('ascii')).hexdigest()
  if h.startswith('00000'):
    part1 += h[5]
    if '0' <= h[5] <= '7':
      position = int(h[5])
      if part2[position] is None:
        # print(i, position, h[6])
        part2[position] = h[6]

        if part2.count(None) == 0:
          break
print('part1:', part1[:8])
print('part2:', ''.join(part2))
