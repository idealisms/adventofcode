import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

# I originally used a set() of trap coordinates. It took ~28s to run compared
# to this solution which takes ~1.4s.
def solve(num_rows):
  rows = ['.' + inp + '.']

  for _ in range(1, num_rows):
    next_row = '.'
    for col in range(1, len(inp) + 1):
      prev = rows[-1][col-1:col+2]
      next_row += '^' if prev in ('^^.', '.^^', '^..', '..^') else '.'
    next_row += '.'
    rows.append(next_row)

  traps = sum(row.count('^') for row in rows)
  return len(inp) * num_rows - traps

print('part1:', solve(40))
print('part2:', solve(400000))
