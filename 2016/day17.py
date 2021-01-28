import collections
import hashlib
import itertools
import math
import re

prefix = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

def get_open_doors(steps):
  h = hashlib.md5(f'{prefix}{steps}'.encode('ascii')).hexdigest()[:4]
  open_doors = set()
  for c, direction in zip(h, 'UDLR'):
    if c in 'bcdef':
      open_doors.add(direction)
  return open_doors

DIRECTIONS = {
  'U': -1,
  'D': 1,
  'L': -1j,
  'R': 1j,
}

# (row, col, steps)
queue = [(0+0j, '')]
part1 = None
part2 = 0
while len(queue):
  pos, steps = queue.pop(0)
  if pos.real == 3 and pos.imag == 3:
    if part1 is None:
      part1 = steps
    part2 = max(part2, len(steps))
    continue

  open_doors = get_open_doors(steps)
  if pos.real == 0:
    open_doors -= {'U'}
  if pos.real == 3:
    open_doors -= {'D'}
  if pos.imag == 0:
    open_doors -= {'L'}
  if pos.imag == 3:
    open_doors -= {'R'}

  for direction in open_doors:
    queue.append((pos + DIRECTIONS[direction], steps + direction))

print('part1:', part1)
print('part2:', part2)
