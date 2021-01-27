import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
fav_number = int(inp)

mem = {}
def at(x, y):
  if x < 0 or y < 0:
    return '#'

  key = (x, y)
  if key in mem:
    return mem[key]

  n = (x*x + 3*x + 2*x*y + y + y*y) + fav_number
  # binary representation without the 0b prefix.
  ones = bin(n)[2:].count('1')
  result = '.' if ones % 2 == 0 else '#'
  mem[key] = result
  return result

queue = [(1, 1, 0)]  # (x, y, steps)
seen = set([(1, 1)])  # (x, y)
part1 = 0
part2 = 0
while True:
  x, y, steps = queue.pop(0)

  if steps <= 50:
    part2 += 1

  if x == 31 and y == 39:
    part1 = steps
    break

  pts = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
  for pt in pts:
    if pt in seen or at(*pt) == '#':
      continue
    seen.add(pt)
    queue.append((pt[0], pt[1], steps + 1))

print('part1:', part1)
print('part2:', part2)
