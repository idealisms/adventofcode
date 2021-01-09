import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

def look_and_say(inp):
  cur = None
  count = 0
  ans = []
  for c in inp:
    if c != cur:
      if cur is not None:
        ans.append(str(count))
        ans.append(str(cur))
      cur = c
      count = 1
    else:
      count += 1
  ans.append(str(count))
  ans.append(str(cur))
  return ''.join(ans)

for _ in range(40):
  inp = look_and_say(inp)
print('part1:', len(inp))

for _ in range(10):
  inp = look_and_say(inp)
print('part2:', len(inp))

# $ time pypy3 day10.py
# real    0m3.403s
# user    0m2.891s
# sys     0m0.512s
