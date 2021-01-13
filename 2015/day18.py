import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

lights_on = set()
for row, line in enumerate(inp.splitlines()):
  for col, c in enumerate(line):
    if c == '#':
      lights_on.add((row, col))

def step(lights_on):
  new_lights_on = set()
  for row, col in itertools.product(range(100), range(100)):
    adj_on = 0
    for adj_row, adj_col in itertools.product((row - 1, row, row + 1), (col - 1, col, col + 1)):
      if adj_row == row and adj_col == col:
        continue
      if (adj_row, adj_col) in lights_on:
        adj_on += 1
    if (row, col) in lights_on and adj_on in (2, 3):
      new_lights_on.add((row, col))
    if (row, col) not in lights_on and adj_on == 3:
      new_lights_on.add((row, col))
  return new_lights_on

part1_lights_on = set(lights_on)
for _ in range(100):
  part1_lights_on = step(part1_lights_on)
print('part1:', len(part1_lights_on))

part2_lights_on = set(lights_on)
part2_lights_on.add((0, 0))
part2_lights_on.add((0, 99))
part2_lights_on.add((99, 0))
part2_lights_on.add((99, 99))
for _ in range(100):
  part2_lights_on = step(part2_lights_on)
  part2_lights_on.add((0, 0))
  part2_lights_on.add((0, 99))
  part2_lights_on.add((99, 0))
  part2_lights_on.add((99, 99))
print('part2:', len(part2_lights_on))
