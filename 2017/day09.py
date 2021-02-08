import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

score = 0
is_garbage = False
cancel = False
total_score = 0
garbage_count = 0
for c in inp:
  if is_garbage:
    if cancel:
      cancel = False
    elif c == '!':
      cancel = True
    elif c == '>':
      is_garbage = False
    else:
      garbage_count += 1
  else:
    if c == '{':
      score += 1
    elif c == '}':
      total_score += score
      score -= 1
    elif c == '<':
      is_garbage = True

print('part1:', total_score)
print('part2:', garbage_count)
