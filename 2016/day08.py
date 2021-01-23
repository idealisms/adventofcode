import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

grid = [[0] * 50 for _ in range(6)]

for line in inp.splitlines():
  a, b = [int(n) for n in re.findall(r'\d+', line)]
  if line.startswith('rect'):
    for row, col in itertools.product(range(b), range(a)):
      grid[row][col] = 1
  elif line.startswith('rotate row'):
    row = a
    new_row = []
    for i in range(50):
      new_row.append(grid[row][(i - b) % 50])
    grid[row] = new_row
  elif line.startswith('rotate col'):
    col = a
    new_col = []
    for i in range(6):
      new_col.append(grid[(i - b) % 6][col])
    for i in range(6):
      grid[i][col] = new_col[i]

print('part1:', sum(sum(row) for row in grid))

for row in grid:
  print(''.join({0: ' ', 1: '#'}[n] for n in row))

###  #  # ###  #  #  ##  ####  ##  ####  ### #
#  # #  # #  # #  # #  # #    #  # #      #  #
#  # #  # #  # #  # #    ###  #  # ###    #  #
###  #  # ###  #  # #    #    #  # #      #  #
# #  #  # # #  #  # #  # #    #  # #      #  #
#  #  ##  #  #  ##   ##  ####  ##  ####  ### ####
