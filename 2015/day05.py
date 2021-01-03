import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
lines = inp.splitlines()

total = 0
for line in lines:
  vowels = sum(line.count(c) for c in 'aeiou')
  has_dupe = re.search(r'(.)\1', line) is not None
  has_no_forbidden = re.search(r'ab|cd|pq|xy', line) is None
  if vowels >= 3 and has_dupe and has_no_forbidden:
    total += 1
print('part1:', total)

total = 0
for line in lines:
  has_dupe = re.search(r'(..).*\1', line) is not None
  has_split = re.search(r'(.).\1', line) is not None
  if has_dupe and has_split:
    total += 1
print('part2:', total)
