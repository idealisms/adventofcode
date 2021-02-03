import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
grid = inp.splitlines()

waypoints = {}
for r, row in enumerate(grid):
  for c, char in enumerate(row):
    if char not in ('.', '#'):
      waypoints[int(char)] = (r, c)

def bfs_dist(pt1, pt2):
  # (r, c, num_steps)
  queue = [(pt1[0], pt1[1], 0)]
  seen = set([pt1])
  while True:
    r, c, num_steps = queue.pop(0)
    if (r, c) == pt2:
      return num_steps
    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
      if (nr, nc) in seen or grid[nr][nc] == '#':
        continue
      seen.add((nr, nc))
      queue.append((nr, nc, num_steps + 1))

waypoint_ids = sorted(waypoints.keys())
distances = {}
for i, j in itertools.combinations(waypoint_ids, 2):
  dist = bfs_dist(waypoints[i], waypoints[j])
  distances[(i, j)] = dist
  distances[(j, i)] = dist

waypoint_ids.remove(0)
part1 = 10**9
for order in itertools.permutations(waypoint_ids):
  order = (0,) + order
  part1 = min(part1, sum(distances[(order[i], order[i+1])] for i in range(len(order) - 1)))
print('part1:', part1)

part2 = 10**9
for order in itertools.permutations(waypoint_ids):
  order = (0,) + order + (0,)
  part2 = min(part2, sum(distances[(order[i], order[i+1])] for i in range(len(order) - 1)))
print('part2:', part2)