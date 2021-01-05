import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
commands = inp.splitlines()

grid = [[0] * 1000 for _ in range(1000)]
toggles = 0
for cmd in commands:
  x1, y1, x2, y2 = [int(n) for n in re.findall(r'\d+', cmd)]
  toggles += (x2 - x1 + 1) * (y2 - y1 + 1)
  action = lambda x: 1 - x
  if cmd.startswith('turn on'):
    action = lambda x: 1
  elif cmd.startswith('turn off'):
    action = lambda x : 0

  for x, y in itertools.product(range(x1, x2 + 1), range(y1, y2 + 1)):
    grid[x][y] = action(grid[x][y])

# print(toggles)  # ~20mil, which is doable.
print('part1:', sum([sum(row) for row in grid]))

grid = [[0] * 1000 for _ in range(1000)]
for cmd in commands:
  x1, y1, x2, y2 = [int(n) for n in re.findall(r'\d+', cmd)]
  toggles += (x2 - x1 + 1) * (y2 - y1 + 1)
  action = lambda x: x + 2
  if cmd.startswith('turn on'):
    action = lambda x: x + 1
  elif cmd.startswith('turn off'):
    action = lambda x : max(0, x - 1)

  for x, y in itertools.product(range(x1, x2 + 1), range(y1, y2 + 1)):
    grid[x][y] = action(grid[x][y])
print('part2:', sum([sum(row) for row in grid]))

# $ time pypy3 day06.py
# real    0m2.258s
# user    0m2.198s
# sys     0m0.050s
