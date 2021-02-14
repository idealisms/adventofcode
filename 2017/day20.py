import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

class Point(object):
  def __init__(self, line, idx):
    self.index = idx
    (self.x, self.y, self.z,
     self.vx, self.vy, self.vz,
     self.ax, self.ay, self.az) = [int(n) for n in re.findall(r'[-]?\d+', line)]
    self.destroyed = False

  def update(self):
    self.vx += self.ax
    self.vy += self.ay
    self.vz += self.az

    self.x += self.vx
    self.y += self.vy
    self.z += self.vz

  def distance(self):
    return abs(self.x) + abs(self.y) + abs(self.z)

  def get_pos(self):
    return self.x, self.y, self.z

  def __lt__(self, rhs):
    return self.distance() < rhs.distance()

points = []
for idx, line in enumerate(inp.splitlines()):
  points.append(Point(line, idx))

# Guess at how long we need to run before we've hit a stable state.
repeats = 1000
closest = []
while True:
  for point in points:
    point.update()

  positions = collections.defaultdict(int)
  for point in points:
    if not point.destroyed:
      positions[point.get_pos()] += 1
  for point in points:
    if positions[point.get_pos()] > 1:
      point.destroyed = True

  closest.append(min(points).index)
  if len(closest) > repeats and all(idx == closest[-1] for idx in closest[-repeats:]):
    print('part1:', closest[-1])
    # print(len(closest)) # 1319
    break

print('part2:', len([pt for pt in points if not pt.destroyed]))
