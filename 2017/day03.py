import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
target = int(inp)

pts = {}  # part 2
pts[(0, 0)] = 1
n = 2  # part 1
x, y = (0, 0)
radius = 1
part1 = 0
part2 = 0
while n < target:
  x += 1
  y -= 1
  side = radius * 2
  for dx, dy in ((0, 1), (-1, 0), (0, -1), (1, 0)):
    for i in range(side):
      x += dx
      y += dy
      if part2 == 0:
        adj_sum = 0
        for ax, ay in itertools.product((x - 1, x, x + 1), (y - 1, y, y + 1)):
          adj_sum += pts.get((ax, ay), 0)
        pts[(x, y)] = adj_sum
        if adj_sum > target:
          part2 = adj_sum
      if n == target:
        part1 = abs(x) + abs(y)
      n += 1
  radius += 1

print('part1:', part1)
print('part2:', part2)
