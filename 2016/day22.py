import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

nodes = []
for line in inp.splitlines()[2:]:
  x, y, disk_size, used, avail, use_p = [int(n) for n in re.findall(r'\d+', line)]
  nodes.append((x, y, disk_size, used))

part1 = 0
for node_a, node_b in itertools.product(nodes, nodes):
  if node_a == node_b:
    continue
  if node_a[3] == 0:
    continue
  if node_a[3] <= node_b[2] - node_b[3]:
    part1 += 1
print('part1:', part1)

max_x = max([n[0] for n in nodes])
max_y = max([n[1] for n in nodes])
size_to_move = [n[3] for n in nodes if n[0] == 32 and n[1] == 0][0]
empty_nodes = [n[:2] for n in nodes if n[3] == 0]  # There's only one.
print(max_x, max_y, size_to_move, empty_nodes)
# 32 30 70 [(3, 28)]

# Conveniently, we can move the data (70T) across the y=0 nodes.
# Strategy: Move the empty node to (x-1, 0), move the data, then
# repeat until the data has moved all the way to (0, 0).

grid = {}
empty_node = empty_nodes[0][:2]
for x, y, disk_size, used in nodes:
  grid[(x, y)] = (disk_size, used)

def move_empty_node_path(empty_node, destination, data_location):
  '''Returns a list of steps to move the empty node to destination.'''
  # Do a BFS to find the path.
  # (x, y, steps)
  queue = [(empty_node[0], empty_node[1], [])]
  seen = set([empty_node])
  while len(queue):
    x, y, steps = queue.pop(0)
    if x == destination[0] and y == destination[1]:
      return steps
    for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
      if (nx, ny) in seen or (nx, ny) not in grid or (nx, ny) == data_location:
        continue
      available, _ = grid[(x, y)]
      _, used = grid[(nx, ny)]
      if available < used:
        continue
      seen.add((nx, ny))
      queue.append((nx, ny, steps + [(nx, ny)]))

data_location = (max_x, 0)
num_steps = 0
for x in range(max_x - 1, -1, -1):
  steps = move_empty_node_path(empty_node, (x, 0), data_location)
  steps.append(data_location)
  for step in steps:
    grid[empty_node], grid[step] = (
      (grid[empty_node][0], grid[step][1]),
      (grid[step][0], grid[empty_node][1]),
    )
    empty_node = step
  data_location = (x, 0)
  num_steps += len(steps)
print('part2:', num_steps)
