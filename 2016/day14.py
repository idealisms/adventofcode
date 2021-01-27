import collections
import hashlib
import itertools
import math
import re

salt = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

def calc(index):
  return hashlib.md5(f'{salt}{index}'.encode('ascii')).hexdigest()

def calc2016(index):
  h = calc(index)
  for _ in range(2016):
    h = hashlib.md5(h.encode('ascii')).hexdigest()
  return h

def solve(calc_func):
  hashes = [calc_func(n) for n in range(1000)]

  index = -1
  found = 0
  while found < 64:
    index += 1

    h = hashes.pop(0)
    hashes.append(calc_func(index + 1000))

    mo = re.search(r'(.)\1\1', h)
    if mo:
      pattern = mo.group(0)
      pattern += pattern[:2]
      for h in hashes:
        if h.find(pattern) != -1:
          found += 1
          break
  return index

print('part1:', solve(calc))
print('part2:', solve(calc2016))
