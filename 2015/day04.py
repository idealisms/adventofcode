import collections
import hashlib
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

part1 = None
for i in itertools.count(1):
  h = hashlib.md5(f'{inp}{i}'.encode('ascii')).hexdigest()

  if not part1 and h.startswith('00000'):
    part1 = i
    print('part1:', part1)
  if h.startswith('000000'):
    print('part2:', i)
    break
