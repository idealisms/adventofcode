import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read()
grid = {}
for r, line in enumerate(inp.splitlines()):
  for c, char in enumerate(line):
    if char != ' ':
      grid[(r, c)] = char
UP, RIGHT, DOWN, LEFT = range(4)

row = 0
col = inp.splitlines()[0].find('|')
dir_ = DOWN
part1 = ''
# We start on step 1, but we take an extra step at
# the end.
steps = 0
while True:
  # print(row, col)
  if (row, col) not in grid:
    break
  c = grid[(row, col)]
  if c not in '+-|':
    part1 += c
  if c == '+':
    # Turn
    if dir_ in (UP, DOWN):
      if (row, col + 1) in grid:
        dir_ = RIGHT
      else:
        dir_ = LEFT
    else:
      if (row + 1, col) in grid:
        dir_ = DOWN
      else:
        dir_ = UP
  if dir_ == UP:
    row -= 1
  elif dir_ == RIGHT:
    col += 1
  elif dir_ == DOWN:
    row += 1
  elif dir_ == LEFT:
    col -= 1
  steps += 1
print('part1:', part1)
print('part2:', steps)